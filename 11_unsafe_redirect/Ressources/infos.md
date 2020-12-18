# Recherches

1. En cliquant sur les réseaux sociaux dans le footer
2. On remarque que le site nous redirige dessus
3. En changeant le paramètre `site` de la requête on peut donc rediriger sur n'importe quel site

> FLAG: B9E775A0291FED784A2D9680FCFAD7EDD6B8CDF87648DA647AAF4BBA288BCAB3

# Explications

Ce type d'attaques peut être utilisé afin de rediriger l'utilisateur sur un site de phishing.

# Corrections

Pour éviter cette vulnérabilité il aurait suffi de vérifier le paramètre GET avant de rediriger.