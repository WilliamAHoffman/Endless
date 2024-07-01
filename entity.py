import start
import moves

class Entity:
  def __init__(self, name, attack, defence, health, maxhealth, maxenergy, energy, moves, desc, ammoname, ammo, items, basepriority, priority, affliction, shield, energyregen, regen, crit, lvl, speed, life, id, baseshield, basespeed, healthincrease):
    self.name = name
    self.attack = attack
    self.defence = defence
    self.health = health
    self.maxhealth = maxhealth
    self.maxenergy = maxenergy
    self.energy = energy
    self.moves = moves
    self.desc = desc
    self.ammoname = ammoname
    self.ammo = ammo
    self.items = items
    self.basepriority = basepriority
    self.priority = priority
    self.affliction = affliction
    self.shield = shield
    self.energyregen = energyregen
    self.regen = regen
    self.crit = crit
    self.lvl = lvl
    self.speed = speed
    self.life = life
    self.id = id
    self.baseshield = baseshield
    self.basespeed = basespeed
    self.healthincrease = healthincrease

crewlvl = 1

#players
#ID used for health increase
soldieraff = [0, 0, 0, 0, 0, 0] #expose, defend, strength, weaken, poison, stun
soldieritems = [moves.phaseblaster, moves.conversion, moves.energyafterburners, moves.satanstrike]
soldiermoves = [moves.photonblaster, moves.barrage, moves.flaregun, moves.energysheild, moves.slice]
soldierdesc = "The Soldier uses energy and bullets to deal lots of small bursts of damage. They have strong defenses and are not often targeted by enemies first."
soldier = Entity(start.soldier, 30, 10, 250, 250, 30, 30, soldiermoves, soldierdesc, start.bullets, 20, soldieritems, 20, 20, soldieraff, 0, 0, 0, 1, 0, 10, True, 1, 0, 10, 30)

marauderaff = [0, 0, 0, 0, 0, 0] #expose, defend, strength, weaken, poison, stun
marauderitems = [moves.confusionbomb, moves.lifesteal, moves.sensoryoverflow, moves.laceddagger]
maraudermoves = [moves.kineticcollide, moves.backstab, moves.stealthgear, moves.blindingstrike, moves.strike]
marauderdesc = "The Marauder uses energy and plating to deal large amounts of damage. They have extremely weak defenses and are very often targeted by enemies first."
marauder = Entity(start.marauder, 30, 0, 100, 100, 50, 50, maraudermoves, marauderdesc, start.plating, 20, marauderitems, 40, 40, marauderaff, 0, 0, 0, 1, 0, 20, True, 2, 0, 20, 10)

medicaff = [0, 0, 0, 0, 0, 0] #expose, defend, strength, weaken, poison, stun
medicitems = [moves.sensoryunderflow, moves.burningblood, moves.terrarium, moves.blooddonation]
medicmoves = [moves.leech, moves.vitalsabotage, moves.bioreport, moves.bioreactor, moves.chop]
medicdesc = "The Medic uses energy and biomass to heal other explorers. They have weak defenses and are often targeted by enemies first."
medic = Entity(start.medic, 30, 0, 150, 150, 30, 30, medicmoves, medicdesc, start.biomass, 20, medicitems, 30, 30, medicaff, 0, 0, 0, 1, 0, 15, True, 3, 0, 15, 20)

engineeraff = [0, 0, 0, 0, 0, 0] #expose, defend, strength, weaken, poison, stun
engineeritems = [moves.ascend, moves.mechanicallock, moves.barricade, moves.c4]
engineermoves = [moves.battleturret, moves.forcefeild, moves.pipebomb, moves.concussiongrenade, moves.wack]
engineerdesc = "The Engineer uses energy and bolts to create sentries to help the crew. They have extremely weak defenses and are often targeted by enemies first."
engineer = Entity(start.engineer, 30, 0, 100, 100, 30, 30, engineermoves, engineerdesc, start.bolts, 20, engineeritems, 30, 30, engineeraff, 0, 0, 0, 1, 0, 5, True, 5, 0, 4, 20)

captainaff = [0, 0, 0, 0, 0, 0] #expose, defend, strength, weaken, poison, stun
captainitems = [moves.energywell, moves.malware, moves.unstablecatalyst, moves.syntheticbread]
captainmoves = [moves.salute, moves.nanobots, moves.defenseturrets, moves.personalbarrier, moves.slap]
captaindesc = "The Captain uses energy to strengthen other explorers and call in reinforcements. They have good defenses and are not often targeted by enemies first."
captain = Entity(start.captain, 30, 0, 200, 200, 100, 100, captainmoves, captaindesc, 0, 0, captainitems, 25, 25, captainaff, 0, 0, 0, 1, 0, 5, True, 5, 0, 5, 25)

