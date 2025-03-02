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
Timeout = 60
Slow_Mode = False

Attributes = [
        
        ### Sphere 0 Checks ###
        Attribute(
                name="Firestorm",
                addresses=[0xa752],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,38,
                                    41,   43,44,45,      48,49,
                                 50,51,52,53,54,55,56,57,58,59,
                                 64                                 
                                 ]
                ),
        Attribute(
                name="bat_reward",
                addresses=[0x2ca09],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,38,
                                    41,   43,44,45,      48,49,
                                 50,51,52,53,54,55,56,57,58,59,
                                 64                                 
                                 ]
                ),
        Attribute(
                name="Quake",
                addresses=[0xA738],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,   28,29,
                                 30,31,32,33,34,35,36,37,38,
                                    41,   43,44,45,      48,49,
                                 50,51,52,53,54,55,56,57,58,59,
                                 64                                 
                                 ]
                ),


        ### Lamp Checks (3) ###
        Attribute(
                name="Hard_Shield",
                addresses=[0xA74E],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,38,
                                    41,   43,44,45,      48,
                                 50,51,52,53,54,55,56,57,58,59,
                                 64                                 
                                 ]
                ),
        Attribute(
                name="Trident",
                addresses=[0xA756],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,38,
                                    41,   43,44,45,      48,
                                 50,51,52,53,54,55,56,57,58,59,
                                 64                                 
                                 ]
                ),      
        Attribute(
                name="Elixer_Chests",
                addresses=[0xA74C],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,38,
                                    41,   43,44,45,      48,
                                 50,51,52,53,54,55,56,57,58,59,
                                 64                                 
                                 ]
                ),

        ### Trident Checks (5) ###
        Attribute(
                name="First_Money",
                addresses=[0xa75e],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,38,
                                    41,   43,44,45,      48,49,
                                 50,51,52,53,54,55,56,57,58,59,
                                 64                                 
                                 ]
                ),        
        Attribute(
                name="Pygmy_Armor",
                addresses=[0xA72A],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,38,
                                    41,   43,44,45,      48,49,
                                 50,51,52,53,54,55,56,57,58,59,
                                 64                                 
                                 ]
                ),
        Attribute(
                name="Pygmy_Sword",
                addresses=[0xA728],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,38,
                                    41,   43,44,45,      48,49,
                                 50,51,52,53,54,55,56,57,58,59,
                                 64                                 
                                 ]
                ),
        Attribute(
                name="Amulet",
                addresses=[0xA754],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,38,
                                    41,   43,44,45,      48,49,
                                 50,51,52,53,54,55,56,57,58,59,
                                 64                                 
                                 ]
                ),
        Attribute(
                name="Thunder",
                addresses=[0xA734],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,38,
                                    41,   43,44,45,      48,49,
                                 50,51,52,53,54,55,56,57,58,59,
                                 64                                 
                                 ]
                ),

        ### Oasis Check (1) ###
        Attribute(
                name="Shield_Magic_Chest",
                addresses=[0xA730],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                 30,31,32,33,34,35,36,37,38,
                                    41,   43,44,45,      48,49,
                                 50,51,52,53,54,55,56,57,58,59,
                                 64                                 
                                 ]
                ),

        ### Bracelet Checks (3) ###
        Attribute(
                name="Pygmy_Boots",
                addresses=[0xA72E],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,38,
                                    41,   43,44,45,      48,49,
                                 50,51,52,53,54,55,56,57,   59,
                                 64                                 
                                 ]
                ),
        Attribute(
                name="Blue_Gem",
                addresses=[0xA744],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,38,
                                    41,   43,44,45,      48,49,
                                 50,51,52,53,54,55,56,57,   59,
                                 64                                 
                                 ]
                ),
        Attribute(
                name="Gold_Gem",
                addresses=[0xA746],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,38,
                                    41,   43,44,45,      48,49,
                                 50,51,52,53,54,55,56,57,   59,
                                 64                                 
                                 ]
                ),     

        ### Trident + Amulet Checks ###
        Attribute(
                name="Oasis_Boots",
                addresses=[0xA732],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                 30,31,32,33,34,35,36,   38,
                                    41,   43,44,45,      48,
                                    51,52,53,54,55,56,57,   59,
                                 64                                 
                                 ]
                ),        
        Attribute(
                name="Return",
                addresses=[0xA736],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                 30,31,32,33,34,35,36,   38,
                                    41,   43,44,45,      48,
                                    51,52,53,54,55,56,57,   59,
                                 64                                 
                                 ]
                ),

        ### Trident + Oasis Check ###
        Attribute(
                name="Sun_Key",
                addresses=[0xA73C],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                 30,31,32,33,34,35,36,   38,
                                    41,   43,44,45,      48,
                                 50,51,52,53,54,55,56,57,   59,
                                 64                                 
                                 ]
                ),

        ### Oasis + Sun Key Checks ###
        Attribute(
                name="Moon_Key",
                addresses=[0xA73A],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                 30,31,32,33,34,35,36,   38,
                                    41,   43,44,45,      48,
                                 50,   52,53,54,55,56,57,   59,
                                 64                                 
                                 ]
                ),
        Attribute(
                name="Secret_Pyramid_1",
                addresses=[0xa76a],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                 30,31,32,33,34,35,36,   38,
                                    41,   43,44,45,      48,
                                 50,   52,53,54,55,56,57,   59,
                                 64                                 
                                 ]
                ),
        Attribute(
                name="Secret_Pyramid_2",
                addresses=[0xa76c],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                 30,31,32,33,34,35,36,   38,
                                    41,   43,44,45,      48,
                                 50,   52,53,54,55,56,57,   59,
                                 64                                 
                                 ]
                ),
        Attribute(
                name="Secret_Pyramid_3",
                addresses=[0xa76e],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                 30,31,32,33,34,35,36,   38,
                                    41,   43,44,45,      48,
                                 50,   52,53,54,55,56,57,   59,
                                 64                                 
                                 ]
                ),
        Attribute(
                name="Secret_Pyramid_4",
                addresses=[0xa770],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                 30,31,32,33,34,35,36,   38,
                                    41,   43,44,45,      48,
                                 50,   52,53,54,55,56,57,   59,
                                 64                                 
                                 ]
                ),
        Attribute(
                name="Secret_Pyramid_5",
                addresses=[0xa772],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                 30,31,32,33,34,35,36,   38,
                                    41,   43,44,45,      48,
                                 50,   52,53,54,55,56,57,   59,
                                 64                                 
                                 ]
                ),
        Attribute(
                name="Star_Key",
                addresses=[0xA73E],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                 30,31,32,33,34,35,36,   38,
                                    41,   43,44,45,      48,
                                 50,   52,53,54,55,56,57,   59,
                                 64                                 
                                 ]
                ),

        ### Oasis + Moon Key Check ###
        Attribute(
                name="Pygmy_Shield",
                addresses=[0xA72C],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                 30,31,32,33,34,35,36,   38,
                                    41,   43,44,45,      48,
                                 50,51,   53,54,55,56,57,   59,
                                 64                                 
                                 ]
                ),

        ### Oasis + Star Key Check ###
        Attribute(
                name="Power",
                addresses=[0xA750],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                 30,31,32,33,34,35,36,   38,
                                    41,   43,44,45,      48,
                                 50,51,52,   54,55,56,57,   59,
                                 64                                 
                                 ]
                ),

        ### Sphere 3+ ###        
        Attribute(
                name="Old_Axe",
                addresses=[0xA758],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                 30,31,32,33,34,35,36,   38,
                                    41,   43,44,45,      48,
                                                   56,57,   59,
                                 64                                 
                                 ]
                ),
        
        
        Attribute(
                name="Fire_Urn",
                addresses=[0xA75A],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6,    8, 9,
                                 10,11,12,13,14,   16,17,18,19,
                                 20,21,22,   24,25,   27,28,29,
                                 30,   32,33,34,35,36,   38,
                                    41,   43,44,45,      48,
                                                   56,57,   59,
                                 64                                 
                                 ]
                ),        
        Attribute(
                name="Charmstone_Chest",
                addresses=[0xA740],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6,    8, 9,
                                 10,11,12,13,14,   16,17,18,19,
                                 20,21,22,   24,25,   27,28,29,
                                 30,   32,33,34,35,36,   38,
                                    41,   43,44,45,      48,
                                                   56,57,   59,
                                 64                                 
                                 ]
                ),

        ###Shops###
        Attribute(
                name="leather_boots",
                addresses=[0x1e239],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,
                                 40,41,42,43,44,45,46                           
                                 ] 
                ),
        Attribute(
                name="medicine",
                addresses=[0x1e292],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,
                                 40,41,42,43,44,45,46                           
                                 ] 
                ),
        Attribute(
                name="small_spear",
                addresses=[0x1e1c1],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,
                                 40,41,42,43,44,45,46                           
                                 ] 
                ),
        Attribute(
                name="chain_mail",
                addresses=[0x1e1e5],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,
                                 40,41,42,43,44,45,46                           
                                 ] 
                ),
        Attribute(
                name="wood_shield",
                addresses=[0x1e215],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,
                                 40,41,42,43,44,45,46                           
                                 ]  
                ),        
       Attribute(
                name="Knight_Sword",
                addresses=[0x1e1b5],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                           
                                 ] 
                ),
        Attribute(
                name="Hard_Armor",
                addresses=[0x1e1df],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                           
                                 ]
                ),
        Attribute(
                name="Charmstone_Purchase",
                addresses=[0x1e28c],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                           
                                 ]
                ),
        Attribute(
                name="Potion",
                addresses=[0x1e298],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                           
                                 ]
                ),
        Attribute(
                name="Ladder_Boots",
                addresses=[0x1e233],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                           
                                 ]
                ),
        Attribute(
                name="Marine_Boots",
                addresses=[0x1e22d],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                           
                                 ]
                ),
        Attribute(
                name="Shield_Magic_Shop",
                addresses=[0x1e251],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                           
                                 ]
                ),
        Attribute(
                name="Shell_Shield",
                addresses=[0x1e20f],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                           
                                 ]
                ),
        Attribute(
                name="Steel_Armor",
                addresses=[0x1e1d9],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                           
                                 ]
                ),
        Attribute(
                name="excalibur",
                addresses=[0x1e1af],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                 30,31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                           
                                 ]
                ),
        Attribute(
                name="steel_shield",
                addresses=[0x1e203],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                 30,31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                           
                                 ]
                ),       
        Attribute(
                name="Ceramic_Boots",
                addresses=[0x1e221],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                           
                                 ]
                ),
        Attribute(
                name="Battle_Spear",
                addresses=[0x1e1bb],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                           
                                 ] 
                ),
        Attribute(
                name="Knight_Armor",
                addresses=[0x1e1d3],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                           
                                 ]
                ),
        Attribute(
                name="Knight_Shield",
                addresses=[0x1e1fd],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                           
                                 ]
                ),
        Attribute(
                name="Holy_Water",
                addresses=[0x1e29e],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                           
                                 ] 
                ),        
        Attribute(
                name="Flame_Shield",
                addresses=[0x1e1f7],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,      28,29,
                                 30,31,32,33,34,35,36,
                                    41,42,43,44,45,46                           
                                 ]
                ),        
        Attribute(
                name="Flame_Armor",
                addresses=[0x1e1cd],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,      28,29,
                                 30,31,32,33,34,35,36,
                                    41,42,43,44,45,46                           
                                 ]
                ),        
        Attribute(
                name="Hi_Potion",
                addresses=[0x1e2a4],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,      28,29,
                                 30,31,32,33,34,35,36,
                                    41,42,43,44,45,46                           
                                 ] 
                ),        
        Attribute(
                name="Elixer_Shop",
                addresses=[0x1e25d],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,      28,29,
                                 30,31,32,33,34,35,36,
                                    41,42,43,44,45,46                           
                                 ]
                ),
        ###Elder###
        Attribute(
                name="elder_elixer",
                addresses=[0x1e07f],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,38,
                                 40,41,   43,44,45,      48,49,
                                 50,51,52,53,54,55,56,57,58,59       
                                 ]                                 
                ),
        Attribute(
                name="elder_firestorm",
                addresses=[0x1e08b],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,38,
                                 40,41,   43,44,45,      48,49,
                                 50,51,52,53,54,55,56,57,58,59       
                                 ] 
                ),
        ###Legend Sword###
        Attribute(
                name="Legend_Sword",
                addresses=[0x1EE29],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6,    8, 9,
                                 10,11,12,13,14,   16,17,18,19,
                                 20,21,22,   24,25,      28,29,
                                 30,   32,33,34,35,36,   38,
                                    41,   43,44,45,      48,
                                                   56,      59                                                                  
                                 ]
                ),
        Attribute(
                name="Legend_Sword_Text_1",
                addresses=[0x1EE0E],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[11]
                ),
        Attribute(
                name="Legend_Sword_Text_2",
                addresses=[0x1EE0F],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[10]
                ),
        Attribute(
                name="Legend_Item",
                addresses=[0x1EE10],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6,    8, 9,
                                 10,11,12,13,14,   16,17,18,19,
                                 20,21,22,   24,25,      28,29,
                                 30,   32,33,34,35,36,   38,
                                    41,   43,44,45,      48,
                                                   56,      59                                                                  
                                 ]
                ),
        Attribute(
                name="Legend_Sword_Text_3",
                addresses=[0x1EE11],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[12] 
                ),
        Attribute(
                name="Legend_Sword_Text_4",
                addresses=[0x1EE12],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[2] 
                ),
        ###Ocarina###
        Attribute(
                name="Ocarina_Text",
                addresses=[0x1e277],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,38,
                                 40,41,   43,44,45,      48,49,
                                 50,51,52,53,54,55,56,57,58,59       
                                 ] 
                ),
        Attribute(
                name="Ocarina_Reward",
                addresses=[0x1e27c],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,38,
                                 40,41,   43,44,45,      48,49,
                                 50,51,52,53,54,55,56,57,58,59       
                                 ]  
                ),
        
        ###Prices####
        Attribute(
                name="Medecine_Price",
                addresses=[0x1e5d],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=1,
		max_value=10,
		min_max_interval=1,
                ),
        Attribute(
                name="LeatherBoots_Price",
                addresses=[0x1e25],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=1,
		max_value=30,
		min_max_interval=1,
                ),
        Attribute(
                name="Wood_Shield_Price",
                addresses=[0x1e09],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=1,
		max_value=50,
		min_max_interval=1,
                ),
        Attribute(
                name="Ladder_Price",
                addresses=[0x1e21],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=1,
		max_value=50,
		min_max_interval=1,
                ),
        Attribute(
                name="Potion_Price",
                addresses=[0x1e61],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=1,
		max_value=50,
		min_max_interval=1,
                ),
        Attribute(
                name="Chain_Price",
                addresses=[0x1de5],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=1,
		max_value=70,
		min_max_interval=1,
                ),
        Attribute(
                name="SmallSpear_Price",
                addresses=[0x1dc9],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=1,
		max_value=80,
		min_max_interval=1,
                ),
        Attribute(
                name="HardShield_Price",
                addresses=[0x1e01],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=1,
		max_value=150,
		min_max_interval=1,
                ),
        Attribute(
                name="ShelldShield_Price",
                addresses=[0x1e05],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=1,
		max_value=200,
		min_max_interval=1,
                ),
        Attribute(
                name="HolyWater_Price",
                addresses=[0x1e65],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=1,
		max_value=200,
		min_max_interval=1,
                ),
        Attribute(
                name="HardArmor_Price",
                addresses=[0x1de1],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=1,
		max_value=220,
		min_max_interval=1,
                ),
        Attribute(
                name="Knight_Sword_Price",
                addresses=[0x1db9],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=1,
		max_value=250,
		min_max_interval=1,
                ),
        Attribute(
                name="Firestorm_Price1",
                addresses=[0x1e30],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=1,
		min_max_interval=1,
                ),
        Attribute(
                name="Firestorm_Price2",
                addresses=[0x1e31],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=1,
		max_value=244,
		min_max_interval=1,
                ),
        Attribute(
                name="Quake_Price1",
                addresses=[0x1e34],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=0,
		max_value=1,
		min_max_interval=1,
                ),
        Attribute(
                name="Quake_Price2",
                addresses=[0x1e35],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=244,
		min_max_interval=1,
                ),
        Attribute(
                name="Thunder_Price1",
                addresses=[0x1e38],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=0,
		max_value=1,
		min_max_interval=1,
                ),
        Attribute(
                name="Thunder_Price2",
                addresses=[0x1e39],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=244,
		min_max_interval=1,
                ),
        Attribute(
                name="Power_Price1",
                addresses=[0x1e3c],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=0,
		max_value=1,
		min_max_interval=1,
                ),
        Attribute(
                name="Power_Price2",
                addresses=[0x1e3d],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=244,
		min_max_interval=1,
                ),
        Attribute(
                name="Shield_Price1",
                addresses=[0x1e340],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=0,
		max_value=1,
		min_max_interval=1,
                ),
        Attribute(
                name="Shield_Price2",
                addresses=[0x1e41],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=244,
		min_max_interval=1,
                ),
        Attribute(
                name="Return_Price1",
                addresses=[0x1e44],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=0,
		max_value=1,
		min_max_interval=1,
                ),
        Attribute(
                name="Return_Price2",
                addresses=[0x1e45],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=244,
		min_max_interval=1,
                ),
        Attribute(
                name="Marine_Price1",
                addresses=[0x1e1c],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=0,
		max_value=1,
		min_max_interval=1,
                ),
        Attribute(
                name="Marine_Price2",
                addresses=[0x1e1d],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=44,
		min_max_interval=1,
                ),
        Attribute(
                name="SteelArmor_Price1",
                addresses=[0x1ddc],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=3,
		min_max_interval=1,
                ),
        Attribute(
                name="SteelArmor_Price2",
                addresses=[0x1ddd],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=32,
		min_max_interval=1,
                ),
        Attribute(
                name="Oasis_Price1",
                addresses=[0x1e18],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=1,
		min_max_interval=1,
                ),
        Attribute(
                name="Oasis_Price2",
                addresses=[0x1e19],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=244,
		max_value=244,
		min_max_interval=1,
                ),
        Attribute(
                name="SteelShield_Price1",
                addresses=[0x1dfc],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=7,
		min_max_interval=1,
                ),
        Attribute(
                name="SteelShield_Price2",
                addresses=[0x1dfd],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=208,
		min_max_interval=1,
                ),
        Attribute(
                name="Ocarina_Price1",
                addresses=[0x1e50],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=0,
		max_value=0,
		min_max_interval=1,
                ),
        Attribute(
                name="Ocarina_Price2",
                addresses=[0x1e51],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=30,
		max_value=30,
		min_max_interval=1,
                ),
        Attribute(
                name="Excalibur_Price1",
                addresses=[0x1db4],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=9,
		min_max_interval=1,
                ),
        Attribute(
                name="Excalibur_Price2",
                addresses=[0x1db5],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=196,
		min_max_interval=1,
                ),
        Attribute(
                name="Elixer_Price1",
                addresses=[0x1e58],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=11,
		min_max_interval=1,
                ),
        Attribute(
                name="Elixer_Price2",
                addresses=[0x1e59],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=184,
		min_max_interval=1,
                ),
        Attribute(
                name="Knight_Shield_Price1",
                addresses=[0x1df8],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=13,
		min_max_interval=1,
                ),
        Attribute(
                name="Knight_Shield_Price2",
                addresses=[0x1df9],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=172,
		min_max_interval=1,
                ),
        Attribute(
                name="Ceramic_Price1",
                addresses=[0x1e14],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=15,
		min_max_interval=1,
                ),
        Attribute(
                name="Ceramic_Price2",
                addresses=[0x1e15],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=160,
		min_max_interval=1,
                ),
        Attribute(
                name="Trident_Price1",
                addresses=[0x1dc4],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=1,
		min_max_interval=1,
                ),
        Attribute(
                name="Trident_Price2",
                addresses=[0x1dc5],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=44,
		max_value=44,
		min_max_interval=1,
                ),
        Attribute(
                name="KnightArmor_Price1",
                addresses=[0x1dd8],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=13,
		min_max_interval=1,
                ),
        Attribute(
                name="KnightArmor_Price2",
                addresses=[0x1dd9],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=136,
		min_max_interval=1,
                ),
        Attribute(
                name="PygmyBoots_Price1",
                addresses=[0x1e2c],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=3,
		max_value=3,
		min_max_interval=1,
                ),
        Attribute(
                name="PygmyBoots_Price2",
                addresses=[0x1e2d],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=232,
		max_value=232,
		min_max_interval=1,
                ),
        Attribute(
                name="HiPotion_Price1",
                addresses=[0x1e68],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=13,
		min_max_interval=1,
                ),
        Attribute(
                name="HiPotion_Price2",
                addresses=[0x1e69],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=136,
		min_max_interval=1,
                ),
        Attribute(
                name="FlameShield_Price1",
                addresses=[0x1df4],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=31,
		min_max_interval=1,
                ),
        Attribute(
                name="FlameShield_Price2",
                addresses=[0x1df5],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=64,
		min_max_interval=1,
                ),
        Attribute(
                name="PygmySword_Price1",
                addresses=[0x1dcc],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=3,
		max_value=3,
		min_max_interval=1,
                ),
        Attribute(
                name="PygmySword_Price2",
                addresses=[0x1dcd],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=232,
		max_value=232,
		min_max_interval=1,
                ),
        Attribute(
                name="BattleSpear_Price1",
                addresses=[0x1dc0],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=27,
		min_max_interval=1,
                ),
        Attribute(
                name="BattleSpear_Price2",
                addresses=[0x1dc1],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=16,
		min_max_interval=1,
                ),
        Attribute(
                name="FlameArmor_Price1",
                addresses=[0x1dd4],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=27,
		min_max_interval=1,
                ),
        Attribute(
                name="FlameArmor_Price2",
                addresses=[0x1dd5],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=16,
		min_max_interval=1,
                ),
        Attribute(
                name="PygmyArmor_Price1",
                addresses=[0x1dec],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=3,
		max_value=3,
		min_max_interval=1,
                ),
        Attribute(
                name="PygmyArmor_Price2",
                addresses=[0x1ded],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=232,
		max_value=232,
		min_max_interval=1,
                ),
        Attribute(
                name="LegendBoots_Price1",
                addresses=[0x1e10],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=19,
		max_value=19,
		min_max_interval=1,
                ),
        Attribute(
                name="LegendBoots_Price2",
                addresses=[0x1e11],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=136,
		max_value=136,
		min_max_interval=1,
                ),
        Attribute(
                name="PygmyShield_Price1",
                addresses=[0x1e0c],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=3,
		max_value=3,
		min_max_interval=1,
                ),
        Attribute(
                name="PygmyShield_Price2",
                addresses=[0x1e0d],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=232,
		max_value=232,
		min_max_interval=1,
                ),
        Attribute(
                name="LegendSword_Price1",
                addresses=[0x1db0],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=29,
		max_value=29,
		min_max_interval=1,
                ),
        Attribute(
                name="LegendSword_Price2",
                addresses=[0x1db1],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=76,
		max_value=76,
		min_max_interval=1,
                ),
        Attribute(
                name="LegendShield_Price1",
                addresses=[0x1df0],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=19,
		max_value=19,
		min_max_interval=1,
                ),
        Attribute(
                name="LegendShield_Price2",
                addresses=[0x1df1],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=136,
		max_value=136,
		min_max_interval=1,
                ),
        Attribute(
                name="LegendArmor_Price1",
                addresses=[0x1dd0],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=19,
		max_value=19,
		min_max_interval=1,
                ),
        Attribute(
                name="LegendArmor_Price2",
                addresses=[0x1dd1],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=136,
		max_value=136,
		min_max_interval=1,
                ),
        Attribute(
                name="Charmstone_Price1",
                addresses=[0x1e53],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=0,
		max_value=0,
		min_max_interval=1,
                ),
        Attribute(
                name="Charmstone_Price2",
                addresses=[0x1e54],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=97,
		max_value=97,
		min_max_interval=1,
                ),
        Attribute(
                name="Charmstone_Price3",
                addresses=[0x1e55],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=168,
		max_value=168,
		min_max_interval=1,
                ),
     
        ###Quality of Life Stuff####
        Attribute(
                name="Openning_Text_Speed",
                addresses=[0x1df28],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[8]
                ),
        Attribute(
                name="Ocarina_Reward_Speed",
                addresses=[0x1e264],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[8] 
                ),
        Attribute(
                name="Ocarina_Speed1",
                addresses=[0x2b91],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0]
                ),
        Attribute(
                name="Ocarina_Speed2",
                addresses=[0x2bab],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0]
                ),
        Attribute(
                name="Ocarina_Speed3",
                addresses=[0x2be7],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0]
                ),
        Attribute(
                name="Ocarina_Speed4",
                addresses=[0x2bc6],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0]
                ),        
        Attribute(
                name="Sphinx_Text_Speed",
                addresses=[0x20086],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[8]
                ),
        Attribute(
                name="Sphinx_Text_Speed2",
                addresses=[0x21427],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[8]
                ),
        Attribute(
                name="Dwarf_Text_Speed",
                addresses=[0x2114A],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[8]
                ),
        Attribute(
                name="Gem_Speed",
                addresses=[0x20E35],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[8]
                ),
        Attribute(
                name="Prince_Speech_Speed_1",
                addresses=[0x20C13],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[8] 
                ),
        Attribute(
                name="Prince_Speech_Speed_2",
                addresses=[0x20CC7],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[8] 
                ),
        Attribute(
                name="SRAM_1",
                addresses=[0x1b2],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[248]
                ),
        Attribute(
                name="SRAM_2",
                addresses=[0x1b3],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32]
                ),
        Attribute(
                name="SRAM_3",
                addresses=[0x1ba],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[3]
                ),
        Attribute(
                name="SRAM_4",
                addresses=[0x1bb],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[255]
                ),        
        Attribute(
                name="Ocarina_Sonia_Check",
                addresses=[0x1e5a7],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[39]                
                ),
        Attribute(
                name="Ocarina_Cave_Sprite",
                addresses=[0x27946],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]                
                ),
        Attribute(
                name="bat_spawn",
                addresses=[0x2ca05],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[39]
                ),
        Attribute(
                name="First_Money_Control",
                addresses=[0xa75f],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0] 
                ),
        Attribute(
                name="Legend_Sword_Control",
                addresses=[0x1ece4],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[39] 
                ),
        ###Sprites####
        Attribute(
                name="Leather_Boots_Sprite",
                addresses=[0x22b08],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),
        Attribute(
                name="Medecine_Sprite",
                addresses=[0x22b62],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),
        Attribute(
                name="Small_Spear_Sprite",
                addresses=[0x22b36],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),
        Attribute(
                name="Chailmail_Sprite",
                addresses=[0x22b3c],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),
        Attribute(
                name="Wood_Shield",
                addresses=[0x22b42],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),
        Attribute(
                name="Excalibur_Sprite",
                addresses=[0x22b8a],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),
        Attribute(
                name="SteelShield_Sprite",
                addresses=[0x22b84],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),
        Attribute(
                name="Knight_Sword_Sprite",
                addresses=[0x22B94],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),
        Attribute(
                name="Hard_Armor_Sprite",
                addresses=[0x22B9A],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),
        Attribute(
                name="Potion_Sprite_Pura",
                addresses=[0x22BDC],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),        
        Attribute(
                name="Charm_sprite",
                addresses=[0x22BE2],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),
        Attribute(
                name="Ladder_Sprite",
                addresses=[0x22BD6],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),
        Attribute(
                name="Marine_Sprite",
                addresses=[0x22C62],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),
        Attribute(
                name="Potion_Sprite_Pad",
                addresses=[0x22C6E],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),  
        Attribute(
                name="Steel_Armor_Sprite",
                addresses=[0x22C4E],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),
        Attribute(
                name="Shell_Shield_Sprite",
                addresses=[0x22C48],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),
        Attribute(
                name="Battle_Spear_Sprite",
                addresses=[0x22d08],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),
        Attribute(
                name="Knight_Armor_Sprite",
                addresses=[0x22d0e],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),
        Attribute(
                name="Ceramic_Boots_Sprite",
                addresses=[0x22CF4],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),
        Attribute(
                name="Knight_Shield_Sprite",
                addresses=[0x22D14],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),
        Attribute(
                name="HolyWater_Sprite",
                addresses=[0x22CEE],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),
        Attribute(
                name="Flame_Shield_Sprite",
                addresses=[0x22C92],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),
        Attribute(
                name="Flame_Armor_Sprite",
                addresses=[0x22C8C],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),
        Attribute(
                name="HiPotion_Sprite",
                addresses=[0x22CAC],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),
        Attribute(
                name="Elixer_Sprite",
                addresses=[0x22CA6],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[78]
                ),
        #### Hints ####
        Attribute(
                name="Poss_Hint_Text1",
                addresses=[0x20ADb],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[80]
                ),
        Attribute(
                name="Poss_Hint_Text2",
                addresses=[0x20ADc],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[111]
                ),
        Attribute(
                name="Poss_Hint_Text3",
                addresses=[0x20ADd],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[115]
                ),
        Attribute(
                name="Poss_Hint_Text4",
                addresses=[0x20ADe],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[101]
                ),
        Attribute(
                name="Poss_Hint_Text5",
                addresses=[0x20ADf],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[105]
                ),
        Attribute(
                name="Poss_Hint_Text6",
                addresses=[0x20Ae0],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[100]
                ),
        Attribute(
                name="Poss_Hint_Text7",
                addresses=[0x20Ae1],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[111]
                ),
        Attribute(
                name="Poss_Hint_Text8",
                addresses=[0x20Ae2],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[110]
                ),
        Attribute(
                name="Poss_Hint_Text9",
                addresses=[0x20Ae3],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32]
                ),
        Attribute(
                name="Poss_Hint_Text10",
                addresses=[0x20Ae4],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[104]
                ),
        Attribute(
                name="Poss_Hint_Text11",
                addresses=[0x20Ae5],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[97]
                ),
        Attribute(
                name="Poss_Hint_Text12",
                addresses=[0x20Ae6],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[115]
                ),
        Attribute(
                name="Poss_Hint_Text13",
                addresses=[0x20Ae7],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32]
                ),
        Attribute(
                name="Poss_Hint_Text14",
                addresses=[0x20Ae8],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[11]
                ),
        Attribute(
                name="Poss_Hint_Text15",
                addresses=[0x20Ae9],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[10]
                ),
        Attribute(
                name="POSS_HINT",
                addresses=[0x20Aea],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,   28,29,
                                 30,31,32,33,34,35,36,37,38,
                                    41,42,43,44,45,46,   48,49,
                                    51,52,53,54,55,56,57,58,59,
                                 64                                 
                                 ]
                ),
        Attribute(
                name="Poss_Hint_Text16",
                addresses=[0x20Aeb],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[12]
                ),
        Attribute(
                name="Poss_Hint_Text17",
                addresses=[0x20Aec],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[2]
                ),
        Attribute(
                name="Poss_Hint_Text18",
                addresses=[0x20Aed],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[5]
                ),
        Attribute(
                name="Poss_Hint_Text19",
                addresses=[0x20Aee],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0]
                ),        
        Attribute(
                name="Sphinx_Hint_Text1",
                addresses=[0x20ac9],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[104]
                ),
        Attribute(
                name="Sphinx_Hint_Text2",
                addresses=[0x20aca],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[97]
                ),
        Attribute(
                name="Sphinx_Hint_Text3",
                addresses=[0x20acb],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[115]
                ),
        Attribute(
                name="Sphinx_Hint_Text4",
                addresses=[0x20acc],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32]
                ),
        Attribute(
                name="Sphinx_Hint_Text5",
                addresses=[0x20acd],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[97]
                ),
        Attribute(
                name="Sphinx_Hint_Text6",
                addresses=[0x20ace],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32]
                ),
        Attribute(
                name="Sphinx_Hint_Text7",
                addresses=[0x20acf],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[11]
                ),
        Attribute(
                name="Sphinx_Hint_Text8",
                addresses=[0x20ad0],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[10]
                ),
        Attribute(
                name="SPHINX_HINT",
                addresses=[0x20ad1],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                 30,31,32,33,34,35,36,37,38,
                                    41,42,43,44,45,46,   48,49,
                                 50,   52,53,54,55,56,57,58,59,
                                 64                                 
                                 ]
                ),
        Attribute(
                name="Sphinx_Hint_Text10",
                addresses=[0x20ad2],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[12]
                ),
        Attribute(
                name="Sphinx_Hint_Text11",
                addresses=[0x20ad3],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[2]
                ),
        Attribute(
                name="Sphinx_Hint_Text12",
                addresses=[0x20ad4],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32]
                ),
        Attribute(
                name="Sphinx_Hint_Text13",
                addresses=[0x20ad5],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32]
                ),
        Attribute(
                name="Sphinx_Hint_Text14",
                addresses=[0x20ad6],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32]
                ),
       Attribute(
                name="Fire_Urn_Text_1",
                addresses=[0x2041e],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[11]
                ),
        Attribute(
                name="Fire_Urn_Text_2",
                addresses=[0x2041f],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[10]
                ),
        Attribute(
                name="Fire_Urn_Text",
                addresses=[0x20420],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4,    6,    8, 9,
                                 10,11,12,13,14,   16,17,18,19,
                                 20,21,22,   24,25,      28,29,
                                 30,   32,33,34,35,36,37,38,
                                    41,42,43,44,45,46,   48,
                                                   56,57,   59,
                                 64                                 
                                 ]
                ),
        Attribute(
                name="Fire_Urn_Text_3",
                addresses=[0x20421],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[12] 
                ),
        Attribute(
                name="Fire_Urn_Text_4",
                addresses=[0x20422],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[2] 
                ),
        Attribute(
                name="Fire_Urn_Text_5",
                addresses=[0x20423],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32] 
                ),
        Attribute(
                name="Fire_Urn_Text_6",
                addresses=[0x20424],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32] 
                ),
        Attribute(
                name="Fire_Urn_Text_7",
                addresses=[0x20425],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32] 
                ),
        ### Sonia and Ocarina ###
        Attribute(
                name="Sonia_Text1",
                addresses=[0x1e731],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[73]
                ),
        Attribute(
                name="Sonia_Text2",
                addresses=[0x1e732],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32]
                ),
        Attribute(
                name="Sonia_Text3",
                addresses=[0x1e733],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[108]
                ),
        Attribute(
                name="Sonia_Text4",
                addresses=[0x1e734],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[111]
                ),
        Attribute(
                name="Sonia_Text5",
                addresses=[0x1e735],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[115]
                ),
        Attribute(
                name="Sonia_Text6",
                addresses=[0x1e736],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[116]
                ),
        Attribute(
                name="Sonia_Text7",
                addresses=[0x1e737],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32]
                ),
        Attribute(
                name="Sonia_Text8",
                addresses=[0x1e738],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[109]
                ),
        Attribute(
                name="Sonia_Text9",
                addresses=[0x1e739],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[121]
                ),
        Attribute(
                name="Sonia_Text10",
                addresses=[0x1e73a],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32]
                ),
        Attribute(
                name="Sonia_Text11",
                addresses=[0x1e73b],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[11]
                ),
        Attribute(
                name="Sonia_Text12",
                addresses=[0x1e73c],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[10]
                ),
        Attribute(
                name="Sonia_Item",
                addresses=[0x1e73d],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                 10,11,12,13,14,15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                 30,31,32,33,34,35,36,37,38,
                                 40,41,42,43,44,45,46,   48,49,
                                 50,51,52,53,54,55,56,57,58,59       
                                 ] 
                ),
        Attribute(
                name="Sonia_Text14",
                addresses=[0x1e73e],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[12] 
                ),
        Attribute(
                name="Sonia_Text15",
                addresses=[0x1e73f],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[2] 
                ),
        Attribute(
                name="Sonia_Text16",
                addresses=[0x1e740],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32] 
                ),
        Attribute(
                name="Sonia_Text17",
                addresses=[0x1e741],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[105] 
                ),
        Attribute(
                name="Sonia_Text18",
                addresses=[0x1e742],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[110] 
                ),
        Attribute(
                name="Sonia_Text19",
                addresses=[0x1e743],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32] 
                ),
        Attribute(
                name="Sonia_Text20",
                addresses=[0x1e744],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[116] 
                ),
        Attribute(
                name="Sonia_Text21",
                addresses=[0x1e745],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[104] 
                ),
        Attribute(
                name="Sonia_Text22",
                addresses=[0x1e746],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[101] 
                ),
        Attribute(
                name="Sonia_Text23",
                addresses=[0x1e747],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32] 
                ),
        Attribute(
                name="Sonia_Text24",
                addresses=[0x1e748],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[99] 
                ),
        Attribute(
                name="Sonia_Text25",
                addresses=[0x1e749],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[97] 
                ),
        Attribute(
                name="Sonia_Text26",
                addresses=[0x1e74a],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[118] 
                ),
        Attribute(
                name="Sonia_Text27",
                addresses=[0x1e74b],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[101] 
                ),
        Attribute(
                name="Sonia_Text28",
                addresses=[0x1e74c],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[46] 
                ),
        Attribute(
                name="Sonia_Text29",
                addresses=[0x1e74d],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[5] 
                ),
        Attribute(
                name="Sonia_Text30",
                addresses=[0x1e74e],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[9] 
                ),
        Attribute(
                name="Sonia_Text31",
                addresses=[0x1e74f],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[9] 
                ),
        Attribute(
                name="Sonia_Text32",
                addresses=[0x1e750],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0] 
                ),
        ### Legend Stuff ###
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
                description="Checks are Different",
                left_side=[ value("Firestorm"),value("Quake"),value("bat_reward"),value("Pygmy_Sword"),value("Pygmy_Armor"),
                            value("Pygmy_Boots"),value("Pygmy_Shield"),value("Sun_Key"),value("Moon_Key"),value("Star_Key"),
                            value("Blue_Gem"),value("Gold_Gem"),value("Thunder"),value("Return"),value("Power"),
                            value("Shield_Magic_Chest"),value("Old_Axe"),value("Fire_Urn"),value("Charmstone_Chest"),value("Hard_Shield"),
                            value("Trident"),value("Oasis_Boots"),value("Amulet"),value("Elixer_Chests"),value("First_Money"),
                            value("Secret_Pyramid_1"),value("Secret_Pyramid_2"),value("Secret_Pyramid_3"),value("Secret_Pyramid_4"),value("Secret_Pyramid_5"),
                            #value("Water_Money_Chest2_Item1"),value("Water_Money_Chest2_Item2"),value("Water_Money_Chest2_Item3"),
                            #value("Water_Money_Chest2_Item4"),value("Water_Money_Chest2_Item5"),value("Water_Money_Chest2_Item6"),
                            #value("Water_Money_Chest3_Item1"),value("Water_Money_Chest3_Item2"),value("Water_Money_Chest3_Item3"),
                            #value("Water_Money_Chest3_Item4"),value("Water_Money_Chest3_Item5"),
                            value("leather_boots"),value("medicine"),value("small_spear"),value("chain_mail"),value("wood_shield"),
                            value("Knight_Sword"),value("Hard_Armor"),value("Charmstone_Purchase"),value("Potion"),value("Ladder_Boots"),
                            value("excalibur"),value("steel_shield"),                           
                            value("Marine_Boots"),value("Shield_Magic_Shop"),value("Shell_Shield"),value("Steel_Armor"),
                            value("Ceramic_Boots"),value("Battle_Spear"),value("Knight_Armor"),value("Knight_Shield"),value("Holy_Water"),
                            value("Flame_Shield"),value("Flame_Armor"),value("Hi_Potion"),value("Elixer_Shop"),
                            value("elder_elixer"),value("elder_firestorm"),
                            value("Legend_Sword"),value("Ocarina_Reward")
                           ],
                rule_type="!=",
                right_side=None
        ),
        Rule(
                description="Trident + Bracelet",
                left_side=[ (value("Pygmy_Sword"),"=",58),(value("Pygmy_Armor"),"=",58),(value("First_Money"),"=",58),
                            (value("Thunder"),"=",58),(value("Amulet"),"=",58),
                            (value("Blue_Gem"),"=",5),(value("Gold_Gem"),"=",5),(value("Pygmy_Boots"),"=",5),
                            (value("Battle_Spear"),"=",5),(value("Ceramic_Boots"),"=",5),(value("Knight_Armor"),"=",5),
                            (value("Knight_Shield"),"=",5),(value("Holy_Water"),"=",5)
                            ],
                rule_type="count",
                right_side=("==",1,"<",2)
        ),
        Rule(
                description="Trident + Oasis",
                left_side=[ (value("Pygmy_Sword"),"=",26),(value("Pygmy_Armor"),"=",26),(value("First_Money"),"=",26),
                            (value("Thunder"),"=",26),(value("Amulet"),"=",26),
                            (value("Shield_Magic_Chest"),"=",5)
                            ],
                rule_type="count",
                right_side=("==",1,"<",2)
        ),
        Rule(
                description="Trident + Lamp",
                left_side=[ (value("Pygmy_Sword"),"=",49),(value("Pygmy_Armor"),"=",49),(value("First_Money"),"=",49),
                            (value("Thunder"),"=",49),(value("Amulet"),"=",49),
                            (value("Hard_Shield"),"=",5),(value("Trident"),"=",5)
                            ],
                rule_type="count",
                right_side=("==",1,"<",2)
        ),
        Rule(
                description="Bracelet + Oasis",
                left_side=[ (value("Shield_Magic_Chest"),"=",58),
                            (value("Blue_Gem"),"=",26),(value("Gold_Gem"),"=",26),(value("Pygmy_Boots"),"=",26),
                            (value("Battle_Spear"),"=",26),(value("Ceramic_Boots"),"=",26),(value("Knight_Armor"),"=",26),
                            (value("Knight_Shield"),"=",26),(value("Holy_Water"),"=",26)
                            ],
                rule_type="count",
                right_side=("==",1,"<",2)
        ),
        Rule(
                description="Bracelet + Lamp",
                left_side=[ (value("Hard_Shield"),"=",58),(value("Trident"),"=",58),
                            (value("Blue_Gem"),"=",49),(value("Gold_Gem"),"=",49),(value("Pygmy_Boots"),"=",49)
                            ],
                rule_type="count",
                right_side=("==",1,"<",2)
        ),
        Rule(
                description="Lamp + Oasis",
                left_side=[ (value("Hard_Shield"),"=",26),(value("Trident"),"=",26),
                            (value("Shield_Magic_Chest"),"=",49)
                            ],
                rule_type="count",
                right_side=("==",1,"<",2)
        ),

        Rule(
                description="Legends are Different",
                left_side=[ value("Legend_Boots"),value("Legend_Sword"),value("Legend_Armor")
                           ],
                rule_type="!=",
                right_side=None
        ),   
        Rule(
                description="Ocarina Sync",
                left_side=[ value("Ocarina_Reward"),value("Ocarina_Text"),value("Sonia_Item")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Fire Urn Hint",
                left_side=[ value("Fire_Urn"),value("Fire_Urn_Text")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Posseidon Hint",
                left_side=[ value("Oasis_Boots"),value("POSS_HINT")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Sphinx Hint",
                left_side=[ value("Star_Key"),value("SPHINX_HINT")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Legend Sword Item",
                left_side=[ value("Legend_Sword"),value("Legend_Item")
                           ],
                rule_type="==",
                right_side=None
        ),
]

Optional_Rulesets = [
        Ruleset(
		name="Difficulty - Very Easy",
		description="First 4 Free Checks - Legend Items",
		rules=[
                        Rule(
				description="Elixer",
				left_side=[value("elder_elixer")],
				rule_type="=",
				right_side=0,
			),
			Rule(
				description="Firestorm",
				left_side=[value("elder_firestorm")],
				rule_type="=",
				right_side=24,
                        ),
                        Rule(
				description="Ocarina",
				left_side=[value("Ocarina_Reward")],
				rule_type="=",
				right_side=8,
                        ),
                        Rule(
				description="Myconid",
				left_side=[value("Firestorm")],
				rule_type="=",
                                right_side=16,
                        ),   
                ],
                must_be_enabled=None,
		must_be_disabled=None,
	),
        Ruleset(
		name="Difficulty - Easy",
		description="First 4 Free Checks - Strong Items",
		rules=[
                        Rule(
				description="Elixer",
				left_side=[value("elder_elixer")],
				rule_type="=",
				right_side=1,
			),
			Rule(
				description="Firestorm",
				left_side=[value("elder_firestorm")],
				rule_type="=",
				right_side=25,
                        ),
                        Rule(
				description="Ocarina",
				left_side=[value("Ocarina_Reward")],
				rule_type="=",
				right_side=10,
                        ),
                        Rule(
				description="Myconid",
				left_side=[value("Firestorm")],
				rule_type="=",
                                right_side=18,
                        ),   
                ],
                must_be_enabled=None,
		must_be_disabled=None,
	),
        
        Ruleset(
		name="Difficulty - Very Hard",
		description="First 4 Free Checks - Junk Items",
		rules=[
                        Rule(
				description="Elixer",
				left_side=[value("elder_elixer")],
				rule_type="=",
				right_side=3,
			),
			Rule(
				description="Firestorm",
				left_side=[value("elder_firestorm")],
				rule_type="=",
				right_side=14,
                        ),
                        Rule(
				description="Ocarina",
				left_side=[value("Ocarina_Reward")],
				rule_type="=",
				right_side=30,
                        ),
                        Rule(
				description="Myconid",
				left_side=[value("Firestorm")],
				rule_type="=",
                                right_side=55,
                        ),   
                ],
                must_be_enabled=None,
		must_be_disabled=None,
	),   
	
]
