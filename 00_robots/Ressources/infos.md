# Recherches

1. Vérification du fichier `robots.txt` afin de vérifier les fichiers/dossiers que l'admin veut cacher aux moteurs de recherche
2. Vérification du dossier `/whatever`
3. Download htpasswd [htpasswd permet de créer et de maintenir les fichiers textes où sont stockés les noms d'utilisateurs et mots de passe pour l'authentification de base des utilisateurs HTTP](https://httpd.apache.org/docs/2.4/fr/programs/htpasswd.html)
4. Recherche du panel d'administration => `/admin`
5. Décryptage du MD5 sur [md5decrypt.net](https://md5decrypt.net/) `md5(8621ffdbc5698829397d97767ac13db30 == "dragon"`
6. Connexion user: `root` pass: `dragon`

> FLAG: d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff

# Explications

Une erreur courante est d'utiliser les règles du fichier `robots.txt` en pensant que si elles interdisent l’accès à un robot d’indexation elles empêchent un utilisateur d’accéder à ces pages.

# Corrections

Le seul moyen de protéger l’accès à une page est une forme d’authentification.

Il est très fortement recommandé de ne pas stocker de fichiers sensibles tel que `htaccess` dans les dossiers qui sont hébergés.