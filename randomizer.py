# This is a randomizer file for the Simple Randomizer Maker.
# This file must be named randomizer.py in order to work.
# For more information on what each variable means, see "Readme (Tutorial).md"

from classes import *

def value(name):
	for att in Attributes:
		if att.name == name:
			return att
	print("This attribute does not exist: "+name)
	return None

########################
# EDIT BELOW THIS LINE #
########################

Program_Name = "Wonder Boy in Monster World (WBV or MWIII) - Randomizer"
Rom_Name = "Wonder Boy in Monster World (USA, Europe)"
Rom_File_Format = "" # File format (nes, gba, etc.)
Rom_Hash = None
About_Page_Text = "Wonderful Monster Boy."
Timeout = 5000
Slow_Mode = False

Attributes = [
        ###Quality of Life Stuff####
        Attribute(
                name="Openning_Text",
                addresses=[0x1df29],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0]
                ),
        Attribute(
                name="Sonia_Text",
                addresses=[0x1e731],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0]
                ),
        Attribute(
                name="bat_spawn",
                addresses=[0x2ca05],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0]
                ),
        ###Sprites####
        Attribute(
                name="Leather_Boots_Sprite",
                addresses=[0x22b08],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),
        Attribute(
                name="Medecine_Sprite",
                addresses=[0x22b62],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),
        Attribute(
                name="Small_Spear_Sprite",
                addresses=[0x22b36],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),
        Attribute(
                name="Chailmail_Sprite",
                addresses=[0x22b3c],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),
        Attribute(
                name="Wood_Shield",
                addresses=[0x22b42],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),
        Attribute(
                name="Excalibur_Sprite",
                addresses=[0x22b8a],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),
        Attribute(
                name="SteelShield_Sprite",
                addresses=[0x22b84],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),
        Attribute(
                name="Knight_Sword_Sprite",
                addresses=[0x22B94],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),
        Attribute(
                name="Hard_Armor_Sprite",
                addresses=[0x22B9A],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),
        Attribute(
                name="Potion_Sprite_Pura",
                addresses=[0x22BDC],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),        
        Attribute(
                name="Charm_sprite",
                addresses=[0x22BE2],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),
        Attribute(
                name="Ladder_Sprite",
                addresses=[0x22BD6],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),
        Attribute(
                name="Marine_Sprite",
                addresses=[0x22C62],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),
        Attribute(
                name="Potion_Sprite_Pad",
                addresses=[0x22C6E],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),  
        Attribute(
                name="Steel_Armor_Sprite",
                addresses=[0x22C4E],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),
        Attribute(
                name="Shell_Shield_Sprite",
                addresses=[0x22C48],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),
        Attribute(
                name="Battle_Spear_Sprite",
                addresses=[0x22d08],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),
        Attribute(
                name="Knight_Armor_Sprite",
                addresses=[0x22d0e],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),
        Attribute(
                name="Ceramic_Boots_Sprite",
                addresses=[0x22CF4],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),
        Attribute(
                name="Knight_Shield_Sprite",
                addresses=[0x22D14],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),
        Attribute(
                name="HolyWater_Sprite",
                addresses=[0x22CEE],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),
        Attribute(
                name="Flame_Shield_Sprite",
                addresses=[0x22C92],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),
        Attribute(
                name="Flame_Armor_Sprite",
                addresses=[0x22C8C],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),
        Attribute(
                name="HiPotion_Sprite",
                addresses=[0x22CAC],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),
        Attribute(
                name="Elixer_Sprite",
                addresses=[0x22CA6],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]
                ),
        ###Starter Stuff###
        Attribute(
                name="elder_elixer",
                addresses=[0x1e07f],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32,33,34,36,37,42]                                 
                ),
        Attribute(
                name="elder_firestorm",
                addresses=[0x1e08b],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32,33,34,36,37,42]
                ),
        ### Don't Randomize these. Placeholders for later ###
        # Attribute(
        #        name="Heart_Chests",
        #        addresses=[0xa722],
        #        number_of_bytes=1,
        #        is_little_endian=False,
        #        possible_values=[192]
        #        ),
        #Attribute(
        #        name="Bracelet_Check",
        #        addresses=[0x1F237],
        #        number_of_bytes=1,
        #        is_little_endian=False,
        #        possible_values=[0]
        #        ),
        #Attribute(
        #        name="Bracelet",
        #        addresses=[0x1F23C],
        #        number_of_bytes=1,
        #        is_little_endian=False,
        #        possible_values=[133,    177,186,
        #                         178,            182,183,
        #                         135,143,151,159,
        #                         184,185]
        #        ),
        
        ###Shops###
        Attribute(
                name="leather_boots",
                addresses=[0x1e239],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[43,29,22,28,44] 
                ),
        Attribute(
                name="medicine",
                addresses=[0x1e292],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[43,29,22,28,44,
                                 13,6,20] 
                ),
        Attribute(
                name="small_spear",
                addresses=[0x1e1c1],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[43,29,22,28,44,
                                 13,6,20] 
                ),
        Attribute(
                name="chain_mail",
                addresses=[0x1e1e5],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[43,29,22,28,44,
                                 13,6,20] 
                ),
        Attribute(
                name="wood_shield",
                addresses=[0x1e215],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[43,29,22,28,44,
                                 13,6,20] 
                ),        
       Attribute(
                name="Knight_Sword",
                addresses=[0x1e1b5],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[13,6,20,
                                 21,45,12,2,27] 
                ),
        Attribute(
                name="Hard_Armor",
                addresses=[0x1e1df],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[13,6,20,
                                 21,45,12,2,27] 
                ),
        Attribute(
                name="Charmstone_Purchase",
                addresses=[0x1e28c],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[13,6,20,
                                 21,45,12,2,27] 
                ),
        Attribute(
                name="Potion",
                addresses=[0x1e298],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[13,6,20,
                                 21,45,12,2,27] 
                ),
        Attribute(
                name="Ladder_Boots",
                addresses=[0x1e233],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[13,6,20,
                                 21,45,12,2,27] 
                ),
        Attribute(
                name="Marine_Boots",
                addresses=[0x1e22d],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[21,45,12,2,27,
                                 32,33,34,35,36,37,11] 
                ),
        Attribute(
                name="Shield_Magic_Shop",
                addresses=[0x1e251],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[21,45,12,2,27,
                                 32,33,34,35,36,37,11] 
                ),
        Attribute(
                name="Shell_Shield",
                addresses=[0x1e20f],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[21,45,12,2,27,
                                 32,33,34,35,36,37,11] 
                ),
        Attribute(
                name="Steel_Armor",
                addresses=[0x1e1d9],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[21,45,12,2,27,
                                 32,33,34,35,36,37,11] 
                ),
        Attribute(
                name="excalibur",
                addresses=[0x1e1af],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32,33,34,35,36,37,11,
                                 19,1,42] 
                ),
        Attribute(
                name="steel_shield",
                addresses=[0x1e203],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32,33,34,35,36,37,11,
                                 19,1,42] 
                ),       
        Attribute(
                name="Ceramic_Boots",
                addresses=[0x1e221],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[19,1,42,
                                 18,25,10,46,17,4,9] 
                ),
        Attribute(
                name="Battle_Spear",
                addresses=[0x1e1bb],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[19,1,42,
                                 18,25,10,46,17,4,9] 
                ),
        Attribute(
                name="Knight_Armor",
                addresses=[0x1e1d3],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[19,1,42,
                                 18,25,10,46,17,4,9] 
                ),
        Attribute(
                name="Knight_Shield",
                addresses=[0x1e1fd],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[19,1,42,
                                 18,25,10,46,17,4,9] 
                ),
        Attribute(
                name="Holy_Water",
                addresses=[0x1e29e],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[19,1,42,
                                 18,25,10,46,17,4,9] 
                ),        
        Attribute(
                name="Flame_Shield",
                addresses=[0x1e1f7],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[18,25,10,46,17,4,9,
                                 0,16,8] 
                ),        
        Attribute(
                name="Flame_Armor",
                addresses=[0x1e1cd],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[18,25,10,46,17,4,9,
                                 0,16,8] 
                ),        
        Attribute(
                name="Hi_Potion",
                addresses=[0x1e2a4],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[18,25,10,46,17,4,9,
                                 0,16,8] 
                ),        
        Attribute(
                name="Elixer_Shop",
                addresses=[0x1e25d],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[18,25,10,46,17,4,9,
                                 0,16,8] 
                ),

        ### Sphere 0 Checks (3 Checks)###
        Attribute(
                name="Firestorm",
                addresses=[0xa752],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,154,177,186]
                ),
        Attribute(
                name="bat_reward",
                addresses=[0x2ca09],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,154,177,186]
                ),
        Attribute(
                name="Quake",
                addresses=[0xA738],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,154,177,186]
                ),

        ### Sphere 1 Checks (10 Checks)###
        Attribute(
                name="Hard_Shield",
                addresses=[0xA74E],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,154,    186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 160]
                ),
        Attribute(
                name="Trident",
                addresses=[0xA756],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,154,    186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 161]
                ),
        Attribute(
                name="Pygmy_Armor",
                addresses=[0xA72A],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[    154,177,186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 162]
                ),
        Attribute(
                name="Pygmy_Sword",
                addresses=[0xA728],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[    154,177,186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 163]
                ),
        Attribute(
                name="Amulet",
                addresses=[0xA754],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[    154,177,186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 164]
                ),
        Attribute(
                name="Thunder",
                addresses=[0xA734],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[    154,177,186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 165]
                ),
        Attribute(
                name="Shield_Magic_Chest",
                addresses=[0xA730],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,    177,186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 192]
                ),
        Attribute(
                name="Pygmy_Boots",
                addresses=[0xA72E],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,154,177,
                                 178,179,180,181,182,183,
                                 135,143,151,159]
                ),
        Attribute(
                name="Blue_Gem",
                addresses=[0xA744],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,154,177,
                                 178,179,180,181,182,183,
                                 135,143,151,159]
                ),
        Attribute(
                name="Gold_Gem",
                addresses=[0xA746],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,154,177,
                                 178,179,180,181,182,183,
                                 135,143,151,159]
                ),

        ### Sphere 2 Checks (4 Checks)###
        Attribute(
                name="Oasis_Boots",
                addresses=[0xA732],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[    154,177,186,
                                     179,180,181,182,183,
                                 135,143,151,159,
                                 184,185,
                                 160,161,162]
                ),        
        Attribute(
                name="Return",
                addresses=[0xA736],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[    154,177,186,
                                     179,180,181,182,183,
                                 135,143,151,159,
                                 184,185,
                                 163,164,165]
                ),
        Attribute(
                name="Sun_Key",
                addresses=[0xA73C],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[        177,186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 184,185,
                                 160,161,192]
                ),
        Attribute(
                name="Moon_Key",
                addresses=[0xA73A],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,    177,186,
                                 178,    180,181,182,183,
                                 135,143,151,159,
                                 184,185,
                                 162,163,192]
                ),


        ### Sphere 3 Checks (2 Checks)###
        Attribute(
                name="Star_Key",
                addresses=[0xA73E],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,    177,186,
                                 178,        181,182,183,
                                 135,143,151,159,
                                 184,185,
                                 164]
                ),
        Attribute(
                name="Old_Axe",
                addresses=[0xA758],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,154,177,
                                 178,179,180,181,
                                 135,143,151,159,
                                 184,185,
                                 165]
                ),
        
        ### Sphere 4 Checks (3 Checks)###
        Attribute(
                name="Pygmy_Shield",
                addresses=[0xA72C],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,    177,186,
                                 178,            182,183,
                                 135,143,151,159,
                                 184,185]
                ),
        Attribute(
                name="Power",
                addresses=[0xA750],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,    177,186,
                                 178,            182,183,
                                 135,143,151,159,
                                 184,185]
                ),
        
        ### Sphere Pygmy Checks (2 Checks)###
        Attribute(
                name="Fire_Urn",
                addresses=[0xA75A],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,    177,186,
                                 178,            182,183,
                                 
                                 184,185]
                ),        
        Attribute(
                name="Charmstone_Chest",
                addresses=[0xA740],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,    177,186,
                                 178,            182,183,
                                 
                                 184,185]
                ),

        ### Legend Stuff (To Do: Find Legend Sword Check)
        Attribute(
                name="Legend_Boots",
                addresses=[0xA742],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[136,144,152]
                ),        
        Attribute(
                name="Legend_Shield",
                addresses=[0xA74A],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[136,144,152]
                ),        
        Attribute(
                name="Legend_Armor",
                addresses=[0xA748],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[136,144,152]
                )
        
]
Required_Rules = [
        Rule(
                description="Chests are Different",
                left_side=[value("Firestorm"),value("Quake"),value("bat_reward"),value("Pygmy_Sword"),value("Pygmy_Armor"),
                           value("Pygmy_Boots"),value("Pygmy_Shield"),value("Sun_Key"),value("Moon_Key"),value("Star_Key"),
                           value("Blue_Gem"),value("Gold_Gem"),value("Thunder"),value("Return"),value("Power"),value("Shield_Magic_Chest"),
                           value("Old_Axe"),value("Fire_Urn"),value("Charmstone_Chest"),
                           value("Hard_Shield"),value("Trident"),value("Oasis_Boots"),value("Amulet")],
                rule_type="!=",
                right_side=None
        ),

        Rule(
                description="Shops are Different",
                left_side=[value("leather_boots"),
                           value("medicine"),value("small_spear"),value("chain_mail"),value("wood_shield"),
                           value("Knight_Sword"),value("Hard_Armor"),value("Charmstone_Purchase"),value("Potion"),value("Ladder_Boots"),
                           value("excalibur"),value("steel_shield"),                           
                           value("Marine_Boots"),value("Shield_Magic_Shop"),value("Shell_Shield"),value("Steel_Armor"),
                           value("Ceramic_Boots"),value("Battle_Spear"),value("Knight_Armor"),value("Knight_Shield"),value("Holy_Water"),
                           value("Flame_Shield"),value("Flame_Armor"),value("Hi_Potion"),value("Elixer_Shop")],
                rule_type="!=",
                right_side=None
        ),

        Rule(
                description="Elder is Different",
                left_side=[value("elder_elixer"),value("elder_firestorm")],
                rule_type="!=",
                right_side=None
        ),

        Rule(
                description="Legends are Different",
                left_side=[value("Legend_Boots"),value("Legend_Shield"),value("Legend_Armor")],
                rule_type="!=",
                right_side=None
        ),

### Ensure Marine Boots are found so that you can do the quake chest ###
        Rule(
                description="Marine_Logic",
                left_side=[value("Knight_Sword"),value("Hard_Armor"),value("Potion"),value("Charmstone_Purchase"),value("Ladder_Boots"),value("Marine_Boots"),value("Shield_Magic_Shop"),
                           value("Shell_Shield"),value("Steel_Armor")],
                rule_type="count",
                right_side=("==",1,"==",27)
        ),

### Ensure late game you can get the health stuff for final battle. ###
        Rule(
                description="Hi_Potion_Logic",
                left_side=[value("Ceramic_Boots"),value("Battle_Spear"),value("Knight_Armor"),value("Knight_Shield"),value("Holy_Water"),
                           value("Flame_Shield"),value("Flame_Armor"),value("Hi_Potion"),value("Elixer_Shop")],
                rule_type="count",
                right_side=("==",1,"==",46)
        ),

        Rule(
                description="Elixer_Logic",
                left_side=[value("Ceramic_Boots"),value("Battle_Spear"),value("Knight_Armor"),value("Knight_Shield"),value("Holy_Water"),
                           value("Flame_Shield"),value("Flame_Armor"),value("Hi_Potion"),value("Elixer_Shop")],
                rule_type="count",
                right_side=("==",1,"==",47)
        )

]
#64 is a heart, but it didn't increase my health.

