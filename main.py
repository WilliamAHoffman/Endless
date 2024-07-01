import entity
import moves
import battle
import copy
import random
import senerios
import items
import start

#--------------------------------------------------------------------------------
def characterchoice():
    crewpicked = []
    times = 4
    altmoves = []
    choices = [copy.deepcopy(entity.soldier), copy.deepcopy(entity.marauder), copy.deepcopy(entity.medic), copy.deepcopy(entity.engineer), copy.deepcopy(entity.captain), copy.deepcopy(entity.survivor)]
    while times > 0:
        counter = 0
        print("Choose", str(times) + ":")
        while counter < len(choices):
            print("[" + str(counter) + "]", choices[counter].name + ":", choices[counter].desc)
            counter = counter + 1
        try:
            choice = int(input(">"))
            if choice < counter:
                crewpicked.append(choices[choice])
                altmoves.append(choices[choice].items[0])
                altmoves.append(choices[choice].items[1])
                altmoves.append(choices[choice].items[2])
                altmoves.append(choices[choice].items[3])
                start.clear()
                choices.pop(choice)
                times = times - 1
        except:
            print("Invalid")
            start.clear()
    return crewpicked, altmoves

class Team:
  def __init__(self, lvl, xp, gold, crewlist, luck, storedmoves):
    self.lvl = lvl
    self.xp = xp
    self.gold = gold
    self.crewlist = crewlist
    self.luck = luck
    self.storedmoves = storedmoves

#summons = [entity.forcefield, entity.defenceturret, entity.battleturret]
storedmoves = []
explorers, altmoves = characterchoice()
crew = Team(entity.crewlvl, 0, 0, explorers, 0, storedmoves)

def test():
    testmove = moves.mechanicallock
    print(testmove.name+":",testmove.desc)
    print("ammo:", testmove.ammo)
    print("energy:", testmove.energy)
    print("dmg:", testmove.dmg)
    print("leech:", testmove.leech)
    print("sacrifice:", testmove.sacrifice)
    print("shield:", testmove.shield)
    print("stun:", testmove.stun)
    print("poison:", testmove.poison)
    print("weaken:", testmove.weaken)
    print("strength:", testmove.strength)
    print("expose:", testmove.expose)
    print("defend:", testmove.defend)
    print("pierce:", testmove.pierce)
    print("spd:", testmove.spd)
    print("priority:", testmove.priority)
    print("summon:", testmove.summon)
    print('Speed', testmove.speed)
    input("")
#test()
#--------------------------------------------------------------------------------
def reset(crew):
    counter = 0
    summoned = 0
    lencrew = len(crew)
    while lencrew > counter:
        crew[counter].priority = crew[counter].basepriority
        crew[counter].affliction = [0, 0, 0, 0, 0, 0]
        crew[counter].shield = crew[counter].baseshield
        crew[counter].energy = crew[counter].maxenergy
        crew[counter].speed = crew[counter].basespeed
        if crew[counter].health > crew[counter].maxhealth:
            crew[counter].health = crew[counter].maxhealth
        if crew[counter].energy > crew[counter].maxenergy:
            crew[counter].energy = crew[counter].maxenergy
        if crew[counter].life == False:
            crew[counter].life = True
            crew[counter].health = 1
        if crew[counter].id == False:
            summoned = summoned + 1
        counter = counter + 1
    while summoned > 0:
        crew.pop(len(crew) - 1)
        summoned = summoned - 1

def levelup(lvl, xp, crew):
    scaling = lvl
    required = int(((scaling**2)/2)+scaling*100)
    while xp >= required:
        counter = 0
        required = int(((scaling ** 2) / 2) + scaling * 50) + 50
        xp = xp - required
        lvl = lvl + 1
        print("You leveled up!")
        print("lvl:", lvl)
        scaling = scaling + 1
        while counter < len(crew):
            levelstats(crew[counter])
            counter = counter + 1
    return lvl

def levelstats(entity):
    entity.attack = int(entity.attack + 4)
    if entity.maxhealth > 10:
        entity.maxhealth = int(entity.maxhealth + entity.healthincrease)
    else:
        entity.baseshield = int(entity.baseshield + 10)
    entity.maxenergy = int(entity.maxenergy + 5)
    entity.health = int(entity.health + entity.healthincrease)

