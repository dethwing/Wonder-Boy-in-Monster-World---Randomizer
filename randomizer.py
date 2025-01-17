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
        Attribute(
                name="First_Money_Control",
                addresses=[0xa75f],
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
                possible_values=[1,2,3,4,5,6,7,8,9,10,11,12,
                                 13,14,15,16,17,18,19,20,21,
                                 22,23,24,25,26,27,28,29,30,
                                 31,32,33,34,35,36,37,41,42,
                                 43,44,45,46,49,50,51,52,53,
                                 54,55,56,57,58]                                 
                ),
        Attribute(
                name="elder_firestorm",
                addresses=[0x1e08b],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,11,12,
                                 13,14,15,16,17,18,19,20,21,
                                 22,23,24,25,26,27,28,29,30,
                                 31,32,33,34,35,36,37,41,42,
                                 43,44,45,46,49,50,51,52,53,
                                 54,55,56,57,58]
                ),
        ### Don't Randomize these. Placeholders for later ###
        # Attribute(
        #        name="Heart_Chests",
        #        addresses=[0xa722],
        #        number_of_bytes=1,
        #        is_little_endian=False,
        #        possible_values=[185]
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
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),
        Attribute(
                name="medicine",
                addresses=[0x1e292],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),
        Attribute(
                name="small_spear",
                addresses=[0x1e1c1],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),
        Attribute(
                name="chain_mail",
                addresses=[0x1e1e5],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),
        Attribute(
                name="wood_shield",
                addresses=[0x1e215],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),        
       Attribute(
                name="Knight_Sword",
                addresses=[0x1e1b5],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),
        Attribute(
                name="Hard_Armor",
                addresses=[0x1e1df],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),
        Attribute(
                name="Charmstone_Purchase",
                addresses=[0x1e28c],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),
        Attribute(
                name="Potion",
                addresses=[0x1e298],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),
        Attribute(
                name="Ladder_Boots",
                addresses=[0x1e233],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),
        Attribute(
                name="Marine_Boots",
                addresses=[0x1e22d],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),
        Attribute(
                name="Shield_Magic_Shop",
                addresses=[0x1e251],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),
        Attribute(
                name="Shell_Shield",
                addresses=[0x1e20f],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),
        Attribute(
                name="Steel_Armor",
                addresses=[0x1e1d9],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),
        Attribute(
                name="excalibur",
                addresses=[0x1e1af],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),
        Attribute(
                name="steel_shield",
                addresses=[0x1e203],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),       
        Attribute(
                name="Ceramic_Boots",
                addresses=[0x1e221],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),
        Attribute(
                name="Battle_Spear",
                addresses=[0x1e1bb],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),
        Attribute(
                name="Knight_Armor",
                addresses=[0x1e1d3],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),
        Attribute(
                name="Knight_Shield",
                addresses=[0x1e1fd],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),
        Attribute(
                name="Holy_Water",
                addresses=[0x1e29e],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),        
        Attribute(
                name="Flame_Shield",
                addresses=[0x1e1f7],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),        
        Attribute(
                name="Flame_Armor",
                addresses=[0x1e1cd],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),        
        Attribute(
                name="Hi_Potion",
                addresses=[0x1e2a4],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),        
        Attribute(
                name="Elixer_Shop",
                addresses=[0x1e25d],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),

        ### Sphere 0 Checks (3 Checks - 4 Prog.)###
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

        ### Sphere 1 Checks (12 Checks - 14 Prog (No Urn) / 5 Spells / Elixer)###
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
        ### Elixer Chest can be accessed in 3 places. One is Sphere 1, and two are Sphere 2. ###
        ### I have chosen to treat it as a Sphere 1, though it can technically have it's only key###
        Attribute(
                name="Elixer_Chests",
                addresses=[0xA74C],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,154,177,186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 162]
                ),
        Attribute(
                name="First_Money",
                addresses=[0xa75e],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[    154,177,186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 163] 
                ),
        Attribute(
                name="Pygmy_Armor",
                addresses=[0xA72A],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[    154,177,186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 165]
                ),
        Attribute(
                name="Pygmy_Sword",
                addresses=[0xA728],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[    154,177,186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 170]
                ),
        Attribute(
                name="Amulet",
                addresses=[0xA754],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[    154,177,186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 160]
                ),
        Attribute(
                name="Thunder",
                addresses=[0xA734],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[    154,177,186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 161]
                ),
        Attribute(
                name="Shield_Magic_Chest",
                addresses=[0xA730],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,    177,186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 162]
                ),
        Attribute(
                name="Pygmy_Boots",
                addresses=[0xA72E],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,154,177,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 163]
                ),
        Attribute(
                name="Blue_Gem",
                addresses=[0xA744],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,154,177,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 165]
                ),
        Attribute(
                name="Gold_Gem",
                addresses=[0xA746],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,154,177,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 170]
                ),

        ### Sphere 2 Checks (7 Checks - 15 Prog / 5 Spells / Elixer / 3 Legend)###
        ### Deeper Checks (Oasis/Star/Power) are more likely to have Legend Equipment###
        Attribute(
                name="Oasis_Boots",
                addresses=[0xA732],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[    154,177,186,
                                     179,180,181,182,183,
                                 135,143,151,159,
                                 185,
                                 192,136]
                ),        
        Attribute(
                name="Return",
                addresses=[0xA736],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[    154,177,186,
                                     179,180,181,182,183,
                                 135,143,151,159,
                                 185,
                                 160,144]
                ),
        Attribute(
                name="Sun_Key",
                addresses=[0xA73C],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[        177,186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 185,
                                 161,162]
                ),
        Attribute(
                name="Moon_Key",
                addresses=[0xA73A],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,    177,186,
                                 178,    180,181,182,183,
                                 135,143,151,159,
                                 185,
                                 163,164]
                ),
        Attribute(
                name="Star_Key",
                addresses=[0xA73E],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,    177,186,
                                 178,    180,181,182,183,
                                 135,143,151,159,
                                 185,
                                 152,192]
                ),
        Attribute(
                name="Pygmy_Shield",
                addresses=[0xA72C],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,    177,186,
                                 178,179,    181,182,183,
                                 135,143,151,159,
                                 185,
                                 170,136]
                ),
        Attribute(
                name="Power",
                addresses=[0xA750],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,    177,186,
                                 178,179,180,    182,183,
                                 135,143,151,159,
                                 185,
                                 144,152]
                ),

        ### Sphere 3+ (3 Checks - Fire Urn and non essentials only)###        
        Attribute(
                name="Old_Axe",
                addresses=[0xA758],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[185,
                                 160,161,162,163,165,
                                 170,192,136,144,154]
                ),
        
        
        Attribute(
                name="Fire_Urn",
                addresses=[0xA75A],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[185,
                                 160,161,162,163,165,
                                 170,192,136,144,154]
                ),        
        Attribute(
                name="Charmstone_Chest",
                addresses=[0xA740],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[185,
                                 160,161,162,163,165,
                                 170,192,136,144,154]
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
                           value("Hard_Shield"),value("Trident"),value("Oasis_Boots"),value("Amulet"),
                           value("Elixer_Chests"),value("First_Money")],
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

