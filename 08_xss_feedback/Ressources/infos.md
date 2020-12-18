# Recherches

1. Envoi d'un commentaire contenant du html
2. Le commentaire affiché n'est pas echape une attaque XSS est possible
3. Envoi du payload suivant `<script>alert(1)</script>`

> FLAG: 0FBB54BBF7D099713CA4BE297E1BC7DA0173D8B3C21C1811B916A3A86652724E

# Explications

Les failles XSS existent dès lors qu'un utilisateur peut envoyer du texte non verifié qui sera affiché ensuite sur le site. Si l'utilisateur envoie du code HTML le navigateur va l'interpréter une fois affiché sur le site.

# Corrections

Pour éviter les failles XSS il suffit d'échapper ou de nettoyer le texte avant de l'afficher sur le site ou de le stocker en DB.