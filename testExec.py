# Testing module for all feautures

from Collection import collection
import time
from DuplicateEntryException import DuplicateEntryException
from EntryNoExistsException import EntryNoExistsException

myPasswords = collection()

# data entry for testing
try:
    myPasswords.addEntry('Facebook', 'pippo', '1234')
    myPasswords.addEntry('Instagram', 'pippo', '4567')
    myPasswords.addEntry('PornHub', 'pippo', '5432')
    myPasswords.addEntry('PornHub', 'gino', '5432')   # exception test
except DuplicateEntryException as e:
    print(e.value)

print('Collection size: ', myPasswords.getSize())

# show services list for choosing
print('Type the name of website to copy login informations.')
myPasswords.printAll()

src=input()   # search key from user

# copying user and password to clipboard and wait 15 (for both) seconds to paste it anywhere
# if the entry given by parameter doesn't exists in the collection, the execution will be interrupted
try:
    myPasswords.copyUsr(src)
except EntryNoExistsException as e1:
    print(e1.value)
    exit()

print('The userID will be on the clipboard for 15 seconds...')
time.sleep(15)


myPasswords.copyPsw(src)
print('Now you can paste your password')
print('Program will be closed in 15 seconds...')
time.sleep(15)

myPasswords.addEntry('Twitter','Carmelo','admin')
myPasswords.printAll()

# edit password testing
try:
    myPasswords.editPass('PornHub')
    myPasswords.copyPsw('PornHub')
    print('The password will be on the clipboard for 15 seconds...')
    time.sleep(15)
except EntryNoExistsException as e2:
    print(e2.value)    

# edit user testing
try:    
    myPasswords.editUser('Facebook')
    myPasswords.copyUsr('Facebook')
    print('The userID will be on the clipboard for 15 seconds...')
    time.sleep(15)
except EntryNoExistsException as e3:
    print(e3.value)

# remove entry testing
try:
    myPasswords.removeEntry('Instagram')
    myPasswords.printAll()
except EntryNoExistsException as e4:
    print(e4.value)