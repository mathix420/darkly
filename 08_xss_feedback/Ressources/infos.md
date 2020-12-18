# Recherches

1. Envoie d'un commentaire contenant du html
2. Le commentaire afficher n'est pas echape une attaque XSS est possible
3. Envoie du payload suivant `<script>alert(1)</script>`

> FLAG: 0FBB54BBF7D099713CA4BE297E1BC7DA0173D8B3C21C1811B916A3A86652724E

# Explications

Les failles XSS existes des lors qu'un utilisateur peut envoyer du texte non verifier qui sera afficher ensuite sur le site. Si l'utilisateur envoie du code HTML le navigateur va l'interprerter une fois afficher sur le site.

# Corrections

Pour eviter les failles XSS il suffi d'echapper ou nettoyer le texte avant de l'afficher sur le site ou de le stocker en DB.


