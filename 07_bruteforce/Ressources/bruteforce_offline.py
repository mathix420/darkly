import hashlib

HASH = input('HASH:')
DIC = input('DIC PATH:')

with open(DIC) as fp:
    dictionnary = fp.read()

for password in dictionnary.split('\n'):
    hashed = hashlib.md5(password.encode()).hexdigest()

    if hashed == HASH:
        print(password)
        break