def levelenemies(entity, lvl):
    entity.attack = int(entity.attack * (1.1**lvl))
    entity.maxhealth = int(entity.maxhealth * (1.1**lvl))
    entity.baseshield = int(entity.baseshield * (1.1**lvl))
    entity.shield = entity.baseshield
    entity.health = entity.maxhealth
    entity.lvl = lvl

def enemylevelup(lvl, enemies):
    counter = 0
    while counter < len(enemies):
        randlvl = lvl + random.randint(-1, 1)
        levelenemies(enemies[counter], randlvl)
        counter = counter + 1

def xpamt(difficulty, lvl, xp):
    xpadd = int(difficulty * lvl) * 10 + random.randint(0, 25)
    xp = xp + xpadd
    print("You gained", xpadd, "xp!")
    return xp

def rewardapply(choice2, crew, itemchoice, choice):
    start.clear()
    lenteam = len(crew.crewlist)
    while 1 == 1:
        if choice2 < choice:
            print("Who should receive this?")
            counter = 0
            while lenteam > counter:
                print("["+str(counter)+"]", crew.crewlist[counter].name)
                print("Speed:", crew.crewlist[counter].speed, "Health:", str(crew.crewlist[counter].health) + "/" + str(crew.crewlist[counter].maxhealth),
                      "Shields:", crew.crewlist[counter].shield, "Priority:", crew.crewlist[counter].priority, "Defence:", crew.crewlist[counter].defence, "Regen:",
                      crew.crewlist[counter].regen, "Energy_Regen:", crew.crewlist[counter].energyregen, "Energy:", crew.crewlist[counter].energy, "Attack:", crew.crewlist[counter].attack)
                counter = counter + 1
            if choice2 < choice:
                try:
                    choice3 = int(input(""))
                except:
                    print("Not a number.")
            if choice3 in range(0, counter):
                if choice2 < choice:
                    crew.crewlist[choice3].items.append(itemchoice[choice2])
                    cc = crew.crewlist[choice3]
                    it = itemchoice[choice2]
                    cc.attack = int(cc.attack + (cc.attack * (it.attack/100)))
                    cc.defence = int(cc.defence + it.defence)
                    if cc.defence > 40:
                        cc.defence = 40
                    cc.maxhealth = int(cc.maxhealth + (cc.maxhealth * (it.maxhealth/100)))
                    cc.health = int(cc.health + (cc.maxhealth * (it.maxhealth / 100)))
                    cc.maxenergy = int(cc.maxenergy + (cc.maxenergy * (it.maxenergy/100)))
                    cc.energy = int(cc.energy + (cc.maxenergy * (it.maxenergy/100)))
                    cc.basepriority = int(cc.basepriority + it.basepriority)
                    if cc.basepriority > 100:
                        cc.basepriority = 100
                    elif cc.basepriority < 0:
                        cc.basepriority = 0
                    cc.baseshield = int(cc.baseshield + it.baseshield)
                    cc.energyregen = int(cc.energyregen + it.energyregen)
                    cc.regen = int(cc.regen + it.regen)
                    cc.crit = int(cc.crit + it.crit)
                    cc.basespeed = int(cc.basespeed + it.speed)
                    if cc.basespeed > 100:
                        cc.basespeed = 100
                    elif cc.basespeed < 0:
                        cc.basespeed = 0
                    cc.speed = cc.basespeed
                    return
        amount = len(crew.crewlist) - 1
        if choice2 == choice:
            while amount >= 0:
                crew.crewlist[amount].health = int(crew.crewlist[amount].health + (crew.crewlist[amount].maxhealth/2))
                if crew.crewlist[amount].health > crew.crewlist[amount].maxhealth:
                    crew.crewlist[amount].health = crew.crewlist[amount].maxhealth
                amount = amount - 1
            return
        if choice2 == choice + 1:
            while amount >= 0:
                crew.crewlist[amount].ammo = crew.crewlist[amount].ammo + 20
                amount = amount - 1
            return
        #if choice2 == choice + 2:
        #    while amount >= 0:
        #        crew.crewlist[amount].energy = crew.crewlist[amount].maxenergy
        #        amount = amount - 1
        #    return

