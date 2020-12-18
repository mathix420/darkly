# Recherches

1. En cliquant sur la dernière image de la NSA sur la page d'accueil on arrive sur une page affichant un média
2. En regardant l'URL on peut remarquer que la source est indiquée via le paramètre `src` qui est utilisé dans un object image HTML
3. Si son utilisation n'est pas protégée (ce qui est le cas ici) on peut faire du XSS
4. Payload:
   ```
   <script>alert(1)</script>
   ```
5. Base64: `PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==`
6. GET request: `/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==`

> FLAG: 928D819FC19405AE09921A2B71227BD9ABA106F9D2D37AC412E9E5A750F1506D

# Explications

Encore une faille XSS, cette fois dans l'URL, elle pourrait permettre de récupérer des cookies de sessions.

# Corrections

Pour éviter cette vulnérabilité on pourrait utiliser une bdd et donc des ids qui pointeraient sur une image spécifique.