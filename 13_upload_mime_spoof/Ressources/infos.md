# Recherches

1. Upload d'un exploit php
2. Via BrupSuite change the MIME type to `image/jpeg`

> FLAG: 46910D9CE35B385885A9F7E2B336249D622F29B267A1771FBACF52133BEDDBA8

# Explications

Ce type de vulnerabilité permet à l'attaquant d'uploader n'importe quel type d'exploit directement sur le serveur.
Ensuite il est possible d'exécuter l'exploit grâce à d'autres techniques.
Tout devient possible pour l'attaquant, escalation de privileges, suppression de tous les fichiers, ... 

# Corrections

Pour corriger cette faille on pourrait mettre en place une vérification de la signature de l'image, ou encore une vérification de l'image complète en utilisant des librairies telle que pillow en python.
Si l'image possède une taille, elle est valide.