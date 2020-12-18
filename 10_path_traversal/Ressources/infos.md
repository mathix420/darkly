# Recherches

1. On remarque que les URL du site sont gerer via un parametre GET `page=`
2. En supposant que le serveur utilise ce parametre pour definir le chemin de la page a retourner on peut acceder a d'autres fichiers que les pages si il n'y a pas de securites en place
3. Un des fichier les plus interresant est `/etc/passwd` car il contient les mots de passe du serveur. Ce fichier se trouve a la racine il faut donc descendre.
4. `?page=../../../../../../../../../etc/passwd` nous permet d'atteindre le fichier


> FLAG: b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0


# Corrections

Verifier que le fichier pointer par le path du parametre est bien dans un dossier predefini ne contenant que les pages visitables.
