from Entry import entry
from DuplicateEntryException import DuplicateEntryException
from EntryNoExistsException import EntryNoExistsException
import pyperclip

pyperclip.init_osx_pbcopy_clipboard() # you can modify this for working in different OS

class collection:

    def __init__(self):
        self.entries = list()
        self.size = 0

    def addEntry(self, svc, usr, psw):
        if self.size == 0:
            new = entry(svc, usr, psw)
            self.entries.append(new)
            self.size = 1
            print('New entry created succesfully ', new.service)
        else:
            for elt in self.entries:
                tmp = elt.getSvc()
                if tmp == svc:
                    raise DuplicateEntryException('Service name already exists!')
            new = entry(svc, usr, psw)
            self.entries.append(new)
            self.size = self.size + 1
            print('New entry created succesfully ', new.getSvc())

    def printAll(self):
        print('SERVICES LIST: ')
        for elt in self.entries:
            print('WEBSITE: ', elt.getSvc())

    def removeEntry(self, svc):
        ch = False
        for elt in self.entries:
            if elt.service == svc:
                ch = True
                self.entries.remove(elt)
                self.size = self.size - 1
        if ch == False:
            raise EntryNoExistsException('No entry to delete!')

    def editUser(self, svc):
        ch = False
        for elt in self.entries:
            if elt.getSvc() == svc:
                ch = True
                elt.editUsr()
        if ch == False:
            raise EntryNoExistsException('No entry to edit!')

    def editPass(self, svc):
        ch = False
        for elt in self.entries:
            if elt.getSvc() == svc:
                ch = True
                elt.editPsw()
        if ch == False:
            raise EntryNoExistsException('No entry to edit!')

    def copyUsr(self, svc):
        ch = False
        for elt in self.entries:
            if elt.getSvc() == svc:
                ch = True
                pyperclip.copy(elt.getUsr())
        if ch == False:
            raise EntryNoExistsException('No entry present whith this name!')

    def copyPsw(self, svc):
        ch = False
        for elt in self.entries:
            if elt.getSvc() == svc:
                ch = True
                pyperclip.copy(elt.getPsw())
        if ch == False:
            raise EntryNoExistsException('No entry present whith this name!')

    def getSize(self):
        return self.size
