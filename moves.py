import start

class Move:
    def __init__(self, name, character, ammo, energy, dmg, leech, sacrifice, shield, stun, poison, weaken, strength,
                 expose, defend, summon, pierce, spd, priority, desc, speed, helpful):
        self.name = name
        self.character = character
        self.ammo = ammo
        self.energy = energy
        self.dmg = dmg
        self.leech = leech
        self.sacrifice = sacrifice
        self.shield = shield
        self.stun = stun
        self.poison = poison
        self.weaken = weaken
        self.strength = strength
        self.expose = expose
        self.defend = defend
        self.summon = summon
        self.pierce = pierce
        self.spd = spd
        self.priority = priority
        self.desc = desc
        self.speed = speed
        self.helpful = helpful #wether the attack should be used on your team or the other team


# Soldier(character ID 1)
# name, character, ammo, energy, dmg, leech, sacrifice, shield, stun, poison, weaken, strength, expose, defend, summon, pierce, spd, priority, desc
desc1 = "Fires three rounds for 50% damage each. Uses 15 energy."
photonblaster = Move(start.photonblaster, 1, 0, 15, 50, False, False, False, False, False, False, False, False, False, False, False, 3, False, desc1, False, False)

desc2 = "Fires a shotgun blast using 4 bullets to deal 200% damage exposes the enemy for 2 turns."
barrage = Move(start.barrage, 1, 4, 0, 200, False, False, False, False, False, False, False, 2, False, False, False, 1, False, desc2, False, False)

desc3 = "Uses 1 bullet to fire a flare that increases enemy aggression by 25. Strengthens the target for 2 turn."
flaregun = Move(start.flaregun, 1, 1, 0, 0, False, False, False, False, False, False, 2, False, False, False, False, 1, 25, desc3, False, True)

desc4 = "Uses 10 energy to create a shield that is 30% of the HP of the target."
energysheild = Move(start.energysheild, 1, 0, 10, 0, False, False, 30, False, False, False, False, False, False, False, False, 1, False, desc4, False, True)

desc5 = "Slice an enemy for 50% damage twice."
slice = Move(start.slice, 1, 0, 0, 50, False, False, False, False, False, False, False, False, False, False, False, 2, False, desc5, False, False)

# Marauder(character ID 2)
desc6 = "Deals 500% damage but deals 100% damage to self. Uses 10 plating."
kineticcollide = Move(start.kineticcollide, 2, 10, 0, 500, False, 100, False, False, False, False, False, False, False, False, False, 1, False, desc6, False, False)

desc7 = "Ignores defense while dealing 200% damage. Exposes target for 1 turn. Uses 10 energy."
backstab = Move(start.backstab, 2, 0, 10, 200, False, False, False, False, False, False, False, 1, False, False, True, 1, False, desc7, False, False)

desc8 = "Decreases enemy aggression by 10. Defends the target for 2 turns. Uses 10 energy."
stealthgear = Move(start.stealthgear, 2, 0, 10, 0, False, False, False, False, False, False, False, False, 2, False, False, 1, -10, desc8, False, True)

desc9 = "Deals 250% damage while stunning the target for 1 turn. Uses 20 energy, 10 plating."
blindingstrike = Move(start.blindingstrike, 2, 10, 20, 250, False, False, False, 1, False, False, False, False, False, False, False, 1, False, desc9, False, False)

desc10 = "Strike an enemy for 150% damage."
strike = Move(start.strike, 2, 0, 0, 150, False, False, False, False, False, False, False, False, False, False, False, 1, False, desc10, False, False)

# Medic(character ID 3)
desc11 = "Leech an enemy for its health dealing 100% damage. Uses 10 energy."
leech = Move(start.leech, 3, 0, 10, 100, True, False, False, False, False, False, False, False, False, False, False, 1, False, desc11, False, False)

desc12 = "Poison an enemy for 5 turns. Uses 10 biomass."
vitalsabotage = Move(start.vitalsabotage, 3, 10, 0, 0, False, False, False, False, 5, False, False, False, False, False, False, 1, False, desc12, False, False)