survivoraff = [0, 0, 0, 0, 0, 0] #expose, defend, strength, weaken, poison, stun
survivoritems = [moves.pray, moves.nullsmash, moves.nullchant, moves.voidmiracle]
survivormoves = [moves.gravitywell, moves.siphon, moves.toughtimes, moves.powerup, moves.shred]
survivordesc = "The Survivor uses energy to deal large amounts of damage while hurting themself. They have very good defenses and are almost always targeted by enemies first."
survivor = Entity(start.survivor, 30, 0, 200, 200, 100, 100, survivormoves, survivordesc, 0, 0, survivoritems, 50, 50, survivoraff, 0, 0, 0, 1, 0, 1, True, 6, 0, 1, 30)

#summons

#id 7
battleturretaff = [0, 0, 0, 0, 0, 0]
battleturretitems = []
battleturretmoves = [moves.blast, moves.blast, moves.blast, moves.blast, moves.bash]
battleturretdesc = "A basic battle turret."
battleturret = Entity(start.battleturretnm, 20, 0, 1, 1, 50, 50, battleturretmoves, battleturretdesc, 0, 0, battleturretitems, 10, 10, battleturretaff, 50, 0, 0, 1, 0, 8, True, 7, 100, 8, 0)

#id 8
forcefieldaff = [0, 0, 0, 0, 0, 0]
forcefielditems = []
forcefieldmoves = [moves.protect, moves.protect, moves.protect, moves.shield, moves.shield]
forcefielddesc = "A shield that is often attacked first."
forcefield = Entity(start.forcefieldnm, 20, 20, 1, 1, 50, 50, forcefieldmoves, forcefielddesc, 0, 0, forcefielditems, 100, 100, forcefieldaff, 100, 0, 0, 0, 0, 60, True, 8, 100, 60, 0)

#id 9
defenceturretaff = [0, 0, 0, 0, 0, 0]
defenceturretitems = []
defenceturretmoves = [moves.protect, moves.protect, moves.protect, moves.blast, moves.blast]
defenceturretdesc = "A turret to protect and attack."
defenceturret = Entity(start.defenceturretnm, 20, 0, 1, 1, 50, 50, defenceturretmoves, defenceturretdesc, 0, 0, defenceturretitems, 30, 30, defenceturretaff, 50, 0, 0, 1, 0, 1, True, 9, 100, 1, 0)

#enemies easy

#id 12
mothaff = [0, 0, 0, 0, 0, 0]
mothitems = []
mothmoves = [moves.slash, moves.slash, moves.slash, moves.slash, moves.ram]
mothdesc = "A large but weak moth."
moth = Entity(start.moth, 10, 0, 50, 50, 20, 20, mothmoves, mothdesc, 0, 0, mothitems, 5, 5, mothaff, 0, 0, 0, 1, 0, 25, True, 12, 0, 25, 0)

#id 13
beetleaff = [0, 0, 0, 0, 0, 0]
beetleitems = []
beetlemoves = [moves.ram, moves.ram, moves.harden, moves.spray, moves.spray]
beetledesc = "A large but weak beetle."
beetle = Entity(start.beetle, 15, 10, 60, 60, 30, 30, beetlemoves, beetledesc, 0, 0, beetleitems, 7, 7, beetleaff, 10, 0, 0, 1, 0, 5, True, 13, 10, 5, 0)

#id 14
reploidaff = [0, 0, 0, 0, 0, 0]
reploiditems = []
reploidmoves = [moves.replicate, moves.replicate, moves.replicate, moves.lash, moves.lash]
reploiddesc = "An extremely weak replicating organism."
reploid = Entity(start.reploid, 10, 0, 30, 30, 40, 40, reploidmoves, reploiddesc, 0, 0, reploiditems, 0, 0, reploidaff, 0, 10, -10, 10, 0, 6, True, 14, 0, 6, 0)

#id 16
probeaff = [0, 0, 0, 0, 0, 0]
probeitems = []
probemoves = [moves.bash, moves.blast, moves.blast, moves.shield, moves.blast]
probedesc = "A glitched out probe from the crews own ship"
probe = Entity(start.probe, 15, 10, 1, 1, 100, 100, probemoves, probedesc, 0, 0, probeitems, 12, 12, probeaff, 150, 0, 0, 1, 0, 17, True, 16, 150, 17, 0)

