import random, linecache, os
#disclaimer: you may use this source code for anything, but if you simply rip it off i consider that a copyright violation
#i will define rip off as simply re releasing with changed data(releasing mods without the executable is fine however
#or if i feel it resembles my game in any way
autosave = False
filename = "derp"
ischosen = 0
counter = 0


def character():
    address = raw_input("Please type your name\n\n")
    print "        RACE SCREEN                        "
    print "********************************************"
    print "*  Ancient World of Generica Version 0.05  *\n*                                          *\n*                                          *"
    print "*    which race do you want:               *"
    print "*       1: Human                           *"
    print "*       2: Elf                             *"
    print "*       3: Dwarf                           *"
    print "*       4: Orc (You will die mode)         *"
    print "*       5: Load file                       *"
    print "*                                          *"
    print "*                                          *"
    print "*This is the first alpha, so expect errors *"
    print "*                                          *"
    print "*If you can, run it on a console           *"
    print "Please press enter after you have written  "
    print "********************************************"
    choice = raw_input("> ")

    if choice == "1":
        rand1 =  random.randint (1, 5)
        dap = "Human"
        hp = 75 * rand1
        attack = 8 - rand1
        print "you are a %r" % dap
    elif choice == "2":
        rand1 =  random.randint (1, 5)
        dap = "Elf"
        hp = 60 * rand1
        attack = 10 - rand1

        print "you are a %r" % dap
    elif choice == "3":
        rand1 =  random.randint (1, 5)
        dap = "Dwarf"
        hp = 90 * rand1
        attack = 6 - rand1

        print "you are a %r" % dap
    elif choice == "4":
        rand1 =  random.randint (1, 5)
        dap = "Orc"
        hp = 60 * rand1
        attack = 6 - rand1

        print "you are a %r" % dap
    elif choice == "5":
        load()

    else:
        rand1 =  random.randint (1, 5)
        dap = "Pony"
        hp = 60 * rand1
        attack = 7 - rand1
        print "you found the secret character, the Pony!, NOTE: I am not a brony"

    raw_input("Please press enter")    
    print "\n\n"
    print "           CLASS SCREEN               "
    print "**************************************"
    print "*Select the warrior you think you are*"
    print "*      press 1 for a Berserker       *"
    print "*      press 2 for a Huscarl         *"
    print "*      press 3 for a Mercenary       *"
    print "*      and then press enter          *"
    print "*                                    *"
    print "**************************************"

    choice = raw_input("> ")


    if choice == "1":
        print "you are a Beserker"
        xp = 0
        rand1 = random.randint(1, 5)
        rand2 = random.randint(1,2)
        level = 2
        hp = hp + (3 * (rand1 + rand2))
        attack = attack + rand1 + rand2 + 4
        name = address +" , " + dap + " Huscarl"
        weapon = "Awful Greatsword"
        armorname = "Rusty Cuirnass"
        armor = 4


    elif choice == "2":
        print "you are a Huscarl"
        xp = 0
        rand1 = random.randint (1, 5)
        rand2 = random.randint(1,2)
        level = 2
        hp = hp + (3 * (rand1 + rand2)) + 4
        attack = attack + (rand1 + rand2)
        name = address +" , " + dap + " Huscarl"
        weapon = "Terrible Lumber axe"
        armorname = "Old Leather Armor"
        armor = 6


    elif choice == "3":
        print "you are a Mercenary"
        rand2 = random.randint(2,3)
        xp = 0
        level = 2
        rand1 = random.randint (1, 6)
        hp = hp + (3 * (rand1 + rand2))
        attack = attack + (rand1 + rand2)
        name = address +" , " + dap + " Huscarl"
        weapon = "Rusty Halberd"
        armorname = "Old Lorica Segmentum"
        armor = 8


    else:
        print "You Found the Secret class, the Peasant"
        level = 2
        hp = hp + 20
        attack =  attack + 2
        address +" , " + dap + " Huscarl"
        xp = 0
        weapon = "Weak Fists"
        armorname = "Leather Outfit"
        armor = 8
        
	
    
    start(level,hp, attack, name, xp, weapon, armorname, armor)


def cls():
     os.system(['clear','cls'][os.name == 'nt'])