desc13 = "Heal target for 200% of your base damage. Uses 5 biomass and 10 energy."
bioreport = Move(start.bioreport, 3, 5, 10, -200, False, False, False, False, False, False, False, False, False, False, False, 1, False, desc13, False, True)

desc14 = "Restores 10 of the medic’s energy. Strengthens target for 1 turn. Uses 1 biomass."
bioreactor = Move(start.bioreactor, 3, 1, -10, 0, False, False, False, False, False, False, 1, False, False, False, False, 1, False, desc14, False, True)

desc15 = "Chop an enemy for 70% damage."
chop = Move(start.chop, 3, 0, 0, 70, False, False, False, False, False, False, False, False, False, False, False, 1, False, desc15, False, False)

# Engineer(character ID 4)
desc16 = "Build a turret that will fight for you. Uses 10 bolts and 20 energy."
battleturret = Move(start.battleturret, 4, 10, 10, 0, False, False, False, False, False, False, False, False, False, 7, False, 1, False, desc16, False, True)

desc17 = "Build a forcefield that will always be attacked first by enemies. Uses 30 energy."
forcefeild = Move(start.forcefield, 4, 0, 30, 0, False, False, False, False, False, False, False, False, False, 8, False, 1, False, desc17, False, True)

desc18 = "Create a pipe bomb that deals 200% damage and ignores defense. Uses 5 bolts and 10 energy."
pipebomb = Move(start.pipebomb, 4, 5, 10, 200, False, False, False, False, False, False, False, False, False, False, True, 1, False, desc18, False, False)

desc19 = "Expose and weaken target for 2 turns. Uses 10 energy."
concussiongrenade = Move(start.concussiongrenade, 4, 0, 10, 0, False, False, False, False, False, 2, False, 2, False, False, False, 1, False, desc19, False, False)

desc20 = "Wack an enemy for 80% damage."
wack = Move(start.wack, 4, 0, 0, 80, False, False, False, False, False, False, False, False, False, False, False, 1, False, desc20, False, False)

# Captain(character ID 5)
desc21 = "strengthen target for 2 turns. Uses 10 energy."
salute = Move(start.salute, 5, 0, 10, 0, False, False, False, False, False, False, 2, False, False, False, False, 1, False, desc21, False, True)

desc22 = "Create nanobots that defend a target for 2 turns. Target gains 10 speed. Uses 20 energy."
nanobots = Move(start.nanobots, 5, 0, 20, 0, False, False, False, False, False, False, False, False, 2, False, False, 1, False, desc22, 10, True)

desc23 = "Create turrets that are targeted before the captain. They have 100% HP and 20% damage. Uses 30 energy."
defenseturrets = Move(start.defenseturrets, 5, 0, 30, 0, False, False, False, False, False, False, False, False, False, 9, False, 1, False, desc23, False, True)

desc24 = "Creates a shield around the target equal to 100% of their HP. Uses 20 energy. Increases enemy aggression by 5."
personalbarrier = Move(start.personalbarrier, 5, 0, 20, 0, False, False, 100, False, False, False, False, False, False, False, False, 1, 5, desc24, False, True)

desc25 = "Slap an enemy for 100% damage."
slap = Move(start.slap, 5, 0, 0, 100, False, False, False, False, False, False, False, False, False, False, False, 1, False, desc25, False, False)

# Survivor(character ID 6)
desc26 = "Deal 600% damage to an enemy while dealing 200% to self. Uses 40 energy."
gravitywell = Move(start.gravitywell, 6, 0, 40, 600, False, 200, False, False, False, False, False, False, False, False, False, 1, False, desc26, False, False)

desc27 = "Deal 200% damage while leeching. Uses 30 energy."
siphon = Move(start.siphon, 6, 0, 30, 200, True, False, False, False, False, False, False, False, False, False, False, 1, False, desc27, False, False)

desc28 = "Weaken, poison and expose target for 4 turns. Deals 100% to self. Uses 20 energy"
toughtimes = Move(start.toughtimes, 6, 0, 20, 0, False, 100, False, False, 4, 4, False, 4, False, False, False, 1, False, desc28, False, False)

desc29 = "Target gets defended and strengthened for 2 turns but is hurt for 50% damage. Uses 30 energy."
powerup = Move(start.powerup, 6, 0, 30, 0, False, 50, False, False, False, False, 2, False, 2, False, False, 1, False, desc29, False, True)

