from sty import fg

white = fg(255, 255, 255)
red = fg(255, 80, 80)
orange = fg(242, 184, 75)
yellow = fg(255, 255, 117)
light_green = fg(0, 255, 76)
green = fg(107, 143, 35)
light_blue = fg(82, 180, 255)
blue = fg(0, 123, 255)
dark_blue = fg(19, 85, 156)
purple = fg(162, 0, 255)
light_purple = fg(205, 117, 255)
gray = fg(130, 130, 130)
silver = fg(200, 230, 255)
brown = fg(150, 70, 0)
black = fg(255, 255, 255)
pink = fg(255, 105, 180)
cyan = fg(46, 161, 185)
mustard = fg(191, 144, 0)
aqua = fg(80, 255, 155)
blood = fg(133, 32, 12)
lavender = fg(136, 3, 252)

bold = "\033[1m"
italic = "\033[3m"

print(white + "")
# sets default color to white

def clear():
    x = 0
    while x < 10:
        print("")
        x = x + 1

#Explorers
soldier = blue + "Soldier" + white
marauder = orange + "Marauder" + white
medic = light_green + "Medic" + white
engineer = red + "Engineer" + white
captain = light_purple + "Captain" + white
survivor = purple + "Survivor" + white
#turrets
battleturretnm = light_blue + "Battle Turret" + white
forcefieldnm = light_blue + "Force Field" + white
defenceturretnm = light_blue + "Defence Turret" + white

#Ammo types
energy = light_blue + "Energy" + white
bullets = blue + "Bullets" + white
plating = orange + "Plating" + white
biomass = light_green + "Biomass" + white
bolts = red + "Bolts" + white
scrap = brown + "Scrap" + white

