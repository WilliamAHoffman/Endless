import copy
import entity
import start
import moves
import random

def summon(move, target, enemies, crewlist, attacker):
    summoned = entity.battleturret
    if move.summon == 7:
        summoned = entity.battleturret
    elif move.summon == 8:
        summoned = entity.forcefield
    elif move.summon == 9:
        summoned = entity.defenceturret
    elif move.summon == 10:
        summoned = entity.scavenger
    elif move.summon == 14:
        summoned = entity.reploid
    elif move.summon == 17:
        summoned = entity.funga
    elif move.summon == 18:
        summoned = entity.caracal
    summonedcpy = copy.deepcopy(summoned)
    summonedcpy.lvl = attacker.lvl
    summonedcpy.maxhealth = int(summonedcpy.maxhealth * (1.1**summonedcpy.lvl))
    summonedcpy.maxenergy = int(summonedcpy.maxenergy + (5*summonedcpy.lvl))
    summonedcpy.attack = int(summonedcpy.attack * (1.1**summonedcpy.lvl))
    summonedcpy.baseshield = int(summonedcpy.baseshield * (1.1 ** summonedcpy.lvl))
    summonedcpy.shield = summonedcpy.baseshield
    summonedcpy.health = summonedcpy.maxhealth
    summonedcpy.energy = summonedcpy.maxenergy
    summonedcpy.id = False
    if target in crewlist:
        crewlist.append(summonedcpy)
    if target in enemies:
        enemies.append(summonedcpy)

def regen(attacker):
    if attacker.maxhealth > 10:
        attacker.health = attacker.health + attacker.regen
        attacker.energy = attacker.energy + attacker.energyregen
        if attacker.health < 0:
            attacker.health = 1

def affapply(move, target, attacker):
    if move.stun != False:
        if move.stun > 0:
            target.affliction[5] = target.affliction[5] + move.stun
            print(target.name, "was stunned for", move.stun, "turns!")
        if move.stun < 0:
            attacker.affliction[5] = attacker.affliction[5] - move.stun
            print(attacker.name, "was stunned for", -move.stun, "turns!")
    if move.poison != False:
        if move.poison > 0:
            target.affliction[4] = target.affliction[4] + move.poison
            print(target.name, "was poisoned for", move.poison, "turns!")
        if move.poison < 0:
            attacker.affliction[4] = attacker.affliction[4] - move.poison
            print(attacker.name, "was poisoned for", -move.poison, "turns!")
    if move.weaken != False:
        if move.weaken > 0:
            target.affliction[3] = target.affliction[3] + move.weaken
            print(target.name, "was weakened for", move.weaken, "turns!")
        if move.weaken < 0:
            attacker.affliction[3] = attacker.affliction[3] - move.weaken
            print(attacker.name, "was weakened for", -move.weaken, "turns!")
    if move.strength != False:
        if move.strength > 0:
            target.affliction[2] = target.affliction[2] + move.strength
            print(target.name, "was strengthened for", move.strength, "turns!")
        if move.strength < 0:
            attacker.affliction[2] = attacker.affliction[2] - move.strength
            print(attacker.name, "was strengthened for", -move.strength, "turns!")
    if move.expose != False:
        if move.expose > 0:
            target.affliction[0] = target.affliction[0] + move.expose
            print(target.name, "was exposed for", move.expose, "turns!")
        if move.expose < 0:
            attacker.affliction[0] = attacker.affliction[0] - move.expose
            print(attacker.name, "was exposed for", -move.expose, "turns!")
    if move.defend != False:
        if move.defend > 0:
            target.affliction[1] = target.affliction[1] + move.defend
            print(target.name, "was defended for", move.defend, "turns!")
        if move.defend < 0:
            attacker.affliction[1] = attacker.affliction[1] - move.defend
            print(attacker.name, "was defended for", -move.defend, "turns!")