desc30 = "Shred an enemy for 130% damage while dealing 10% damage to self."
shred = Move(start.shred, 6, 0, 0, 130, False, 10, False, False, False, False, False, False, False, False, False, 1, False, desc30, False, False)

#random

desc31 = "Does nothing..."
nothing = Move(start.nothing, 0, 0, 0, 0, False, False, False, False, False, False, False, False, False, False, False, 1, False, desc31, False, False)

#turret moves

desc32 = "Blast the enemy for 100% damage. Uses 10 energy."
blast = Move(start.blast, 7, 0, 10, 100, False, False, False, False, False, False, False, False, False, False, False, 1, False, desc32, False, False)

desc33 = "Bash the enemy for 70% damage. Sacrifice 30% health."
bash = Move(start.bash, 7, 0, 0, 70, False, 30, False, False, False, False, False, False, False, False, False, 1, False, desc33, False, False)

desc34 = "Defend someone for 2 turn. Uses 10 energy."
protect = Move(start.protect, 7, 0, 10, 0, False, False, False, False, False, False, False, False, 2, False, False, 1, False, desc34, False, True)

desc35 = "Create a shield around someone for 20%. Uses 10 energy."
shield = Move(start.shield, 7, 0, 10, 0, False, False, 20, False, False, False, False, False, False, False, False, 1, False, desc35, False, True)

#scavenger moves ID 10

desc36 = "Fire a large blast dealing 300% damage. uses 6 scrap."
tripleshotgun = Move(start.tripleshotgun, 10, 6, 0, 300, False, False, False, False, False, False, False, False, False, False, False, 1, False, desc36, False, False)

desc37 = "Fire a homemade rocket dealing 100% damage and pierces armor, stuns the target for 1 turn. uses 3 scrap and 10 energy."
bottlerocket = Move(start.bottlerocket, 10, 3, 10, 100, False, False, False, 1, False, False, False, False, False, False, True, 1, False, desc37, False, False)

desc38 = "Create a scrap barrier that shields the target for 20% of their HP. Uses 2 scrap."
scrapbarrier = Move(start.scrapbarrier, 10, 2, 0, 0, False, False, 20, False, False, False, False, False, False, False, False, 1, False, desc38, False, True)

desc39 = "Poison a target for 3 turns deals 50% damage. Uses 10 energy."
bagofacid = Move(start.bagofacid, 10, 0, 10, 50, False, False, False, False, 3, False, False, False, False, False, False, 1, False, desc39, False, False)

#twisted scavenger moves ID 11

desc40 = "Fire a large blast dealing 400% damage. uses 8 scrap."
quadshotgun = Move(start.quadshotgun, 11, 8, 0, 400, False, False, False, False, False, False, False, False, False, False, False, 1, False, desc40, False, False)

desc41 = "Open a portal and summon a scavenger. Uses 100 energy"
endlessportal = Move(start.endlessportal, 11, 0, 100, 0, False, False, False, False, False, False, False, False, False, 10, False, 1, False, desc41, False, True)

desc42 = "Consume and leech your own allies to strengthen yourself. Deals 10000% damage, pierces and leeches. strengthen yourself for 3 turns. Uses 50 energy."
cannibalism = Move(start.cannibalism, 11, 0, 50, 10000, True, False, False, False, False, False, -3, False, False, False, True, 1, False, desc42, False, True)

desc43 = "Expose and weaken a target for 3 turns. Deals 100% damage. Uses 20 energy."
twistedtentacle = Move(start.twistedtentacle, 11, 0, 20, 100, False, False, False, False, False, 3, False, 3, False, False, False, 1, False, desc43, False, False)

#solus moves

desc44 = "Slash the target for 100% damage. Uses 5 energy"
slash = Move(start.slash, 0, 0, 5, 100, False, False, False, False, False, False, False, False, False, False, False, 1, False, desc44, False, False)

desc45 = "Ram the target for 150% damage. Deals 20% damage to self. Uses 5 energy."
ram = Move(start.ram, 0, 0, 5, 150, False, 20, False, False, False, False, False, False, False, False, False, 1, False, desc45, False, False)