### Ensure Marine Boots are available in an early shop so that you can do the quake chest ###
        Rule(
                description="Marine Logic",
                left_side=[value("leather_boots"),
                           value("medicine"),value("small_spear"),value("chain_mail"),value("wood_shield"),
                           value("Knight_Sword"),value("Hard_Armor"),value("Charmstone_Purchase"),value("Potion"),value("Ladder_Boots"),
                           value("Marine_Boots"),value("Shield_Magic_Shop"),value("Shell_Shield"),value("Steel_Armor")],
                rule_type="count",
                right_side=("==",27,"==",1)
        ),

### Ensure late game you can get the health stuff for final battle. ###
        Rule(
                description="Hi-Potion Logic",
                left_side=[value("leather_boots"),
                           value("medicine"),value("small_spear"),value("chain_mail"),value("wood_shield"),
                           value("Knight_Sword"),value("Hard_Armor"),value("Charmstone_Purchase"),value("Potion"),value("Ladder_Boots"),
                           value("excalibur"),value("steel_shield"),                           
                           value("Marine_Boots"),value("Shield_Magic_Shop"),value("Shell_Shield"),value("Steel_Armor"),
                           value("Ceramic_Boots"),value("Battle_Spear"),value("Knight_Armor"),value("Knight_Shield"),value("Holy_Water"),
                           value("Flame_Shield"),value("Flame_Armor"),value("Hi_Potion"),value("Elixer_Shop")],
                rule_type="count",
                right_side=("==",46,"==",1)
        ),
        Rule(
                description="Elixer Logic",
                left_side=[value("leather_boots"),
                           value("medicine"),value("small_spear"),value("chain_mail"),value("wood_shield"),
                           value("Knight_Sword"),value("Hard_Armor"),value("Charmstone_Purchase"),value("Potion"),value("Ladder_Boots"),
                           value("excalibur"),value("steel_shield"),                           
                           value("Marine_Boots"),value("Shield_Magic_Shop"),value("Shell_Shield"),value("Steel_Armor"),
                           value("Ceramic_Boots"),value("Battle_Spear"),value("Knight_Armor"),value("Knight_Shield"),value("Holy_Water"),
                           value("Flame_Shield"),value("Flame_Armor"),value("Hi_Potion"),value("Elixer_Shop")],
                rule_type="count",
                right_side=("==",42,"==",1)
        )

]

