# Recherches

1. En utilisant les outils de developeurs sur le navigateur on verifie les cookies
2. Cookie suspect `I_am_admin` contenant `68934a3e9455fa72420237eb05902327` soit `false` en MD5
3. On remplace cette valeur par `md5(true) = b326b5062b2f0e69046810717534cb09`

> FLAG: df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3

# Corrections

Pour eviter ce type d'attaque on peut:
     - utiliser des sessions contenant des caracteres aleatoires de cette facon il est plus dificile de deviner la clef
     - generer des sessions temporaires apres chaque connexions


