# Recherches

Le listing des tables SQL laisse apparaître `Member_Brute_Forceid_comment` ce qui laisse à penser que du bruteforce est nécessaire, néanmoins cette db contient le mot de passe pour admin et root `3bf1114a986ba87ed28fc1b5884fc2f8` en utilisant un decrypter en ligne on obtient le mot de passe `shadow`, qui se trouve être le 65e mot de passe le plus utilise de 2020.

1. Pour réaliser une attaque par bruteforce il faut une liste de mots de passe (https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt)
2. Ecrire un script permettant le bruteforce
   - soit en utilisant le site pour vérifier
   - soit en utilisant le hash récupérer suite à une attaque
3. Connexion

> FLAG: B3A6E43DDF8B4BBB4125E5E7D23040433827759D4DE1C04EA63907479A80A6B2

# Corrections

Un moyen simple de réduire les risques liés au bruteforce est d'utiliser des méthodes de hashages plus lentes et plus complexes que MD5 ou SHA1. Bcrypt serait une meilleure option.
Le second moyen est de demander à l'utilisateur de définir un mot de passe plus complexe.
Finalement s'il n'y a pas de fuites de base de données il est toujours possible de faire du bruteforce sur le formulaire en ligne. Pour réduire ce risque il est recommandé d'utiliser soit un captcha soit un WAF pouvant détecter les actions de scripts sur un site.