def itemloot(crew):
    choice = 0
    randitem = [items.aspectofaxo, items.energycell, items.orb, items.mask, items.stemcells, items.ironshield,items.blitz, items.scope, items.doubleedge, items.cellular, items.nova, items.mind]
    itemchoice = []
    upper = 11
    while choice < 3:
        randomchoice = random.randint(0, upper)
        itemchoice.append(randitem[randomchoice])
        randitem.pop(randomchoice)
        upper = upper - 1
        choice = choice + 1
    while 1 == 1:
        print("Choose a reword!")
        print("[" + str(choice-3) + "]", itemchoice[choice-3].name + ":", itemchoice[choice-3].desc)
        print("[" + str(choice-2) + "]", itemchoice[choice-2].name + ":", itemchoice[choice-2].desc)
        print("[" + str(choice-1) + "]", itemchoice[choice-1].name + ":", itemchoice[choice-1].desc)
        print("[" + str(choice) + "]", start.heal + ": Heal all crew members by 50%.")
        print("[" + str(choice + 1) + "]", start.ammo + ": Gain 20 ammo for all crew members.")
        #print("[" + str(choice + 2) + "]", start.energy + ": Gain max energy for all crew members.")
        try:
            choice2 = int(input(""))
            if choice2 in range(0, choice+2):
                rewardapply(choice2, crew, itemchoice, choice)
                return
        except:
            start.clear()

def perkapply(enemies):
    counter = len(enemies) - 1
    while counter >= 0:
        perk = random.randint(0, 12)
        if perk == 0:
            #regenerating
            enemy[counter].name = start.light_blue+"Regenerating " + enemy[counter].name
            enemy[counter].regen = int(enemy[counter].regen + 10)
        elif perk == 1:
            #mechanical
            enemy[counter].name = start.light_blue+"Mechanical " + enemy[counter].name
            enemy[counter].baseshield = int(enemy[counter].baseshield + (enemy[counter].maxhealth * 1.3))
            enemy[counter].maxhealth = 1
        elif perk == 2:
            #hungry
            enemy[counter].name = start.light_blue+"Hungry " + enemy[counter].name
            enemy[counter].attack = int(enemy[counter].attack * 1.3)
            enemy[counter].maxhealth = int(enemy[counter].maxhealth * 0.7)
        elif perk == 3:
            #corrupted
            enemy[counter].name = start.light_blue+"Corrupted " + enemy[counter].name
            enemy[counter].attack = int(enemy[counter].attack * 1.5)
            enemy[counter].regen = int(enemy[counter].regen - 20)
        elif perk == 4:
            #experienced
            enemy[counter].name = start.light_blue+"Experienced " + enemy[counter].name
            enemy[counter].crit = int(enemy[counter].crit + 20)
        elif perk == 5:
            #sick
            enemy[counter].name = start.light_blue+"Sick " + enemy[counter].name
            enemy[counter].maxhealth = int(enemy[counter].maxhealth * 0.7)
            enemy[counter].attack = int(enemy[counter].attack * 0.7)
        elif perk == 6:
            #fast
            enemy[counter].name = start.light_blue + "Fast " + enemy[counter].name
            enemy[counter].speed = int(enemy[counter].speed + 15)
        elif perk == 7:
            #Bulky
            enemy[counter].name = start.light_blue + "Bulky " + enemy[counter].name
            enemy[counter].maxhealth = int(enemy[counter].maxhealth * 1.3)
        if enemy[counter].maxhealth <= 0:
            enemy[counter].maxhealth = 1
            enemy[counter].health = 1
        counter = counter - 1
    return

def newmoves(crew, alts):
    luck = random.randint(0, len(alts)-1)
    if luck > 11:
        id = 3
    elif luck > 7:
        id = 2
    elif luck > 3:
        id = 1
    else:
        id = 0
    while 1 == 1:
        print("The", crew[id].name, "found a new move!")
        print("Name:", alts[luck].name)
        print("Description:", alts[luck].desc)
        print("Replace it with something?")
        lenmoves = len(crew[id].moves)
        counter = 0
        while lenmoves > counter:
            print("[" + str(counter) + "]", crew[id].moves[counter].name+":", crew[id].moves[counter].desc)
            counter = counter + 1
        print("[" + str(counter) + "]", "Skip.")
        try:
            choice = int(input(">"))
            if choice < counter:
                print("Replaced!")
                crew[id].moves[choice] = alts[luck]
                return
            if choice == counter:
                print("Ok!")
                return
            start.clear()
        except:
            start.clear()

def randomevents(crew, alts):
    start.clear()
    luck = random.randint(1, 2)
    if luck == 1:
        newmoves(crew.crewlist, alts)
    return

