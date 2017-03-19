'''
Emulator-arm binary patcher to change hardcoded IMEI,
IMSI, phone number and Network Operator to mitigate emulator detection

Usage: python replace.py emu_in emu_out
emu_in - your emulator-arm binary
DONT FORGET TO BACKUP IT
'''

import sys
import  random
from string import ascii_letters, digits
with open(sys.argv[1], 'r+b') as old, open(sys.argv[2], 'wb') as new:
    for line in old:
        if line.find('+CRSM: 144,0,fffffff') > 1:
            print 'found phone number'
            oldp = line[line.find('+CRSM: 144,0,ff') + 53 :line.find('+CRSM: 144,0,ff') + 59]
            newp= ''
            for i in range(6):  # Generate new phone Number
                newp += str(random.randint(1,9))
            print 'new phone number is ', newp
            line = line.replace(oldp, newp)
        if line.find('+CGSN') > 1:
            print 'found IMEI'
            oldp= line[line.find('+CGSN') + 6 :line.find('+CGSN') + 21]
            newp = ''
            for i in range(15):  # Generate new IMEI Number
                newp += str(random.randint(1,9))
            print 'new IMEI number is ', newp
            line = line.replace(oldp, newp)
        if line.find('+CIMI') > 1:
            print 'found IMSI'
            oldp= line[line.find('+CIMI') + 6 :line.find('+CIMI') + 21]
            newp = ''
            for i in range(15):  # Generate new IMSI Number
                newp += str(random.randint(1,9))
            print 'new IMSI number is ', newp
            line = line.replace(oldp, newp)
        if line.find('TelKila') > 1:
            print 'found Network Operator'
            oldp= line[line.find('TelKila') - 58 :line.find('TelKila') - 51]
            newp = ''
            for i in range(7):  # Generate new Network provider
                newp += str(random.choice(ascii_letters + digits))
            print 'new Network Provider is ', newp
            line = line.replace(oldp, newp)
        new.write(line)
