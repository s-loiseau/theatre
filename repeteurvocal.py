#!/usr/bin/env python3
# Read text files, with pauses for comedy learning.

import os
import sys

VOICE=False
AUTO=False
ROLE="DAVID:"
roleother=False

PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

colorline=""

if len(sys.argv) < 2:
    print("ERROR, give filename to read.")
    sys.exit()

scene=sys.argv[1]
if not os.path.isfile(scene):
    print("ERROR, file not found")
    sys.exit()

if "voice" in sys.argv:
    VOICE=True

if "auto" in sys.argv:
    AUTO=True


os.system('clear')

counter=0
with open(scene,'r') as fh:
    for line in fh.readlines():
        line = line.strip()
        if line.startswith('__'):
            print(DARKCYAN,"     ",line,END)
        elif line in ["LOUIS:","DAVID:","CLAIRE:"]:
            if line != ROLE:
                roleother=True
            else:
                roleother=False

            colorline=CYAN
            if line.startswith('LOUIS'):
                counter+=1
                #os.system('clear')
            elif line.startswith('DAVID'):
                colorline=PURPLE
                if not AUTO:
                    input()
            print(BOLD,YELLOW,counter,line,END)
        else:
            if not line.isupper():
                print(BOLD,colorline,line,END)
                if VOICE and roleother:
                    os.system(f'espeak-ng -v fr "{line}"')
            else:
                print(line)

