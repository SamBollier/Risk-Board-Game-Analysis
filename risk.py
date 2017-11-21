#Uses Monte Carlo simulation to estimate the likelihood that an attack in the game of Risk will succeed in eliminating the defense.
#User enters three inputs when running the program. 1: the number of attacking troops; 2: the number of defending troops; and 3: the number of iterations to simulate.

import sys
import time
import random

attack = int(sys.argv[1])
defend = int(sys.argv[2])
runs = int(sys.argv[3])
attackwins = 0
defendwins = 0

for a in range(1, runs):
    attack = int(sys.argv[1])
    defend = int(sys.argv[2])
    while(attack > 1 and defend != 0):
        a1=0
        a2=0
        a3=0
        d1=0
        d2=0
        if(defend>1 and attack>3):
            a1=random.randint(1,6)
            a2=random.randint(1,6)
            a3=random.randint(1,6)
            d1=random.randint(1,6)
            d2=random.randint(1,6)
        else:
            if(defend>1 and attack>2):
                a1=random.randint(1,6)
                a2=random.randint(1,6)
                d1=random.randint(1,6)
                d2=random.randint(1,6)        
            else:
                if(defend>1 and attack>1):
                    a1=random.randint(1,6)
                    d1=random.randint(1,6)
                    d2=random.randint(1,6)        
                else:
                    if(defend>0 and attack>3):
                        a1=random.randint(1,6)
                        a2=random.randint(1,6)
                        a3=random.randint(1,6)
                        d1=random.randint(1,6)
                    else:
                        if(defend>0 and attack>2):
                            a1=random.randint(1,6)
                            a2=random.randint(1,6)
                            d1=random.randint(1,6)
                        else:
                            if(defend>0 and attack>1):
                                a1=random.randint(1,6)
                                d1=random.randint(1,6)

        if(defend>1 and attack > 2):
            if(max(a1, a2, a3) > max(d1, d2)):
                defend -= 1
                if(max(a1, a2, a3) == a1):
                    a1 = 0
                if(max(a1, a2, a3) == a2):
                    a2 = 0
                if(max(a1, a2, a3) == a3):
                    a3 = 0
                if(max(d1, d2) == d1):
                    d1 = 0
                if(max(d1, d2) == d2):
                    d2 = 0
                if(max(a1, a2, a3) > max(d1, d2)):
                    defend -= 1
                else:
                    attack -= 1
            else:
                attack -= 1
                if(max(a1, a2, a3) == a1):
                    a1 = 0
                if(max(a1, a2, a3) == a2):
                    a2 = 0
                if(max(a1, a2, a3) == a3):
                    a3 = 0
                if(max(d1, d2) == d1):
                    d1 = 0
                if(max(d1, d2) == d2):
                    d2 = 0
                if(max(a1, a2, a3) > max(d1, d2)):
                    defend -= 1
                else:
                    attack -= 1
        else:
            if(defend == 1 and attack > 2):
                if(max(a1, a2, a3) > max(d1, d2)):
                    defend -= 1
                else:
                    attack -= 1
            if(defend == 1 and attack == 2):
                if(max(a1, a2, a3) > max(d1, d2)):
                    defend -= 1
                else:
                    attack -= 1
            if(defend > 1 and attack == 2):
                if(max(a1, a2, a3) > max(d1, d2)):
                    defend -= 1
                else:
                    attack -= 1
    if(defend == 0):
        attackwins += 1
    else:
        defendwins += 1
print("Probability of attack win: " + str(round(100*float(attackwins/(attackwins+defendwins)), 2)) + " percent.")