#id 17
fungaaff = [0, 0, 0, 0, 0, 0]
fungaitems = []
fungamoves = [moves.shroom, moves.shroom, moves.shroom, moves.shroom, moves.shroom]
fungadesc = "A small explosive shroom."
funga = Entity(start.fungapede, 10, 0, 40, 40, 10, 10, fungamoves, fungadesc, 0, 0, fungaitems, 10, 10, fungaaff, 0, 0, 0, 0, 0, 20, True, 17, 0, 20, 0)

#enemies medium

#id 10
scavengeraff = [0, 0, 0, 0, 0, 0]
scavengeritems = []
scavengermoves = [moves.tripleshotgun, moves.bottlerocket, moves.scrapbarrier, moves.bagofacid, moves.tripleshotgun]
scavengerdesc = "A quick thinking scavenger using junk to battle."
scavenger = Entity(start.scavenger, 10, 0, 300, 300, 70, 70, scavengermoves, scavengerdesc, start.scrap, 20, scavengeritems, 50, 50, scavengeraff, 0, 3, 3, 10, 0, 40, True, 10, 0, 40, 0)

#id 18
caracalaff = [0, 0, 0, 0, 0, 0]
caracalitems = []
caracalmoves = [moves.spore, moves.spore, moves.spore, moves.regrow, moves.regrow]
caracaldesc = "A small and quick caracal covered in fungus."
caracal = Entity(start.caracal, 20, 0, 100, 100, 50, 50, caracalmoves, caracaldesc, 0, 0, caracalitems, 20, 20, caracalaff, 0, 0, 0, 10, 0, 30, True, 18, 0, 30, 0)

#id 20
novasoldieraff = [0, 0, 0, 0, 0, 0]
novasoldieritems = []
novasoldiermoves = [moves.photonblaster, moves.photonblaster, moves.riotshield, moves.smokebomb, moves.barrage]
novasoldierdesc = "Standard soldier of the nova army."
novasoldier = Entity(start.novasoldier, 25, 10, 200, 200, 60, 60, novasoldiermoves, soldierdesc, 0, 0, novasoldieritems, 55, 55, novasoldieraff, 25, 0, 0, 5, 0, 20, True, 20, 25, 20, 0)

#id 23
shamanaff = [0, 0, 0, 0, 0, 0]
shamanitems = []
shamanmoves = [moves.healritual, moves.healritual, moves.healritual, moves.defritual, moves.strritual]
shamandesc = "A pacifist shaman."
shaman = Entity(start.shaman, 15, 0, 150, 150, 100, 100, shamanmoves, shamandesc, 0, 0, shamanitems, 1, 1, shamanaff, 0, 0, 0, 1, 0, 16, True, 23, 0, 16, 0)

#id 26
vampireaff = [0, 0, 0, 0, 0, 0]
vampireitems = []
vampiremoves = [moves.vampirebite, moves.vampirebite, moves.vampirebite, moves.vampirebite, moves.vampirebite]
vampiredesc = "A deer that leeches enemy lives."
vampire = Entity(start.vampire, 10, 0, 160, 160, 10, 10, vampiremoves, vampiredesc, 0, 0, vampireitems, 20, 20, vampireaff, 0, 0, -5, 30, 0, 30, True, 26, 0, 30, 0)

#enemies hard

#id 15
judgeaff = [0, 0, 0, 0, 0, 0]
judgeitems = []
judgemoves = [moves.execution, moves.justice, moves.justice, moves.truth, moves.call]
judgedesc = "A guardian of the planet Solus."
judge = Entity(start.judge, 25, 0, 500, 500, 60, 60, judgemoves, judgedesc, 0, 0, judgeitems, 60, 60, judgeaff, 0, 0, 0, 1, 0, 13, True, 15, 0, 13, 0)

#id 21
enforceraff = [0, 0, 0, 0, 0, 0]
enforceritems = []
enforcermoves = [moves.lightning, moves.lightning, moves.riotshield, moves.battleturret, moves.defenseturrets]
enforcerdesc = "A large enforcer."
enforcer = Entity(start.enforcer, 25, 20, 1, 1, 500, 500, enforcermoves, enforcerdesc, 0, 0, enforceritems, 70, 70, enforceraff, 300, 0, 0, 1, 0, 40, True, 21, 300, 40, 0)

#id 24
witchaff = [0, 0, 0, 0, 0, 0]
witchitems = []
witchmoves = [moves.healritual, moves.strritual, moves.defritual, moves.poisonspear, moves.ancientshield]
witchdesc = "An angry witch doctor."
witch = Entity(start.witch, 30, 0, 400, 400, 100, 100, witchmoves, witchdesc, 0, 0, witchitems, 5, 5, witchaff, 0, 0, 10, 1, 0, 20, True, 24, 0, 20, 0)

