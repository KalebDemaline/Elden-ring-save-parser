from typing import Dict

class item_properties:
    def __init__(self, name, category):
        self.name = name
        self.category = category

all_item_dict: Dict[str, Dict[str, item_properties]] = {
    "armament": {
        "000F4240": {
        "name": "Dagger",
        "category": "Dagger"
      },
      "000F6950": {
        "name": "Black Knife",
        "category": "Dagger"
      },
      "000F9060": {
        "name": "Parrying Dagger",
        "category": "Dagger"
      },
      "000FB770": {
        "name": "Misericorde",
        "category": "Dagger"
      },
      "000FDE80": {
        "name": "Reduvia",
        "category": "Dagger"
      },
      "00100590": {
        "name": "Crystal Knife",
        "category": "Dagger"
      },
      "00102CA0": {
        "name": "Celebrant's Sickle",
        "category": "Dagger"
      },
      "001053B0": {
        "name": "Glintstone Kris",
        "category": "Dagger"
      },
      "00107AC0": {
        "name": "Scorpion's Stinger",
        "category": "Dagger"
      },
      "0010A1D0": {
        "name": "Great Knife",
        "category": "Dagger"
      },
      "0010C8E0": {
        "name": "Wakizashi",
        "category": "Dagger"
      },
      "0010EFF0": {
        "name": "Cinquedea",
        "category": "Dagger"
      },
      "00113E10": {
        "name": "Ivory Sickle",
        "category": "Dagger"
      },
      "00116520": {
        "name": "Bloodstained Dagger",
        "category": "Dagger"
      },
      "00118C30": {
        "name": "Erdsteel Dagger",
        "category": "Dagger"
      },
      "0011B340": {
        "name": "Blade of Calling",
        "category": "Dagger"
      },
      "001E8480": {
        "name": "Longsword",
        "category": "Straight Sword"
      },
      "001EAB90": {
        "name": "Short Sword",
        "category": "Straight Sword"
      },
      "001ED2A0": {
        "name": "Broadsword",
        "category": "Straight Sword"
      },
      "001F20C0": {
        "name": "Lordsworn's Straight Sword",
        "category": "Straight Sword"
      },
      "001F47D0": {
        "name": "Weathered Straight Sword",
        "category": "Straight Sword"
      },
      "001F6EE0": {
        "name": "Ornamental Straight Sword",
        "category": "Straight Sword"
      },
      "001F95F0": {
        "name": "Golden Epitaph",
        "category": "Straight Sword"
      },
      "001FBD00": {
        "name": "Nox Flowing Sword",
        "category": "Curved Sword"
      },
      "001FE410": {
        "name": "Inseparable Sword",
        "category": "Greatsword"
      },
      "00203230": {
        "name": "Coded Sword",
        "category": "Straight Sword"
      },
      "0020A760": {
        "name": "Sword of Night and Flame",
        "category": "Straight Sword"
      },
      "0020CE70": {
        "name": "Crystal Sword",
        "category": "Straight Sword"
      },
      "002143A0": {
        "name": "Carian Knight's Sword",
        "category": "Straight Sword"
      },
      "00216AB0": {
        "name": "Sword of St. Trina",
        "category": "Straight Sword"
      },
      "002191C0": {
        "name": "Miquellan Knight's Sword",
        "category": "Straight Sword"
      },
      "0021B8D0": {
        "name": "Cane Sword",
        "category": "Straight Sword"
      },
      "0021DFE0": {
        "name": "Regalia of Eochaid",
        "category": "Straight Sword"
      },
      "002206F0": {
        "name": "Noble's Slender Sword",
        "category": "Straight Sword"
      },
      "00222E00": {
        "name": "Warhawk's Talon",
        "category": "Straight Sword"
      },
      "00225510": {
        "name": "Lazuli Glintstone Sword",
        "category": "Straight Sword"
      },
      "00227C20": {
        "name": "Rotten Crystal Sword",
        "category": "Straight Sword"
      },
      "002DC6C0": {
        "name": "Bastard Sword",
        "category": "Greatsword"
      },
      "002DEDD0": {
        "name": "Forked Greatsword",
        "category": "Greatsword"
      },
      "002E14E0": {
        "name": "Iron Greatsword",
        "category": "Greatsword"
      },
      "002E3BF0": {
        "name": "Lordsworn's Greatsword",
        "category": "Greatsword"
      },
      "002E6300": {
        "name": "Knight's Greatsword",
        "category": "Greatsword"
      },
      "002E8A10": {
        "name": "Flamberge",
        "category": "Greatsword"
      },
      "002EB120": {
        "name": "Ordovis's Greatsword",
        "category": "Greatsword"
      },
      "002ED830": {
        "name": "Alabaster Lord's Sword",
        "category": "Greatsword"
      },
      "002EFF40": {
        "name": "Banished Knight's Greatsword",
        "category": "Greatsword"
      },
      "002F2650": {
        "name": "Dark Moon Greatsword",
        "category": "Greatsword"
      },
      "002F4D60": {
        "name": "Sacred Relic Sword",
        "category": "Greatsword"
      },
      "002FC290": {
        "name": "Helphen's Steeple",
        "category": "Greatsword"
      },
      "002FE9A0": {
        "name": "Blasphemous Blade",
        "category": "Greatsword"
      },
      "003010B0": {
        "name": "Marais Executioner's Sword",
        "category": "Greatsword"
      },
      "003037C0": {
        "name": "Sword of Milos",
        "category": "Greatsword"
      },
      "00305ED0": {
        "name": "Golden Order Greatsword",
        "category": "Greatsword"
      },
      "003085E0": {
        "name": "Claymore",
        "category": "Greatsword"
      },
      "0030ACF0": {
        "name": "Gargoyle's Greatsword",
        "category": "Greatsword"
      },
      "0030D400": {
        "name": "Death's Poker",
        "category": "Greatsword"
      },
      "0030FB10": {
        "name": "Gargoyle's Blackblade",
        "category": "Greatsword"
      },
      "003D0900": {
        "name": "Greatsword",
        "category": "Colossal Sword"
      },
      "003D3010": {
        "name": "Watchdog's Greatsword",
        "category": "Colossal Sword"
      },
      "003D5720": {
        "name": "Maliketh's Black Blade",
        "category": "Colossal Sword"
      },
      "003D7E30": {
        "name": "Troll's Golden Sword",
        "category": "Colossal Sword"
      },
      "003DA540": {
        "name": "Zweihander",
        "category": "Colossal Sword"
      },
      "003DCC50": {
        "name": "Starscourge Greatsword",
        "category": "Colossal Sword"
      },
      "003DF360": {
        "name": "Royal Greatsword",
        "category": "Colossal Sword"
      },
      "003E1A70": {
        "name": "Godslayer's Greatsword",
        "category": "Colossal Sword"
      },
      "003E4180": {
        "name": "Ruins Greatsword",
        "category": "Colossal Sword"
      },
      "003E8FA0": {
        "name": "Grafted Blade Greatsword",
        "category": "Colossal Sword"
      },
      "003EB6B0": {
        "name": "Troll Knight's Sword",
        "category": "Colossal Sword"
      },
      "004C4B40": {
        "name": "Estoc",
        "category": "Thrusting Sword"
      },
      "004C7250": {
        "name": "Cleanrot Knight's Sword",
        "category": "Thrusting Sword"
      },
      "004C9960": {
        "name": "Rapier",
        "category": "Thrusting Sword"
      },
      "004CC070": {
        "name": "Rogier's Rapier",
        "category": "Thrusting Sword"
      },
      "004CE780": {
        "name": "Antspur Rapier",
        "category": "Thrusting Sword"
      },
      "004D0E90": {
        "name": "Frozen Needle",
        "category": "Thrusting Sword"
      },
      "004D35A0": {
        "name": "Noble's Estoc",
        "category": "Thrusting Sword"
      },
      "005B8D80": {
        "name": "Bloody Helice",
        "category": "Heavy Thrusting Sword"
      },
      "005BB490": {
        "name": "Godskin Stitcher",
        "category": "Heavy Thrusting Sword"
      },
      "005BDBA0": {
        "name": "Great Epee",
        "category": "Heavy Thrusting Sword"
      },
      "005C29C0": {
        "name": "Dragon King's Cragblade",
        "category": "Heavy Thrusting Sword"
      },
      "006ACFC0": {
        "name": "Falchion",
        "category": "Curved Sword"
      },
      "006AF6D0": {
        "name": "Beastman's Curved Sword",
        "category": "Curved Sword"
      },
      "006B1DE0": {
        "name": "Shotel",
        "category": "Curved Sword"
      },
      "006B44F0": {
        "name": "Shamshir",
        "category": "Curved Sword"
      },
      "006B6C00": {
        "name": "Bandit's Curved Sword",
        "category": "Curved Sword"
      },
      "006B9310": {
        "name": "Magma Blade",
        "category": "Curved Sword"
      },
      "006BBA20": {
        "name": "Flowing Curved Sword",
        "category": "Curved Sword"
      },
      "006BE130": {
        "name": "Wing of Astel",
        "category": "Curved Sword"
      },
      "006C0840": {
        "name": "Scavenger's Curved Sword",
        "category": "Curved Sword"
      },
      "006C5660": {
        "name": "Eclipse Shotel",
        "category": "Curved Sword"
      },
      "006C7D70": {
        "name": "Serpent-God's Curved Sword",
        "category": "Curved Sword"
      },
      "006CA480": {
        "name": "Mantis Blade",
        "category": "Curved Sword"
      },
      "006CF2A0": {
        "name": "Scimitar",
        "category": "Curved Sword"
      },
      "006D19B0": {
        "name": "Grossmesser",
        "category": "Curved Sword"
      },
      "007A3910": {
        "name": "Onyx Lord's Greatsword",
        "category": "Curved Greatsword"
      },
      "007A6020": {
        "name": "Dismounter",
        "category": "Curved Greatsword"
      },
      "007A8730": {
        "name": "Bloodhound's Fang",
        "category": "Curved Greatsword"
      },
      "007AAE40": {
        "name": "Magma Wyrm's Scalesword",
        "category": "Curved Greatsword"
      },
      "007AD550": {
        "name": "Zamor Curved Sword",
        "category": "Curved Greatsword"
      },
      "007AFC60": {
        "name": "Omen Cleaver",
        "category": "Curved Greatsword"
      },
      "007B2370": {
        "name": "Monk's Flameblade",
        "category": "Curved Greatsword"
      },
      "007B4A80": {
        "name": "Beastman's Cleaver",
        "category": "Curved Greatsword"
      },
      "007B98A0": {
        "name": "Morgott's Cursed Sword",
        "category": "Curved Greatsword"
      },
      "00895440": {
        "name": "Uchigatana",
        "category": "Katana"
      },
      "00897B50": {
        "name": "Nagakiba",
        "category": "Katana"
      },
      "0089A260": {
        "name": "Hand of Malenia",
        "category": "Katana"
      },
      "0089C970": {
        "name": "Meteoric Ore Blade",
        "category": "Katana"
      },
      "0089F080": {
        "name": "Rivers of Blood",
        "category": "Katana"
      },
      "008A3EA0": {
        "name": "Moonveil",
        "category": "Katana"
      },
      "008A65B0": {
        "name": "Dragonscale Blade",
        "category": "Katana"
      },
      "008A8CC0": {
        "name": "Serpentbone Blade",
        "category": "Katana"
      },
      "00989680": {
        "name": "Twinblade",
        "category": "Twinblade"
      },
      "0098BD90": {
        "name": "Godskin Peeler",
        "category": "Twinblade"
      },
      "00990BB0": {
        "name": "Twinned Knight Swords",
        "category": "Twinblade"
      },
      "009959D0": {
        "name": "Eleonora's Poleblade",
        "category": "Twinblade"
      },
      "0099CF00": {
        "name": "Gargoyle's Twinblade",
        "category": "Twinblade"
      },
      "0099F610": {
        "name": "Gargoyle's Black Blades",
        "category": "Twinblade"
      },
      "00A7D8C0": {
        "name": "Mace",
        "category": "Hammer"
      },
      "00A7FFD0": {
        "name": "Club",
        "category": "Hammer"
      },
      "00A84DF0": {
        "name": "Curved Club",
        "category": "Hammer"
      },
      "00A87500": {
        "name": "Warpick",
        "category": "Hammer"
      },
      "00A89C10": {
        "name": "Morning Star",
        "category": "Hammer"
      },
      "00A8C320": {
        "name": "Varre's Bouquet",
        "category": "Hammer"
      },
      "00A8EA30": {
        "name": "Spiked Club",
        "category": "Hammer"
      },
      "00A91140": {
        "name": "Hammer",
        "category": "Hammer"
      },
      "00A93850": {
        "name": "Monk's Flamemace",
        "category": "Hammer"
      },
      "00A95F60": {
        "name": "Envoy's Horn",
        "category": "Hammer"
      },
      "00A98670": {
        "name": "Scepter of the All-Knowing",
        "category": "Hammer"
      },
      "00A9AD80": {
        "name": "Nox Flowing Hammer",
        "category": "Hammer"
      },
      "00A9D490": {
        "name": "Ringed Finger",
        "category": "Hammer"
      },
      "00A9FBA0": {
        "name": "Stone Club",
        "category": "Hammer"
      },
      "00AA22B0": {
        "name": "Marika's Hammer",
        "category": "Hammer"
      },
      "00B71B00": {
        "name": "Large Club",
        "category": "Great Hammer"
      },
      "00B74210": {
        "name": "Greathorn Hammer",
        "category": "Great Hammer"
      },
      "00B76920": {
        "name": "Battle Hammer",
        "category": "Great Hammer"
      },
      "00B80560": {
        "name": "Great Mace",
        "category": "Great Hammer"
      },
      "00B85380": {
        "name": "Curved Great Club",
        "category": "Great Hammer"
      },
      "00B916D0": {
        "name": "Celebrant's Skull",
        "category": "Great Hammer"
      },
      "00B93DE0": {
        "name": "Pickaxe",
        "category": "Great Hammer"
      },
      "00B964F0": {
        "name": "Beastclaw Greathammer",
        "category": "Great Hammer"
      },
      "00B98C00": {
        "name": "Envoy's Long Horn",
        "category": "Great Hammer"
      },
      "00B9B310": {
        "name": "Cranial Vessel Candlestand",
        "category": "Great Hammer"
      },
      "00B9DA20": {
        "name": "Great Stars",
        "category": "Great Hammer"
      },
      "00BA0130": {
        "name": "Brick Hammer",
        "category": "Great Hammer"
      },
      "00BA2840": {
        "name": "Devourer's Scepter",
        "category": "Great Hammer"
      },
      "00BA4F50": {
        "name": "Rotten Battle Hammer",
        "category": "Great Hammer"
      },
      "00C65D40": {
        "name": "Nightrider Flail",
        "category": "Flail"
      },
      "00C68450": {
        "name": "Flail",
        "category": "Flail"
      },
      "00C6AB60": {
        "name": "Family Heads",
        "category": "Flail"
      },
      "00C6D270": {
        "name": "Bastard's Stars",
        "category": "Flail"
      },
      "00C6F980": {
        "name": "Chainlink Flail",
        "category": "Flail"
      },
      "00D59F80": {
        "name": "Battle Axe",
        "category": "Axe"
      },
      "00D5C690": {
        "name": "Forked Hatchet",
        "category": "Axe"
      },
      "00D5EDA0": {
        "name": "Hand Axe",
        "category": "Axe"
      },
      "00D614B0": {
        "name": "Jawbone Axe",
        "category": "Axe"
      },
      "00D63BC0": {
        "name": "Iron Cleaver",
        "category": "Axe"
      },
      "00D662D0": {
        "name": "Ripple Blade",
        "category": "Axe"
      },
      "00D689E0": {
        "name": "Celebrant's Cleaver",
        "category": "Axe"
      },
      "00D6D800": {
        "name": "Icerind Hatchet",
        "category": "Axe"
      },
      "00D72620": {
        "name": "Highland Axe",
        "category": "Axe"
      },
      "00D74D30": {
        "name": "Sacrificial Axe",
        "category": "Axe"
      },
      "00D77440": {
        "name": "Rosus' Axe",
        "category": "Axe"
      },
      "00D7C260": {
        "name": "Stormhawk Axe",
        "category": "Axe"
      },
      "00E4E1C0": {
        "name": "Greataxe",
        "category": "Greataxe"
      },
      "00E508D0": {
        "name": "Warped Axe",
        "category": "Axe"
      },
      "00E52FE0": {
        "name": "Great Omenkiller Cleaver",
        "category": "Greataxe"
      },
      "00E556F0": {
        "name": "Crescent Moon Axe",
        "category": "Greataxe"
      },
      "00E57E00": {
        "name": "Axe of Godrick",
        "category": "Greataxe"
      },
      "00E5A510": {
        "name": "Longhaft Axe",
        "category": "Greataxe"
      },
      "00E5CC20": {
        "name": "Rusted Anchor",
        "category": "Greataxe"
      },
      "00E61A40": {
        "name": "Executioner's Greataxe",
        "category": "Greataxe"
      },
      "00E68F70": {
        "name": "Winged Greathorn",
        "category": "Greataxe"
      },
      "00E6B680": {
        "name": "Butchering Knife",
        "category": "Greataxe"
      },
      "00E6DD90": {
        "name": "Gargoyle's Great Axe",
        "category": "Greataxe"
      },
      "00E704A0": {
        "name": "Gargoyle's Black Axe",
        "category": "Greataxe"
      },
      "00F42400": {
        "name": "Short Spear",
        "category": "Spear"
      },
      "00F44B10": {
        "name": "Spear",
        "category": "Spear"
      },
      "00F47220": {
        "name": "Crystal Spear",
        "category": "Spear"
      },
      "00F49930": {
        "name": "Clayman's Harpoon",
        "category": "Spear"
      },
      "00F4C040": {
        "name": "Cleanrot Spear",
        "category": "Spear"
      },
      "00F4E750": {
        "name": "Partisan",
        "category": "Spear"
      },
      "00F50E60": {
        "name": "Celebrant's Rib-Rake",
        "category": "Spear"
      },
      "00F53570": {
        "name": "Pike",
        "category": "Spear"
      },
      "00F55C80": {
        "name": "Torchpole",
        "category": "Spear"
      },
      "00F58390": {
        "name": "Bolt of Gransax",
        "category": "Spear"
      },
      "00F5D1B0": {
        "name": "Cross-Naginata",
        "category": "Spear"
      },
      "00F5F8C0": {
        "name": "Death Ritual Spear",
        "category": "Spear"
      },
      "00F61FD0": {
        "name": "Inquisitor's Girandole",
        "category": "Spear"
      },
      "00F646E0": {
        "name": "Spiked Spear",
        "category": "Spear"
      },
      "00F66DF0": {
        "name": "Iron Spear",
        "category": "Spear"
      },
      "00F69500": {
        "name": "Rotten Crystal Spear",
        "category": "Spear"
      },
      "01038D50": {
        "name": "Mohgwyn's Sacred Spear",
        "category": "Great Spear"
      },
      "0103B460": {
        "name": "Siluria's Tree",
        "category": "Great Spear"
      },
      "0103DB70": {
        "name": "Serpent-Hunter",
        "category": "Great Spear"
      },
      "01042990": {
        "name": "Vyke's War Spear",
        "category": "Great Spear"
      },
      "010450A0": {
        "name": "Lance",
        "category": "Great Spear"
      },
      "010477B0": {
        "name": "Treespear",
        "category": "Great Spear"
      },
      "0112A880": {
        "name": "Halberd",
        "category": "Halberd"
      },
      "0112CF90": {
        "name": "Pest's Glaive",
        "category": "Halberd"
      },
      "0112F6A0": {
        "name": "Lucerne",
        "category": "Halberd"
      },
      "01131DB0": {
        "name": "Banished Knight's Halberd",
        "category": "Halberd"
      },
      "011344C0": {
        "name": "Commander's Standard",
        "category": "Halberd"
      },
      "01136BD0": {
        "name": "Nightrider Glaive",
        "category": "Halberd"
      },
      "011392E0": {
        "name": "Ripple Crescent Halberd",
        "category": "Halberd"
      },
      "0113B9F0": {
        "name": "Vulgar Militia Saw",
        "category": "Halberd"
      },
      "0113E100": {
        "name": "Golden Halberd",
        "category": "Halberd"
      },
      "01140810": {
        "name": "Glaive",
        "category": "Halberd"
      },
      "01142F20": {
        "name": "Loretta's War Sickle",
        "category": "Halberd"
      },
      "01145630": {
        "name": "Guardian's Swordspear",
        "category": "Halberd"
      },
      "0114A450": {
        "name": "Vulgar Militia Shotel",
        "category": "Halberd"
      },
      "0114CB60": {
        "name": "Dragon Halberd",
        "category": "Halberd"
      },
      "0114F270": {
        "name": "Gargoyle's Halberd",
        "category": "Halberd"
      },
      "01151980": {
        "name": "Gargoyle's Black Halberd",
        "category": "Halberd"
      },
      "0121EAC0": {
        "name": "Scythe",
        "category": "Reaper"
      },
      "012211D0": {
        "name": "Grave Scythe",
        "category": "Reaper"
      },
      "012238E0": {
        "name": "Halo Scythe",
        "category": "Reaper"
      },
      "0122D520": {
        "name": "Winged Scythe",
        "category": "Reaper"
      },
      "01312D00": {
        "name": "Whip",
        "category": "Whip"
      },
      "01317B20": {
        "name": "Thorned Whip",
        "category": "Whip"
      },
      "0131A230": {
        "name": "Magma Whip Candlestick",
        "category": "Whip"
      },
      "0131F050": {
        "name": "Hoslow's Petal Whip",
        "category": "Whip"
      },
      "01321760": {
        "name": "Giant's Red Braid",
        "category": "Whip"
      },
      "01323E70": {
        "name": "Urumi",
        "category": "Whip"
      },
      "01406F40": {
        "name": "Caestus",
        "category": "Fist"
      },
      "01409650": {
        "name": "Spiked Caestus",
        "category": "Fist"
      },
      "014159A0": {
        "name": "Grafted Dragon",
        "category": "Fist"
      },
      "014180B0": {
        "name": "Iron Ball",
        "category": "Fist"
      },
      "0141A7C0": {
        "name": "Star Fist",
        "category": "Fist"
      },
      "0141F5E0": {
        "name": "Katar",
        "category": "Fist"
      },
      "01421CF0": {
        "name": "Clinging Bone",
        "category": "Fist"
      },
      "01424400": {
        "name": "Veteran's Prosthesis",
        "category": "Fist"
      },
      "01426B10": {
        "name": "Cipher Pata",
        "category": "Fist"
      },
      "014FB180": {
        "name": "Hookclaws",
        "category": "Claw"
      },
      "014FD890": {
        "name": "Venomous Fang",
        "category": "Claw"
      },
      "014FFFA0": {
        "name": "Bloodhound Claws",
        "category": "Claw"
      },
      "015026B0": {
        "name": "Raptor Talons",
        "category": "Claw"
      },
      "015EF3C0": {
        "name": "Prelate's Inferno Crozier",
        "category": "Colossal Weapon"
      },
      "015F1AD0": {
        "name": "Watchdog's Staff",
        "category": "Colossal Weapon"
      },
      "015F41E0": {
        "name": "Great Club",
        "category": "Colossal Weapon"
      },
      "015F68F0": {
        "name": "Envoy's Greathorn",
        "category": "Colossal Weapon"
      },
      "015F9000": {
        "name": "Duelist Greataxe",
        "category": "Colossal Weapon"
      },
      "015FB710": {
        "name": "Axe of Godfrey",
        "category": "Colossal Weapon"
      },
      "015FDE20": {
        "name": "Dragon Greatclaw",
        "category": "Colossal Weapon"
      },
      "01600530": {
        "name": "Staff of the Avatar",
        "category": "Colossal Weapon"
      },
      "01602C40": {
        "name": "Fallingstar Beast Jaw",
        "category": "Colossal Weapon"
      },
      "01607A60": {
        "name": "Ghiza's Wheel",
        "category": "Colossal Weapon"
      },
      "0160A170": {
        "name": "Giant-Crusher",
        "category": "Colossal Weapon"
      },
      "0160C880": {
        "name": "Golem's Halberd",
        "category": "Colossal Weapon"
      },
      "0160EF90": {
        "name": "Troll's Hammer",
        "category": "Colossal Weapon"
      },
      "016116A0": {
        "name": "Rotten Staff",
        "category": "Colossal Weapon"
      },
      "01613DB0": {
        "name": "Rotten Greataxe",
        "category": "Colossal Weapon"
      },
      "016E3600": {
        "name": "Torch",
        "category": "Torch"
      },
      "016E8420": {
        "name": "Steel-Wire Torch",
        "category": "Torch"
      },
      "016ED240": {
        "name": "St. Trina's Torch",
        "category": "Torch"
      },
      "016EF950": {
        "name": "Ghostflame Torch",
        "category": "Torch"
      },
      "016F2060": {
        "name": "Beast-Repellent Torch",
        "category": "Torch"
      },
      "016F4770": {
        "name": "Sentry's Torch",
        "category": "Torch"
      },
      "01C9C380": {
        "name": "Buckler",
        "category": "Small Shield"
      },
      "01C9EA90": {
        "name": "Perfumer's Shield",
        "category": "Small Shield"
      },
      "01CA11A0": {
        "name": "Man-Serpent's Shield",
        "category": "Small Shield"
      },
      "01CA38B0": {
        "name": "Rickety Shield",
        "category": "Small Shield"
      },
      "01CA5FC0": {
        "name": "Pillory Shield",
        "category": "Small Shield"
      },
      "01CAADE0": {
        "name": "Beastman's Jar-Shield",
        "category": "Medium Shield"
      },
      "01CAD4F0": {
        "name": "Red Thorn Roundshield",
        "category": "Small Shield"
      },
      "01CAFC00": {
        "name": "Scripture Wooden Shield",
        "category": "Small Shield"
      },
      "01CB2310": {
        "name": "Riveted Wooden Shield",
        "category": "Small Shield"
      },
      "01CB4A20": {
        "name": "Blue-White Wooden Shield",
        "category": "Small Shield"
      },
      "01CB7130": {
        "name": "Rift Shield",
        "category": "Small Shield"
      },
      "01CB9840": {
        "name": "Iron Roundshield",
        "category": "Small Shield"
      },
      "01CBBF50": {
        "name": "Gilded Iron Shield",
        "category": "Small Shield"
      },
      "01CBE660": {
        "name": "Ice Crest Shield",
        "category": "Small Shield"
      },
      "01CC0D70": {
        "name": "Smoldering Shield",
        "category": "Small Shield"
      },
      "01CCA9B0": {
        "name": "Spiralhorn Shield",
        "category": "Small Shield"
      },
      "01CCD0C0": {
        "name": "Coil Shield",
        "category": "Small Shield"
      },
      "01D905C0": {
        "name": "Kite Shield",
        "category": "Medium Shield"
      },
      "01D92CD0": {
        "name": "Marred Leather Shield",
        "category": "Medium Shield"
      },
      "01D953E0": {
        "name": "Marred Wooden Shield",
        "category": "Medium Shield"
      },
      "01D97AF0": {
        "name": "Banished Knight's Shield",
        "category": "Medium Shield"
      },
      "01D9A200": {
        "name": "Albinauric Shield",
        "category": "Medium Shield"
      },
      "01D9C910": {
        "name": "Sun Realm Shield",
        "category": "Medium Shield"
      },
      "01D9F020": {
        "name": "Silver Mirrorshield",
        "category": "Medium Shield"
      },
      "01DA1730": {
        "name": "Round Shield",
        "category": "Medium Shield"
      },
      "01DA3E40": {
        "name": "Scorpion Kite Shield",
        "category": "Medium Shield"
      },
      "01DA6550": {
        "name": "Twinbird Kite Shield",
        "category": "Medium Shield"
      },
      "01DA8C60": {
        "name": "Blue-Gold Kite Shield",
        "category": "Medium Shield"
      },
      "01DB0190": {
        "name": "Brass Shield",
        "category": "Medium Shield"
      },
      "01DB28A0": {
        "name": "Great Turtle Shell",
        "category": "Medium Shield"
      },
      "01DB9DD0": {
        "name": "Shield of the Guilty",
        "category": "Small Shield"
      },
      "01DBEBF0": {
        "name": "Carian Knight's Shield",
        "category": "Medium Shield"
      },
      "01DC8830": {
        "name": "Large Leather Shield",
        "category": "Medium Shield"
      },
      "01DCAF40": {
        "name": "Horse Crest Wooden Shield",
        "category": "Medium Shield"
      },
      "01DCD650": {
        "name": "Candletree Wooden Shield",
        "category": "Medium Shield"
      },
      "01DCFD60": {
        "name": "Flame Crest Wooden Shield",
        "category": "Medium Shield"
      },
      "01DD2470": {
        "name": "Hawk Crest Wooden Shield",
        "category": "Medium Shield"
      },
      "01DD4B80": {
        "name": "Beast Crest Heater Shield",
        "category": "Medium Shield"
      },
      "01DD7290": {
        "name": "Red Crest Heater Shield",
        "category": "Medium Shield"
      },
      "01DD99A0": {
        "name": "Blue Crest Heater Shield",
        "category": "Medium Shield"
      },
      "01DDC0B0": {
        "name": "Eclipse Crest Heater Shield",
        "category": "Medium Shield"
      },
      "01DDE7C0": {
        "name": "Inverted Hawk Heater Shield",
        "category": "Medium Shield"
      },
      "01DE0ED0": {
        "name": "Heater Shield",
        "category": "Medium Shield"
      },
      "01DE35E0": {
        "name": "Black Leather Shield",
        "category": "Medium Shield"
      },
      "01E84800": {
        "name": "Dragon Towershield",
        "category": "Greatshield"
      },
      "01E89620": {
        "name": "Distinguished Greatshield",
        "category": "Greatshield"
      },
      "01E8BD30": {
        "name": "Crucible Hornshield",
        "category": "Greatshield"
      },
      "01E8E440": {
        "name": "Dragonclaw Shield",
        "category": "Greatshield"
      },
      "01E90B50": {
        "name": "Briar Greatshield",
        "category": "Greatshield"
      },
      "01E98080": {
        "name": "Erdtree Greatshield",
        "category": "Greatshield"
      },
      "01E9A790": {
        "name": "Golden Beast Crest Shield",
        "category": "Greatshield"
      },
      "01EA1CC0": {
        "name": "Jellyfish Shield",
        "category": "Greatshield"
      },
      "01EA43D0": {
        "name": "Fingerprint Stone Shield",
        "category": "Greatshield"
      },
      "01EA6AE0": {
        "name": "Icon Shield",
        "category": "Greatshield"
      },
      "01EA91F0": {
        "name": "One-Eyed Shield",
        "category": "Greatshield"
      },
      "01EAB900": {
        "name": "Visage Shield",
        "category": "Greatshield"
      },
      "01EAE010": {
        "name": "Spiked Palisade Shield",
        "category": "Greatshield"
      },
      "01EB2E30": {
        "name": "Manor Towershield",
        "category": "Greatshield"
      },
      "01EB5540": {
        "name": "Crossed-Tree Towershield",
        "category": "Greatshield"
      },
      "01EB7C50": {
        "name": "Inverted Hawk Towershield",
        "category": "Greatshield"
      },
      "01EBA360": {
        "name": "Ant's Skull Plate",
        "category": "Greatshield"
      },
      "01EBCA70": {
        "name": "Redmane Greatshield",
        "category": "Greatshield"
      },
      "01EBF180": {
        "name": "Eclipse Crest Greatshield",
        "category": "Greatshield"
      },
      "01EC1890": {
        "name": "Cuckoo Greatshield",
        "category": "Greatshield"
      },
      "01EC3FA0": {
        "name": "Golden Greatshield",
        "category": "Greatshield"
      },
      "01EC66B0": {
        "name": "Gilded Greatshield",
        "category": "Greatshield"
      },
      "01EC8DC0": {
        "name": "Haligtree Crest Greatshield",
        "category": "Greatshield"
      },
      "01ECB4D0": {
        "name": "Wooden Greatshield",
        "category": "Greatshield"
      },
      "01ECDBE0": {
        "name": "Lordsworn's Shield",
        "category": "Greatshield"
      },
      "01F78A40": {
        "name": "Glintstone Staff",
        "category": "Glintstone Staff"
      },
      "01F82680": {
        "name": "Crystal Staff",
        "category": "Glintstone Staff"
      },
      "01F84D90": {
        "name": "Gelmir Glintstone Staff",
        "category": "Glintstone Staff"
      },
      "01F874A0": {
        "name": "Demi-Human Queen's Staff",
        "category": "Glintstone Staff"
      },
      "01F8E9D0": {
        "name": "Carian Regal Scepter",
        "category": "Glintstone Staff"
      },
      "01F95F00": {
        "name": "Digger's Staff",
        "category": "Glintstone Staff"
      },
      "01F98610": {
        "name": "Astrologer's Staff",
        "category": "Glintstone Staff"
      },
      "01FA2250": {
        "name": "Carian Glintblade Staff",
        "category": "Glintstone Staff"
      },
      "01FA4960": {
        "name": "Prince of Death's Staff",
        "category": "Glintstone Staff"
      },
      "01FA7070": {
        "name": "Albinauric Staff",
        "category": "Glintstone Staff"
      },
      "01FA9780": {
        "name": "Academy Glintstone Staff",
        "category": "Glintstone Staff"
      },
      "01FABE90": {
        "name": "Carian Glintstone Staff",
        "category": "Glintstone Staff"
      },
      "01FB0CB0": {
        "name": "Azur's Glintstone Staff",
        "category": "Glintstone Staff"
      },
      "01FB33C0": {
        "name": "Lusat's Glintstone Staff",
        "category": "Glintstone Staff"
      },
      "01FB5AD0": {
        "name": "Meteorite Staff",
        "category": "Glintstone Staff"
      },
      "01FB81E0": {
        "name": "Staff of the Guilty",
        "category": "Glintstone Staff"
      },
      "01FBA8F0": {
        "name": "Rotten Crystal Staff",
        "category": "Glintstone Staff"
      },
      "01FBD000": {
        "name": "Staff of Loss",
        "category": "Glintstone Staff"
      },
      "0206CC80": {
        "name": "Finger Seal",
        "category": "Sacred Seal"
      },
      "0206F390": {
        "name": "Godslayer's Seal",
        "category": "Sacred Seal"
      },
      "02071AA0": {
        "name": "Giant's Seal",
        "category": "Sacred Seal"
      },
      "020741B0": {
        "name": "Gravel Stone Seal",
        "category": "Sacred Seal"
      },
      "020768C0": {
        "name": "Clawmark Seal",
        "category": "Sacred Seal"
      },
      "0207B6E0": {
        "name": "Golden Order Seal",
        "category": "Sacred Seal"
      },
      "0207DDF0": {
        "name": "Erdtree Seal",
        "category": "Sacred Seal"
      },
      "02080500": {
        "name": "Dragon Communion Seal",
        "category": "Sacred Seal"
      },
      "02082C10": {
        "name": "Frenzied Flame Seal",
        "category": "Sacred Seal"
      },
      "02625A00": {
        "name": "Shortbow",
        "category": "Light Bow"
      },
      "02628110": {
        "name": "Misbegotten Shortbow",
        "category": "Light Bow"
      },
      "0262A820": {
        "name": "Red Branch Shortbow",
        "category": "Light Bow"
      },
      "0262CF30": {
        "name": "Harp Bow",
        "category": "Light Bow"
      },
      "02631D50": {
        "name": "Composite Bow",
        "category": "Light Bow"
      },
      "02719C40": {
        "name": "Longbow",
        "category": "Bow"
      },
      "0271C350": {
        "name": "Albinauric Bow",
        "category": "Bow"
      },
      "0271EA60": {
        "name": "Horn Bow",
        "category": "Bow"
      },
      "02721170": {
        "name": "Erdtree Bow",
        "category": "Bow"
      },
      "02723880": {
        "name": "Serpent Bow",
        "category": "Bow"
      },
      "027286A0": {
        "name": "Pulley Bow",
        "category": "Bow"
      },
      "0272ADB0": {
        "name": "Black Bow",
        "category": "Bow"
      },
      "0280DE80": {
        "name": "Lion Greatbow",
        "category": "Greatbow"
      },
      "02810590": {
        "name": "Golem Greatbow",
        "category": "Greatbow"
      },
      "028153B0": {
        "name": "Erdtree Greatbow",
        "category": "Greatbow"
      },
      "02817AC0": {
        "name": "Greatbow",
        "category": "Greatbow"
      },
      "029020C0": {
        "name": "Soldier's Crossbow",
        "category": "Crossbow"
      },
      "02906EE0": {
        "name": "Light Crossbow",
        "category": "Crossbow"
      },
      "029095F0": {
        "name": "Heavy Crossbow",
        "category": "Crossbow"
      },
      "0290E410": {
        "name": "Pulley Crossbow",
        "category": "Crossbow"
      },
      "02910B20": {
        "name": "Full Moon Crossbow",
        "category": "Crossbow"
      },
      "02915940": {
        "name": "Arbalest",
        "category": "Crossbow"
      },
      "0291CE70": {
        "name": "Crepus's Black-Key Crossbow",
        "category": "Crossbow"
      },
      "029F6300": {
        "name": "Hand Ballista",
        "category": "Ballista"
      },
      "029F8A10": {
        "name": "Jar Cannon",
        "category": "Ballista"
      }
    },
    "armor": {
      "100C5C10": {
        "name": "Commoner's Headband",
        "category": "Head"
      },
      "1005A550": {
        "name": "Aristocrat Headband",
        "category": "Head"
      },
      "1005CC60": {
        "name": "Aristocrat Hat",
        "category": "Head"
      },
      "1005F370": {
        "name": "Old Aristocrat Cowl",
        "category": "Head"
      },
      "10035B60": {
        "name": "Page Hood",
        "category": "Head"
      },
      "101E5D70": {
        "name": "High Page Hood",
        "category": "Head"
      },
      "10050910": {
        "name": "Guardian Mask",
        "category": "Head"
      },
      "100C3500": {
        "name": "Festive Hood",
        "category": "Head"
      },
      "100C3CD0": {
        "name": "Blue Festive Hood",
        "category": "Head"
      },
      "10027100": {
        "name": "Guilty Hood",
        "category": "Head"
      },
      "100D9490": {
        "name": "Prisoner Iron Mask",
        "category": "Head"
      },
      "100D9878": {
        "name": "Blackguard's Iron Mask",
        "category": "Head"
      },
      "100EB5A0": {
        "name": "Bloodsoaked Mask",
        "category": "Head"
      },
      "101ED2A0": {
        "name": "Black Dumpling",
        "category": "Head"
      },
      "10113E10": {
        "name": "Mushroom Head",
        "category": "Head"
      },
      "101EAB90": {
        "name": "Mushroom Crown",
        "category": "Head"
      },
      "10099CF0": {
        "name": "Astrologer Hood",
        "category": "Head"
      },
      "100FB770": {
        "name": "Juvenile Scholar Cap",
        "category": "Head"
      },
      "100CB5E8": {
        "name": "Karolos Glintstone Crown",
        "category": "Head"
      },
      "100CAE18": {
        "name": "Olivinus Glintstone Crown",
        "category": "Head"
      },
      "100CAA30": {
        "name": "Twinsage Glintstone Crown",
        "category": "Head"
      },
      "100CB9D0": {
        "name": "Witch's Glintstone Crown",
        "category": "Head"
      },
      "100CB200": {
        "name": "Lazuli Glintstone Crown",
        "category": "Head"
      },
      "100F4240": {
        "name": "Haima Glintstone Crown",
        "category": "Head"
      },
      "100F1B30": {
        "name": "Hierodas Glintstone Crown",
        "category": "Head"
      },
      "1001FBD0": {
        "name": "Spellblade's Pointed Hat",
        "category": "Head"
      },
      "1001D4C0": {
        "name": "Alberich's Pointed Hat",
        "category": "Head"
      },
      "100DE2B0": {
        "name": "Preceptor's Big Hat",
        "category": "Head"
      },
      "100DE698": {
        "name": "Mask of Confidence",
        "category": "Head"
      },
      "1008DD88": {
        "name": "Azur's Glintstone Crown",
        "category": "Head"
      },
      "1008D9A0": {
        "name": "Lusat's Glintstone Crown",
        "category": "Head"
      },
      "1007C830": {
        "name": "Queen's Crescent Crown",
        "category": "Head"
      },
      "100F6950": {
        "name": "Snow Witch Hat",
        "category": "Head"
      },
      "101D9A20": {
        "name": "Fia's Hood",
        "category": "Head"
      },
      "100975E0": {
        "name": "Prophet Blindfold",
        "category": "Head"
      },
      "100DBBA0": {
        "name": "Traveling Maiden Hood",
        "category": "Head"
      },
      "100DC370": {
        "name": "Finger Maiden Fillet",
        "category": "Head"
      },
      "10068FB0": {
        "name": "Sage Hood",
        "category": "Head"
      },
      "10186A00": {
        "name": "Greathood",
        "category": "Head"
      },
      "100FDE80": {
        "name": "Radiant Gold Mask",
        "category": "Head"
      },
      "10015F90": {
        "name": "Perfumer Hood",
        "category": "Head"
      },
      "100186A0": {
        "name": "Traveler's Hat",
        "category": "Head"
      },
      "10083D60": {
        "name": "Depraved Perfumer Headscarf",
        "category": "Head"
      },
      "100EA9E8": {
        "name": "Ruler's Mask",
        "category": "Head"
      },
      "100EA600": {
        "name": "Consort's Mask",
        "category": "Head"
      },
      "100EB1B8": {
        "name": "Marais Mask",
        "category": "Head"
      },
      "100493E0": {
        "name": "Great Horned Headband",
        "category": "Head"
      },
      "100497C8": {
        "name": "Shining Horned Headband",
        "category": "Head"
      },
      "1007EF40": {
        "name": "Godskin Apostle Hood",
        "category": "Head"
      },
      "10081650": {
        "name": "Godskin Noble Hood",
        "category": "Head"
      },
      "1004E200": {
        "name": "Sanguine Noble Hood",
        "category": "Head"
      },
      "101D24F0": {
        "name": "Crimson Tear Scarab",
        "category": "Head"
      },
      "101D4C00": {
        "name": "Cerulean Tear Scarab",
        "category": "Head"
      },
      "101CFDE0": {
        "name": "Ash-of-War Scarab",
        "category": "Head"
      },
      "101D05B0": {
        "name": "Glintstone Scarab",
        "category": "Head"
      },
      "101D01C8": {
        "name": "Incantation Scarab",
        "category": "Head"
      },
      "10107AC0": {
        "name": "Imp Head (Cat)",
        "category": "Head"
      },
      "10108A60": {
        "name": "Imp Head (Wolf)",
        "category": "Head"
      },
      "10107EA8": {
        "name": "Imp Head (Fanged)",
        "category": "Head"
      },
      "10108290": {
        "name": "Imp Head (Long-Tongued)",
        "category": "Head"
      },
      "10108678": {
        "name": "Imp Head (Corpse)",
        "category": "Head"
      },
      "10108E48": {
        "name": "Imp Head (Elder)",
        "category": "Head"
      },
      "1013D620": {
        "name": "Nox Mirrorhelm",
        "category": "Head"
      },
      "1013DA08": {
        "name": "Iji's Mirrorhelm",
        "category": "Head"
      },
      "1010A1D0": {
        "name": "Silver Tear Mask",
        "category": "Head"
      },
      "100C8320": {
        "name": "Envoy Crown",
        "category": "Head"
      },
      "1010EFF0": {
        "name": "Octopus Head",
        "category": "Head"
      },
      "10111700": {
        "name": "Jar",
        "category": "Head"
      },
      "10102CA0": {
        "name": "Albinauric Mask",
        "category": "Head"
      },
      "10029810": {
        "name": "Black Wolf Mask",
        "category": "Head"
      },
      "100A3930": {
        "name": "Blue Cloth Cowl",
        "category": "Head"
      },
      "100B4AA0": {
        "name": "Crimson Hood",
        "category": "Head"
      },
      "100B4E88": {
        "name": "Navy Hood",
        "category": "Head"
      },
      "100A6040": {
        "name": "White Mask",
        "category": "Head"
      },
      "1003D090": {
        "name": "Nomadic Merchant's Chapeau",
        "category": "Head"
      },
      "101560A8": {
        "name": "Bandit Mask",
        "category": "Head"
      },
      "10155CC0": {
        "name": "Black Hood",
        "category": "Head"
      },
      "100D6D80": {
        "name": "Confessor Hood",
        "category": "Head"
      },
      "101CD6D0": {
        "name": "Omensmirk Mask",
        "category": "Head"
      },
      "100E30D0": {
        "name": "Skeletal Mask",
        "category": "Head"
      },
      "101C61A0": {
        "name": "Foot Soldier Helm",
        "category": "Head"
      },
      "101C1380": {
        "name": "Foot Soldier Helmet",
        "category": "Head"
      },
      "101BEC70": {
        "name": "Foot Soldier Cap",
        "category": "Head"
      },
      "101C3A90": {
        "name": "Gilded Foot Soldier Cap",
        "category": "Head"
      },
      "101CAFC0": {
        "name": "Sacred Crown Helm",
        "category": "Head"
      },
      "101E3660": {
        "name": "Highwayman Hood",
        "category": "Head"
      },
      "100668A0": {
        "name": "Vulgar Militia Helm",
        "category": "Head"
      },
      "1004BAF0": {
        "name": "Duelist Helm",
        "category": "Head"
      },
      "101E8480": {
        "name": "Rotten Duelist Helm",
        "category": "Head"
      },
      "10046CD0": {
        "name": "Nox Monk Hood",
        "category": "Head"
      },
      "100474A0": {
        "name": "Nox Swordstress Crown",
        "category": "Head"
      },
      "10047888": {
        "name": "Night Maiden Twin Crown",
        "category": "Head"
      },
      "100B2390": {
        "name": "Champion Headband",
        "category": "Head"
      },
      "1010C8E0": {
        "name": "Chain Coif",
        "category": "Head"
      },
      "10009C40": {
        "name": "Iron Helmet",
        "category": "Head"
      },
      "1019F0A0": {
        "name": "Godrick Soldier Helm",
        "category": "Head"
      },
      "101A17B0": {
        "name": "Raya Lucarian Helm",
        "category": "Head"
      },
      "101A65D0": {
        "name": "Radahn Soldier Helm",
        "category": "Head"
      },
      "101A3EC0": {
        "name": "Leyndell Soldier Helm",
        "category": "Head"
      },
      "101AB3F0": {
        "name": "Haligtree Helm",
        "category": "Head"
      },
      "1002E630": {
        "name": "Exile Hood",
        "category": "Head"
      },
      "1000C350": {
        "name": "Kaiden Helm",
        "category": "Head"
      },
      "100D4670": {
        "name": "Land of Reeds Helm",
        "category": "Head"
      },
      "100D4E40": {
        "name": "Okina Mask",
        "category": "Head"
      },
      "100249F0": {
        "name": "Iron Kasa",
        "category": "Head"
      },
      "100E57E0": {
        "name": "Eccentric's Hood",
        "category": "Head"
      },
      "100CD140": {
        "name": "Marionette Soldier Helm",
        "category": "Head"
      },
      "100CF850": {
        "name": "Marionette Soldier Birdhelm",
        "category": "Head"
      },
      "1003A980": {
        "name": "Blue Silver Mail Hood",
        "category": "Head"
      },
      "10055730": {
        "name": "Fire Monk Hood",
        "category": "Head"
      },
      "10055B18": {
        "name": "Blackflame Monk Hood",
        "category": "Head"
      },
      "101053B0": {
        "name": "Zamor Mask",
        "category": "Head"
      },
      "1002BF20": {
        "name": "Black Knife Hood",
        "category": "Head"
      },
      "100BBFD0": {
        "name": "Malenia's Winged Helm",
        "category": "Head"
      },
      "100704E0": {
        "name": "Elden Lord Crown",
        "category": "Head"
      },
      "1016E360": {
        "name": "Knight Helm",
        "category": "Head"
      },
      "100A1220": {
        "name": "Vagabond Knight Helm",
        "category": "Head"
      },
      "1010CCC8": {
        "name": "Greathelm",
        "category": "Head"
      },
      "100EF420": {
        "name": "Carian Knight Helm",
        "category": "Head"
      },
      "101B0210": {
        "name": "Godrick Knight Helm",
        "category": "Head"
      },
      "101B2920": {
        "name": "Cuckoo Knight Helm",
        "category": "Head"
      },
      "101B7740": {
        "name": "Redmane Knight Helm",
        "category": "Head"
      },
      "101ADB00": {
        "name": "Gelmir Knight Helm",
        "category": "Head"
      },
      "101B5030": {
        "name": "Leyndell Knight Helm",
        "category": "Head"
      },
      "101BC560": {
        "name": "Haligtree Knight Helm",
        "category": "Head"
      },
      "100C0DF0": {
        "name": "Bloodhound Knight Helm",
        "category": "Head"
      },
      "10053020": {
        "name": "Cleanrot Helm",
        "category": "Head"
      },
      "100D1F60": {
        "name": "Raging Wolf Helm",
        "category": "Head"
      },
      "1009EB10": {
        "name": "Hoslow's Helm",
        "category": "Head"
      },
      "1009EEF8": {
        "name": "Diallos's Mask",
        "category": "Head"
      },
      "100927C0": {
        "name": "Twinned Helm",
        "category": "Head"
      },
      "1000EA60": {
        "name": "Drake Knight Helm",
        "category": "Head"
      },
      "10033450": {
        "name": "Briar Helm",
        "category": "Head"
      },
      "100E7EF0": {
        "name": "Fingerprint Helm",
        "category": "Head"
      },
      "100A8750": {
        "name": "Royal Remains Helm",
        "category": "Head"
      },
      "100900B0": {
        "name": "All-Knowing Helm",
        "category": "Head"
      },
      "100445C0": {
        "name": "Royal Knight Helm",
        "category": "Head"
      },
      "100B98C0": {
        "name": "Maliketh's Helm",
        "category": "Head"
      },
      "10030D40": {
        "name": "Banished Knight Helm",
        "category": "Head"
      },
      "10038270": {
        "name": "Night's Cavalry Helm",
        "category": "Head"
      },
      "100BE6E0": {
        "name": "Veteran's Helm",
        "category": "Head"
      },
      "10013880": {
        "name": "Scaled Helm",
        "category": "Head"
      },
      "100AFC80": {
        "name": "Beast Champion Helm",
        "category": "Head"
      },
      "10041EB0": {
        "name": "Tree Sentinel Helm",
        "category": "Head"
      },
      "1003F7A0": {
        "name": "Malformed Dragon Helm",
        "category": "Head"
      },
      "1008B290": {
        "name": "Crucible Axe Helm",
        "category": "Head"
      },
      "1008B678": {
        "name": "Crucible Tree Helm",
        "category": "Head"
      },
      "10072BF0": {
        "name": "Radahn's Redmane Helm",
        "category": "Head"
      },
      "1009C400": {
        "name": "Lionel's Helm",
        "category": "Head"
      },
      "100222E0": {
        "name": "Bull-Goat Helm",
        "category": "Head"
      },
      "100ECD10": {
        "name": "Omen Helm",
        "category": "Head"
      },
      "10057E40": {
        "name": "Fire Prelate Helm",
        "category": "Head"
      },
      "1006B6C0": {
        "name": "Pumpkin Helm",
        "category": "Head"
      },
      "10027164": {
        "name": "Cloth Garb",
        "category": "Body"
      },
      "100F90C4": {
        "name": "Traveler's Clothes",
        "category": "Body"
      },
      "100C63E0": {
        "name": "Commoner's Simple Garb",
        "category": "Body"
      },
      "100C5C74": {
        "name": "Commoner's Garb",
        "category": "Body"
      },
      "1005A5B4": {
        "name": "Aristocrat Garb",
        "category": "Body"
      },
      "1005CCC4": {
        "name": "Aristocrat Coat",
        "category": "Body"
      },
      "1005F3D4": {
        "name": "Old Aristocrat Gown",
        "category": "Body"
      },
      "10035BC4": {
        "name": "Page Garb",
        "category": "Body"
      },
      "101E5DD4": {
        "name": "High Page Clothes",
        "category": "Body"
      },
      "10050D5C": {
        "name": "Guardian Garb",
        "category": "Body"
      },
      "10050974": {
        "name": "Guardian Garb (Full Bloom)",
        "category": "Body"
      },
      "100C3564": {
        "name": "Festive Garb",
        "category": "Body"
      },
      "100C3D34": {
        "name": "Blue Festive Garb",
        "category": "Body"
      },
      "100D94F4": {
        "name": "Prisoner Clothing",
        "category": "Body"
      },
      "10113E74": {
        "name": "Mushroom Body",
        "category": "Body"
      },
      "10099D54": {
        "name": "Astrologer Robe",
        "category": "Body"
      },
      "100FB7D4": {
        "name": "Juvenile Scholar Robe",
        "category": "Body"
      },
      "100CAA94": {
        "name": "Raya Lucarian Robe",
        "category": "Body"
      },
      "101EF9B0": {
        "name": "Lazuli Robe",
        "category": "Body"
      },
      "100F42A4": {
        "name": "Battlemage Robe",
        "category": "Body"
      },
      "100F1B94": {
        "name": "Errant Sorcerer Robe",
        "category": "Body"
      },
      "1001FC34": {
        "name": "Spellblade's Traveling Attire",
        "category": "Body"
      },
      "1001D524": {
        "name": "Alberich's Robe",
        "category": "Body"
      },
      "100DE314": {
        "name": "Preceptor's Long Gown",
        "category": "Body"
      },
      "1008DDEC": {
        "name": "Azur's Glintstone Robe",
        "category": "Body"
      },
      "1008DA04": {
        "name": "Lusat's Robe",
        "category": "Body"
      },
      "1007C894": {
        "name": "Queen's Robe",
        "category": "Body"
      },
      "100F69B4": {
        "name": "Snow Witch Robe",
        "category": "Body"
      },
      "101D9A84": {
        "name": "Fia's Robe",
        "category": "Body"
      },
      "101D7374": {
        "name": "Deathbed Dress",
        "category": "Body"
      },
      "10097E14": {
        "name": "Prophet Robe",
        "category": "Body"
      },
      "10097644": {
        "name": "Corhyn's Robe",
        "category": "Body"
      },
      "100DBC04": {
        "name": "Traveling Maiden Robe",
        "category": "Body"
      },
      "100DC3D4": {
        "name": "Finger Maiden Robe",
        "category": "Body"
      },
      "10069014": {
        "name": "Sage Robe",
        "category": "Body"
      },
      "100FDEE4": {
        "name": "Goldmask's Rags",
        "category": "Body"
      },
      "10015FF4": {
        "name": "Perfumer Robe",
        "category": "Body"
      },
      "10018704": {
        "name": "Perfumer's Traveling Garb",
        "category": "Body"
      },
      "10083DC4": {
        "name": "Depraved Perfumer Robe",
        "category": "Body"
      },
      "100EAE34": {
        "name": "Upper-Class Robe",
        "category": "Body"
      },
      "100EAA4C": {
        "name": "Ruler's Robe",
        "category": "Body"
      },
      "100EA664": {
        "name": "Consort's Robe",
        "category": "Body"
      },
      "100EB604": {
        "name": "Official's Attire",
        "category": "Body"
      },
      "100EB21C": {
        "name": "Marais Robe",
        "category": "Body"
      },
      "10049444": {
        "name": "Fur Raiment",
        "category": "Body"
      },
      "1004982C": {
        "name": "Shaman Furs",
        "category": "Body"
      },
      "1007EFA4": {
        "name": "Godskin Apostle Robe",
        "category": "Body"
      },
      "100816B4": {
        "name": "Godskin Noble Robe",
        "category": "Body"
      },
      "101005F4": {
        "name": "Fell Omen Cloak",
        "category": "Body"
      },
      "1004E264": {
        "name": "Sanguine Noble Robe",
        "category": "Body"
      },
      "10075364": {
        "name": "Lord of Blood's Robe",
        "category": "Body"
      },
      "10155D24": {
        "name": "Leather Armor",
        "category": "Body"
      },
      "100A3994": {
        "name": "Blue Cloth Vest",
        "category": "Body"
      },
      "100B4B04": {
        "name": "Noble's Traveling Garb",
        "category": "Body"
      },
      "100A60A4": {
        "name": "War Surgeon Gown",
        "category": "Body"
      },
      "1003D0F4": {
        "name": "Nomadic Merchant's Finery",
        "category": "Body"
      },
      "100E351C": {
        "name": "Bandit Garb",
        "category": "Body"
      },
      "100D6DE4": {
        "name": "Confessor Armor",
        "category": "Body"
      },
      "101CD734": {
        "name": "Omenkiller Robe",
        "category": "Body"
      },
      "100E3134": {
        "name": "Raptor's Black Feathers",
        "category": "Body"
      },
      "101C13E4": {
        "name": "Foot Soldier Tabard",
        "category": "Body"
      },
      "101C3AF4": {
        "name": "Leather-Draped Tabard",
        "category": "Body"
      },
      "101BECD4": {
        "name": "Chain-Draped Tabard",
        "category": "Body"
      },
      "101CB024": {
        "name": "Ivory-Draped Tabard",
        "category": "Body"
      },
      "101C6204": {
        "name": "Scarlet Tabard",
        "category": "Body"
      },
      "101C8914": {
        "name": "Bloodsoaked Tabard",
        "category": "Body"
      },
      "101E36C4": {
        "name": "Highwayman Cloth Armor",
        "category": "Body"
      },
      "10066904": {
        "name": "Vulgar Militia Armor",
        "category": "Body"
      },
      "1004BB54": {
        "name": "Gravekeeper Cloak",
        "category": "Body"
      },
      "101E84E4": {
        "name": "Rotten Gravekeeper Cloak",
        "category": "Body"
      },
      "10046D34": {
        "name": "Nox Monk Armor",
        "category": "Body"
      },
      "10047504": {
        "name": "Nox Swordstress Armor",
        "category": "Body"
      },
      "100478EC": {
        "name": "Night Maiden Armor",
        "category": "Body"
      },
      "100B23F4": {
        "name": "Champion Pauldron",
        "category": "Body"
      },
      "1010C944": {
        "name": "Chain Armor",
        "category": "Body"
      },
      "10102D04": {
        "name": "Dirty Chainmail",
        "category": "Body"
      },
      "1010D114": {
        "name": "Tree Surcoat",
        "category": "Body"
      },
      "1010CD2C": {
        "name": "Eye Surcoat",
        "category": "Body"
      },
      "1019F104": {
        "name": "Tree-and-Beast Surcoat",
        "category": "Body"
      },
      "101A1814": {
        "name": "Cuckoo Surcoat",
        "category": "Body"
      },
      "101A6634": {
        "name": "Redmane Surcoat",
        "category": "Body"
      },
      "101A3F24": {
        "name": "Erdtree Surcoat",
        "category": "Body"
      },
      "101AB454": {
        "name": "Haligtree Crest Surcoat",
        "category": "Body"
      },
      "101A8D44": {
        "name": "Mausoleum Surcoat",
        "category": "Body"
      },
      "10009CA4": {
        "name": "Scale Armor",
        "category": "Body"
      },
      "1002E694": {
        "name": "Exile Armor",
        "category": "Body"
      },
      "1000C3B4": {
        "name": "Kaiden Armor",
        "category": "Body"
      },
      "100D46D4": {
        "name": "Land of Reeds Armor",
        "category": "Body"
      },
      "100D4EA4": {
        "name": "White Reed Armor",
        "category": "Body"
      },
      "10024A54": {
        "name": "Ronin's Armor",
        "category": "Body"
      },
      "100E5844": {
        "name": "Eccentric's Armor",
        "category": "Body"
      },
      "100CD1A4": {
        "name": "Marionette Soldier Armor",
        "category": "Body"
      },
      "1003A9E4": {
        "name": "Blue Silver Mail Armor",
        "category": "Body"
      },
      "10055794": {
        "name": "Fire Monk Armor",
        "category": "Body"
      },
      "10055B7C": {
        "name": "Blackflame Monk Armor",
        "category": "Body"
      },
      "10105414": {
        "name": "Zamor Armor",
        "category": "Body"
      },
      "1002BF84": {
        "name": "Black Knife Armor",
        "category": "Body"
      },
      "100BC034": {
        "name": "Malenia's Armor",
        "category": "Body"
      },
      "10070544": {
        "name": "Elden Lord Armor",
        "category": "Body"
      },
      "1016E3C4": {
        "name": "Knight Armor",
        "category": "Body"
      },
      "100A1284": {
        "name": "Vagabond Knight Armor",
        "category": "Body"
      },
      "100EF484": {
        "name": "Carian Knight Armor",
        "category": "Body"
      },
      "101B0274": {
        "name": "Godrick Knight Armor",
        "category": "Body"
      },
      "101B2984": {
        "name": "Cuckoo Knight Armor",
        "category": "Body"
      },
      "101B77A4": {
        "name": "Redmane Knight Armor",
        "category": "Body"
      },
      "101ADB64": {
        "name": "Gelmir Knight Armor",
        "category": "Body"
      },
      "101B5094": {
        "name": "Leyndell Knight Armor",
        "category": "Body"
      },
      "101BC5C4": {
        "name": "Haligtree Knight Armor",
        "category": "Body"
      },
      "101B9EB4": {
        "name": "Mausoleum Knight Armor",
        "category": "Body"
      },
      "100C0E54": {
        "name": "Bloodhound Knight Armor",
        "category": "Body"
      },
      "10053084": {
        "name": "Cleanrot Armor",
        "category": "Body"
      },
      "100D1FC4": {
        "name": "Raging Wolf Armor",
        "category": "Body"
      },
      "1009EB74": {
        "name": "Hoslow's Armor",
        "category": "Body"
      },
      "10092824": {
        "name": "Twinned Armor",
        "category": "Body"
      },
      "1000EAC4": {
        "name": "Drake Knight Armor",
        "category": "Body"
      },
      "10029874": {
        "name": "Blaidd's Armor",
        "category": "Body"
      },
      "100334B4": {
        "name": "Briar Armor",
        "category": "Body"
      },
      "100E7F54": {
        "name": "Fingerprint Armor",
        "category": "Body"
      },
      "100A87B4": {
        "name": "Royal Remains Armor",
        "category": "Body"
      },
      "10090114": {
        "name": "All-Knowing Armor",
        "category": "Body"
      },
      "10044624": {
        "name": "Royal Knight Armor",
        "category": "Body"
      },
      "100B9924": {
        "name": "Maliketh's Armor",
        "category": "Body"
      },
      "10030DA4": {
        "name": "Banished Knight Armor",
        "category": "Body"
      },
      "100382D4": {
        "name": "Night's Cavalry Armor",
        "category": "Body"
      },
      "100BE744": {
        "name": "Veteran's Armor",
        "category": "Body"
      },
      "100138E4": {
        "name": "Scaled Armor",
        "category": "Body"
      },
      "100AFCE4": {
        "name": "Beast Champion Armor",
        "category": "Body"
      },
      "10041F14": {
        "name": "Tree Sentinel Armor",
        "category": "Body"
      },
      "1003F804": {
        "name": "Malformed Dragon Armor",
        "category": "Body"
      },
      "1008B2F4": {
        "name": "Crucible Axe Armor",
        "category": "Body"
      },
      "1008B6DC": {
        "name": "Crucible Tree Armor",
        "category": "Body"
      },
      "10072C54": {
        "name": "Radahn's Lion Armor",
        "category": "Body"
      },
      "1009C464": {
        "name": "Lionel's Armor",
        "category": "Body"
      },
      "10022344": {
        "name": "Bull-Goat Armor",
        "category": "Body"
      },
      "100ECD74": {
        "name": "Omen Armor",
        "category": "Body"
      },
      "10057EA4": {
        "name": "Fire Prelate Armor",
        "category": "Body"
      },
      "100F9128": {
        "name": "Traveler's Manchettes",
        "category": "Arms"
      },
      "100509D8": {
        "name": "Guardian Bracers",
        "category": "Arms"
      },
      "100EB280": {
        "name": "Bloodsoaked Manchettes",
        "category": "Arms"
      },
      "10113ED8": {
        "name": "Mushroom Arms",
        "category": "Arms"
      },
      "10099DB8": {
        "name": "Astrologer Gloves",
        "category": "Arms"
      },
      "100CAAF8": {
        "name": "Sorcerer Manchettes",
        "category": "Arms"
      },
      "100F4308": {
        "name": "Battlemage Manchettes",
        "category": "Arms"
      },
      "100F1BF8": {
        "name": "Errant Sorcerer Manchettes",
        "category": "Arms"
      },
      "1001FC98": {
        "name": "Spellblade's Gloves",
        "category": "Arms"
      },
      "1001D588": {
        "name": "Alberich's Bracers",
        "category": "Arms"
      },
      "100DE378": {
        "name": "Preceptor's Gloves",
        "category": "Arms"
      },
      "1008DE50": {
        "name": "Azur's Manchettes",
        "category": "Arms"
      },
      "1008DA68": {
        "name": "Lusat's Manchettes",
        "category": "Arms"
      },
      "1007C8F8": {
        "name": "Queen's Bracelets",
        "category": "Arms"
      },
      "100DBC68": {
        "name": "Traveling Maiden Gloves",
        "category": "Arms"
      },
      "100FDF48": {
        "name": "Gold Bracelets",
        "category": "Arms"
      },
      "10016058": {
        "name": "Perfumer Gloves",
        "category": "Arms"
      },
      "10018768": {
        "name": "Traveler's Gloves",
        "category": "Arms"
      },
      "10083E28": {
        "name": "Depraved Perfumer Gloves",
        "category": "Arms"
      },
      "1007F008": {
        "name": "Godskin Apostle Bracelets",
        "category": "Arms"
      },
      "10081718": {
        "name": "Godskin Noble Bracelets",
        "category": "Arms"
      },
      "10155D88": {
        "name": "Leather Gloves",
        "category": "Arms"
      },
      "100A39F8": {
        "name": "Warrior Gauntlets",
        "category": "Arms"
      },
      "100B4B68": {
        "name": "Noble's Gloves",
        "category": "Arms"
      },
      "100A6108": {
        "name": "War Surgeon Gloves",
        "category": "Arms"
      },
      "100E3198": {
        "name": "Bandit Manchettes",
        "category": "Arms"
      },
      "100D6E48": {
        "name": "Confessor Gloves",
        "category": "Arms"
      },
      "101CD798": {
        "name": "Omenkiller Long Gloves",
        "category": "Arms"
      },
      "101BED38": {
        "name": "Foot Soldier Gauntlets",
        "category": "Arms"
      },
      "101E3728": {
        "name": "Highwayman Gauntlets",
        "category": "Arms"
      },
      "10066968": {
        "name": "Vulgar Militia Gauntlets",
        "category": "Arms"
      },
      "10046D98": {
        "name": "Nox Bracelets",
        "category": "Arms"
      },
      "100B2458": {
        "name": "Champion Bracers",
        "category": "Arms"
      },
      "1010C9A8": {
        "name": "Gauntlets",
        "category": "Arms"
      },
      "10009D08": {
        "name": "Iron Gauntlets",
        "category": "Arms"
      },
      "1019F168": {
        "name": "Godrick Soldier Gauntlets",
        "category": "Arms"
      },
      "101A1878": {
        "name": "Raya Lucarian Gauntlets",
        "category": "Arms"
      },
      "101A6698": {
        "name": "Radahn Soldier Gauntlets",
        "category": "Arms"
      },
      "101A3F88": {
        "name": "Leyndell Soldier Gauntlets",
        "category": "Arms"
      },
      "101AB4B8": {
        "name": "Haligtree Gauntlets",
        "category": "Arms"
      },
      "101A8DA8": {
        "name": "Mausoleum Gauntlets",
        "category": "Arms"
      },
      "1002E6F8": {
        "name": "Exile Gauntlets",
        "category": "Arms"
      },
      "1000C418": {
        "name": "Kaiden Gauntlets",
        "category": "Arms"
      },
      "100D4738": {
        "name": "Land of Reeds Gauntlets",
        "category": "Arms"
      },
      "100D4F08": {
        "name": "White Reed Gauntlets",
        "category": "Arms"
      },
      "10024AB8": {
        "name": "Ronin's Gauntlets",
        "category": "Arms"
      },
      "100E58A8": {
        "name": "Eccentric's Manchettes",
        "category": "Arms"
      },
      "1003AA48": {
        "name": "Blue Silver Bracelets",
        "category": "Arms"
      },
      "100557F8": {
        "name": "Fire Monk Gauntlets",
        "category": "Arms"
      },
      "10055BE0": {
        "name": "Blackflame Monk Gauntlets",
        "category": "Arms"
      },
      "10105478": {
        "name": "Zamor Bracelets",
        "category": "Arms"
      },
      "1002BFE8": {
        "name": "Black Knife Gauntlets",
        "category": "Arms"
      },
      "100BC098": {
        "name": "Malenia's Gauntlet",
        "category": "Arms"
      },
      "100705A8": {
        "name": "Elden Lord Bracers",
        "category": "Arms"
      },
      "1016E428": {
        "name": "Knight Gauntlets",
        "category": "Arms"
      },
      "100A12E8": {
        "name": "Vagabond Knight Gauntlets",
        "category": "Arms"
      },
      "100EF4E8": {
        "name": "Carian Knight Gauntlets",
        "category": "Arms"
      },
      "101B02D8": {
        "name": "Godrick Knight Gauntlets",
        "category": "Arms"
      },
      "101B29E8": {
        "name": "Cuckoo Knight Gauntlets",
        "category": "Arms"
      },
      "101B7808": {
        "name": "Redmane Knight Gauntlets",
        "category": "Arms"
      },
      "101ADBC8": {
        "name": "Gelmir Knight Gauntlets",
        "category": "Arms"
      },
      "101B50F8": {
        "name": "Leyndell Knight Gauntlets",
        "category": "Arms"
      },
      "101BC628": {
        "name": "Haligtree Knight Gauntlets",
        "category": "Arms"
      },
      "101B9F18": {
        "name": "Mausoleum Knight Gauntlets",
        "category": "Arms"
      },
      "100C0EB8": {
        "name": "Bloodhound Knight Gauntlets",
        "category": "Arms"
      },
      "100530E8": {
        "name": "Cleanrot Gauntlets",
        "category": "Arms"
      },
      "100D2028": {
        "name": "Raging Wolf Gauntlets",
        "category": "Arms"
      },
      "1009EBD8": {
        "name": "Hoslow's Gauntlets",
        "category": "Arms"
      },
      "10092888": {
        "name": "Twinned Gauntlets",
        "category": "Arms"
      },
      "1000EB28": {
        "name": "Drake Knight Gauntlets",
        "category": "Arms"
      },
      "100298D8": {
        "name": "Blaidd's Gauntlets",
        "category": "Arms"
      },
      "10033518": {
        "name": "Briar Gauntlets",
        "category": "Arms"
      },
      "100E7FB8": {
        "name": "Fingerprint Gauntlets",
        "category": "Arms"
      },
      "100A8818": {
        "name": "Royal Remains Gauntlets",
        "category": "Arms"
      },
      "10090178": {
        "name": "All-Knowing Gauntlets",
        "category": "Arms"
      },
      "10044688": {
        "name": "Royal Knight Gauntlets",
        "category": "Arms"
      },
      "100B9988": {
        "name": "Maliketh's Gauntlets",
        "category": "Arms"
      },
      "10030E08": {
        "name": "Banished Knight Gauntlets",
        "category": "Arms"
      },
      "10038338": {
        "name": "Night's Cavalry Gauntlets",
        "category": "Arms"
      },
      "100BE7A8": {
        "name": "Veteran's Gauntlets",
        "category": "Arms"
      },
      "10013948": {
        "name": "Scaled Gauntlets",
        "category": "Arms"
      },
      "100AFD48": {
        "name": "Beast Champion Gauntlets",
        "category": "Arms"
      },
      "10041F78": {
        "name": "Tree Sentinel Gauntlets",
        "category": "Arms"
      },
      "1003F868": {
        "name": "Malformed Dragon Gauntlets",
        "category": "Arms"
      },
      "1008B358": {
        "name": "Crucible Gauntlets",
        "category": "Arms"
      },
      "10072CB8": {
        "name": "Radahn's Gauntlets",
        "category": "Arms"
      },
      "1009C4C8": {
        "name": "Lionel's Gauntlets",
        "category": "Arms"
      },
      "100223A8": {
        "name": "Bull-Goat Gauntlets",
        "category": "Arms"
      },
      "100ECDD8": {
        "name": "Omen Gauntlets",
        "category": "Arms"
      },
      "10057F08": {
        "name": "Fire Prelate Gauntlets",
        "category": "Arms"
      },
      "1002722C": {
        "name": "Cloth Trousers",
        "category": "Legs"
      },
      "100F918C": {
        "name": "Traveler's Boots",
        "category": "Legs"
      },
      "100C5D3C": {
        "name": "Commoner's Shoes",
        "category": "Legs"
      },
      "1005A67C": {
        "name": "Aristocrat Boots",
        "category": "Legs"
      },
      "1005F49C": {
        "name": "Old Aristocrat Shoes",
        "category": "Legs"
      },
      "10035C8C": {
        "name": "Page Trousers",
        "category": "Legs"
      },
      "10050A3C": {
        "name": "Guardian Greaves",
        "category": "Legs"
      },
      "100D95BC": {
        "name": "Prisoner Trousers",
        "category": "Legs"
      },
      "10113F3C": {
        "name": "Mushroom Legs",
        "category": "Legs"
      },
      "10099E1C": {
        "name": "Astrologer Trousers",
        "category": "Legs"
      },
      "100CAB5C": {
        "name": "Sorcerer Leggings",
        "category": "Legs"
      },
      "100F436C": {
        "name": "Battlemage Legwraps",
        "category": "Legs"
      },
      "100F1C5C": {
        "name": "Errant Sorcerer Boots",
        "category": "Legs"
      },
      "1001FCFC": {
        "name": "Spellblade's Trousers",
        "category": "Legs"
      },
      "1001D5EC": {
        "name": "Alberich's Trousers",
        "category": "Legs"
      },
      "100DE3DC": {
        "name": "Preceptor's Trousers",
        "category": "Legs"
      },
      "1008DACC": {
        "name": "Old Sorcerer's Legwraps",
        "category": "Legs"
      },
      "1007C95C": {
        "name": "Queen's Leggings",
        "category": "Legs"
      },
      "100F6A7C": {
        "name": "Snow Witch Skirt",
        "category": "Legs"
      },
      "1009770C": {
        "name": "Prophet Trousers",
        "category": "Legs"
      },
      "100DBCCC": {
        "name": "Traveling Maiden Boots",
        "category": "Legs"
      },
      "100DC49C": {
        "name": "Finger Maiden Shoes",
        "category": "Legs"
      },
      "100690DC": {
        "name": "Sage Trousers",
        "category": "Legs"
      },
      "100FDFAC": {
        "name": "Gold Waistwrap",
        "category": "Legs"
      },
      "100160BC": {
        "name": "Perfumer Sarong",
        "category": "Legs"
      },
      "100187CC": {
        "name": "Traveler's Slops",
        "category": "Legs"
      },
      "10083E8C": {
        "name": "Depraved Perfumer Trousers",
        "category": "Legs"
      },
      "100EA72C": {
        "name": "Consort's Trousers",
        "category": "Legs"
      },
      "1004950C": {
        "name": "Fur Leggings",
        "category": "Legs"
      },
      "100498F4": {
        "name": "Shaman Leggings",
        "category": "Legs"
      },
      "1007F06C": {
        "name": "Godskin Apostle Trousers",
        "category": "Legs"
      },
      "1008177C": {
        "name": "Godskin Noble Trousers",
        "category": "Legs"
      },
      "1004E32C": {
        "name": "Sanguine Noble Waistcloth",
        "category": "Legs"
      },
      "10009D6C": {
        "name": "Leather Trousers",
        "category": "Legs"
      },
      "10155DEC": {
        "name": "Leather Boots",
        "category": "Legs"
      },
      "100A3A5C": {
        "name": "Warrior Greaves",
        "category": "Legs"
      },
      "100B4BCC": {
        "name": "Noble's Trousers",
        "category": "Legs"
      },
      "100A616C": {
        "name": "War Surgeon Trousers",
        "category": "Legs"
      },
      "1003D1BC": {
        "name": "Nomadic Merchant's Trousers",
        "category": "Legs"
      },
      "100E31FC": {
        "name": "Bandit Boots",
        "category": "Legs"
      },
      "100D6EAC": {
        "name": "Confessor Boots",
        "category": "Legs"
      },
      "101CD7FC": {
        "name": "Omenkiller Boots",
        "category": "Legs"
      },
      "101BED9C": {
        "name": "Foot Soldier Greaves",
        "category": "Legs"
      },
      "100669CC": {
        "name": "Vulgar Militia Greaves",
        "category": "Legs"
      },
      "1004BC1C": {
        "name": "Duelist Greaves",
        "category": "Legs"
      },
      "101E85AC": {
        "name": "Rotten Duelist Greaves",
        "category": "Legs"
      },
      "10046DFC": {
        "name": "Nox Greaves",
        "category": "Legs"
      },
      "100B24BC": {
        "name": "Champion Gaiters",
        "category": "Legs"
      },
      "1010CA0C": {
        "name": "Chain Leggings",
        "category": "Legs"
      },
      "1019F1CC": {
        "name": "Godrick Soldier Greaves",
        "category": "Legs"
      },
      "101A18DC": {
        "name": "Raya Lucarian Greaves",
        "category": "Legs"
      },
      "101A66FC": {
        "name": "Radahn Soldier Greaves",
        "category": "Legs"
      },
      "101A3FEC": {
        "name": "Leyndell Soldier Greaves",
        "category": "Legs"
      },
      "101AB51C": {
        "name": "Haligtree Greaves",
        "category": "Legs"
      },
      "101A8E0C": {
        "name": "Mausoleum Greaves",
        "category": "Legs"
      },
      "1002E75C": {
        "name": "Exile Greaves",
        "category": "Legs"
      },
      "1000C47C": {
        "name": "Kaiden Trousers",
        "category": "Legs"
      },
      "100D479C": {
        "name": "Land of Reeds Greaves",
        "category": "Legs"
      },
      "100D4F6C": {
        "name": "White Reed Greaves",
        "category": "Legs"
      },
      "10024B1C": {
        "name": "Ronin's Greaves",
        "category": "Legs"
      },
      "100E590C": {
        "name": "Eccentric's Breeches",
        "category": "Legs"
      },
      "1003AAAC": {
        "name": "Blue Silver Mail Skirt",
        "category": "Legs"
      },
      "1005585C": {
        "name": "Fire Monk Greaves",
        "category": "Legs"
      },
      "10055C44": {
        "name": "Blackflame Monk Greaves",
        "category": "Legs"
      },
      "101054DC": {
        "name": "Zamor Legwraps",
        "category": "Legs"
      },
      "1002C04C": {
        "name": "Black Knife Greaves",
        "category": "Legs"
      },
      "100BC0FC": {
        "name": "Malenia's Greaves",
        "category": "Legs"
      },
      "1007060C": {
        "name": "Elden Lord Greaves",
        "category": "Legs"
      },
      "1016E48C": {
        "name": "Knight Greaves",
        "category": "Legs"
      },
      "100A134C": {
        "name": "Vagabond Knight Greaves",
        "category": "Legs"
      },
      "100EF54C": {
        "name": "Carian Knight Greaves",
        "category": "Legs"
      },
      "101B033C": {
        "name": "Godrick Knight Greaves",
        "category": "Legs"
      },
      "101B2A4C": {
        "name": "Cuckoo Knight Greaves",
        "category": "Legs"
      },
      "101B786C": {
        "name": "Redmane Knight Greaves",
        "category": "Legs"
      },
      "101ADC2C": {
        "name": "Gelmir Knight Greaves",
        "category": "Legs"
      },
      "101B515C": {
        "name": "Leyndell Knight Greaves",
        "category": "Legs"
      },
      "101BC68C": {
        "name": "Haligtree Knight Greaves",
        "category": "Legs"
      },
      "101B9F7C": {
        "name": "Mausoleum Knight Greaves",
        "category": "Legs"
      },
      "100C0F1C": {
        "name": "Bloodhound Knight Greaves",
        "category": "Legs"
      },
      "1005314C": {
        "name": "Cleanrot Greaves",
        "category": "Legs"
      },
      "100D208C": {
        "name": "Raging Wolf Greaves",
        "category": "Legs"
      },
      "1009EC3C": {
        "name": "Hoslow's Greaves",
        "category": "Legs"
      },
      "100928EC": {
        "name": "Twinned Greaves",
        "category": "Legs"
      },
      "1000EB8C": {
        "name": "Drake Knight Greaves",
        "category": "Legs"
      },
      "1002993C": {
        "name": "Blaidd's Greaves",
        "category": "Legs"
      },
      "1003357C": {
        "name": "Briar Greaves",
        "category": "Legs"
      },
      "100E801C": {
        "name": "Fingerprint Greaves",
        "category": "Legs"
      },
      "100A887C": {
        "name": "Royal Remains Greaves",
        "category": "Legs"
      },
      "100901DC": {
        "name": "All-Knowing Greaves",
        "category": "Legs"
      },
      "100446EC": {
        "name": "Royal Knight Greaves",
        "category": "Legs"
      },
      "100B99EC": {
        "name": "Maliketh's Greaves",
        "category": "Legs"
      },
      "10030E6C": {
        "name": "Banished Knight Greaves",
        "category": "Legs"
      },
      "1003839C": {
        "name": "Night's Cavalry Greaves",
        "category": "Legs"
      },
      "100BE80C": {
        "name": "Veteran's Greaves",
        "category": "Legs"
      },
      "100139AC": {
        "name": "Scaled Greaves",
        "category": "Legs"
      },
      "100AFDAC": {
        "name": "Beast Champion Greaves",
        "category": "Legs"
      },
      "10041FDC": {
        "name": "Tree Sentinel Greaves",
        "category": "Legs"
      },
      "1003F8CC": {
        "name": "Malformed Dragon Greaves",
        "category": "Legs"
      },
      "1008B3BC": {
        "name": "Crucible Greaves",
        "category": "Legs"
      },
      "10072D1C": {
        "name": "Radahn's Greaves",
        "category": "Legs"
      },
      "1009C52C": {
        "name": "Lionel's Greaves",
        "category": "Legs"
      },
      "1002240C": {
        "name": "Bull-Goat Greaves",
        "category": "Legs"
      },
      "100ECE3C": {
        "name": "Omen Greaves",
        "category": "Legs"
      },
      "10057F6C": {
        "name": "Fire Prelate Greaves",
        "category": "Legs"
      }
    },
}