desc46 = "Shield target for 20% and defend for 1 turn. Uses 6 energy."
harden = Move(start.harden, 0, 0, 6, 0, False, False, 20, False, False, False, False, False, 1, False, False, 1, False, desc46, False, True)

desc47 = "Spray the target for 70% damage and inflict poison for 2 turns. Uses 10 energy."
spray = Move(start.spray, 0, 0, 10, 70, False, False, False, False, 2, False, False, False, False, False, False, 1, False, desc47, False, False)

#Reploid moves

desc48 = "Replicate yourself. Uses 5 energy."
replicate = Move(start.replicate, 0, 0, 5, 0, False, False, False, False, False, False, False, False, False, 14, False, 1, False, desc48, False, True)

desc49 = "Lash for 100% damage."
lash = Move(start.lash, 0, 0, 0, 100, False, False, False, False, False, False, False, False, False, False, False, 1, False, desc49, False, False)

#Judge moves

desc50 = "Smash the target for 250% damage. Exposes the target for 2 turns. Uses 10 energy."
justice = Move(start.justice, 0, 0, 10, 250, False, False, False, False, False, False, False, 2, False, False, False, 1, False, desc50, False, False)

desc51 = "Expose target for 2 turns and strengthen self for 2 turns. Uses 20 Energy."
truth = Move(start.truth, 0, 0, 20, 0, False, False, False, False, False, False, -2, 2, False, False, False, 1, False, desc51, False, False)

desc52 = "Hit the target 4 times for 60% each while weakening 1 each time. Uses 25 energy."
execution = Move(start.execution, 0, 0, 25, 60, False, False, False, False, False, 1, False, False, False, False, False, 4, False, desc52, False, False)

desc53 = "Increase priority of target to 100. Stun target for 1 turn. Uses 10 energy."
call = Move(start.call, 0, 0, 10, 0, False, False, False, 1, False, False, False, False, False, False, False, 1, 100, desc53, False, False)

#shroom moves

desc54 = "Explodes dealing 300% damage to target while dealing 10000% damage to self."
shroom = Move(start.shroom, 0, 0, 0, 300, False, 10000, False, False, False, False, False, False, False, False, False, 1, False, desc54, False, False)

desc55 = "Summons a small Fungapede."
spore = Move(start.spore, 0, 0, 0, 0, False, False, False, False, False, False, False, False, False, 17, False, 1, False, desc55, False, True)

desc56 = "Summons a small Fungal Caracal."
strspore = Move(start.strspore, 0, 0, 0, 0, False, False, False, False, False, False, False, False, False, 18, False, 1, False, desc56, False, True)

desc57 = "Regrow target for 100% damage."
regrow = Move(start.regrow, 0, 0, 0, -100, False, False, False, False, False, False, False, False, False, False, False, 1, False, desc57, False, True)

desc58 = "Crush your opponents for 200% damage."
smash = Move(start.smash, 0, 0, 0, 200, False, False, False, False, False, False, False, False, False, False, False, 1, False, desc58, False, False)

#nova moves

desc59 = "Create a shield that is 30% of the HP of the target. Defend yourself for 2 turns."
riotshield = Move(start.riotshield, 0, 0, 0, 0, False, False, 30, False, False, False, False, False, -2, False, False, 1, False, desc59, False, True)

desc60 = "Expose and weaken the target for 3 turns and deal 50% damage."
smokebomb = Move(start.smokebomb, 0, 0, 0, 50, False, False, False, False, False, 2, False, 2, False, False, False, 1, False, desc60, False, False)

desc61 = "Deal 300% damage and stun target for 2 turns."
lightning = Move(start.lightning, 0, 0, 0, 300, False, False, False, 2, False, False, False, False, False, False, False, 1, False, desc61, False, False)

desc62 = "Deal 340% damage and. strengthen self, weaken target for 3 turns."
supernova = Move(start.supernova, 0, 0, 0, 340, False, False, False, False, False, 3, -3, False, False, False, False, 1, False, desc62, False, False)

#tribe moves

desc63 = "Strengthen target for 5 turns."
strritual = Move(start.strritual, 0, 0, 0, 0, False, False, False, False, False, False, 5, False, False, False, False, 1, False, desc63, False, True)