#id 27
hunteraff = [0, 0, 0, 0, 0, 0]
hunteritems = []
huntermoves = [moves.revolver, moves.revolver, moves.revolver, moves.huntergear, moves.stungun]
hunterdesc = "Hunter coming for yo ass."
hunter = Entity(start.hunter, 20, 10, 500, 500, 0, 0, huntermoves, hunterdesc, 0, 0, hunteritems, 60, 60, hunteraff, 0, 0, 0, 100, 0, 40, True, 27, 0, 40, 0)

#id 28
worshiperaff = [0, 0, 0, 0, 0, 0]
worshiperitems = []
worshipermoves = [moves.voidstrike, moves.voidstrike, moves.nullchant, moves.nullchant, moves.nullchant]
worshiperdesc = "Worshiper of the void beast."
worshiper = Entity(start.worshiper, 25, 0, 600, 600, 0, 0, worshipermoves, worshiperdesc, 0, 0, worshiperitems, 30, 30, worshiperaff, 0, 0, 0, 5, 0, 30, True, 28, 0, 30, 0)
#bosses

#id 11
twstscavengeraff = [0, 0, 0, 0, 0, 0]
twstscavengeritems = []
twstscavengermoves = [moves.quadshotgun, moves.endlessportal, moves.cannibalism, moves.twistedtentacle, moves.quadshotgun]
twstscavengerdesc = "A large corrupted scavenger."
twstscavenger = Entity(start.twistedscavenger, 30, 20, 1000, 1000, 500, 500, twstscavengermoves, twstscavengerdesc, start.scrap, 70, twstscavengeritems, 0, 0, twstscavengeraff, 0, 10, 10, 10, 0, 1, True, 11, 0, 1, 0)

#id 19
hiveaff = [999, 0, 0, 0, 0, 0]
hiveitems = []
hivemoves = [moves.strspore, moves.spore, moves.spore, moves.smash, moves.smash]
hivedesc = "The large leader of the hive!"
hive = Entity(start.hive, 40, 0, 1500, 1500, 500, 500, hivemoves, hivedesc, 0, 0, hiveitems, 100, 100, hiveaff, 0, 0, 0, 1, 0, 10, True, 19, 0, 10, 0)

#id 22
novacaptainaff = [0, 0, 0, 0, 0, 0]
novacaptainitems = []
novacaptainmoves = [moves.supernova, moves.lightning, moves.lightning, moves.battleturret, moves.defenseturrets]
novacaptaindesc = "The leader of the Nova Crew."
novacaptain = Entity(start.novacaptain, 30, 0, 900, 900, 500, 500, novacaptainmoves, novacaptaindesc, 0, 0, novacaptainitems, 100, 100, novacaptainaff, 0, 0, 0, 1, 0, 60, True, 22, 0, 60, 0)

#id 25
mainframeaff = [0, 0, 0, 0, 0, 0]
mainframeitems = []
mainframemoves = [moves.defenseturrets, moves.forcefeild, moves.battleturret, moves.blast, moves.blast]
mainframedesc = "The ships mainframe of the crew."
mainframe = Entity(start.mainframe, 50, 40, 1, 1, 10, 10, mainframemoves, mainframedesc, 0, 0, mainframeitems, 100, 100, mainframeaff, 1500, 0, 0, 1, 0, 30, True, 25, 1500, 30, 0)

#id 29
priestaff = [0, 0, 0, 0, 0, 0]
priestitems = []
priestmoves = [moves.pray, moves.pray, moves.voidmiracle, moves.nullchant, moves.voidmiracle]
priestdesc = "The high priest of void."
priest = Entity(start.priest, 20, 0, 600, 600, 0, 0, priestmoves, priestdesc, 0, 0, priestitems, 60, 60, priestaff, 0, 0, 0, 1, 0, 77, True, 29, 0, 77, 0)

#id 30
beastaff = [0, 0, 0, 0, 0, 0]
beastitems = []
beastmoves = [moves.nullsmash, moves.nullsmash, moves.nullsmash, moves.voidstrike, moves.voidstrike]
beastdesc = "Big boi"
beast = Entity(start.beast, 30, 0, 1200, 1200, 0, 0, beastmoves, beastdesc, 0, 0, beastitems, 100, 100, beastaff, 0, 0, 0, 1, 0, 40, True, 40, 0, 40, 0)