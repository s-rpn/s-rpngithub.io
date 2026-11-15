# Dorodourcalé — site SEO gratuit en 3 pages

Marque de voitures **fictive** créée pour un concours de référencement sur « dorodourcalé ».

## Contenu
- `index.html` : accueil, présentation de la marque, modèles et FAQ.
- `modeles.html` : concepts Aura, Veloce, Horizon.
- `univers.html` : histoire et identité de la marque.
- `assets/` : illustration SVG locale, favicon, CSS, JavaScript.
- `robots.txt` : autorise l’exploration.
- `generate-seo.py` : crée un sitemap et des URL canoniques lorsque l’URL définitive est connue.

## Publication gratuite sur GitHub Pages
1. Inscrivez-vous sur https://github.com/ .
2. Créez un dépôt **public** nommé `votre-utilisateur.github.io` (site utilisateur) ou `dorodourcale` (site de projet).
3. Dans le dépôt, utilisez **Add file → Upload files** pour importer **le contenu du dossier** (pas le ZIP). Confirmez le commit.
4. Ouvrez **Settings → Pages → Build and deployment** : sélectionnez **Deploy from a branch**, puis `main` et `/ (root)` ; enregistrez.
5. Votre adresse sera `https://votre-utilisateur.github.io/` ou `https://votre-utilisateur.github.io/dorodourcale/` selon le dépôt.
6. Une fois l’adresse connue, exécutez localement : `python generate-seo.py https://votre-utilisateur.github.io/` (ou votre véritable URL, avec le sous-chemin si nécessaire), puis envoyez sur GitHub les fichiers générés.
7. Ajoutez votre adresse dans https://search.google.com/search-console/ , vérifiez la propriété, soumettez le fichier `sitemap.xml` et demandez l’indexation de la page d’accueil.

**Important :** le nom `dorodourcale.github.io` est un exemple et n’est pas garanti disponible. Ne créez pas de données ou de liens fictifs pour les moteurs. Un classement n’est jamais garanti.

## Stratégie SEO pendant les 3 mois
- Semaines 1–2 : mise en ligne, sitemap, Search Console et indexation.
- Semaines 3–4 : vérifier le rendu mobile, l’indexation des trois pages et les requêtes.
- Semaines 5–8 : enrichir les pages avec des créations vraiment originales, sans répétition abusive du mot-clé ; présenter le projet sur des plateformes pertinentes et obtenir des liens éditoriaux réels.
- Semaines 9–12 : suivre Google Search Console, comparer les résultats concurrents et améliorer titres, contenu et navigation si nécessaire.

## Prévisualiser
Ouvrez `index.html` dans un navigateur. Les 3 pages sont reliées par des liens relatifs et fonctionnent aussi sur un hébergement dans un sous-répertoire. La police en ligne nécessite une connexion, mais des polices de secours sont prévues.

## Transparence
Les voitures sont fictives. Le modèle SVG est une illustration conceptuelle commune avec variantes de couleur, et non une représentation de produits fabriqués ou commercialisés.
