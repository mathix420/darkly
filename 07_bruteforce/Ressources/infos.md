# Recherches

Le listing des tables SQL laisse apparaitre `Member_Brute_Forceid_comment` ce qui laisse a pense que du bruteforce est necessaire, neanmoins cette db contient le mot de passe pour admin et root `3bf1114a986ba87ed28fc1b5884fc2f8` en utilisant un decrypter en ligne on obtient le mot de pass `shadow`, qui se trouve etre le 65e mot de passe le plus utilise de 2020.

1. Pour realiser une attaque par brute force il faut une liste de mots de passe (https://nordpass.com/most-common-passwords-list/)
2. Ecrire un script permettant le bruteforce
   - soit en utilisant le site pour verifier
   - soit en utilisant le hash recuperer suite a une attaque
3. Connexion

> FLAG: B3A6E43DDF8B4BBB4125E5E7D23040433827759D4DE1C04EA63907479A80A6B2

# Corrections

Un moyen simple de mitiger les risques lies au bruteforce est d'utiliser des methodes de hashages plus lentes et plus complexes que MD5 ou SHA1. Bcrypt serait une meilleur option.
Le second moyen est de demander a l'utilisateur de definir un mot de passe plus complexe.
Finalement si il n'y a pas de fuites de base de donnees il est toujours possible de faire du bruteforce sur le formulaire en ligne. Pour mitiger ce risque il est recommander d'utiliser soit un captcha soit un WAF pouvant detecter les actions de scripts sur un site.