desc64 = "Defend target for 5 turns."
defritual = Move(start.defritual, 0, 0, 0, 0, False, False, False, False, False, False, False, False, 5, False, False, 1, False, desc64, False, True)

desc65 = "Heal target for 150% damage."
healritual = Move(start.healritual, 0, 0, 0, -150, False, False, False, False, False, False, False, False, False, False, False, 1, False, desc65, False, True)

desc66 = "Pierce target defence and poison for 3 turns. Deals 100% damage."
poisonspear = Move(start.poisonspear, 0, 0, 0, 150, False, False, False, False, 3, False, False, False, False, False, False, 1, False, desc66, False, False)

desc67 = "Shield target for 30% health."
ancientshield = Move(start.ancientshield, 0, 0, 0, 0, False, False, 30, False, False, False, False, False, False, False, False, 1, False, desc67, False, True)

#vampire moves

desc68 = "Bite the target for 150% and leech. strengthen for 2 turns."
vampirebite = Move(start.vampirebite, 0, 0, 0, 150, True, False, False, False, False, False, -2, False, False, False, False, 1, False, desc68, False, False)

#bounty hunter moves

desc69 = "Fire dealing 25% damage 6 times."
revolver = Move(start.revolver, 0, 0, 0, 25, False, False, False, False, False, False, False, False, False, False, False, 6, False, desc69, False, False)

desc70 = "Stun target for 2 turns and expose for 2 turns."
stungun = Move(start.stungun, 0, 0, 0, 0, False, False, False, 2, False, False, False, 2, False, False, False, 1, False, desc70, False, False)

desc71 = "Strength target for 3 turns."
huntergear = Move(start.huntergear, 0, 0, 0, 0, False, False, False, False, False, False, 5, False, False, False, False, 1, False, desc71, False, True)

#void moves

desc72 = "Strike the enemy for 200% damage. Dealing 140% to self."
voidstrike = Move(start.voidstrike, 0, 0, 0, 200, False, 140, False, False, False, False, False, False, False, False, False, 1, False, desc72, False, False)

desc73 = "Strength the target for 2 turns. Uses 20 energy."
nullchant = Move(start.nullchant, 6, 0, 20, 0, False, False, False, False, False, False, 2, False, False, False, False, 1, False, desc73, False, True)

desc74 = "Heal target for 200% damage. Uses 100 energy."
pray = Move(start.pray, 6, 0, 100, -200, False, False, False, False, False, False, False, False, False, False, False, 1, False, desc74, False, True)

desc75 = "Smash the enemy for 400% damage dealing 100% to self, uses 30 energy."
nullsmash = Move(start.nullsmash, 6, 0, 30, 400, False, 100, False, False, False, False, False, False, False, False, False, 1, False, desc72, False, False)

desc76 = "Deal 300% to target while dealing 100% damage to self. Defend self for 2 turns. uses 30 energy."
voidmiracle = Move(start.voidmiracle, 6, 0, 30, 300, False, 100, False, False, False, False, False, False, -2, False, False, 1, False, desc76, False, False)

#alt soldier

desc77 = "Fires 6 times dealing 40% damage each time. Uses 6 bullets."
phaseblaster = Move(start.phaseblaster, 1, 6, 0, 40, False, False, False, False, False, False, False, False, False, False, False, 6, False, desc77, False, False)

desc78 = "Deal 50% damage to self but target gains 60% shield. Defends target for 2 turns. Uses 15 energy."
conversion = Move(start.conversion, 1, 0, 15, 0, False, 50, 60, False, False, False, False, False, False, False, False, 1, False, desc78, False, True)

desc79 = "Increases target’s speed by 20. Strengthens target for 2 turns. Uses 20 energy."
energyafterburners = Move(start.energyafterburners, 1, 0, 20, 0, False, False, False, False, False, False, 2, False, False, False, False, 1, False, desc79, 20, True)

desc80 = "Deal 1000% to self and 1000% to target. Uses 100 energy."
satanstrike = Move(start.satanstrike, 1, 0, 100, 1000, False, 1000, False, False, False, False, False, False, False, False, False, 1, False, desc80, False, False)

