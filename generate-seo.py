#!/usr/bin/env python3
"""Generate sitemap.xml and canonical/OG URLs using the real deployed root URL."""
import sys
from pathlib import Path
from urllib.parse import urlparse
from xml.sax.saxutils import escape
if len(sys.argv) != 2:
    sys.exit('Usage: python generate-seo.py https://YOUR-SITE-URL/')
root = sys.argv[1].rstrip('/') + '/'
parsed = urlparse(root)
if parsed.scheme != 'https' or not parsed.netloc:
    sys.exit('Use a valid public HTTPS site URL, ending with / if desired.')
files = ['index.html', 'modeles.html', 'univers.html']
site = Path(__file__).resolve().parent
urls = [root if f == 'index.html' else root + f for f in files]
xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join('  <url><loc>' + escape(url) + '</loc></url>\n' for url in urls) + '</urlset>\n'
(site/'sitemap.xml').write_text(xml, encoding='utf-8')
(site/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: ' + root + 'sitemap.xml\n',encoding='utf-8')
for f, url in zip(files, urls):
    path = site/f
    content = path.read_text(encoding='utf-8')
    # Re-running safely replaces old canonical + OG URL entries.
    import re
    content = re.sub(r'<link rel="canonical" href="[^"]*">', '', content)
    content = re.sub(r'<meta property="og:url" content="[^"]*">', '', content)
    content = content.replace('<meta name="robots"', '<link rel="canonical" href="'+url+'"><meta property="og:url" content="'+url+'"><meta name="robots"',1)
    path.write_text(content,encoding='utf-8')
print('Generated sitemap.xml, robots.txt, and canonical/OG URLs for', root)