def start(level,hp, attack, name, xp, weapon, armorname, armor):
    global autosave,filename,ischosen,counter
    if ischosen == 0:
         print "\n\n\n\n"
         choice = raw_input("Do you want autosave on or off?, Y/N\n")
         if choice == "y" or choice == "Y":
             autosave = True
             filename = raw_input("Please input filename\n")
             ischosen = 23
         else:
             ischosen = 34
    if xp  > (level * 400):
         levelup(level, hp, attack, name, xp, weapon, armorname, armor)
    cls()
    print "Welcome to the magical world of Generica"
    print "the most generic fantasy world you will ever visit\n\n"
    print "class: ", name
    print "level: ", level
    print "Weapon: %r " %  weapon 
    print "Armor: %r" % armorname



    print "1: Save Game"
    print "2: see stats for weapons and armour"
    print "\n\nanything else starts the game"
    print "REMEMBER: Enter confirms all input" 
    print "CTRL-Z to exit"
    print "what do you wish to do"


    choice = raw_input("> ")
    if autosave == True and choice != "2" and counter > 5:
         counter = 0
         save(name,level,xp,hp,attack,weapon,armorname,armor)
    if choice == "1":
        save(name, level, xp, hp, attack,weapon, armorname, armor)
    elif choice == "2":
         cls()
         print "Health Points: %d" % hp
         print "Armour name: %r" % armorname
         print "Armour value: %d\n" % armor
         print "Weapon name: %r" % weapon
         print "Weapon damage: %dd%d\n\n" % (level, attack)
         raw_input("Please press enter to continue")
         start(level,hp,attack,name,xp,weapon,armorname,armor)
    else:
        counter = counter + 1

        animal(name, hp, attack, level, xp, weapon, armorname, armor)






def animal(name, hp, attack, level, xp, weapon,armorname, armor):
    random.seed()
    print "class: ", name
    print "hp: ", hp
    print "attack: ", attack
    print "level: ", level
    print "xp: ", xp
    filen = open("data/monsters.txt", 'r')
    limit = filen.readline()
    filen.close()
    limit = int(limit)
    rand1 = random.randint(2,limit)

    line = linecache.getline("data/monsters.txt", rand1)

    words = line.split(";")



    elevel = words[0]
    elevel = int(elevel)
    ename = words[1]
    ehp = words[2]
    eattack = words[3]
    everb = words[4]
    everbfail = words[5]
    exp = words[6]






    ehp = int(ehp)
    eattack = int(eattack)
    exp = int(exp)
    elevel = int(elevel)

    
    ename2 = ["NULL","Near Death", "Tiny", "Idiotic", "Weak", "Old", "Baby","Dumb", "Blind", "Deaf", "Small",
    "Juvenile", "Average", "Alpha", "Intelligent", "Strong", "Huge", "Powerful", "Fear-inducing", "Terrifying","Epic"]
    derp = random.randint(1,20)
    ehp = ehp * (derp / 10)
    eattack = eattack * (derp / 10)
    exp = exp * (derp / 10)
	
    
    if elevel < level:
         ename = ", Superior " + ename
         elevel = elevel + level
         eattack = eattack * elevel
         ehp = ehp * elevel
    elif elevel > level:
         ename = ", Inferior " + ename
         elevel = elevel - level
         eattack = eattack / elevel
         ehp = ehp / elevel
    if ehp <= 0:
	    ehp = 20
    if eattack <= 0:
	    eattack = 5
    if exp <= 0:
        exp = 20
	
    ename = ename2[derp] + " " +  ename
    choice = raw_input("Would you like to see the Monsters's stats before you fight(Y/N)?\n") 
    if choice == "y" or choice == "Y":
        cls()
        print "Monster Name: %r\n" % ename
        print "Monster Hitpoints: %d\n" % ehp
        print "Monster attack %dd%d" % (elevel, eattack)
        print "XP = %d" % exp
        raw_input("Please press enter to continue")




    combat(hp, attack, level, name, ename, ehp, eattack, everb,elevel, exp, xp,weapon, everbfail, armorname, armor)