def afflictions(target):
    len = 5
    afflictionlist = []
    while len >= 0:
        # expose, defend, strength, weaken, poison, stun
        if len == 5:
            afflictionlist.append(start.stun)
            afflictionlist.append(target[len])
        elif len == 4:
            afflictionlist.append(start.poison)
            afflictionlist.append(target[len])
        elif len == 3:
            afflictionlist.append(start.weaken)
            afflictionlist.append(target[len])
        elif len == 2:
            afflictionlist.append(start.strength)
            afflictionlist.append(target[len])
        elif len == 1:
            afflictionlist.append(start.defend)
            afflictionlist.append(target[len])
        elif len == 0:
            afflictionlist.append(start.expose)
            afflictionlist.append(target[len])
        len = len - 1
    print(afflictionlist[0]+":", afflictionlist[1],afflictionlist[2]+":", afflictionlist[3], afflictionlist[4]+":",  afflictionlist[5], afflictionlist[6]+":", afflictionlist[7], afflictionlist[8]+":",  afflictionlist[9], afflictionlist[10]+":", afflictionlist[11])
    #print("")

def variance(value):
    spread = random.randint(-3, 3)
    value = value + spread
    return value

def battle(attacker, target, move, enemies, crewlist):
    if attacker.life == True:
        # regen
        regen(attacker)
        #poison
        if attacker.affliction[4] > 0:
            poison = int(attacker.maxhealth/10)
            attacker.health = attacker.health - poison
            if attacker.health <= 0:
                attacker.health = 1
            print(attacker.name, "took", poison, "damage from poison!")
        if target.life == True:
            if move.desc != "Does nothing...":
                if attacker.affliction[5] <= 0:
                    speed = move.spd
                    attacker.energy = attacker.energy - move.energy
                    attacker.ammo = attacker.ammo - move.ammo
                    while speed > 0:
                        #summon
                        if move.summon != False:
                            summon(move, target, enemies, crewlist, attacker)
                        speed = speed - 1
                        print(attacker.name, "used", move.name, "on", target.name+"!")

                        #Attack damage
                        if move.dmg > 0:
                            damage = (move.dmg/100)*attacker.attack
                            damage = variance(damage)
                            if move.pierce == False:
                                damage = damage - (damage * target.defence/100)
                            if move.pierce == True:
                                print("The attack pierced")
                            spread = random.randint(0, 100)
                            if attacker.crit >= spread:
                                damage = damage * 2
                                print("It's a critical!")
                            damage = int(damage)
                            #afflictions
                            if attacker.affliction[3] > 0:
                                print(attacker.name, "is weakened.")
                                damage = damage * 0.5
                            if attacker.affliction[2] > 0:
                                print(attacker.name, "is boosted by strength.")
                                damage = damage * 1.5
                            if target.affliction[1] > 0:
                                print(target.name, "is defended.")
                                damage = damage * 0.5
                            if target.affliction[0] > 0:
                                print(target.name, "is exposed.")
                                damage = damage * 1.5
                            damage = int(damage)
                            if damage < 0:
                                damage = 0
                            print(target.name, "took", damage, "damage!")
                            if damage > target.shield:
                                target.health = target.health + target.shield - damage
                                target.shield = 0
                            else:
                                target.shield = target.shield - damage
                            #leeching
                            if move.leech == True:
                                print(attacker.name, "healed", int(damage/2))
                                attacker.health = attacker.health + int(damage/2)
                        #healing
                        if move.dmg < 0:
                            healing = -((move.dmg/100)*attacker.attack)
                            healing = variance(healing)
                            healing = int(healing)
                            target.health = target.health + healing
                            print(target.name, "was healed for", healing)
                        #sacrifice
                        if move.sacrifice > 0:
                            sacrifice = (move.sacrifice/100) * attacker.attack
                            sacrifice = variance(sacrifice)
                            sacrifice = int(sacrifice)
                            if sacrifice <= 0:
                                sacrifice = 1
                            if sacrifice > attacker.shield:
                                attacker.health = attacker.health + attacker.shield - sacrifice
                                attacker.shield = 0
                            else:
                                attacker.shield = attacker.shield - sacrifice
                            print(attacker.name, "took", sacrifice, "self damage.")
                        #priority
                        if move.priority != 0:
                            target.priority = target.priority + move.priority
                            if target.priority < 0:
                                target.priority = 0
                            if target.priority > 100:
                                target.priority = 100
                            if move.priority > 0:
                                print(target.name, "priority increased by", move.priority)
                            else:
                                print(target.name, "priority decreased by", -(move.priority))
                        #shields
                        if move.shield > 0:
                            shield = (move.shield / 100) * target.maxhealth
                            shield = int(shield)
                            if target.maxhealth < 10:
                                shield = int((move.shield / 100) * target.shield * 1.5)
                            target.shield = int(target.shield + shield)
                            print(target.name, "was shielded for", shield)
                        if move.speed != False:
                            target.speed = target.speed + move.speed
                            if move.speed > 0:
                                print(target.name, "increased", move.speed, "speed")
                            else:
                                print(target.name, "decreased", -move.speed, "speed")
                        affapply(move, target, attacker)
                else:
                    print(attacker.name, "was stunned!")
                input("> ")
    #checks
    #if attacker.health == False:
    #    attacker.life = False
    #if target.health == False:
    #    target.life = False
    if attacker.health <= 0:
        attacker.life = False
    if target.health <= 0:
        target.life = False
    if attacker.energy > attacker.maxenergy:
        attacker.energy = attacker.maxenergy
    if attacker.health > attacker.maxhealth:
        attacker.health = attacker.maxhealth
    if target.health > target.maxhealth:
        target.health = target.maxhealth
    counter5 = 5
    while counter5 >= 0:
        if attacker.affliction[counter5] > 0:
            attacker.affliction[counter5] = attacker.affliction[counter5] - 1
        counter5 = counter5 - 1

