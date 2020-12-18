# Recherches

1. Upload d'un exploit php
2. Via BrupSuite change the MIME type to `image/jpeg`

> FLAG: 46910D9CE35B385885A9F7E2B336249D622F29B267A1771FBACF52133BEDDBA8

# Explications

Ce type de vulnerabilite permet a l'attaquant d'uploader n'importe quel type d'exploit directement sur le serveur.
Ensuite il est possible d'executer l'exploit grace a d'autres techniques.
Tout deviens possible pour l'attauant, escalation de privileges, suppression de tous les fichiers, ... 

# Corrections

Pour corriger cette faille on pourrait mettre en place une verification de la signature de l'image, ou encore une verification de l'image complete en utilisant des librairies tel que pillow en python.
Si l'image possede une taille, elle est valide.