# --------------------------------------------------------------------------------
print("Welcome to the endless ordeal!")
input(">")
print('You are stuck on the planet Solus and must fight to survive.')
input(">")
start.clear()
newmoves(crew.crewlist, altmoves)

def battleloop(enemy, difficulty, battlecounter):
    enemies = enemy
    enemyxp = copy.copy(enemy)
    enemylevelup(battlecounter, enemies)
    #win = True
    #input2 = input("")
    #if input2 == "h":
    win = battle.main(crew, enemies)
    reset(crew.crewlist)
    counter = 0
    if win == True:
        while counter < len(enemyxp):
            crew.xp = xpamt(difficulty, enemyxp[counter].lvl, crew.xp)
            counter = counter + 1
        entity.crewlvl = levelup(crew.lvl, crew.xp, crew.crewlist)
        crew.lvl = entity.crewlvl
        input("")
    return win

battlecounter = 1
while 1 == 1:
    if battlecounter % 10 == 0:
        enemies = [senerios.bs1, senerios.bs2, senerios.bs3, senerios.bs4, senerios.bs5]
        rand = random.randint(0, len(enemies)-1)
        enemy = copy.deepcopy(enemies[rand])
        difficulty = 4
    elif battlecounter % 4 == 0:
        enemies = [senerios.hs1, senerios.hs2, senerios.hs3, senerios.hs4, senerios.hs5, senerios.hs6, senerios.hs7, senerios.hs8, senerios.hs9, senerios.hs10, senerios.hs11, senerios.hs12, senerios.hs13, senerios.hs14, senerios.hs15, senerios.hs16, senerios.hs17, senerios.hs18, senerios.hs19, senerios.hs20]
        rand = random.randint(0, len(enemies)-1)
        enemy = copy.deepcopy(enemies[rand])
        perkapply(enemy)
        difficulty = 3
    elif battlecounter % 3 == 0:
        enemies = [senerios.ms1, senerios.ms2, senerios.ms3, senerios.ms4, senerios.ms5, senerios.ms6, senerios.ms7, senerios.ms8, senerios.ms9, senerios.ms10, senerios.ms11, senerios.ms12, senerios.ms13, senerios.ms14, senerios.ms15, senerios.ms16, senerios.ms17, senerios.ms18, senerios.ms19, senerios.ms20]
        rand = random.randint(0, len(enemies) - 1)
        enemy = copy.deepcopy(enemies[rand])
        perkapply(enemy)
        difficulty = 2
    elif battlecounter % 1 == 0:
        enemies = [senerios.es1, senerios.es2, senerios.es3, senerios.es4, senerios.es5, senerios.es6, senerios.es7, senerios.es8, senerios.es9, senerios.es10, senerios.es11, senerios.es12, senerios.es13, senerios.es14, senerios.es15, senerios.es16, senerios.es17, senerios.es18, senerios.es19, senerios.es20]
        rand = random.randint(0, len(enemies) - 1)
        enemy = copy.deepcopy(enemies[rand])
        perkapply(enemy)
        difficulty = 1
    start.clear()
    print("round:", battlecounter)
    win = battleloop(enemy, difficulty, battlecounter)
    battlecounter = battlecounter + 1
    counter = 0
    if battlecounter % 10 == 0:
        print("Congrats you won!")
        input(">")
    print("Stats:")
    while len(crew.crewlist) > counter:
        print(crew.crewlist[counter].name)
        print("Speed:", crew.crewlist[counter].speed, "Health:",
              str(crew.crewlist[counter].health) + "/" + str(crew.crewlist[counter].maxhealth),
              "Shields:", crew.crewlist[counter].shield, "Priority:", crew.crewlist[counter].priority, "Defence:",
              crew.crewlist[counter].defence, "Regen:",
              crew.crewlist[counter].regen, "Energy_Regen:", crew.crewlist[counter].energyregen, "Energy:",
              crew.crewlist[counter].energy, "Attack:", crew.crewlist[counter].attack, "Ammo:", crew.crewlist[counter].ammo)
        counter = counter + 1
    if battlecounter % 10 == 0:
        print("Next fight: Boss")
    elif battlecounter % 4 == 0:
        print("Next fight: Hard")
    elif battlecounter % 3 == 0:
        print("Next fight: Medium")
    elif battlecounter % 1 == 0:
        print("Next fight: Easy")
    input(">")
    if win == True:
        itemloot(crew)
        randomevents(crew, altmoves)
    if win == False:
        break
    reset(crew.crewlist)