def startbattle(usedmove, usedon, crewlist, enemies):
    lenteam = len(enemies)
    counter = 0
    while lenteam > counter:
        choice = random.randint(0,4)
        usedmove.append(enemies[counter].moves[choice])
        if enemies[counter].moves[choice].helpful == False:
            target = sorted(crewlist, key=lambda x: x.priority)
            lentarget = len(target)
            counter4 = 1
            while lentarget >= counter4:
                if target[lentarget-counter4].life == True:
                    choice = random.randint(0, 4)
                    if choice >= 1:
                        usedon.append(target[lentarget - counter4])
                        counter4 = counter4 + lentarget
                    if choice == 0:
                        if counter4 == lentarget:
                            usedon.append(target[lentarget - counter4])
                            counter4 = counter4 + lentarget
                counter4 = counter4 + 1
        else:
            choice = random.randint(0,4)
            if choice > 3:
                lenenemies = len(enemies)
                choice = random.randint(1, lenenemies)
                usedon.append(enemies[choice-1])
            else:
                target = sorted(enemies, key=lambda x: x.priority)
                lentarget = len(target)
                usedon.append(target[lentarget-1])
        counter = counter + 1
    attackers = crewlist + enemies
    #ordering the attackers by their speed
    lenattackers = len(attackers)
    counter = 0
    speeds = []
    while lenattackers > counter:
        speeds.append(attackers[counter].speed)
        counter = counter + 1
    counter = 0
    while lenattackers > counter:
        maxvalue = max(speeds)
        indexmax = speeds.index(maxvalue)
        battle(attackers[indexmax], usedon[indexmax], usedmove[indexmax], enemies, crewlist)
        speeds[indexmax] = -1
        counter = counter + 1

def usage(crewlist, enemies):
    lenteam = len(crewlist)
    while 1 == 1:
        print("Who should they target?")
        counter = 0
        print("Crew:")
        while lenteam > counter:
            if crewlist[counter].life == False:
                life = start.red + "Dead" + start.white
            else:
                life = start.green + "Alive" + start.white
            print("[" + str(counter) + "]", crewlist[counter].name)
            print("Health:", str(crewlist[counter].health)+"/"+str(crewlist[counter].maxhealth), "Shield:", crewlist[counter].shield, "Afflictions:", "Status:", life)
            counter = counter + 1
        counter2 = 0
        lenteam2 = len(enemies)
        print("Enemies:")
        while lenteam2 > counter2:
            print("[" + str(counter+counter2) + "]", enemies[counter2].name)
            print("Health:",str(enemies[counter2].health)+"/"+str(enemies[counter2].maxhealth), "Shield:", enemies[counter2].shield, "Afflictions:")
            counter2 = counter2 + 1
        try:
            choice = int(input("> "))
            if choice >= lenteam:
                usedon = enemies[choice-lenteam]
                start.clear()
                return usedon
            else:
                usedon = crewlist[choice]
                start.clear()
                return usedon
        except:
            print(start.red + "Invalid command!" + start.white)

