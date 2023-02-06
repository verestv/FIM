import hashlib
import time
import os
from colorama import Fore,Style

def integrity_monitoring():
    #open created baseline and read content , then add it to list 
    with open('baseline.txt','r') as bl:
        hashes = bl.readlines()
    check_list = [x.strip() for x in hashes]
    #create a dict with file names and hashes 
    check_hashes = {}
    for x in check_list:
    
        check_hashes[x.split(' | ')[0]] = x.split(' | ')[1]
    #func for monitoring
    def Monitor():
        files = os.listdir('CF2') #get all files from specisific directory to a list
        new_hashes = []
        #func for setting a hash
        def getHash(path):
            sha512 = hashlib.sha512()
            with open(path,'rb') as file:
                hash = file.read()
                sha512.update(hash)
                return sha512.hexdigest()
        for x in files:
            txt = 'CF2/' + x
            new_hashes.append( f'CF2/{x} | {getHash(txt)}') #create new list with new hashes
        check_new_hashes = {}
        for x in new_hashes:
            check_new_hashes[x.split(' | ')[0]] = x.split(' | ')[1] 
    #alerts
        
        for v in check_new_hashes.values():
            if v not in check_hashes.values() and len(check_hashes) == len(check_new_hashes):
                key = list(filter(lambda x: check_new_hashes[x]==v,check_new_hashes))[0]
                print(f'{Style.BRIGHT}{Fore.RED}{key} has been changed!{Style.RESET_ALL}')  

        for k in check_new_hashes.keys():
            if k not in check_hashes:
                print(f'{Style.BRIGHT}{Fore.LIGHTWHITE_EX}{k} has been created!{Style.RESET_ALL}')
                
        for k in check_hashes.keys():
            if k in check_new_hashes:
                pass
            else:
                print(f"{Style.BRIGHT}{Fore.YELLOW}{k} has been deleted!{Style.RESET_ALL}")

    while True:
        time.sleep(1)
        Monitor()
    
        











        
