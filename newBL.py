import hashlib
import os
def newBaseline():
    
    files = os.listdir('CF2')
    con_for_hashing = []

    def getHash(path):
        sha512 = hashlib.sha512()
        with open(path,'rb') as file:
            hash = file.read()
            sha512.update(hash)
            return sha512.hexdigest()
    
    for x in files:
        txt = 'CF2/' + x
        con_for_hashing.append( f'CF2/{x} | {getHash(txt)}')
    with open('baseline.txt','w') as bl:
        for x in con_for_hashing:
            bl.write(x+'\n')


