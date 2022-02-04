from bitcash import *
from bitcash.format import bytes_to_wif
import random
import atexit
import time
from colorama import Fore, Style

print("Start ...")
print(" Official WebSite : https://Mmdrza.com")

count = 0
total = 0
while True:
    x = 0x0000000000000000000000000000000000000000000000000000000000000001
    y = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364140
    ran = random.randint(x, y)
    seed = str(ran)
    key = Key.from_int(ran)
    wif = bytes_to_wif(key.to_bytes(), compressed=False)
    wif2 = bytes_to_wif(key.to_bytes(), compressed=True)
    key1 = Key(wif)
    privkey = key.to_hex()
    privkey2 = key1.to_hex()
    caddr = key.address # For Compressed Address
    uaddr = key1.address # For UNCompressed Address
    bal = key.get_balance('bch')
    bal2 = key1.get_balance('bch')
    count += 1
    total += 2
    #=============================================
    print("=============================================")
    print(Fore.YELLOW+"\nCurrent PrivateKey --> "+seed)
    print(Fore.GREEN+"Compressed Address : "+Fore.LIGHTGREEN_EX+caddr+Style.RESET_ALL)
    print("Private Key : "+privkey)
    print(Fore.RED+"WIF : "+wif2+Fore.CYAN+"  |BAL : "+Style.RESET_ALL+bal)
    print("-----------------------------")
    print(Fore.GREEN+"Uncompressed Address : "+Fore.LIGHTGREEN_EX+uaddr+Style.RESET_ALL)
    print("Private Key : "+privkey2)
    print(Fore.RED+"WiF : "+wif+Fore.CYAN+"  |BAL : "+Style.RESET_ALL+bal2)
    print(Fore.YELLOW+"Scan Number : "+Fore.WHITE+str(count)+Fore.MAGENTA+" Total Wallet : "+Fore.WHITE+str(total))
    time.sleep(1.24)
    if int(bal) > 0:
        print('Found Found Found Found Found Found Found Found Found Found Found Found ')
        print('Ethereum ETH Address           :  ', caddr, '  : VALUE      = ', str(bal))
        print('Found Found Found Found Found Found Found Found Found Found Found Found ')
        f = open("winner.txt", "a")
        f.write('\nPrivate key:' + key.to_hex())
        f.write('\n Bch Address: ' + caddr + '  : TX      = ' + str(wif) + '\n')
        f.close()
        continue
    if int(bal2) > 0:
        print('Found Found Found Found Found Found Found Found Found Found Found Found ')
        print('Ethereum ETH Address           :  ', uaddr, '  : VALUE      = ', str(bal))
        print('Found Found Found Found Found Found Found Found Found Found Found Found ')
        f = open("winner.txt", "a")
        f.write('\nPrivate key:' + key1.to_hex())
        f.write('\n Bch Address: ' + caddr + '  : TX      = ' + str(wif) + '\n')
        f.close()
        continue