Optional_Rulesets = [
        Ruleset(
		name="Elder - No Useless Items",
		description="Elder items not Progression or Starting Equipment",
		rules=[
                        Rule(
				description="Starter_1",
				left_side=[value("elder_elixer"),value("elder_firestorm")],
				rule_type="<=",
				right_side=46,
			),	
                        Rule(
				description="Starter_2",
				left_side=[value("elder_elixer"),value("elder_firestorm")],
				rule_type="!=",
				right_side=3,
			),	
                        Rule(
				description="Starter_3",
				left_side=[value("elder_elixer"),value("elder_firestorm")],
				rule_type="!=",
				right_side=14,
			),	
                        Rule(
				description="Starter_4",
				left_side=[value("elder_elixer"),value("elder_firestorm")],
				rule_type="!=",
				right_side=30,
			),	
		],
		must_be_enabled=None,
		must_be_disabled=None,
	),
        Ruleset(
		name="Elder - No Legend Items",
		description="Elder Items not Legend",
		rules=[
                        Rule(
				description="Starter_1",
				left_side=[value("elder_elixer"),value("elder_firestorm")],
				rule_type="!=",
				right_side=8,
			),			
			Rule(
				description="Starter_2",
				left_side=[value("elder_elixer"),value("elder_firestorm")],
				rule_type="!=",
				right_side=16,
			),
                        Rule(
				description="Starter_3",
				left_side=[value("elder_elixer"),value("elder_firestorm")],
				rule_type="!=",
				right_side=24,
			),	
		],
		must_be_enabled=None,
		must_be_disabled=None,
	),
        Ruleset(
		name="Elder - No Equipment",
		description="Elder Items not Equipment",
		rules=[
                        Rule(
				description="Starter_1",
				left_side=[value("elder_elixer"),value("elder_firestorm")],
				rule_type=">=",
				right_side=32,
			),
                ],
                must_be_enabled=None,
		must_be_disabled=None,
	),
        Ruleset(
		name="Elder - Spells Only",
		description="Elder Items only Spells [Standard]",
		rules=[
                        Rule(
				description="Starter_1",
				left_side=[value("elder_elixer"),value("elder_firestorm")],
				rule_type=">=",
				right_side=32,
			),
                        Rule(
				description="Starter_2",
				left_side=[value("elder_elixer"),value("elder_firestorm")],
				rule_type="<=",
				right_side=37,
			),	
                ],
                must_be_enabled=None,
		must_be_disabled=None,
	),
        Ruleset(
		name="Elder - Equipment Only",
		description="Elder Items Equipment",
		rules=[
                        Rule(
				description="Starter_1",
				left_side=[value("elder_elixer"),value("elder_firestorm")],
				rule_type="<=",
				right_side=31,
			),
                ],
                must_be_enabled=None,
		must_be_disabled=None,
	),
        Ruleset(
		name="Elder - Strong Equipment",
		description="Elder Items Strong Equipment",
		rules=[
                        Rule(
				description="Elixer_1",
				left_side=[value("elder_elixer")],
				rule_type="<=",
				right_side=4,
			),
                        Rule(
				description="Elixer_2",
				left_side=[value("elder_elixer")],
				rule_type=">=",
				right_side=1,
			),
                        Rule(
				description="Elixer_3",
				left_side=[value("elder_elixer")],
				rule_type="!=",
				right_side=3,
			),
			Rule(
				description="Storm_1",
				left_side=[value("elder_firestorm")],
				rule_type=">=",
				right_side=9,
                        ),
                        Rule(
				description="Storm_2",
				left_side=[value("elder_firestorm")],
				rule_type="<=",
				right_side=11,
                        ),
                ],
                must_be_enabled=None,
		must_be_disabled=None,
	),
        Ruleset(
		name="Shops - No Starters",
		description="Starter Items (Gradius/Leather Armor/Cloth Boots) not in Shops",
		rules=[
                        Rule(
				description="No_3",
				left_side=[value("leather_boots"),
                           value("medicine"),value("small_spear"),value("chain_mail"),value("wood_shield"),
                           value("Knight_Sword"),value("Hard_Armor"),value("Charmstone_Purchase"),value("Potion"),value("Ladder_Boots"),
                           value("excalibur"),value("steel_shield"),                           
                           value("Marine_Boots"),value("Shield_Magic_Shop"),value("Shell_Shield"),value("Steel_Armor"),
                           value("Ceramic_Boots"),value("Battle_Spear"),value("Knight_Armor"),value("Knight_Shield"),value("Holy_Water"),
                           value("Flame_Shield"),value("Flame_Armor"),value("Hi_Potion"),value("Elixer_Shop")],
				rule_type="!=",
				right_side=3,
			),
                        Rule(
				description="No_14",
				left_side=[value("leather_boots"),
                           value("medicine"),value("small_spear"),value("chain_mail"),value("wood_shield"),
                           value("Knight_Sword"),value("Hard_Armor"),value("Charmstone_Purchase"),value("Potion"),value("Ladder_Boots"),
                           value("excalibur"),value("steel_shield"),                           
                           value("Marine_Boots"),value("Shield_Magic_Shop"),value("Shell_Shield"),value("Steel_Armor"),
                           value("Ceramic_Boots"),value("Battle_Spear"),value("Knight_Armor"),value("Knight_Shield"),value("Holy_Water"),
                           value("Flame_Shield"),value("Flame_Armor"),value("Hi_Potion"),value("Elixer_Shop")],
				rule_type="!=",
				right_side=14,
			),
                        Rule(
				description="No_30",
				left_side=[value("leather_boots"),
                           value("medicine"),value("small_spear"),value("chain_mail"),value("wood_shield"),
                           value("Knight_Sword"),value("Hard_Armor"),value("Charmstone_Purchase"),value("Potion"),value("Ladder_Boots"),
                           value("excalibur"),value("steel_shield"),                           
                           value("Marine_Boots"),value("Shield_Magic_Shop"),value("Shell_Shield"),value("Steel_Armor"),
                           value("Ceramic_Boots"),value("Battle_Spear"),value("Knight_Armor"),value("Knight_Shield"),value("Holy_Water"),
                           value("Flame_Shield"),value("Flame_Armor"),value("Hi_Potion"),value("Elixer_Shop")],
				rule_type="!=",
				right_side=30,
			),
                        
                ],
                must_be_enabled=None,
		must_be_disabled=None,
	),
        Ruleset(
		name="Shops - No Legends",
		description="Legend Items not in Shops",
		rules=[
                        Rule(
				description="No_8",
				left_side=[value("leather_boots"),
                           value("medicine"),value("small_spear"),value("chain_mail"),value("wood_shield"),
                           value("Knight_Sword"),value("Hard_Armor"),value("Charmstone_Purchase"),value("Potion"),value("Ladder_Boots"),
                           value("excalibur"),value("steel_shield"),                           
                           value("Marine_Boots"),value("Shield_Magic_Shop"),value("Shell_Shield"),value("Steel_Armor"),
                           value("Ceramic_Boots"),value("Battle_Spear"),value("Knight_Armor"),value("Knight_Shield"),value("Holy_Water"),
                           value("Flame_Shield"),value("Flame_Armor"),value("Hi_Potion"),value("Elixer_Shop")],
				rule_type="!=",
				right_side=8,
			),
                        Rule(
				description="No_16",
				left_side=[value("leather_boots"),
                           value("medicine"),value("small_spear"),value("chain_mail"),value("wood_shield"),
                           value("Knight_Sword"),value("Hard_Armor"),value("Charmstone_Purchase"),value("Potion"),value("Ladder_Boots"),
                           value("excalibur"),value("steel_shield"),                           
                           value("Marine_Boots"),value("Shield_Magic_Shop"),value("Shell_Shield"),value("Steel_Armor"),
                           value("Ceramic_Boots"),value("Battle_Spear"),value("Knight_Armor"),value("Knight_Shield"),value("Holy_Water"),
                           value("Flame_Shield"),value("Flame_Armor"),value("Hi_Potion"),value("Elixer_Shop")],
				rule_type="!=",
				right_side=16,
			),
                        Rule(
				description="No_24",
				left_side=[value("leather_boots"),
                           value("medicine"),value("small_spear"),value("chain_mail"),value("wood_shield"),
                           value("Knight_Sword"),value("Hard_Armor"),value("Charmstone_Purchase"),value("Potion"),value("Ladder_Boots"),
                           value("excalibur"),value("steel_shield"),                           
                           value("Marine_Boots"),value("Shield_Magic_Shop"),value("Shell_Shield"),value("Steel_Armor"),
                           value("Ceramic_Boots"),value("Battle_Spear"),value("Knight_Armor"),value("Knight_Shield"),value("Holy_Water"),
                           value("Flame_Shield"),value("Flame_Armor"),value("Hi_Potion"),value("Elixer_Shop")],
				rule_type="!=",
				right_side=24,
			),
                        
                ],
                must_be_enabled=None,
		must_be_disabled=None,
	),
        Ruleset(
		name="Shops - No Progression (Pygmy/Trident/Oasis)",
		description="Progression Items not in Shops",
		rules=[
                        Rule(
				description="No_7",
				left_side=[value("leather_boots"),
                           value("medicine"),value("small_spear"),value("chain_mail"),value("wood_shield"),
                           value("Knight_Sword"),value("Hard_Armor"),value("Charmstone_Purchase"),value("Potion"),value("Ladder_Boots"),
                           value("excalibur"),value("steel_shield"),                           
                           value("Marine_Boots"),value("Shield_Magic_Shop"),value("Shell_Shield"),value("Steel_Armor"),
                           value("Ceramic_Boots"),value("Battle_Spear"),value("Knight_Armor"),value("Knight_Shield"),value("Holy_Water"),
                           value("Flame_Shield"),value("Flame_Armor"),value("Hi_Potion"),value("Elixer_Shop")],
				rule_type="!=",
				right_side=7,
			),
                        Rule(
				description="No_15",
				left_side=[value("leather_boots"),
                           value("medicine"),value("small_spear"),value("chain_mail"),value("wood_shield"),
                           value("Knight_Sword"),value("Hard_Armor"),value("Charmstone_Purchase"),value("Potion"),value("Ladder_Boots"),
                           value("excalibur"),value("steel_shield"),                           
                           value("Marine_Boots"),value("Shield_Magic_Shop"),value("Shell_Shield"),value("Steel_Armor"),
                           value("Ceramic_Boots"),value("Battle_Spear"),value("Knight_Armor"),value("Knight_Shield"),value("Holy_Water"),
                           value("Flame_Shield"),value("Flame_Armor"),value("Hi_Potion"),value("Elixer_Shop")],
				rule_type="!=",
				right_side=15,
			),
                        Rule(
				description="No_23",
				left_side=[value("leather_boots"),
                           value("medicine"),value("small_spear"),value("chain_mail"),value("wood_shield"),
                           value("Knight_Sword"),value("Hard_Armor"),value("Charmstone_Purchase"),value("Potion"),value("Ladder_Boots"),
                           value("excalibur"),value("steel_shield"),                           
                           value("Marine_Boots"),value("Shield_Magic_Shop"),value("Shell_Shield"),value("Steel_Armor"),
                           value("Ceramic_Boots"),value("Battle_Spear"),value("Knight_Armor"),value("Knight_Shield"),value("Holy_Water"),
                           value("Flame_Shield"),value("Flame_Armor"),value("Hi_Potion"),value("Elixer_Shop")],
				rule_type="!=",
				right_side=23,
			),
                        Rule(
				description="No_31",
				left_side=[value("leather_boots"),
                           value("medicine"),value("small_spear"),value("chain_mail"),value("wood_shield"),
                           value("Knight_Sword"),value("Hard_Armor"),value("Charmstone_Purchase"),value("Potion"),value("Ladder_Boots"),
                           value("excalibur"),value("steel_shield"),                           
                           value("Marine_Boots"),value("Shield_Magic_Shop"),value("Shell_Shield"),value("Steel_Armor"),
                           value("Ceramic_Boots"),value("Battle_Spear"),value("Knight_Armor"),value("Knight_Shield"),value("Holy_Water"),
                           value("Flame_Shield"),value("Flame_Armor"),value("Hi_Potion"),value("Elixer_Shop")],
				rule_type="!=",
				right_side=31,
			),
                        Rule(
				description="No_5",
				left_side=[value("leather_boots"),
                           value("medicine"),value("small_spear"),value("chain_mail"),value("wood_shield"),
                           value("Knight_Sword"),value("Hard_Armor"),value("Charmstone_Purchase"),value("Potion"),value("Ladder_Boots"),
                           value("excalibur"),value("steel_shield"),                           
                           value("Marine_Boots"),value("Shield_Magic_Shop"),value("Shell_Shield"),value("Steel_Armor"),
                           value("Ceramic_Boots"),value("Battle_Spear"),value("Knight_Armor"),value("Knight_Shield"),value("Holy_Water"),
                           value("Flame_Shield"),value("Flame_Armor"),value("Hi_Potion"),value("Elixer_Shop")],
				rule_type="!=",
				right_side=5,
			),
                        Rule(
				description="No_36",
				left_side=[value("leather_boots"),
                           value("medicine"),value("small_spear"),value("chain_mail"),value("wood_shield"),
                           value("Knight_Sword"),value("Hard_Armor"),value("Charmstone_Purchase"),value("Potion"),value("Ladder_Boots"),
                           value("excalibur"),value("steel_shield"),                           
                           value("Marine_Boots"),value("Shield_Magic_Shop"),value("Shell_Shield"),value("Steel_Armor"),
                           value("Ceramic_Boots"),value("Battle_Spear"),value("Knight_Armor"),value("Knight_Shield"),value("Holy_Water"),
                           value("Flame_Shield"),value("Flame_Armor"),value("Hi_Potion"),value("Elixer_Shop")],
				rule_type="!=",
				right_side=36,
			),
                        
                        
                ],
                must_be_enabled=None,
		must_be_disabled=None,
	),
        Ruleset(
		name="Shops - Cost Scaled",
		description="Shop items cost scale by region",
		rules=[
                        Rule(
				description="First Area",
				left_side=[value("leather_boots")],
				rule_type="!=",
				right_side=[
                                            22,44,13,6,20,21,
                                            45,12,2,27,32,36,
                                            37,33,34,35,11,26,
                                            19,1,42,18,25,10,
                                            31,46,5,17,7,4,
                                            9,15,24,23,16,8]

			),
                        Rule(
				description="Second Area",
				left_side=[value("medicine"),value("small_spear"),value("chain_mail"),value("wood_shield")],
				rule_type="!=",
				right_side=[
                                        
                                            45,12,2,27,32,36,
                                            37,33,34,35,11,26,
                                            19,1,42,18,25,10,
                                            31,46,5,17,7,4,
                                            9,15,24,23,16,8]

			),
                        Rule(
				description="Third Area",
				left_side=[value("Knight_Sword"),value("Hard_Armor"),value("Charmstone_Purchase"),
                                           value("Potion"),value("Ladder_Boots")],
				rule_type="!=",
				right_side=[43,3,14,30,29,28,

                                            
                                            37,33,34,35,11,26,
                                            19,1,42,18,25,10,
                                            31,46,5,17,7,4,
                                            9,15,24,23,16,8]

			),
                        Rule(
				description="Fourth Area",
				left_side=[value("Marine_Boots"),value("Shield_Magic_Shop"),
                                           value("Shell_Shield"),value("Steel_Armor")],
				rule_type="!=",
				right_side=[43,3,14,30,29,28,
                                            22,44,13,6,20,21,

                                            
                                            19,1,42,18,25,10,
                                            31,46,5,17,7,4,
                                            9,15,24,23,16,8]

			),
                        Rule(
				description="Fifth Area",
				left_side=[value("excalibur"),value("steel_shield")],
				rule_type="!=",
				right_side=[43,3,14,30,29,28,
                                            22,44,13,6,20,21,
                                            45,12,2,27,32,36,

                                            
                                            31,46,5,17,7,4,
                                            9,15,24,23,16,8]

			),
                        Rule(
				description="Sixth Area",
				left_side=[value("Ceramic_Boots"),value("Battle_Spear"),value("Knight_Armor"),
                                           value("Knight_Shield"),value("Holy_Water")],
				rule_type="!=",
				right_side=[43,3,14,30,29,28,
                                            22,44,13,6,20,21,
                                            45,12,2,27,32,36,
                                            37,33,34,35,11,26,

                                            
                                            9,15,24,23,16,8]

			),
                        Rule(
				description="Seventh Area",
				left_side=[value("Flame_Shield"),value("Flame_Armor"),
                                           value("Hi_Potion"),value("Elixer_Shop")],
				rule_type="!=",
				right_side=[43,3,14,30,29,28,
                                            22,44,13,6,20,21,
                                            45,12,2,27,32,36,
                                            37,33,34,35,11,26,
                                            19,1,42,18,25,10
                                            
                                                            ]

			),
		],
                must_be_enabled=None,
		must_be_disabled=None,
	),
	
]