def moveselect(explorer, id, usedmove, usedon, crewlist, enemies):
    while 1 == 1:
        print("What should the", explorer.name, "Do?")
        print("Energy:", str(explorer.energy)+"/"+str(explorer.maxenergy))
        print("Health:", str(explorer.health) + "/" + str(explorer.maxhealth))
        if explorer.ammoname != 0:
            print(str(explorer.ammoname)+":", explorer.ammo)
        print("Shield:", explorer.shield)
        print("Afflictions:")
        lenmoves = len(explorer.moves)
        counter = 0
        while lenmoves > counter:
            print("[" + str(counter) + "]", explorer.moves[counter].name+":", explorer.moves[counter].desc)
            counter = counter + 1
        print("[" + str(counter) + "]", "Go back.")
        try:
            choice = int(input("> "))
            start.clear()
            if choice == counter:
                return
            if explorer.ammo >= explorer.moves[choice].ammo:
                if explorer.energy >= explorer.moves[choice].energy:
                    usedmove[id] = explorer.moves[choice]
                    usedon[id] = usage(crewlist, enemies)
                    return
                else:
                    print(start.red + "Not enough energy!" + start.white)
            else:
                print(start.red+"Not enough ammo!"+start.white)
        except:
            start.clear()

def stats(enemies):
    counter2 = 0
    lenteam2 = len(enemies)
    print("Enemies:")
    while lenteam2 > counter2:
        print("[" + str(counter2) + "]", enemies[counter2].name, "Lvl:", enemies[counter2].lvl)
        print("Health:", str(enemies[counter2].health) + "/" + str(enemies[counter2].maxhealth), "Shield:", enemies[counter2].shield, "Speed:", enemies[counter2].speed, "Defence:", enemies[counter2].defence, "Regen:", enemies[counter2].regen)
        afflictions(enemies[counter2].affliction)
        counter2 = counter2 + 1
    input("> ")

def checklife(crew):
    counter = 0
    alive = 0
    while len(crew) > counter:
        if crew[counter].life == True:
            alive = alive + 1
        if crew[counter].life == False:
            if crew[counter].id == False:
                crew.pop(counter)
        counter = counter + 1
    if alive == 0:
        print("You lost...")
        return False

def checkenemy(enemies):
    enemylen = len(enemies) - 1
    while enemylen >= 0:
        if enemies[enemylen].life == False:
            print(enemies[enemylen].name, "Died!")
            enemies.pop(enemylen)
            if len(enemies) == 0:
                print("You win!")
                input("> ")
                return True
        enemylen = enemylen - 1

def main(crew, enemies):
    usedmove = []
    usedon = []
    enemylen = len(enemies)
    counter = 0
    print("You encountered:")
    while enemylen > counter:
        print(enemies[counter].name,"Lvl:",enemies[counter].lvl)
        counter = counter + 1
    print("Ready?")
    input("> ")
    start.clear()
    lenteam = len(crew.crewlist)
    counter = 0
    while lenteam > counter:
        usedmove.append(moves.nothing)
        usedon.append(enemies[0])
        counter = counter + 1
    while 1 == 1:
        print("What should we do?")
        counter = 0
        while lenteam > counter:
            print("["+str(counter)+"]", crew.crewlist[counter].name, "using:", usedmove[counter].name, "on:", usedon[counter].name)
            print("Speed:", crew.crewlist[counter].speed, "Health:", str(crew.crewlist[counter].health)+ "/"+ str(crew.crewlist[counter].maxhealth),
                  "Shields:", crew.crewlist[counter].shield, "Priority:", crew.crewlist[counter].priority, "Defence:", crew.crewlist[counter].defence,
                  "Regen:", crew.crewlist[counter].regen, "Attack:", crew.crewlist[counter].attack)
            afflictions(crew.crewlist[counter].affliction)
            counter = counter + 1
        print("["+str(counter)+"]", "Ready?")
        print("[" + str(counter+1) + "]", "Enemies")
        try:
            choice = int(input("> "))
            start.clear()
            if choice == counter:
                startbattle(usedmove, usedon, crew.crewlist, enemies)
                life = checklife(crew.crewlist)
                if life == False:
                    return False
                win = checkenemy(enemies)
                if win == True:
                    return True
                choice = counter + 1
                usedmove = []
                usedon = []
                counter3 = 0
                lenteam = len(crew.crewlist)
                while lenteam > counter3:
                    usedmove.append(moves.nothing)
                    usedon.append(enemies[0])
                    counter3 = counter3 + 1
            elif choice == counter+1:
                stats(enemies)
            selected = crew.crewlist[choice]
            if selected.life == True:
                moveselect(selected, choice, usedmove, usedon, crew.crewlist, enemies)
            else:
                print(selected.name, "is dead!")
        except:
            start.clear()