#alt marauder

desc81 = "Ignores defence while dealing 270%. Target priority increased by 50. Uses 40 energy."
confusionbomb = Move(start.confusionbomb, 2, 0, 40, 270, False, False, False, False, False, False, False, False, False, False, True, 1, 50, desc81, False, False)

desc82 = "Deals 150% damage and leeches target. Uses 5 plating."
lifesteal = Move(start.lifesteal, 2, 5, 0, 150, True, False, False, False, False, False, False, False, False, False, False, 1, False, desc82, False, False)

desc83 = "Deal 500% damage but strengthen target for 2 turns. Increase target speed by 20. Uses 10 plating."
sensoryoverflow = Move(start.sensoryoverflow, 2, 10, 0, 500, False, False, False, False, False, False, 2, False, False, False, False, 1, False, desc83, 20, False)

desc84 = "Poison target for 2 turns deals 177% damage. Uses 35 energy."
laceddagger = Move(start.laceddagger, 2, 0, 35, 177, False, False, False, False, 2, False, False, False, False, False, False, 1, False, desc84, False, False)

#alt medic

desc85 = "Heal 300% of your base damage to the target. Target speed decreases by 20 and weakens the target for 2 turns. Uses 5 Biomass."
sensoryunderflow = Move(start.sensoryunderflow, 3, 5, 0, -300, False, False, False, False, False, 2, False, False, False, False, False, 1, False, desc85, -20, True)

desc86 = "Dealing 30% to self while dealing 200% to target. Uses 30 Energy."
burningblood = Move(start.burningblood, 3, 0, 30, 200, False, 30, False, False, False, False, False, False, False, False, False, 1, False, desc86, False, False)

desc87 = "Gain 5 biomass for 50 energy."
terrarium = Move(start.terrarium, 3, 5, -50, 0, False, False, False, False, False, False, False, False, False, False, False, 1, False, desc14, False, True)

desc88 = "Deal 200% to self while healing 400% to the target. Uses 25 energy, 3 biomass."
blooddonation = Move(start.blooddonation, 3, 3, 25, -400, False, 200, False, False, False, False, False, False, False, False, False, 1, False, desc88, False, True)

#alt engineer

desc89 = "Deals 200% to target. Target gains 100% shields. Uses 7 bolts."
ascend = Move(start.ascend, 4, 7, 0, 200, False, False, 100, False, False, False, False, False, False, False, False, 1, False, desc89, False, True)

desc90 = "Deals 180% damage. Lowers target’s speed by 15, uses 15 energy."
mechanicallock = Move(start.mechanicallock, 4, 0, 15, 180, False, False, False, False, False, False, False, False, False, False, False, 1, False, desc90, -15, False)

desc91 = "Defends target for 4 turns. Uses 4 bolts and 20 Energy."
barricade = Move(start.barricade, 4, 4, 20, 0, False, False, False, False, False, False, False, False, 4, False, False, 1, False, desc91, False, True)

desc92 = "Deals 150% damage 2 times. Uses 30 Energy."
c4 = Move(start.c4, 4, 0, 30, 150, False, False, False, False, False, False, False, False, False, False, False, 2, False, desc92, False, False)

#alt captain

desc93 = "Deal 70% damage to a target and gain 10 energy."
energywell = Move(start.energywell, 5, 0, -10, 70, False, False, False, False, False, False, False, False, False, False, False, 1, False, desc93, False, False)

desc94 = "Create malware that exposes the target for 4 turns. slows target for 10. uses 30 energy."
malware = Move(start.malware, 5, 0, 30, 0, False, False, False, False, False, False, False, 4, False, False, False, 1, False, desc94, -10, False)

desc95 = "Weaken target for 4 turns. Uses 20 energy."
unstablecatalyst = Move(start.unstablecatalyst, 5, 0, 20, 0, False, False, False, False, False, 4, False, False, False, False, False, 1, False, desc95, False, False)

desc96 = "Heal target for 100% base damage. Uses 30 energy."
syntheticbread = Move(start.syntheticbread, 5, 0, 30, -100, False, False, False, False, False, False, False, False, False, False, False, 1, False, desc96, False, True)
