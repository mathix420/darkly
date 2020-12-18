# Recherches

1. En utilisant les outils de développeurs sur le navigateur on vérifie les cookies
2. Cookie suspect `I_am_admin` contenant `68934a3e9455fa72420237eb05902327` soit `false` en MD5
3. On remplace cette valeur par `md5(true) = b326b5062b2f0e69046810717534cb09`

> FLAG: df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3

# Corrections

Pour éviter ce type d'attaque on peut :
     - utiliser des sessions contenant des caractères aléatoires de cette façon il est plus difficile de deviner la clef
     - générer des sessions temporaires après chaque connexion