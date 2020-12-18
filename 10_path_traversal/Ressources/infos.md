# Recherches

1. On remarque que les URL du site sont gérés via un paramètre GET `page=`
2. En supposant que le serveur utilise ce paramètre pour définir le chemin de la page à retourner on peut accéder à d'autres fichiers que les pages s'il n'y a pas de securités en place
3. Un des fichiers les plus intéressants est `/etc/passwd` car il contient les mots de passe du serveur. Ce fichier se trouve à la racine, il faut donc descendre.
4. `?page=../../../../../../../../../etc/passwd` nous permet d'atteindre le fichier


> FLAG: b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0


# Corrections

Vérifier que le fichier pointé par le path du paramètre est bien dans un dossier prédéfini ne contenant que les pages visitables.