#moves soldier
photonblaster = blue + "Photon Blaster" + white
barrage = blue + "Barrage" + white
flaregun = blue + "Flare Gun" + white
energysheild = blue + "Energy Shield" + white
slice = blue + "Slice" + white
#alt soldier
phaseblaster = cyan + "Phase Blaster" + white
conversion = cyan + "Conversion" + white
energyafterburners = cyan + "Energy Afterburners" + white
satanstrike = cyan + "Storm Strike" + white
#moves marauder
kineticcollide = orange + "Kinetic Collide" + white
backstab = orange + "Backstab" + white
stealthgear = orange + "Stealth Gear" + white
blindingstrike = orange + "Blinding Strike" + white
strike = orange + "Strike" + white
#alt marauder
confusionbomb = mustard + "Confusion Bomb" + white
lifesteal = mustard + "Life Steal" + white
sensoryoverflow = mustard + "Sensory Overflow" + white
laceddagger = mustard + "Laced Dagger" + white
#moves medic
leech = light_green + "Leech" + white
vitalsabotage = light_green + "Vital Sabotage" + white
bioreport = light_green + "Bio Report" + white
bioreactor = light_green + "Bioreactor" + white
chop = light_green + "Chop" + white
#alt medic
sensoryunderflow = aqua + "Sensory Underflow" + white
burningblood = aqua + "Burning Blood" + white
terrarium = aqua + "Terrarium" + white
blooddonation = aqua + "Blood Donation" + white
#moves engineer
battleturret = red + "Battle Turret" + white
forcefield = red + "Force Field" + white
pipebomb = red + "Pipe Bomb" + white
concussiongrenade = red + "Concussion Grenade" + white
wack = red + "Wack" + white
#alt engineer
ascend = blood + "Ascend" + white
mechanicallock = blood + "Mechanical Lock" + white
barricade = blood + "Barricade" + white
c4 = blood + "C4" + white
#moves captain
salute = light_purple + "Salute" + white
nanobots = light_purple + "Nanobots" + white
defenseturrets = light_purple + "Defense Turrets" + white
personalbarrier = light_purple + "Personal Barrier" + white
slap = light_purple + "Slap" + white
#alt captain
energywell = lavender + "Energy Well" + white
malware = lavender + "Malware" + white
unstablecatalyst = lavender + "Unstable Catalyst" + white
syntheticbread = lavender + "Synthetic Bread" + white
#moves survivor
gravitywell = purple + "Gravity Well" + white
siphon = purple + "Siphon" + white
toughtimes = purple + "Tough Times" + white
powerup = purple + "Power Up" + white
shred = purple + "Shred" + white
#random
nothing = gray + "Nothing" + white
heal = light_green + "Heal" + white
ammo = light_blue + "Ammo" + white
#turret moves
blast = light_blue + "Blast" + white
bash = light_blue + "Bash" + white
protect = light_blue + "Protect" + white
shield = light_blue + "Shield" + white
#scavenger
tripleshotgun = brown + "Triple Barrel Shotgun" + white
bottlerocket = brown + "Bottle Rocket" + white
scrapbarrier = brown + "Scrap Barrier" + white
bagofacid = brown + "Bag of Acid" + white
#twisted scavenger
endlessportal = light_purple + "Endless Portal" + white
quadshotgun = light_purple + "Quadruple Barrel Shotgun" + white
cannibalism = light_purple + "Cannibalism" + white
twistedtentacle = light_purple + "Twisted Tentacle" + white
#solus moves
slash = yellow + "Slash" + white
ram = yellow + "Ram" + white
harden = yellow + "Harden" + white
spray = yellow + "Poison Spray" + white
#reploid moves
replicate = light_green + "Replicate" + white
lash = light_green + "Lash" + white
#judge moves
justice = red + "Crushing Justice" + white
truth = red + "Burning Truth" + white
execution = red + "Execution" + white
call = red + "Call to Arms" + white
#fungal moves
spore = purple + "Fungal Spores" + white
strspore = purple + "Strong Spores" + white
shroom = purple + "Shroomicide" + white
regrow = purple + "Fungal Growth" + white
smash = purple + "Shroom Smash" + white
#nova moves
riotshield = blue + "Riot Shield" + white
smokebomb = blue + "Smoke Bomb" + white
lightning = blue + "Lightning Punch" + white
supernova = blue + "Super Nova" + white
#tribe moves
strritual = green + "Strong Ritual" + white
defritual = green + "Sturdy Ritual" + white
healritual = green + "Healing Ritual" + white
poisonspear = green + "Poison Spear" + white
ancientshield = green + "Ancient Shield" + white
#vampdeer
vampirebite = red + "Vampire Bite" + white
#hunter moves
revolver = brown + "Revolver" + white
stungun = brown + "Stun Gun" + white
huntergear = brown + "Hunter Gear" + white
#void moves
voidstrike = pink + "Void Strike" + white
nullchant = pink + "Null Chant" + white
pray = pink + "Pray" + white
nullsmash = pink + "Null Smash" + white
voidmiracle = pink + "Void Miracle" + white
#enemies
moth = yellow + "Solus Moth" + white
beetle = yellow + "Solus Beetle" + white
reploid = light_green + "Reploid" + white
probe = light_blue + "Glitched Probe" + white
fungapede = purple + "Fungapede" + white

scavenger = brown + "Scavenger" + white
caracal = purple + "Fungal Caracal" + white
novasoldier = blue + "Nova Soldier" + white
shaman = green + "Shaman" + white
vampire = red + "Vampire Deer" + white

judge = red + "Judge" + white
enforcer = blue + "Nova Enforcer" + white
hunter = brown + "Bounty Hunter" + white
witch = green + "Witch Doctor" + white
worshiper = pink + "Void Worshiper" + white

twistedscavenger = light_purple + "Twisted Scavenger" + white
novacaptain = blue + "Nova Captain" + white
mainframe = light_blue + "Glitched Main Frame" + white
hive = purple + "Fungal Hive" + white
priest = pink + "Void Priest" + white
beast = pink + "Void Beast" + white

#afflictions
expose = silver + "Exposed" + white
defend = silver + "Defended" + white
stun = silver + "Stunned" + white
poison = silver + "Poisoned" + white
weaken = silver + "Weakened" + white
strength = silver + "Strengthened" + white

#items
aspectofaxo = pink + "Aspect of the Axolotl" + white
doubleedge = red + "Double Edged Sword" + white
cellular = pink + "Cellular Automata" + white
scope = pink + "Scope" + white
blitz = red + "Blitz Idol" + white
ironshield = red + "Iron Shield" + white
stemcells = pink + "Stem Cells" + white
mask = red + "Mad Mask" + white
energycell = pink + "Energy Cells" + white
orb = red + "Red Orb" + white
mind = red + "Irrational Mind" + white
nova = pink + "Nova Aspect" + white