def combat(hp, attack, level, name, ename, ehp, eattack, everb, elevel, exp, xp,weapon, everbfail, armorname, armor):
    print "\n\n an angry level %d %r fights you" % (elevel, ename)
    rand5 = random.randint(1, 5)
    ealive = True
    alive = True
    while  alive == True and ealive == True:
         rand1 = random.randint(0,100)
         rand2 = random.randint(0,100)
         etrueattack = 0
         trueattack = 0
         eattackar = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
                      ,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
                      ,0,0,0,0,0,0,0,0,0,0,0]
         attackar = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
                     ,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
         hit = False
         ehit = False
         i = 0
         x = 0
         for i in range(elevel):
            herp = random.randint(0,eattack)
            eattackar[i] = herp
            etrueattack += eattackar[i]
         for x in range(level):
            herp = random.randint(0,attack)
            attackar[i] = herp
            trueattack += attackar[i]


         if hp <= 0:
              print "You were killed by the %r, please press enter" % ename
              raw_input("> ")
              alive = False


         else:
                print "where do you wish to hit, 1. head or 2.Body or f(lower case) to flee"
                choice = raw_input("> ")
         if choice == "1" and rand2 < 30 and alive == True and ealive == True:
              print "you hit the %r, causing %d damage with x2 modifier" %(ename, trueattack)
              ehp = ehp - (trueattack * 2)
              hit = True
         elif choice == "2" and rand2 < 85 and rand2 > 30 and alive == True and ealive == True:
              print "you hit the %r, causing %d damage" % (ename, trueattack)
              ehp = ehp - trueattack
              hit = True
         elif choice == "f" and rand2 > (10 + (elevel* 3)) and alive == True and ealive == True:
             print "you flee successfully, you pussy, heroes never get scared"
             alive = False

         elif choice == "f" and rand2 < (10 + (elevel * 3)) and alive == True and ealive == True:
             print "you fail to flee"
         elif alive == True and ealive == True:
               print "you fail to hit"
         else:
             print "\n"
         if trueattack > (attack * 5) and hit == True:
             print "CRITICAL HIT!!!!!!!!!!!!!!!!!!!!!! press enter"
             raw_input("> ")
             cls()
         if ehp <= 0:
             print "congratulations, you have killed the foul %r, please press enter" % ename
             raw_input("> ")
             xp = xp + exp
             ealive = False
         

         if rand1  < 12 and hp <= (ehp + elevel) and ealive == True:
			 if etrueattack <= 0:
				 etrueattack = 1
			 print "the %r %r your head, causing %d damage with x2 modifier"  % (ename, everb, etrueattack)
			 hp = hp - (etrueattack - armor) * 2
			 ehit = True
         elif rand1 < 60 and rand1 > 12 and hp <= (ehp + elevel)and ealive == True and alive == True:
			 if etrueattack <= 0:
				 etrueattack = 1
			 print " the %r %r your body, causing %d damage" % (ename, everb, etrueattack)
			 hp = hp - (etrueattack - armor)
			 ehit = True
         elif rand1 < 12 and hp > (ehp + elevel)and ealive == True and alive == True:
			 if etrueattack <= 0:
				 etrueattack = 1
			 print "the %r %r your head, doing %d damage with no modifier due to being scared of you" %(ename, everb, etrueattack)
			 hp = hp - (etrueattack - armor)
			 ehit = True
         elif rand1 < 60 and hp > (ehp + elevel) and rand1 > 12 and ealive == True and alive == True:
			 if etrueattack <= 0:
				 etrueattack = 1
			 print "the %r %r your body, and does %d damage with a 1/2 modifier due to being scared of you" % (ename, everb, etrueattack)
			 hp = hp - (etrueattack - armor) / 2
			 ehit = True
         elif rand1 > 91 and hp > (ehp + (elevel * 3)) and ealive == True and alive == True and attack > (etrueattack * 2):
			 if etrueattack <= 0:
				 etrueattack = 1
			 print "the %r flees in terror!, you gained %d xp" % (ename,exp)
			 raw_input("Please press enter")
			 xp = xp + exp
			 ealive = False

         elif ealive == True and alive == True:
             print "the %r tries to %r you, but misses" % (ename, everbfail)
         else:
             print "\n"
         if etrueattack > (eattack * 5) and ehit == True:
             print "ENEMY CRITICAL HIT!!!!!!!!!!!!!!!!!!!!!! press enter"
             raw_input("> ")
             cls()
         if hp < 10:
             print "You are on low health, I recommend you run"
         print "\n"
         
    if hp <= 0 and alive == False:
        rip(name, level, xp, hp, attack,weapon, ename ,armorname, armor)
    elif ehp <= 0 and ealive == False:
        
        if rand5 < 2:
            xp = xp + exp
            weapon_drop(name,level,xp,hp,attack,weapon, armorname, armor)
        elif rand5 == 2:
            xp = xp + exp
            weapon_drop(name,level,xp,hp,attack,weapon, armorname, armor)
        elif rand5 == 4:
            xp = xp + exp
            potion_drop(name,level,xp,hp,attack,weapon, armorname, armor)

        elif rand5 < 4 and rand5 > 2:
            xp = xp + exp
            potion_drop(name,level,xp,hp,attack,weapon, armorname, armor)
        elif rand5 > 4:
            xp = xp + exp
            armor_drop(level, hp, attack, name, xp, weapon, armorname, armor)

    else:
        xp = xp + exp
        start(level,hp, attack, name, xp, weapon, armorname, armor)




