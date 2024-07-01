import start

class Item:
  def __init__(self, name, desc, attack, defence, maxhealth, maxenergy, basepriority, baseshield, energyregen, regen, crit, speed, id):
      self.name = name
      self.desc = desc
      self.attack = attack
      self.defence = defence
      self.maxhealth = maxhealth
      self.maxenergy = maxenergy
      self.basepriority = basepriority
      self.baseshield = baseshield
      self.energyregen = energyregen
      self.regen = regen
      self.crit = crit
      self.speed = speed
      self.id = id

#id 1
aspectofaxodesc = "Increases regen by 10."
aspectofaxo = Item(start.aspectofaxo, aspectofaxodesc, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 1)
#id 2
doubleedgedesc = "Increases damage by 20% but decreases health by 10%."
doubleedge = Item(start.doubleedge, doubleedgedesc, 20, 0, -10, 0, 0, 0, 0, 0, 0, 0, 2)
#id 3
cellulardesc = "Increases energy regen by 10."
cellular = Item(start.cellular, cellulardesc, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 3)
#id 4
scopedesc = "Increases critical chance by 20."
scope = Item(start.scope, scopedesc, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 4)
#id 5
blitzdesc = "Increases speed by 20 but lower critical chance by 5."
blitz = Item(start.blitz, blitzdesc, 0, 0, 0, 0, 0, 0, 0, 0, -5, 20, 5)
#id 6
ironshielddesc = "Increases defence by 20 (max 40 defence). Decreases speed by 10."
ironshield = Item(start.ironshield, ironshielddesc, 0, 20, 0, 0, 0, 0, 0, 0, 0, -10, 6)
#id 7
stemcellsdesc = "Increases health by 30%."
stemcells = Item(start.stemcells, stemcellsdesc, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0, 7)
#id 8
maskdesc = "Increases priority by 10. Increases defence by 20 (max 40 defence)."
mask = Item(start.mask, maskdesc, 0, 20, 0, 0, 10, 0, 0, 0, 0, 0, 8)
#id 9
energycelldesc = "Increases max energy by 30%."
energycell = Item(start.energycell, energycelldesc, 0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 9)
#id 10
orbdesc = "Decreases regen by 10. Increases attack by 40%."
orb = Item(start.orb, orbdesc, 40, 0, 0, 0, 0, 0, 0, -10, 0, 0, 10)
#id 11
minddesc = "Lowers priority by 25. Decreases energy regen by 5"
mind = Item(start.mind, minddesc, 0, 0, 0, 0 , -25, 0, 0, -5, 0, 0, 11)
#id 12
novadesc = "Increases base shield by 30."
nova = Item(start.nova, novadesc, 0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0)