Optional_Rulesets = [
        Ruleset(
		name="Not too Slow, eh?",
		description="Legend boots and Sword",
		rules=[
                        Rule(
				description="Legend Boots",
				left_side=[value("elder_elixer")],
				rule_type="==",
				right_side=24,
			),			
			Rule(
				description="Legend Swprd",
				left_side=[value("elder_firestorm")],
				rule_type="==",
				right_side=0,
			),
		],
		must_be_enabled=None,
		must_be_disabled=None,
	),
        Ruleset(
		name="Not too Swim, eh?",
		description="Trident and Marine Boots",
		rules=[
			Rule(
				description="Trident",
				left_side=[value("elder_elixer")],
				rule_type="==",
				right_side=5,
			),
			Rule(
				description="Marine Boots",
				left_side=[value("elder_firestorm")],
				rule_type="==",
				right_side=27,
			),
		],
		must_be_enabled=None,
		must_be_disabled=None,
	),
        Ruleset(
		name="Make sure you can swim Bro",
		description="Swim Stuff",
		rules=[
			Rule(
				description="Trident",
				left_side=[value("Firestorm")],
				rule_type="==",
				right_side=133,
			),
                        Rule(
				description="Marine Boots",
				left_side=[value("Heart_Chests")],
				rule_type="==",
				right_side=155,
			),
                        Rule(
				description="Amulet",
				left_side=[value("Amulet")],
				rule_type="==",
				right_side=178,
			)
		],
		must_be_enabled=None,
		must_be_disabled=None,
	),
        Ruleset(
		name="Shion Uses the Bracelet",
		description="Fire the Ice",
		rules=[
			Rule(
				description="Bracelet",
				left_side=[value("Quake")],
				rule_type="==",
				right_side=186,
			)
		],
		must_be_enabled=None,
		must_be_disabled=None,
	),
        Ruleset(
		name="Don't Sweat it",
		description="Desert_Pyramid_Begonia",
		rules=[
			Rule(
				description="Oasis_Boots",
				left_side=[value("Firestorm")],
				rule_type="==",
				right_side=154,
			),
                        Rule(
				description="Armor",
				left_side=[value("Heart_Chests")],
				rule_type="==",
				right_side=136,
			),
                        Rule(
				description="Sun Key",
				left_side=[value("Shield_Magic_Chest")],
				rule_type="==",
				right_side=181,
			),
                        Rule(
				description="Blue Gem",
				left_side=[value("Quake")],
				rule_type="==",
				right_side=182,
			),
                        Rule(
				description="Gold Gem",
				left_side=[value("Pygmy_Boots")],
				rule_type="==",
				right_side=183,
			)
		],
		must_be_enabled=None,
		must_be_disabled=None,
	),
        Ruleset(
		name="Not too Charm, eh?",
		description="Equipment for Pyramid and Pygmy",
		rules=[
			Rule(
				description="Trident",
				left_side=[value("Firestorm")],
				rule_type="==",
				right_side=133,
			),
                        Rule(
				description="Marine Boots",
				left_side=[value("Heart_Chests")],
				rule_type="==",
				right_side=155,
			),
                        Rule(
				description="P_Armor",
				left_side=[value("Pygmy_Armor")],
				rule_type="==",
				right_side=143,
			),
                        Rule(
				description="P_Sword",
				left_side=[value("Pygmy_Sword")],
				rule_type="==",
				right_side=135,
			),
                        Rule(
				description="P_Boots",
				left_side=[value("Thunder")],
				rule_type="==",
				right_side=159,
			),
                        Rule(
				description="P_Shield",
				left_side=[value("Amulet")],
				rule_type="==",
				right_side=151,
			),
                        Rule(
				description="O_Boots",
				left_side=[value("Quake")],
				rule_type="==",
				right_side=154,
			),
                        Rule(
				description="Star_Key",
				left_side=[value("Sun_Key")],
				rule_type="==",
				right_side=181,
			)
		],
		must_be_enabled=None,
		must_be_disabled=None,
	),
        Ruleset(
		name="Not too Legend, EH?",
		description="Fire Uurn",
		rules=[
			Rule(
				description="Marine Boots",
				left_side=[value("Firestorm")],
				rule_type="==",
				right_side=155,
			),
                        Rule(
				description="Trident",
				left_side=[value("Heart_Chests")],
				rule_type="==",
				right_side=133,
			),
                        Rule(
				description="Star_Key",
				left_side=[value("Shield_Magic_Chest")],
				rule_type="==",
				right_side=181,
			),
                        Rule(
				description="Fire Urn",
				left_side=[value("Quake")],
				rule_type="==",
				right_side=185,
			),
                        Rule(
				description="Oasis Boots",
				left_side=[value("Pygmy_Sword")],
				rule_type="==",
				right_side=154,
			),
                        Rule(
				description="Old Axe",
				left_side=[value("Thunder")],
				rule_type="==",
				right_side=184,
			),
                        Rule(
				description="Armor",
				left_side=[value("Amulet")],
				rule_type="==",
				right_side=136,
			)
		],
		must_be_enabled=None,
		must_be_disabled=None,
	)

]