def levelup(level, hp, attack, name, xp, weapon, armorname, armor):
                 print "LEVEL UP!!!!!, well done!"
                 level = level + 1
                 hp = hp + 50
                 attack = attack + 20



                 start(level, hp, attack, name, xp,weapon ,armorname, armor)

def rip(name, level, xp, hp, attack,weapon, ename, armorname, armor):
    filename = raw_input("what is the name of the deceased?:  ")
    filename = "rip/" + filename
    filen = open(filename, 'w')
    filen.truncate()
    filen.write("name: ")
    filen.write(filename)
    filen.write("\n")
    filen.write("level: ")
    level = str(level)
    filen.write(level)
    filen.write("\n")
    xp = str(xp)
    filen.write("xp: ")
    filen.write(xp)
    attack = str(attack)
    filen.write("\n")
    filen.write("attack: ")
    filen.write(attack)
    filen.write("\n")
    name = str(name)
    filen.write("class: ")
    filen.write(name)
    filen.write("\n")
    filen.write("Weapon: ")
    filen.write(weapon)
    filen.write("\nArmor: ")
    filen.write(armorname)
    filen.write("\n")
    filen.write("Killed by: ")
    filen.write(ename)
    filen.write("\n")
    last_words = raw_input("what would you like written as your last sentance?press enter when done\n>   ")
    filen.write("Famous last words: ")
    filen.write(last_words)
    filen.close()
    print "you can now read your grave file a %r.txt, please press enter to play again or ctrl-z then to exit" % filename
    raw_input("Please press enter")
    cls()
    character()

def weapon_drop(name,level,xp,hp,attack,weapon, armorname, armor):

   filen = open("data/weapons.txt", 'r')
   limit = filen.readline()
   limit = int(limit)
   filen.close()


   rand1 = random.randint(2,limit)
   line = linecache.getline("data/weapons.txt", rand1)

   words = line.split(";")
   weaponame = words[0]
   weaponame = str(weaponame)
   tempatt = words[1]
   tempatt = int(tempatt)
   derp = random.randint(1,31)
   adject = ["NULL", "Archaic", "Improvised", "Obsolete", "Snapped", "Crushed", "Dull", "Old", "Mass-Produced", "Unreliable", "Unwieldy","Heavy", "Brittle",
               "Bad", "Average", "Reasonable", "Sharp", "Powerful", "Impressive", "Blessed", "Good", "Useful", "Excellent", "Holy", "Wicked", "Awesome",
               "Etheral", "God-like", "Eternal", "Epic", "Extra-dimesional", "The best"]
   
   weaponame = adject[derp] + " " + weaponame
   tempatt = (tempatt * derp) / 10
   print"you find an %r, do you want it?(Y/N)" % weaponame
   choice = raw_input("> ")
   if choice == "y" or choice == "Y":
     if name != "Beserker":
           attack = attack - attack
     elif name == "Beserker":
           attack = (attack - attack) + 40
     attack = attack + tempatt
     weapon = weaponame
     start(level, hp, attack, name, xp, weapon, armorname, armor)
   elif choice != "1":
        print "you didnt pick up the %r" % weaponame
   if xp  > (level * 400):
            levelup(level, hp, attack, name, xp, weapon, armorname, armor)
   start(level, hp, attack, name, xp, weapon, armorname, armor)



def potion_drop(name,level,xp,hp,attack,weapon, armorname, armor):
    filen = open("data/potions.txt", 'r')
    limit = filen.readline()
    limit = int(limit)
    filen.close()
    derp = ["Null", "Small ", "Medium ", "Large "] 
    rand1 = random.randint(2,limit)
    line = linecache.getline("data/potions.txt", rand1)

    words = line.split(";")
    potionname = words[0]
    potionname = str(potionname)
    xpe = words[1]
    xpe = int(xpe)
    hpe= words[2]
    hpe = int(hpe)
    hpe= words[2]
    hpe = int(hpe)
    attackpe = words[3]
    attackpe = int(attackpe)
    herp = random.randint(1,3)
    potionname =  derp[herp] + potionname
    hpe = hpe * herp
    xpe = xpe * herp
    attackpe = attackpe * herp
	



    print "The Enemy drops %r, do you want it?(Y/N) note you take it now or you don't take it ever\n" % potionname
    choice = raw_input("> ")
    if choice == "y" or choice == "Y":
        hp = hp + hpe
        xp = xp + xpe
        attack = attack + attackpe



    else:
        print "you don't take the %r" % potionname
    if xp  > (level * 400):
            levelup(level, hp, attack, name, xp, weapon, armorname, armor)


    start(level, hp, attack, name, xp, weapon, armorname, armor)

