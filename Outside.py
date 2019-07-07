hunger = 30
atk2 = 1
atk1 = 1
hp2 = 30
hp1 = 1
xpn = 20
xp = 0
xpg = 20
fullhp = 1
lvl2 = 1
lvl = 1
im = 0
send = 1
while True:
    import os
    import random
    import time
    os.system('cls')
    os.system('color 03')
    print('_________________________________________________________________________________________________________________________                                                                                                                  ')
    print('|                 |                  |                   |                   |                    |                     |                ')
    print('|      _____      |                  |                   |                   |                    |                     |                 ')
    print('|     /     \     |  ==============  |        ____       |       _____       |       _______      |      __________     |                                                                            ')
    print('|    |       |    |  | ... .      |  |       /    \      |      /     \      |      /       \     |     /          \__  |                                                            ')
    print('|    |       |    |  |            |  |     -|      |-    |     |       |     |     | __      |    |    |            __| |                                                   ')
    print('|     \_____/     |  |  __        |  |     -|      |-    |     |       |     |     |/ne\     |    |    \__  _  _   /    |                                                                                 ')
    print('|       | |       |  | /  \   __  |  |     -|      |-    |     |       |     |     |\__/     |    |      / // / / /     |                                                              ')
    print('|       | |       |  | |va|  /ne\ |  |     -|      |-    |     |        \    |     |     <==>|    |      ^^ ^^  ^^      |                                                        ')
    print('|       | |       |  | \   \ \__/ |  |     -|      |-    |     |         |   |     |         |    |                     |                                                     ')
    print('|   |\  | |  /|   |  |  \__/      |  |     -|      |-    |      \_______/    |      \_______/     |                     |                                                                 ')
    print('|   | \ | | / |   |  | .   . <==> |  |       \____/\     |                   |                    |                     |                                              ')
    print('|   |  \| |/  |   |  |   .     .  |  |       / || \ \  / |                   |                    |                     |                                              ')
    print('|   |   \_/   |   |  ==============  |      | / |  \ \/  |                   |                    |                     |                                            ')
    print('|   |         |   |                  |    \/ |  |   \    |                   |                    |                     |             ')
    print('|                 |                  |       |   \   \   |                   |                    |                     |              ')
    print('|  Bacteriophage  |    plant cell    |      bacteria     |       Archea      |     animal cell    |       complex       |')
    print('-------------------------------------------------------------------------------------------------------------------------                                                                                                                  ')
    f = input("choose your fighter: ")
    if f == 'bacteriophage':
        from playsound import playsound
        send -= 2000
        os.system('cls')
        os.system('color 04')
        print("           Bacteriophages            ")
        print('______________________________________                                                                                                                  ')
        print('|                 |                 |')
        print('|      _____      |                 |')
        print('|     /     \     |                 |')
        print('|    |       |    |                 |')
        print('|    |       |    |                 |')
        print('|     \_____/     |       _____     |')
        print('|       | |       |      /     \    |')
        print('|       | |       |     |       |   |')
        print('|       | |       |     |       |   |')
        print('|   |\  | |  /|   |      \_____/    |')
        print('|   | \ | | / |   |    |\  | |  /|  |')
        print('|   |  \| |/  |   |    | \ | | / |  |')
        print('|   |   \_/   |   |    |  \|_|/  |  |')
        print('|   |         |   |    |         |  |')
        print('|                 |                 |')
        print('|  Lambda phage   |  Streptococcus  |')
        print('|                 |     phage C1    |')
        print('-------------------------------------')
        f = input('choose a phage type: ')
        if f == 'lambda phage':
            fhunger = 30
            atk2 = 25
            atk2l = atk2 + lvl2 / 2
            fullhp = 30
            fullhpl = fullhp + lvl / 1.5
            fhp2 = 30
            atk = 20
            fhp2l = fhp2 + lvl2 / 1.5
            hp2 = fhp2l
            hp1 = fullhpl
            lvl = 1
            xp = 0
            hunger = fhunger
            xpn = 20
            xpg = 20
            m = 1
            lvl2 = random.randint(1, m)
            offspring = 0
            qu2 = 1
            im = 0
            x1 = ''
            x2 = ''
            x3 = ''
            x4 = ''
            x5 = ''
            x6 = ''
            s = 0
            l = 1
            while qu2 > 0:
                hp1 = fullhpl
                if lvl == 10 and l == 1:
                    s += 1
                    l -= 1
                else:
                    print('')
                print('')
                if lvl == 10 and s == 1:
                    print('congrats! you have mutated the "anti imu" trait!')
                    print("you can now fight against the bacteria that immuned themself's against you")
                    print('those bacteria are worth more xp but are a bit harder')
                    im += 1
                    s -= 1
                else:
                    print('')
                print('')
                if hunger < 0 or hp1 < 0 or hp1 == 0 or hunger == 0:
                    input('game over: ')
                    qu2 -= 1231
                else:
                    os.system('color 07')
                    os.system('cls')
                    hunger -= 1
                    if xp == xpn or xp > xpn:
                        print('level up!')
                        playsound('levelup.wav')
                        input('press enter to continue: ')
                        lvl += 1
                        xpn += 20
                        fullhp += lvl / 1.5
                        atk += lvl / 2
                        m += 1
                        xpg += lvl 
                        xp = 0
                    else:
                        print("")
                    os.system('color 07')
                    print('')
                    print("  Bacteriophages  ")
                    print('___________________                                                                                                                  ')
                    print('|                 |')
                    print('|      _____      |')
                    print('|     /     \     |')
                    print('|    |       |    |')
                    print('|    |       |    |')
                    print('|     \_____/     |')
                    print('|       | |       |')
                    print('|       | |       |')
                    print('|       | |       |')
                    print('|   |\  | |  /|   |')
                    print('|   | \ | | / |   |')
                    print('|   |  \| |/  |   |')
                    print('|   |   \_/   |   |')
                    print('|   |         |   |')
                    print('|                 |')
                    print('|  Lambda phage   |')
                    print('|                 |')
                    print('-------------------')
                    print(" current organism  ")
                    print('___________________')
                    print("| 1- explore      |")
                    print("+-----------------+")
                    print("| 2- check statts |")
                    print("+-----------------+")
                    e = input('what do you wanna do: ')
                    if e == '1':
                        x = random.randint(0, 8)
                        if x == 1 or x == 2 or x == 3:
                            os.system('cls')
                            input("enemy spotted!")
                            qu = 2
                            lvl2 = random.randint(1, m)
                            fhp2 = 30
                            fhp2l = fhp2 + lvl2 / 1.5
                            hp2 = fhp2l
                            atk2 = 25
                            atk2l = atk2 + lvl2 / 2
                            fullhp = 30
                            fullhpl = fullhp + lvl / 1.5
                            hp1 = fullhpl
                            
                            while qu > 0:
                                if hp2 < 0 or hp2 == 0:
                                    print('you won! XP +',xpg,' colonize lifespan = full offspring + 10')
                                    playsound('victory1.wav')
                                    xp += xpg
                                    hunger = fhunger
                                    offspring += 10
                                    qu -= 1281839819
                                elif hp1 < 0 or hp1 == 0:
                                    input('you lost...')
                                    input('press enter to continue: ')
                                    qu -= 10001090
                                    qu2 -= 98989
                                else:
                                    os.system('cls')
                                    os.system('color 9')
                                    print('     lvl: ',lvl2)
                                    print('     hp2: ',hp2)
                                    print('_____________________                                                                                                                 ')
                                    print('|                   |                    ')
                                    print('|                   |                      ')
                                    print('|        ____       |                                                                                ')
                                    print('|       /    \      |                                                               ')
                                    print('|     -|      |-    |                                                   ')
                                    print('|     -|      |-    |                                                                                   ')
                                    print('|     -|      |-    |                                                                  ')
                                    print('|     -|      |-    |                                                            ')
                                    print('|     -|      |-    |                                                        ')
                                    print('|     -|      |-    |                                                                   ')
                                    print('|       \____/\     |                                                 ')
                                    print('|       / || \ \  / |                                                  ')
                                    print('|      | / |  \ \/  |                                            ')
                                    print('|    \/ |  |   \    |             ')
                                    print('|       |   \   \   |              ')
                                    print('|       E.coli      |')
                                    print('---------------------')
                                    print('         Vs         ')
                                    print('___________________')
                                    print('|                 |')
                                    print('|      _____      |')
                                    print('|     /     \     |')
                                    print('|    |       |    |')
                                    print('|    |       |    |')
                                    print('|     \_____/     |')
                                    print('|       | |       |')
                                    print('|       | |       |')
                                    print('|       | |       |')
                                    print('|   |\  | |  /|   |')
                                    print('|   | \ | | / |   |')
                                    print('|   |  \| |/  |   |')
                                    print('|   |   \_/   |   |')
                                    print('|   |         |   |')
                                    print('|                 |')
                                    print('|  Lambda phage   |')
                                    print('|                 |')
                                    print('-------------------')
                                    print('     hp1: ',hp1)
                                    print('     lvl: ',lvl)
                                    print('your turn!')
                                    print('____________________   _____________________')
                                    print("| 1- J- sting      |   |  2- move          |")
                                    print('+------------------+   +-------------------+')
                                    print('')
                                    print(x1,x4)
                                    print(x2,x5)
                                    print(x3,x6)
                                    z1 = input('choose a move: ')
                                    if z1 == '1':
                                        d = random.randint(0, 4)
                                        if d == 2 or d == 1:
                                            os.system('cls')
                                            hp2 -= atk
                                            print("hit! damage: ",atk)
                                            playsound('phagehit1.wav')
                                            input("E.coli's turn!")
                                            d =  random.randint(0, 2)
                                            if d == 0 and hp2 < 10:
                                                input('E.coli uses move...')
                                                i = random.randint(0,4)
                                                if i == 1 or i == 2:
                                                    input('it worked!')
                                                    qu -= 100010
                                                if hp2 == 0 or hp2 < 0:
                                                    input('it failed')
                                                elif i == 0 or d == 3:
                                                    input('it failed')
                                            elif d == 1 or d == 0:
                                                input('E.coli uses infectious inject...')
                                                c = random.randint(0, 4)
                                                if c == 1:
                                                    hp1 -= atk2l
                                                    print('damage: ',atk2l)
                                                    playsound('phagehit1.wav')
                                                    input('press enter to continue: ')
                                                elif c == 4 or c == 2 or c == 3:
                                                    input("it didn't work")
                                             
                                                
                                        else:
                                            os.system('cls')
                                            input('damn missed!')
                                            input("E.coli's turn!")
                                            d =  random.randint(0, 2)
                                            if d == 0 and hp2 < 10:
                                                input('E.coli uses move...')
                                                i = random.randint(0,4)
                                                if i == 1 or i == 2:
                                                    input('it worked!')
                                                    qu -= 100010
                                                elif hp2 == 0 or hp2 < 0:
                                                    input('it failed')
                                                elif i == 0 or d == 3:
                                                    input('it failed')
                                            elif d == 1 or d == 0:
                                                input('E.coli uses infectious inject...')
                                                c = random.randint(0, 4)
                                                if c == 1:
                                                    hp1 -= atk2l
                                                    print('damage: ',atk2l)
                                                    playsound('phagehit1.wav')
                                                    input('press enter to continue: ')
                                                elif c == 0 or c == 2 or c == 3:
                                                    input("it didn't work")
                                    elif z1 == '2':
                                        d = random.randint(0, 4)
                                        if d == 2:
                                            os.system('cls')
                                            input("you tried to evade...")
                                            input('you escaped!')
                                            qu -= 100010
                                            input("E.coli's turn!")
                                            d =  random.randint(0, 2)
                                            if d == 0 and hp2 < 10:
                                                input('E.coli uses move...')
                                                i = random.randint(0,4)
                                                if i == 1 or i == 2:
                                                    input('it worked!')
                                                    qu -= 100010
                                                elif hp2 == 0 or hp2 < 0:
                                                    input('it failed')
                                                elif i == 0 or d == 3:
                                                    input('it failed')
                                            elif d == 1 or d == 0:
                                                input('E.coli uses infectious inject...')
                                                c = random.randint(0, 4)
                                                if c == 1:
                                                    hp1 -= atk2l
                                                    print('damage: ',atk2l)
                                                    input('press enter to continue: ')
                                                elif c == 0 or c == 2 or c == 3:
                                                    input("it didn't work")
                                        elif d == 3 or d == 1 or d == 0:
                                            os.system('cls')
                                            input("you tried to evade...")
                                            input("but it didn't work!")
                                            input("E.coli's turn!")
                                            d =  random.randint(0, 2)
                                            if d == 0 and hp2 < 10:
                                                input('E.coli uses move...')
                                                i = random.randint(0,4)
                                                if i == 1 or i == 2:
                                                    input('it worked!')
                                                    qu -= 100010
                                                elif i == 0 or d == 3:
                                                    input('it failed')
                                            elif d == 1 or d == 0:
                                                input('E.coli uses infectious inject...')
                                                c = random.randint(0, 4)
                                                if c == 1:
                                                    hp1 -= atk2l
                                                    print('damage: ',atk2l)
                                                    input('pres enter to continue: ')
                                                elif c == 0 or c == 2 or c == 3:
                                                    input("it didn't work")
                                    else:
                                        print('wrong input!')
                                        input("E.coli's turn!")
                                        d =  random.randint(0, 2)
                                        if d == 0 and hp2 < 10:
                                            input('E.coli uses move...')
                                            i = random.randint(0,4)
                                            if i == 1 or i == 2:
                                                input('it worked!')
                                                qu -= 100010
                                            elif hp2 == 0 or hp2 < 0:
                                                input('it failed!')
                                            elif i == 0 or d == 3:
                                                input('it failed!')
                                        elif d == 1 or d == 0:
                                            input('E.coli uses infectious inject...')
                                            c = random.randint(0, 4)
                                            if c == 1:
                                                hp1 -= atk2l
                                                print('damage: ',atk2l)
                                                input('press enter to continue: ')
                                            elif c == 0 or c == 2 or c == 3:
                                                input("it didn't work")
                            input("...")
                            
                                        
                                    
                                    
                        elif x == 7 and im == 1:
                            os.system('cls')
                            input("enemy spotted!")
                            qu = 2
                            lvl2 = random.randint(1, m)
                            fhp2 = 30
                            fhp2l = fhp2 + lvl2 / 1.5
                            hp2 = fhp2l
                            atk2 = 25
                            atk2l = atk2 + lvl2 / 2
                            fullhp = 30
                            fullhpl = fullhp + lvl / 1.5
                            hp1 = fullhpl
                            
                            while qu > 0:
                                from playsound import playsound
                                if hp2 < 0 or hp2 == 0:
                                    print('you won! XP + 20 hunger = full offspring + 10')
                                    playsound('victory1.wav')
                                    xp += xpg * 2
                                    hunger = fhunger
                                    offspring += 10
                                    qu -= 1281839819
                                elif hp1 < 0 or hp1 == 0:
                                    input('you lost...')
                                    input('press enter to continue: ')
                                    qu -= 10001090
                                    qu2 -= 98989
                                else:
                                    os.system('cls')
                                    os.system('color 4')
                                    print('     lvl: ',lvl2)
                                    print('     hp2: ',hp2 + lvl * 1.5)
                                    print('_____________________                                                                                                                 ')
                                    print('|                   |                    ')
                                    print('|                   |                      ')
                                    print('|        ____       |                                                                                ')
                                    print('|       /    \      |                                                               ')
                                    print('|     -|XXXXXX|-    |                                                   ')
                                    print('|     -|XXXXXX|-    |                                                                                   ')
                                    print('|     -|XXXXXX|-    |                                                                  ')
                                    print('|     -|XXXXXX|-    |                                                            ')
                                    print('|     -|XXXXXX|-    |                                                        ')
                                    print('|     -|XXXXXX|-    |                                                                   ')
                                    print('|       \____/\     |                                                 ')
                                    print('|       / || \ \  / |                                                  ')
                                    print('|      | / |  \ \/  |                                            ')
                                    print('|    \/ |  |   \    |             ')
                                    print('|       |   \   \   |              ')
                                    print('|  immune E.coli    |')
                                    print('---------------------')
                                    print('         Vs         ')
                                    print('___________________')
                                    print('|                 |')
                                    print('|      _____      |')
                                    print('|     /     \     |')
                                    print('|    |XXXXXXX|    |')
                                    print('|    |XXXXXXX|    |')
                                    print('|     \_____/     |')
                                    print('|       | |       |')
                                    print('|       | |       |')
                                    print('|       | |       |')
                                    print('|   |\  | |  /|   |')
                                    print('|   | \ | | / |   |')
                                    print('|   |  \| |/  |   |')
                                    print('|   |   \_/   |   |')
                                    print('|   |         |   |')
                                    print('|                 |')
                                    print('|  Lambda phage   |')
                                    print('|                 |')
                                    print('-------------------')
                                    print('     hp1: ',hp1)
                                    print('     lvl: ',lvl)
                                    print('your turn!')
                                    print('____________________   _____________________')
                                    print("| 1- J- sting      |   |  2- move          |")
                                    print('+------------------+   +-------------------+')
                                    print('')
                                    print(x1,x4)
                                    print(x2,x5)
                                    print(x3,x6)
                                    z1 = input('choose a move: ')
                                    if z1 == '1':
                                        d = random.randint(0, 4)
                                        if d == 2 or d == 1:
                                            os.system('cls')
                                            hp2 -= atk
                                            print("hit! damage: ",atk)
                                            playsound('phagehit1.wav')
                                            input("E.coli's turn!")
                                            d =  random.randint(0, 2)
                                            if d == 0 and hp2 < 10:
                                                input('E.coli uses move...')
                                                i = random.randint(0,4)
                                                if i == 1 or i == 2:
                                                    input('it worked!')
                                                    qu -= 100010
                                                elif i == 0 or d == 3:
                                                    input('it failed')
                                            elif d == 1 or d == 0:
                                                input('E.coli uses infectious inject...')
                                                c = random.randint(0, 4)
                                                if c == 1:
                                                    hp1 -= atk2l
                                                    print('damage: ',atk2l)
                                                    playsound('phagehit1.wav')
                                                    input('press enter to continue: ')
                                                elif c == 4 or c == 2 or c == 3:
                                                    input("it didn't work")
                                             
                                                
                                        else:
                                            os.system('cls')
                                            input('damn missed!')
                                            input("E.coli's turn!")
                                            d =  random.randint(0, 2)
                                            if d == 0 and hp2 < 10:
                                                input('E.coli uses move...')
                                                i = random.randint(0,4)
                                                if i == 1 or i == 2:
                                                    input('it worked!')
                                                    qu -= 100010
                                                elif i == 0 or d == 3:
                                                    input('it failed')
                                            elif d == 1 or d == 0:
                                                input('E.coli uses infectious inject...')
                                                c = random.randint(0, 4)
                                                if c == 1:
                                                    hp1 -= atk2l
                                                    print('damage: ',atk2l)
                                                    playsound('phagehit1')
                                                    input('press enter to continue: ')
                                                elif c == 0 or c == 2 or c == 3:
                                                    input("it didn't work")
                                    elif z1 == '2':
                                        d = random.randint(0, 4)
                                        if d == 2:
                                            os.system('cls')
                                            input("you tried to evade...")
                                            input('you escaped!')
                                            qu -= 100010
                                            input("E.coli's turn!")
                                            d =  random.randint(0, 2)
                                            if d == 0 and hp2 < 10:
                                                input('E.coli uses move...')
                                                i = random.randint(0,4)
                                                if i == 1 or i == 2:
                                                    input('it worked!')
                                                    qu -= 100010
                                                elif i == 0 or d == 3:
                                                    input('it failed')
                                            elif d == 1 or d == 0:
                                                input('E.coli uses infectious inject...')
                                                c = random.randint(0, 4)
                                                if c == 1:
                                                    hp1 -= atk2l
                                                    print('damage: ',atk2l)
                                                    playsound('phagehit1.wav')
                                                    input('press enter to continue: ')
                                                elif c == 0 or c == 2 or c == 3:
                                                    input("it didn't work")
                                        elif d == 3 or d == 1 or d == 0:
                                            os.system('cls')
                                            input("you tried to evade...")
                                            input("but it didn't work!")
                                            input("E.coli's turn!")
                                            d =  random.randint(0, 2)
                                            if d == 0 and hp2 < 10:
                                                input('E.coli uses move...')
                                                i = random.randint(0,4)
                                                if i == 1 or i == 2:
                                                    input('it worked!')
                                                    qu -= 100010
                                                elif i == 0 or d == 3:
                                                    input('it failed')
                                            elif d == 1 or d == 0:
                                                input('E.coli uses infectious inject...')
                                                c = random.randint(0, 4)
                                                if c == 1:
                                                    hp1 -= atk2l
                                                    print('damage: ',atk2l)
                                                    playsound('phagehit1.wav')
                                                    input('pres enter to continue: ')
                                                elif c == 0 or c == 2 or c == 3:
                                                    input("it didn't work")
                                    else:
                                        print('wrong input!')
                                        input("E.coli's turn!")
                                        d =  random.randint(0, 2)
                                        if d == 0 and hp2 < 10:
                                            input('E.coli uses move...')
                                            i = random.randint(0,4)
                                            if i == 1 or i == 2:
                                                input('it worked!')
                                                qu -= 100010
                                            elif i == 0 or d == 3:
                                                input('it failed')
                                        elif d == 1 or d == 0:
                                            input('E.coli uses infectious inject...')
                                            c = random.randint(0, 4)
                                            if c == 1:
                                                hp1 -= atk2l
                                                print('damage: ',atk2l)
                                                playsound('phagehit1.wav')
                                                input('press enter to continue: ')
                                            elif c == 0 or c == 2 or c == 3:
                                                input("it didn't work")
                            input("...")
                            
                        elif x == 4 or x == 5 or x == 6:
                            os.system('cls')
                            input('nothing special...')
                    elif e == '2':
                        os.system('cls')
                        print('hp: ',hp1)
                        print('colonize lifespan: ',hunger)
                        print('xp: ',xp)
                        print('lvl: ',lvl)
                        print('colonization: ',offspring)
                        print('atk: ',atk)
                        print('xp gainage every battle: ',xpg)
                        print('xp needed until next level: ',xpn - xp)
                        input('press enter to continue: ')
                    else:
                        os.system('cls')
                        os.system('color 8')
                        input('wrong input')
            input('Game end')
        else:
            os.system('cls')
            os.system('color 6')
            print('wrong input!')
        
        
    elif f == 'plant cell':
        os.system('cls')
        os.system('color A')
        input("plant cell")
    elif f == 'bacteria':
        from playsound import playsound
        os.system('cls')
        os.system('color B')
        print('_____________________')
        print('|                   |')
        print('|                   |')
        print('|        ____       |')
        print('|       /    \      |')
        print('|     -|      |-    |')
        print('|     -|      |-    |')
        print('|     -|      |-    |')
        print('|     -|      |-    |')
        print('|     -|      |-    |')
        print('|     -|      |-    |')
        print('|       \____/\     |')
        print('|       / || \ \  / |')
        print('|      | / |  \ \/  |')
        print('|    \/ |  |   \    |')
        print('|       |   \   \   |')
        print('|       E.coli      |')
        print('---------------------')
        ch2 = input('which one: ')
        if ch2 == 'E.coli' or ch2 == 'e.coli':
            fhunger = 20
            atk2 = 25
            atk2l = atk2 + lvl2 / 2
            fullhp = 30
            fullhpl = fullhp + lvl / 1.5
            fhp2 = 30
            atk = 25
            fhp2l = fhp2 + lvl2 / 1.5
            hp2 = fhp2l
            hp1 = fullhpl
            lvl = 1
            xp = 0
            hunger = fhunger
            xpn = 20
            xpg = 20
            m = 1
            lvl2 = random.randint(1, m)
            offspring = 1
            qu2 = 1
            im = 0
            x1 = ''
            x2 = ''
            x3 = ''
            x4 = ''
            x5 = ''
            x6 = ''
            s = 0
            l = 1
            while qu2 > 0:
                hp1 = fullhpl
                if lvl == 10 and l == 1:
                    s += 1
                    l -= 1
                else:
                    print('')
                print('')
                if lvl == 10 and s == 1:
                    print('congrats! you have mutated the "imu" trait!')
                    print("you can now fight against the phage that immuned themself's against you")
                    print("those Phage's are worth more xp but are a bit harder")
                    im += 1
                    s -= 1
                else:
                    print('')
                print('')
                if hunger < 0 or hp1 < 0 or hp1 == 0 or hunger == 0:
                    input('game over: ')
                    qu2 -= 1231
                else:
                    os.system('color 07')
                    os.system('cls')
                    hunger -= 1
                    if xp == xpn or xp > xpn:
                        print('level up!')
                        playsound('levelup.wav')
                        input('press enter to continue: ')
                        lvl += 1
                        xpn += 20
                        fullhp += 3
                        atk += lvl / 2
                        m += 1
                        xpg += lvl 
                        xp = 0
                    else:
                        print("")
                    os.system('color 07')
                    print('')
                    print("      E.coli       ")
                    print(" current organism  ")
                    print('_____________________')
                    print('|                   |')
                    print('|                   |')
                    print('|        ____       |')
                    print('|       /    \      |')
                    print('|     -|      |-    |')
                    print('|     -|      |-    |')
                    print('|     -|      |-    |')
                    print('|     -|      |-    |')
                    print('|     -|      |-    |')
                    print('|     -|      |-    |')
                    print('|       \____/\     |')
                    print('|       / || \ \  / |')
                    print('|      | / |  \ \/  |')
                    print('|    \/ |  |   \    |')
                    print('|       |   \   \   |')
                    print('|       E.coli      |')
                    print('---------------------')
                    print('___________________')
                    print("| 1- explore      |")
                    print("+-----------------+")
                    print("| 2- check statts |")
                    print("+-----------------+")
                    e = input('what do you wanna do: ')
                    if e == '1':
                        x = random.randint(0, 8)
                        if x == 1 or x == 2:
                            os.system('cls')
                            input("enemy spotted!")
                            qu = 2
                            lvl2 = random.randint(1, m)
                            fhp2 = 30
                            fhp2l = fhp2 + lvl2 / 1.5
                            hp2 = fhp2l
                            atk2 = 20
                            atk2l = atk2 + lvl2 / 2
                            fullhp = 30
                            fullhpl = fullhp + lvl / 1.5
                            hp1 = fullhpl
                            
                            while qu > 0:
                                if hp2 < 0 or hp2 == 0:
                                    print('you won! XP + 20 hunger = full offspring + 10')
                                    playsound('victory1.wav')
                                    xp += xpg
                                    hunger = fhunger
                                    offspring += offspring * 2
                                    qu -= 1281839819
                                elif hp1 < 0 or hp1 == 0:
                                    input('you lost...')
                                    input('press enter to continue: ')
                                    qu -= 10001090
                                    qu2 -= 98989
                                else:
                                    os.system('cls')
                                    os.system('color 9')
                                    print('     lvl: ',lvl2)
                                    print('     hp2: ',hp2)
                                    print('___________________')
                                    print('|                 |')
                                    print('|      _____      |')
                                    print('|     /     \     |')
                                    print('|    |       |    |')
                                    print('|    |       |    |')
                                    print('|     \_____/     |')
                                    print('|       | |       |')
                                    print('|       | |       |')
                                    print('|       | |       |')
                                    print('|   |\  | |  /|   |')
                                    print('|   | \ | | / |   |')
                                    print('|   |  \| |/  |   |')
                                    print('|   |   \_/   |   |')
                                    print('|   |         |   |')
                                    print('|                 |')
                                    print('|  Lambda phage   |')
                                    print('|                 |')
                                    print('-------------------')
                                    print('         Vs         ')
                                    print('_____________________')
                                    print('|                   |')
                                    print('|                   |')
                                    print('|        ____       |')
                                    print('|       /    \      |')
                                    print('|     -|      |-    |')
                                    print('|     -|      |-    |')
                                    print('|     -|      |-    |')
                                    print('|     -|      |-    |')
                                    print('|     -|      |-    |')
                                    print('|     -|      |-    |')
                                    print('|       \____/\     |')
                                    print('|       / || \ \  / |')
                                    print('|      | / |  \ \/  |')
                                    print('|    \/ |  |   \    |')
                                    print('|       |   \   \   |')
                                    print('|       E.coli      |')
                                    print('---------------------')
                                    print('     hp1: ',hp1)
                                    print('     lvl: ',lvl)
                                    print('your turn!')
                                    print('_______________________   _____________________')
                                    print("| 1- infectious inject|   |  2- move          |")
                                    print('+---------------------+   +-------------------+')
                                    print('')
                                    print(x1,x4)
                                    print(x2,x5)
                                    print(x3,x6)
                                    z1 = input('choose a move: ')
                                    if z1 == '1':
                                        d = random.randint(0, 4)
                                        if d == 2:
                                            os.system('cls')
                                            hp2 -= atk
                                            print("hit! damage: ",atk)
                                            playsound('phagehit1.wav')
                                            input("Lamda Phage's turn!")
                                            d =  random.randint(0, 2)
                                            if d == 0 and hp2 < 10:
                                                input('phage uses move...')
                                                i = random.randint(0,4)
                                                if i == 1 or i == 2:
                                                    input('it worked!')
                                                    qu -= 100010
                                                if hp2 == 0 or hp2 < 0:
                                                    input('it failed')
                                                elif i == 0 or d == 3:
                                                    input('it failed')
                                            elif d == 1 or d == 0:
                                                input('Lambda Phage uses J-sting...')
                                                c = random.randint(0, 4)
                                                if c == 1 or c == 2:
                                                    hp1 -= atk2l
                                                    print('damage: ',atk2l)
                                                    playsound('phagehit1.wav')
                                                    input('press enter to continue: ')
                                                elif c == 4 or c == 3:
                                                    input("it didn't work")
                                             
                                                
                                        else:
                                            os.system('cls')
                                            input('damn missed!')
                                            input("Lambda Phage's turn!")
                                            d =  random.randint(0, 2)
                                            if d == 0 and hp2 < 10:
                                                input('Lamda Phage uses move...')
                                                i = random.randint(0,4)
                                                if i == 1 or i == 2:
                                                    input('it worked!')
                                                    qu -= 100010
                                                elif hp2 == 0 or hp2 < 0:
                                                    input('it failed')
                                                elif i == 0 or d == 3:
                                                    input('it failed')
                                            elif d == 1 or d == 0:
                                                input('Lamda Phage uses J-sting')
                                                c = random.randint(0, 4)
                                                if c == 1 or c == 2:
                                                    hp1 -= atk2l
                                                    print('damage: ',atk2l)
                                                    playsound('phagehit1.wav')
                                                    input('press enter to continue: ')
                                                elif c == 0 or c == 3:
                                                    input("it didn't work")
                                    elif z1 == '2':
                                        d = random.randint(0, 4)
                                        if d == 2:
                                            os.system('cls')
                                            input("you tried to evade...")
                                            input('you escaped!')
                                            qu -= 100010
                                            input("E.coli's turn!")
                                            d =  random.randint(0, 2)
                                            if d == 0 and hp2 < 10:
                                                input('Lamda Phage uses move...')
                                                i = random.randint(0,4)
                                                if i == 1 or i == 2:
                                                    input('it worked!')
                                                    qu -= 100010
                                                elif hp2 == 0 or hp2 < 0:
                                                    input('it failed')
                                                elif i == 0 or d == 3:
                                                    input('it failed')
                                            elif d == 1 or d == 0:
                                                input('Lamda Phage uses J-sting...')
                                                c = random.randint(0, 4)
                                                if c == 1 or c == 2:
                                                    hp1 -= atk2l
                                                    print('damage: ',atk2l)
                                                    input('press enter to continue: ')
                                                elif c == 0 or c == 3:
                                                    input("it didn't work")
                                        elif d == 3 or d == 1 or d == 0:
                                            os.system('cls')
                                            input("you tried to evade...")
                                            input("but it didn't work!")
                                            input("Lamda Phage's turn!")
                                            d =  random.randint(0, 2)
                                            if d == 0 and hp2 < 10:
                                                input('Lambda Phage uses move...')
                                                i = random.randint(0,4)
                                                if i == 1 or i == 2:
                                                    input('it worked!')
                                                    qu -= 100010
                                                elif i == 0 or d == 3:
                                                    input('it failed')
                                            elif d == 1 or d == 0:
                                                input('Lambda Phage uses J-sting...')
                                                c = random.randint(0, 4)
                                                if c == 1 or c == 2:
                                                    hp1 -= atk2l
                                                    print('damage: ',atk2l)
                                                    input('pres enter to continue: ')
                                                elif c == 0 or c == 3:
                                                    input("it didn't work")
                                    else:
                                        print('wrong input!')
                                        input("Lambda Phage's turn...")
                                        d =  random.randint(0, 2)
                                        if d == 0 and hp2 < 10:
                                            input('Lambda Phage uses move...')
                                            i = random.randint(0,4)
                                            if i == 1 or i == 2:
                                                input('it worked!')
                                                qu -= 100010
                                            elif hp2 == 0 or hp2 < 0:
                                                input('it failed!')
                                            elif i == 0 or d == 3:
                                                input('it failed!')
                                        elif d == 1 or d == 0:
                                            input('Lambda Phage uses J-sting...')
                                            c = random.randint(0, 4)
                                            if c == 1 or c == 2:
                                                hp1 -= atk2l
                                                print('damage: ',atk2l)
                                                input('press enter to continue: ')
                                            elif c == 0 or c == 3:
                                                input("it didn't work")
                            input("...")
                            
                                        
                                    
                                    
                        elif x == 7 and im == 1:
                            os.system('cls')
                            input("enemy spotted!")
                            qu = 2
                            lvl2 = random.randint(1, m)
                            fhp2 = 30
                            fhp2l = fhp2 + lvl2 / 1.5
                            hp2 = fhp2l
                            atk2 = 20
                            atk2l = atk2 + lvl2 / 2
                            fullhp = 30
                            fullhpl = fullhp + lvl / 1.5
                            hp1 = fullhpl
                            
                            while qu > 0:
                                if hp2 < 0 or hp2 == 0:
                                    input('you won! XP + 20 hunger = full offspring is dubbled')
                                    xp += xpg * 2
                                    hunger = fhunger
                                    offspring = offspring * 2
                                    qu -= 1281839819
                                elif hp1 < 0 or hp1 == 0:
                                    input('you lost...')
                                    input('press enter to continue: ')
                                    qu -= 10001090
                                    qu2 -= 98989
                                else:
                                    os.system('cls')
                                    os.system('color 4')
                                    print('     lvl: ',lvl2)
                                    print('     hp2: ',hp2 + lvl * 1.5)
                                    print('___________________')
                                    print('|                 |')
                                    print('|      _____      |')
                                    print('|     /     \     |')
                                    print('|    |XXXXXXX|    |')
                                    print('|    |XXXXXXX|    |')
                                    print('|     \_____/     |')
                                    print('|       | |       |')
                                    print('|       | |       |')
                                    print('|       | |       |')
                                    print('|   |\  | |  /|   |')
                                    print('|   | \ | | / |   |')
                                    print('|   |  \| |/  |   |')
                                    print('|   |   \_/   |   |')
                                    print('|   |         |   |')
                                    print('|                 |')
                                    print('|  Lambda phage   |')
                                    print('|                 |')
                                    print('-------------------')
                                    print('         Vs         ')
                                    print('_____________________                                                                                                                 ')
                                    print('|                   |                    ')
                                    print('|                   |                      ')
                                    print('|        ____       |                                                                                ')
                                    print('|       /    \      |                                                               ')
                                    print('|     -|XXXXXX|-    |                                                   ')
                                    print('|     -|XXXXXX|-    |                                                                                   ')
                                    print('|     -|XXXXXX|-    |                                                                  ')
                                    print('|     -|XXXXXX|-    |                                                            ')
                                    print('|     -|XXXXXX|-    |                                                        ')
                                    print('|     -|XXXXXX|-    |                                                                   ')
                                    print('|       \____/\     |                                                 ')
                                    print('|       / || \ \  / |                                                  ')
                                    print('|      | / |  \ \/  |                                            ')
                                    print('|    \/ |  |   \    |             ')
                                    print('|       |   \   \   |              ')
                                    print('|  immune E.coli    |')
                                    print('---------------------')
                                    print('     hp1: ',hp1)
                                    print('     lvl: ',lvl)
                                    print('your turn!')
                                    print('_______________________   _____________________')
                                    print("| 1- infectious inject|   |  2- move          |")
                                    print('+---------------------+   +-------------------+')
                                    print('')
                                    print(x1,x4)
                                    print(x2,x5)
                                    print(x3,x6)
                                    z1 = input('choose a move: ')
                                    if z1 == '1':
                                        d = random.randint(0, 4)
                                        if d == 2:
                                            os.system('cls')
                                            hp2 -= atk
                                            print("hit! damage: ",atk)
                                            playsound('phagehit1.wav')
                                            input("Lamda Phage's turn!")
                                            d =  random.randint(0, 2)
                                            if d == 0 and hp2 < 10:
                                                input('phage uses move...')
                                                i = random.randint(0,4)
                                                if i == 1 or i == 2:
                                                    input('it worked!')
                                                    qu -= 100010
                                                if hp2 == 0 or hp2 < 0:
                                                    input('it failed')
                                                elif i == 0 or d == 3:
                                                    input('it failed')
                                            elif d == 1 or d == 0:
                                                input('Lambda Phage uses J-sting...')
                                                c = random.randint(0, 4)
                                                if c == 1 or c == 2:
                                                    hp1 -= atk2l
                                                    print('damage: ',atk2l)
                                                    playsound('phagehit1.wav')
                                                    input('press enter to continue: ')
                                                elif c == 4 or c == 3:
                                                    input("it didn't work")
                                             
                                                
                                        else:
                                            os.system('cls')
                                            input('damn missed!')
                                            input("Lambda Phage's turn!")
                                            d =  random.randint(0, 2)
                                            if d == 0 and hp2 < 10:
                                                input('Lamda Phage uses move...')
                                                i = random.randint(0,4)
                                                if i == 1 or i == 2:
                                                    input('it worked!')
                                                    qu -= 100010
                                                elif hp2 == 0 or hp2 < 0:
                                                    input('it failed')
                                                elif i == 0 or d == 3:
                                                    input('it failed')
                                            elif d == 1 or d == 0:
                                                input('Lamda Phage uses J-sting')
                                                c = random.randint(0, 4)
                                                if c == 1 or c == 2:
                                                    hp1 -= atk2l
                                                    print('damage: ',atk2l)
                                                    playsound('phagehit1.wav')
                                                    input('press enter to continue: ')
                                                elif c == 0 or c == 3:
                                                    input("it didn't work")
                                    elif z1 == '2':
                                        d = random.randint(0, 4)
                                        if d == 2:
                                            os.system('cls')
                                            input("you tried to evade...")
                                            input('you escaped!')
                                            qu -= 100010
                                            input("E.coli's turn!")
                                            d =  random.randint(0, 2)
                                            if d == 0 and hp2 < 10:
                                                input('Lamda Phage uses move...')
                                                i = random.randint(0,4)
                                                if i == 1 or i == 2:
                                                    input('it worked!')
                                                    qu -= 100010
                                                elif hp2 == 0 or hp2 < 0:
                                                    input('it failed')
                                                elif i == 0 or d == 3:
                                                    input('it failed')
                                            elif d == 1 or d == 0:
                                                input('Lamda Phage uses J-sting...')
                                                c = random.randint(0, 4)
                                                if c == 1 or c == 2:
                                                    hp1 -= atk2l
                                                    print('damage: ',atk2l)
                                                    input('press enter to continue: ')
                                                elif c == 0 or c == 3:
                                                    input("it didn't work")
                                        elif d == 3 or d == 1 or d == 0:
                                            os.system('cls')
                                            input("you tried to evade...")
                                            input("but it didn't work!")
                                            input("Lamda Phage's turn!")
                                            d =  random.randint(0, 2)
                                            if d == 0 and hp2 < 10:
                                                input('Lambda Phage uses move...')
                                                i = random.randint(0,4)
                                                if i == 1 or i == 2:
                                                    input('it worked!')
                                                    qu -= 100010
                                                elif i == 0 or d == 3:
                                                    input('it failed')
                                            elif d == 1 or d == 0:
                                                input('Lambda Phage uses J-sting...')
                                                c = random.randint(0, 4)
                                                if c == 1 or c == 2:
                                                    hp1 -= atk2l
                                                    print('damage: ',atk2l)
                                                    input('pres enter to continue: ')
                                                elif c == 0 or c == 3:
                                                    input("it didn't work")
                                    else:
                                        print('wrong input!')
                                        input("Lambda Phage's turn...")
                                        d =  random.randint(0, 2)
                                        if d == 0 and hp2 < 10:
                                            input('Lambda Phage uses move...')
                                            i = random.randint(0,4)
                                            if i == 1 or i == 2:
                                                input('it worked!')
                                                qu -= 100010
                                            elif hp2 == 0 or hp2 < 0:
                                                input('it failed!')
                                            elif i == 0 or d == 3:
                                                input('it failed!')
                                        elif d == 1 or d == 0:
                                            input('Lambda Phage uses J-sting...')
                                            c = random.randint(0, 4)
                                            if c == 1 or c == 2:
                                                hp1 -= atk2l
                                                print('damage: ',atk2l)
                                                input('press enter to continue: ')
                                            elif c == 0 or c == 3:
                                                input("it didn't work")
                            input("...")
                            
                        elif x == 4 or x == 5:
                            os.system('cls')
                            input('Found some ATP!')
                            hunger = 20
                        elif x == 6:
                            os.system('cls')
                            print('nothing interesting...')
                    elif e == '2':
                        os.system('cls')
                        print('hp: ',hp1)
                        print('hunger: ',hunger)
                        print('xp: ',xp)
                        print('lvl: ',lvl)
                        print('colonization: ',offspring)
                        print('atk: ',atk)
                        print('xp gainage every battle: ',xpg)
                        print('xp needed until next level: ',xpn - xp)
                        input('press enter to continue: ')
            
    elif f == 'archea':
        os.system('cls')
        os.system('color 9')
        input('archea')
    elif f == 'animal cell':
        os.system('cls')
        os.system('color 1')
        input('animal cell')
    elif f == 'complex':
        os.system('cls')
        os.system('color 8')
        input('complex')
    else:
        os.system('cls')
        os.system('color 6')
        input("wrong input")
