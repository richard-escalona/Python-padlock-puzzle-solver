#!/usr/bin/env python3
import sys
import re
clues =sys.argv[1:]

#return error if there is no clues entered
if len(clues) == 0:
    print("ERROR: Must provide at least one pattern of the form XYZ-R-W")
    exit()
# print out all clues  (function .join will combine str)
print("Trying", " ".join(clues))

# regex validation for the clues
for clue in clues:
    if re.match('^\d\d\d-[0123]-[0123]$', clue) is None:
        print ("ERROR: invalid agument:", clue)
        exit()

# define the valid digits.
numRange = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# traverse through all possible passwords
possiblePassWords = []
for x in numRange:
    for y in numRange:
        for z in numRange:
           # boolean var to check which password is good
            good_password = True

        # Main Logic Sudo Code
            # X == A                   ->rights += 1
            # X == B or X==C     -> wrong+=1
            # split up the input     rights = 0, wrongs = 1
            # 8 != 5
            # 8 != 7 and 8 == 8

            # 7 != 7                 rights = 1, wrongs = 1
            # 7 != 5 or 7 != 8 
            # starting loop to check what the clues
            for clue in clues:
                clueXYZ, clueR, clueW = clue.split("-")
                r = 0
                w = 0

                # first case x == clue[0] r++  else if y==clue[0] or z==clue[0] w++
                if x == clueXYZ[0]: 
                   r += 1
                elif y == clueXYZ[0] or z == clueXYZ[0]:
                   w += 1
                # first case y == clue[1] r++  else if z==clue[1] or x==clue[1] w++
                if y == clueXYZ[1]: # or x == y or x == z or y == z:
                   r += 1
                elif x == clueXYZ[1] or z == clueXYZ[1]:
                   w += 1

                # third case  z == clue[2] r++  else if x==clue[2] or y==clue[2] w++
                if z == clueXYZ[2] :
                   r += 1
                elif x == clueXYZ[2] or y == clueXYZ[2]:
                    w += 1

                  # r does not equal clueR then it would not be a good PW. Do same for clueW
                if  r != int(clueR) or w != int(clueW) :
                         good_password = False
            #store in possiblepasswords once it passed the clues.    
            if good_password:
             possiblePassWords.append(x+y+z)
passwordCount = len(possiblePassWords)

 # incase there are no solutions
if passwordCount == 0:
    print("No solution found.")
    exit()
    # When only one solution exist
elif passwordCount == 1:
     print("*** Solution #1 is ...                 (there is exactly one answer, which has been hidden)")
     exit()

#finally print the passwords
# loop through starting at one.
for i in range(passwordCount):
    currentPassword = possiblePassWords[i]
    print("*** Solution #{} is {}".format(i+1, currentPassword))