def armor_drop(level, hp, attack, name, xp, weapon, armorname, armor):

    filen = open("data/armor.txt", 'r')
    limit = filen.readline()
    limit = int(limit)
    filen.close()


    rand1 = random.randint(2,limit)
    line = linecache.getline("data/armor.txt", rand1)

    words = line.split(";")
    armornamea = words[0]
    temparm = words[1]
    temparm = int(temparm)
    derp = random.randint(1,31)
    adject = ["NULL", "Archaic", "Improvised", "Obsolete", "Snapped", "Crushed", "Dull", "Old", "Mass-Produced", "Unreliable", "Unwieldy","Heavy", "Brittle",
               "Bad", "Average", "Reasonable", "Sharp", "Powerful", "Impressive", "Blessed", "Good", "Useful", "Excellent", "Holy", "Wicked", "Awesome",
               "Etheral", "God-like", "Eternal", "Epic", "Extra-dimesional", "The best"]
	
	
    armournamea = adject[derp] + " " + armornamea
    temparm = (temparm * derp) / 10
    print "The Enemy drops %r, do you want it?(Y/N)" %  armournamea
    choice = raw_input("> ")
    if choice == "y" or choice == "Y":
        armor = armor - armor
        print "You Take the %r" % armornamea
        armorname =  armournamea
        armor = temparm

    else:
        print "you don't take the %r" %  armornamea
    if xp  > (level * 400):
            levelup(level, hp, attack, name, xp, weapon,armorname, armor)


    start(level, hp, attack, name, xp, weapon, armorname, armor)

def save(name, level, xp, hp, attack,weapon, armorname, armor):
    global autosave, filename
    if autosave != True:
        print "you may overwrite stuff but frankly i dont care if you do so this is your"
        print "last chance to stop before you overwrite anything, ok?"
        choice = raw_input("\n 1 for yes to save, else for no")
        if choice != "1":
             start(level, hp, attack, name, xp, weapon, armorname, armor)

    else:
        if autosave != True:
            print "please type desired filename"
            filename = raw_input(">")
        filenamea = "save/" + filename
        filen = open(filenamea, 'w')
        filen.truncate()
        filen.write(filenamea)#filename
        filen.write("\n")
        level = str(level)
        filen.write(level)#level
        filen.write("\n")
        filen.write(name)#your name
        filen.write("\n")
        xp = str(xp)
        filen.write(xp)#xp
        filen.write("\n")
        attack = str(attack)
        filen.write(weapon)#weapon name
        filen.write("\n")
        filen.write(attack)#attack of said weapon
        filen.write("\n")
        filen.write(armorname)#armor name
        filen.write("\n")
        armor = str(armor)#armor
        filen.write(armor)
        hp = str(hp)#hp
        filen.write("\n")
        filen.write(hp)
        hp = int(hp)
        attack = int(attack)
        armor = int(armor)
        level = int(level)
        xp = int(xp)
        filen.close()
        cls()
        if autosave == True:
		     animal(name, hp, attack, level, xp, weapon, armorname, armor)
        else:     
             start(level, hp, attack, name, xp, weapon, armorname, armor)

def load():
    print "Do you want to load a file? 1 for yes etc for no?"
    choice = raw_input(">")

    if choice == "1":
		filename = raw_input("what is the file's name?")
		filename = "save/" + filename
		try:
			filenamea = open(filename, 'r')
		except IOError as e:
			print "the file doesn't exist, going back to character()"
			character()
			raw_input(">")
		filenamea.readline()
		level = filenamea.readline()
		name = filenamea.readline()
		xp = filenamea.readline()
		weapon = filenamea.readline()
		attack = filenamea.readline()
		armorname = filenamea.readline()
		armor = filenamea.readline()
		hp = filenamea.readline()
		name =  name.rstrip('\n')
		weapon = weapon.rstrip('\n')
		armorname = armorname.rstrip('\n')
		level = int(level)
		xp = int(xp)
		attack = int(attack)
		armor = int(armor)
		hp = int(hp)
		print "level : %r" % level
		print "name : %r" % name
		print "xp: %d" % xp
		print "weapon : %r" % weapon
		print "attack : %d" % attack
		print "armour name : %r" % armorname
		print "armor value: %d" % armor
		print "hp: %d" % hp
		print "FILE loaded, please press enter"
		raw_input(">")
		cls()


    else:
        print "you didn't load the file"
        cls()
        character()
    start(level,hp, attack, name, xp, weapon, armorname, armor)























character()

