        # This is a randomizer file for the Simple Randomizer Maker.
# This file must be named randomizer.py in order to work.
# For more information on what each variable means, see "Readme (Tutorial).md"
# Version 1.1, Updated on 4/19 to fix bat dropping #
# Version 1.2, Updated on 4/26. Prices on some items decreased. #
# Version 1.3, Updated on 5/1. Fixed Heart Check #
# Version 1.4, Updated on 5/4. Added Bracelet and Text #
# Version 1.5, Updated on 5/18. Fixed water logic, updated Prices, added Charm Guy #
# Version 1.6, Updated on 5/30. Fixed Charm text so you can see what you get / Added 4th Water Chest #
# Version 1.7, Updated on 5/31. Pyramid Chest Items #
# Version 1.8, Updated on 6/3. MASSIVE OVERHAUL. SRM does the randomizing, all items in pool, FULL LOGIC IMPLEMENTED #

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
        
        
          
        ### Sphere 0 Checks - 8 (Ocarina) ###
        Attribute(
                name="elder_elixer",
                addresses=[0x1e07f],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                 40,41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58       
                                 ]                                 
                ),
        Attribute(
                name="elder_firestorm",
                addresses=[0x1e08b],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                 40,41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58       
                                 ]   
                ),

        Attribute(
                name="leather_boots",
                addresses=[0x1e239],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                 40,41,42,43,44,45,46                                 
                                 ] 
                ),
        Attribute(
                name="medicine",
                addresses=[0x1e292],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                 40,41,42,43,44,45,46                         
                                 ] 
                ),
        Attribute(
                name="small_spear",
                addresses=[0x1e1c1],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                 40,41,42,43,44,45,46                          
                                 ] 
                ),
        Attribute(
                name="chain_mail",
                addresses=[0x1e1e5],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                 40,41,42,43,44,45,46                           
                                 ] 
                ),
        Attribute(
                name="wood_shield",
                addresses=[0x1e215],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                 40,41,42,43,44,45,46                        
                                 ]  
                ),
        Attribute(
                name="Ocarina_Reward",
                addresses=[0x1e27c],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                 40,41,   43,44,45,         49,
                                 50,51,52,53,54,55,   57,58
                                 ]  
                ),

        
        ### Sphere 0.5 Checks - 14 (No Ocarina) ###
        Attribute(
                name="Heart_Chest",
                addresses=[0xa722],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[  0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Firestorm",
                addresses=[0xa752],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[  0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Knight_Sword",
                addresses=[0x1e1b5],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                          
                                 ] 
                ),
        Attribute(
                name="Hard_Armor",
                addresses=[0x1e1df],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                         
                                 ]
                ),
        Attribute(
                name="Charmstone_Purchase",
                addresses=[0x1e28c],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                          
                                 ]
                ),
        Attribute(
                name="Potion",
                addresses=[0x1e298],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                         
                                 ]
                ),
        Attribute(
                name="Ladder_Boots",
                addresses=[0x1e233],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                          
                                 ]
                ),
        Attribute(
                name="Marine_Boots",
                addresses=[0x1e22d],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                        
                                 ]
                ),
        Attribute(
                name="Shield_Magic_Shop",
                addresses=[0x1e251],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                        
                                 ]
                ),
        Attribute(
                name="Shell_Shield",
                addresses=[0x1e20f],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                         
                                 ]
                ),
        Attribute(
                name="Steel_Armor",
                addresses=[0x1e1d9],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46                      
                                 ]
                ),
        Attribute(
                name="bat_reward",
                addresses=[0x2ca09],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Full_Health_1",
                addresses=[0xA75C],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Quake",
                addresses=[0xA738],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Elixer_Chests",
                addresses=[0xA74C],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        
        ### Sphere 1 Checks - (37) ###
        
        ### Lamp (2) ###        
        Attribute(
                name="Hard_Shield",
                addresses=[0xA74E],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Trident",
                addresses=[0xA756],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[  0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                ]
                ),      
        
        
        ### Trident (24) ###
        Attribute(
                name="First_Money",
                addresses=[0xa75e],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Water_Money_Chest2_Item1",
                addresses=[0xa784],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Water_Money_Chest2_Item2",
                addresses=[0xa786],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),        
        Attribute(
                name="Water_Money_Chest2_Item3",
                addresses=[0xa788],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Water_Money_Chest2_Item4",
                addresses=[0xa78a],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Water_Money_Chest2_Item5",
                addresses=[0xa78c],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Water_Money_Chest2_Item6",
                addresses=[0xa78e],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Water_Money_Chest3_Item1",
                addresses=[0xa790],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Water_Money_Chest3_Item2",
                addresses=[0xa792],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Water_Money_Chest3_Item3",
                addresses=[0xa794],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),        
        Attribute(
                name="Water_Money_Chest3_Item4",
                addresses=[0xa796],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Water_Money_Chest3_Item5",
                addresses=[0xa798],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]             
                ),
        Attribute(
                name="Water_Money_Chest4_Item1",
                addresses=[0xa774],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Water_Money_Chest4_Item2",
                addresses=[0xa776],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Water_Money_Chest4_Item3",
                addresses=[0xa778],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Water_Money_Chest4_Item4",
                addresses=[0xa77a],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Water_Money_Chest4_Item5",
                addresses=[0xa77c],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Water_Money_Chest4_Item6",
                addresses=[0xa77e],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Water_Money_Chest4_Item7",
                addresses=[0xa780],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Water_Money_Chest4_Item8",
                addresses=[0xa782],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Pygmy_Armor",
                addresses=[0xA72A],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Pygmy_Sword",
                addresses=[0xA728],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Amulet",
                addresses=[0xA754],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Thunder",
                addresses=[0xA734],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),

        ### Oasis Boots (3) ###        
        Attribute(
                name="Shield_Magic_Chest",
                addresses=[0xA730],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="excalibur",
                addresses=[0x1e1af],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46
                                 ]
                ),
        Attribute(
                name="steel_shield",
                addresses=[0x1e203],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46
                                 ]
                ),     

        ### Bracelet (8) ###
        Attribute(
                name="Ceramic_Boots",
                addresses=[0x1e221],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46
                                 ]
                ),
        Attribute(
                name="Battle_Spear",
                addresses=[0x1e1bb],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46
                                 ]
                ),
        Attribute(
                name="Knight_Armor",
                addresses=[0x1e1d3],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46
                                 ]
                ),
        Attribute(
                name="Knight_Shield",
                addresses=[0x1e1fd],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46
                                 ]
                ),
        Attribute(
                name="Holy_Water",
                addresses=[0x1e29e],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46
                                 ]
                ),
        Attribute(
                name="Pygmy_Boots",
                addresses=[0xA72E],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Blue_Gem",
                addresses=[0xA744],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Gold_Gem",
                addresses=[0xA746],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),

        ### Sphere 2 Checks - (17) ###

        ### Trident + Amulet (2) ##
        Attribute(
                name="Oasis_Boots",
                addresses=[0xA732],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                    51,52,53,54,55,   57,58,
                                 64
                                 ]
                ),        
        Attribute(
                name="Return",
                addresses=[0xA736],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                    51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),

        ### Trident + Oasis (1) ###
        Attribute(
                name="Sun_Key",
                addresses=[0xA73C],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4,    6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),

        ### Oasis + Sun Key (7) ###
        Attribute(
                name="Moon_Key",
                addresses=[0xA73A],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,   52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Secret_Pyramid_1",
                addresses=[0xa76a],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,   52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Secret_Pyramid_2",
                addresses=[0xa76c],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,   52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Secret_Pyramid_3",
                addresses=[0xa76e],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,   52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Secret_Pyramid_4",
                addresses=[0xa770],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,   52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Secret_Pyramid_5",
                addresses=[0xa772],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,   52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        Attribute(
                name="Star_Key",
                addresses=[0xA73E],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,   52,53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),

        ### Oasis + Moon Key (1) ###
        Attribute(
                name="Pygmy_Shield",
                addresses=[0xA72C],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,   53,54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),

        ### Oasis + Star Key (1) ###
        Attribute(
                name="Power",
                addresses=[0xA750],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,   54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),
        ### Two Charmstones (5) ###
        Attribute(
                name="Charm_Guy_1",
                addresses=[0x1F9FA],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                       42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58
                                 ]                               
                ),
        Attribute(
                name="Charm_Guy_2",
                addresses=[0x1F9FD],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                       42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58
                                 ]                               
                ),
        Attribute(
                name="Charm_Guy_3",
                addresses=[0x1FA00],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                       42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58
                                 ]                                 
                ),
        Attribute(
                name="Charm_Guy_4",
                addresses=[0x1FA03],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                       42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58
                                 ]                                 
                ),
        Attribute(
                name="Charm_Guy_5",
                addresses=[0x1FA06],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                       42,43,44,45,46,      49,
                                 50,51,52,53,54,55,   57,58
                                 ]                                 
                ),

        ### Sphere 3+ (16) Checks ###
        Attribute(
                name="Old_Axe",
                addresses=[0xA758],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,26,27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,53,         57,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]
                ),               
        Attribute(
                name="Flame_Shield",
                addresses=[0x1e1f7],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46
                                 ]
                ),        
        Attribute(
                name="Flame_Armor",
                addresses=[0x1e1cd],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46
                                 ]
                ),        
        Attribute(
                name="Hi_Potion",
                addresses=[0x1e2a4],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46
                                 ]
                ),        
        Attribute(
                name="Elixer_Shop",
                addresses=[0x1e25d],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46
                                 ]
                ),
        Attribute(
                name="Pyramid_Item_1",
                addresses=[0xA712],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6,    8, 9,
                                 10,11,12,13,      16,17,18,19,
                                 20,21,22,   24,25,   27,28,29,
                                       32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,   54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]                                
                ),
        Attribute(
                name="Pyramid_Item_2",
                addresses=[0xA714],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6,    8, 9,
                                 10,11,12,13,      16,17,18,19,
                                 20,21,22,   24,25,   27,28,29,
                                       32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,   54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]                                 
                ),
        Attribute(
                name="Pyramid_Item_3",
                addresses=[0xA716],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6,    8, 9,
                                 10,11,12,13,      16,17,18,19,
                                 20,21,22,   24,25,   27,28,29,
                                       32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,   54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]                                 
                ),
        Attribute(
                name="Pyramid_Item_4",
                addresses=[0xA718],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6,    8, 9,
                                 10,11,12,13,      16,17,18,19,
                                 20,21,22,   24,25,   27,28,29,
                                       32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,   54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]                                 
                ),
        Attribute(
                name="Pyramid_Item_5",
                addresses=[0xA71a],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6,    8, 9,
                                 10,11,12,13,      16,17,18,19,
                                 20,21,22,   24,25,   27,28,29,
                                       32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,   54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]                                 
                ),
        Attribute(
                name="Pyramid_Item_6",
                addresses=[0xA71c],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6,    8, 9,
                                 10,11,12,13,      16,17,18,19,
                                 20,21,22,   24,25,   27,28,29,
                                       32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,   54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]                                  
                ),
        Attribute(
                name="Pyramid_Item_7",
                addresses=[0xA71e],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6,    8, 9,
                                 10,11,12,13,      16,17,18,19,
                                 20,21,22,   24,25,   27,28,29,
                                       32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,   54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]                                  
                ),
        Attribute(
                name="Pyramid_Item_8",
                addresses=[0xA720],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6,    8, 9,
                                 10,11,12,13,      16,17,18,19,
                                 20,21,22,   24,25,   27,28,29,
                                       32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,   54,55,   57,58,
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ]                                 
                ),
        Attribute(
                name="Charmstone_Chest",
                addresses=[0xA740],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6,    8, 9,
                                 10,11,12,13,      16,17,18,19,
                                 20,21,22,   24,25,   27,28,29,
                                       32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,   54,55,   57,58,
                                 64
                                 ] 
                ),
        Attribute(
                name="Fire_Urn",
                addresses=[0xA75A],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6,    8, 9,
                                 10,11,12,13,      16,17,18,19,
                                 20,21,22,   24,25,   27,28,29,
                                       32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,            57,
                                 64
                                 ] 
                ),
        Attribute(
                name="Legend_Sword",
                addresses=[0x1EE29],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,   43,44,45,         49,
                                 50,51,52,   54,55,      58
                                 ]  
                ),

        ### End Game Checks (3) ###
        Attribute(
                name="Legend_Boots",
                addresses=[0xA742],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[    1, 2,    4,    6,    8, 9,
                                 10,11,12,13,      16,17,18,19,
                                 20,21,22,   24,25,   27,28,29,
                                       32,33,34,35,36,37,
                                    41,42,43,44,45,46,
                                     
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ] 
                ),        
        Attribute(
                name="Legend_Shield",
                addresses=[0xA74A],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[    1, 2,    4,    6,    8, 9,
                                 10,11,12,13,      16,17,18,19,
                                 20,21,22,   24,25,   27,28,29,
                                       32,33,34,35,36,37,
                                    41,42,43,44,45,46,
                                     
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ] 
                ),        
        Attribute(
                name="Legend_Armor",
                addresses=[0xA748],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[    1, 2,    4,    6,    8, 9,
                                 10,11,12,13,      16,17,18,19,
                                 20,21,22,   24,25,   27,28,29,
                                       32,33,34,35,36,37,
                                    41,42,43,44,45,46,
                                     
                                 64,
                                 128,130,132,134,136,138,140,
                                 142,144,146,148,150,152,154,156
                                 ] 
                ),


        ### Non-Pool (1) ###
        Attribute(
                name="Bracelet_Item",
                addresses=[0x1f23c],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[ 0, 1, 2,    4, 5, 6, 7, 8, 9,
                                 10,11,12,13,   15,16,17,18,19,
                                 20,21,22,23,24,25,   27,28,29,
                                    31,32,33,34,35,36,37,
                                    41,42,43,44,45,46,      49,
                                 50,51,52,   54,55,   57,58       
                                 ] 
                ),
        

        
        ###Prices####

        ### Weapons 40/100/200/500/2000/5000/750 ###
        Attribute(
                name="SmallSpear_Price",
                addresses=[0x1dc9],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=40,
		max_value=40,
		min_max_interval=1,
                ),
        Attribute(
                name="Knight_Sword_Price",
                addresses=[0x1db9],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=100,
		max_value=100,
		min_max_interval=1,
                ),
        Attribute(
                name="Trident_Price1",
                addresses=[0x1dc4],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=0,
		max_value=0,
		min_max_interval=1,
                ),
        Attribute(
                name="Trident_Price2",
                addresses=[0x1dc5],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=200,
		max_value=200,
		min_max_interval=1,
                ),
        Attribute(
                name="Excalibur_Price1",
                addresses=[0x1db4],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=1,
		min_max_interval=1,
                ),
        Attribute(
                name="Excalibur_Price2",
                addresses=[0x1db5],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=244,
		max_value=244,
		min_max_interval=1,
                ),
        Attribute(
                name="BattleSpear_Price1",
                addresses=[0x1dc0],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=7,
		max_value=7,
		min_max_interval=1,
                ),
        Attribute(
                name="BattleSpear_Price2",
                addresses=[0x1dc1],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=208,
		max_value=208,
		min_max_interval=1,
                ),
        Attribute(
                name="LegendSword_Price1",
                addresses=[0x1db0],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=19,
		max_value=19,
		min_max_interval=1,
                ),
        Attribute(
                name="LegendSword_Price2",
                addresses=[0x1db1],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=136,
		max_value=136,
		min_max_interval=1,
                ),
        Attribute(
                name="PygmySword_Price1",
                addresses=[0x1dcc],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=2,
		max_value=2,
		min_max_interval=1,
                ),
        Attribute(
                name="PygmySword_Price2",
                addresses=[0x1dcd],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=238,
		max_value=238,
		min_max_interval=1,
                ),

        ### Boots 15/25/100/250/1000/4000/750  ###
        Attribute(
                name="LeatherBoots_Price",
                addresses=[0x1e25],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=15,
		max_value=15,
		min_max_interval=1,
                ),
        Attribute(
                name="Ladder_Price",
                addresses=[0x1e21],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=25,
		max_value=25,
		min_max_interval=1,
                ),
        Attribute(
                name="Marine_Price1",
                addresses=[0x1e1c],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=0,
		max_value=0,
		min_max_interval=1,
                ),
        Attribute(
                name="Marine_Price2",
                addresses=[0x1e1d],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=100,
		max_value=100,
		min_max_interval=1,
                ),
        Attribute(
                name="Oasis_Price1",
                addresses=[0x1e18],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=0,
		max_value=0,
		min_max_interval=1,
                ),
        Attribute(
                name="Oasis_Price2",
                addresses=[0x1e19],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=250,
		max_value=250,
		min_max_interval=1,
                ),
        Attribute(
                name="Ceramic_Price1",
                addresses=[0x1e14],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=3,
		max_value=3,
		min_max_interval=1,
                ),
        Attribute(
                name="Ceramic_Price2",
                addresses=[0x1e15],
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
                min_value=15,
		max_value=15,
		min_max_interval=1,
                ),
        Attribute(
                name="LegendBoots_Price2",
                addresses=[0x1e11],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=160,
		max_value=160,
		min_max_interval=1,
                ),
        Attribute(
                name="PygmyBoots_Price1",
                addresses=[0x1e2c],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=2,
		max_value=2,
		min_max_interval=1,
                ),
        Attribute(
                name="PygmyBoots_Price2",
                addresses=[0x1e2d],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=238,
		max_value=238,
		min_max_interval=1,
                ),

        ### Armor 40/100/400/1000/2000/4000/750 ###
        Attribute(
                name="Chain_Price",
                addresses=[0x1de5],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=40,
		max_value=40,
		min_max_interval=1,
                ), 
        Attribute(
                name="HardArmor_Price",
                addresses=[0x1de1],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=100,
		max_value=100,
		min_max_interval=1,
                ),        
        Attribute(
                name="SteelArmor_Price1",
                addresses=[0x1ddc],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=1,
		min_max_interval=1,
                ),
        Attribute(
                name="SteelArmor_Price2",
                addresses=[0x1ddd],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=144,
		max_value=144,
		min_max_interval=1,
                ),
        Attribute(
                name="KnightArmor_Price1",
                addresses=[0x1dd8],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=3,
		max_value=3,
		min_max_interval=1,
                ),
        Attribute(
                name="KnightArmor_Price2",
                addresses=[0x1dd9],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=232,
		max_value=232,
		min_max_interval=1,
                ),
        Attribute(
                name="FlameArmor_Price1",
                addresses=[0x1dd4],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=7,
		max_value=7,
		min_max_interval=1,
                ),
        Attribute(
                name="FlameArmor_Price2",
                addresses=[0x1dd5],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=208,
		max_value=208,
		min_max_interval=1,
                ),
        Attribute(
                name="LegendArmor_Price1",
                addresses=[0x1dd0],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=15,
		max_value=15,
		min_max_interval=1,
                ),
        Attribute(
                name="LegendArmor_Price2",
                addresses=[0x1dd1],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=160,
		max_value=160,
		min_max_interval=1,
                ),
        Attribute(
                name="PygmyArmor_Price1",
                addresses=[0x1dec],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=2,
		max_value=2,
		min_max_interval=1,
                ),
        Attribute(
                name="PygmyArmor_Price2",
                addresses=[0x1ded],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=238,
		max_value=238,
		min_max_interval=1,
                ),  

        ### Shield 10/25/50/500/1000/2000/4000/750 ###
        Attribute(
                name="Wood_Shield_Price",
                addresses=[0x1e09],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=10,
		max_value=10,
		min_max_interval=1,
                ),        
        Attribute(
                name="ShellShield_Price",
                addresses=[0x1e05],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=25,
		max_value=25,
		min_max_interval=1,
                ),               
        Attribute(
                name="HardShield_Price",
                addresses=[0x1e01],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=50,
		max_value=50,
		min_max_interval=1,
                ),
        Attribute(
                name="SteelShield_Price1",
                addresses=[0x1dfc],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=1,
		min_max_interval=1,
                ),
        Attribute(
                name="SteelShield_Price2",
                addresses=[0x1dfd],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=244,
		max_value=244,
		min_max_interval=1,
                ),
        Attribute(
                name="Knight_Shield_Price1",
                addresses=[0x1df8],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=3,
		max_value=3,
		min_max_interval=1,
                ),
        Attribute(
                name="Knight_Shield_Price2",
                addresses=[0x1df9],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=232,
		max_value=232,
		min_max_interval=1,
                ),
        Attribute(
                name="FlameShield_Price1",
                addresses=[0x1df4],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=7,
		max_value=7,
		min_max_interval=1,
                ),
        Attribute(
                name="FlameShield_Price2",
                addresses=[0x1df5],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=208,
		max_value=208,
		min_max_interval=1,
                ),
        Attribute(
                name="LegendShield_Price1",
                addresses=[0x1df0],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=15,
		max_value=15,
		min_max_interval=1,
                ),
        Attribute(
                name="LegendShield_Price2",
                addresses=[0x1df1],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=160,
		max_value=160,
		min_max_interval=1,
                ),
        Attribute(
                name="PygmyShield_Price1",
                addresses=[0x1e0c],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=2,
		max_value=2,
		min_max_interval=1,
                ),
        Attribute(
                name="PygmyShield_Price2",
                addresses=[0x1e0d],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=238,
		max_value=238,
		min_max_interval=1,
                ),
        
        ### Other 30 5/25/100/2000/2000/3000 200 ### 
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
                name="Medecine_Price",
                addresses=[0x1e5d],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=5,
		max_value=5,
		min_max_interval=1,
                ),
        Attribute(
                name="Potion_Price",
                addresses=[0x1e61],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=25,
		max_value=25,
		min_max_interval=1,
                ),
        Attribute(
                name="HolyWater_Price",
                addresses=[0x1e65],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=100,
		max_value=100,
		min_max_interval=1,
                ),        
        Attribute(
                name="HiPotion_Price1",
                addresses=[0x1e68],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=7,
		max_value=7,
		min_max_interval=1,
                ),
        Attribute(
                name="HiPotion_Price2",
                addresses=[0x1e69],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=208,
		max_value=208,
		min_max_interval=1,
                ),
        Attribute(
                name="Elixer_Price1",
                addresses=[0x1e58],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=7,
		max_value=7,
		min_max_interval=1,
                ),
        Attribute(
                name="Elixer_Price2",
                addresses=[0x1e59],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=208,
		max_value=208,
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
                min_value=11,
		max_value=11,
		min_max_interval=1,
                ),
        Attribute(
                name="Charmstone_Price3",
                addresses=[0x1e55],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=184,
		max_value=184,
		min_max_interval=1,
                ),
        Attribute(
                name="Firestorm_Price1",
                addresses=[0x1e30],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=0,
		min_max_interval=1,
                ),
        Attribute(
                name="Firestorm_Price2",
                addresses=[0x1e31],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=200,
		max_value=200,
		min_max_interval=1,
                ),
        Attribute(
                name="Quake_Price1",
                addresses=[0x1e34],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=0,
		max_value=0,
		min_max_interval=1,
                ),
        Attribute(
                name="Quake_Price2",
                addresses=[0x1e35],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=200,
		max_value=200,
		min_max_interval=1,
                ),
        Attribute(
                name="Thunder_Price1",
                addresses=[0x1e38],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=0,
		max_value=0,
		min_max_interval=1,
                ),
        Attribute(
                name="Thunder_Price2",
                addresses=[0x1e39],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=200,
		max_value=200,
		min_max_interval=1,
                ),
        Attribute(
                name="Power_Price1",
                addresses=[0x1e3c],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=0,
		max_value=0,
		min_max_interval=1,
                ),
        Attribute(
                name="Power_Price2",
                addresses=[0x1e3d],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=200,
		max_value=200,
		min_max_interval=1,
                ),
        Attribute(
                name="Shield_Price1",
                addresses=[0x1e40],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=0,
		max_value=0,
		min_max_interval=1,
                ),
        Attribute(
                name="Shield_Price2",
                addresses=[0x1e41],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=200,
		max_value=200,
		min_max_interval=1,
                ),
        Attribute(
                name="Return_Price1",
                addresses=[0x1e44],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=0,
		max_value=0,
		min_max_interval=1,
                ),
        Attribute(
                name="Return_Price2",
                addresses=[0x1e45],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=200,
		max_value=200,
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
                name="Gem_Speed_1",
                addresses=[0x20E35],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[8]
                ),
        Attribute(
                name="Gem_Speed_2",
                addresses=[0x20DD0],
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
                name="Prince_Speech_Speed_3",
                addresses=[0x20CFE],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[8] 
                ),
        Attribute(
                name="Ice_Speed_1",
                addresses=[0x205E9],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[8] 
                ),
        Attribute(
                name="Ice_Speed_2",
                addresses=[0x2060A],
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
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1                
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
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Medecine_Sprite",
                addresses=[0x22b62],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Small_Spear_Sprite",
                addresses=[0x22b36],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Chailmail_Sprite",
                addresses=[0x22b3c],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Wood_Shield_Sprite",
                addresses=[0x22b42],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        
        Attribute(
                name="Excalibur_Sprite",
                addresses=[0x22b8a],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="SteelShield_Sprite",
                addresses=[0x22b84],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Knight_Sword_Sprite",
                addresses=[0x22B94],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Hard_Armor_Sprite",
                addresses=[0x22B9A],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Potion_Sprite_Pura",
                addresses=[0x22BDC],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Potion_Sprite_Pura2",
                addresses=[0x22BF4],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),        
        Attribute(
                name="HolyWater_Sprite2",
                addresses=[0x22BEE],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Charm_sprite",
                addresses=[0x22BE2],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Charm_sprite_2",
                addresses=[0x22BFA],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Ladder_Sprite",
                addresses=[0x22BD6],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Marine_Sprite",
                addresses=[0x22C62],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Shield_Sprite",
                addresses=[0x22C68],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Potion_Sprite_Pad",
                addresses=[0x22C6E],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),  
        Attribute(
                name="Steel_Armor_Sprite",
                addresses=[0x22C4E],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Shell_Shield_Sprite",
                addresses=[0x22C48],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Battle_Spear_Sprite",
                addresses=[0x22d08],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Knight_Armor_Sprite",
                addresses=[0x22d0e],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Ceramic_Boots_Sprite",
                addresses=[0x22CF4],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Knight_Shield_Sprite",
                addresses=[0x22D14],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="HolyWater_Sprite",
                addresses=[0x22CEE],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),        
        Attribute(
                name="Flame_Shield_Sprite",
                addresses=[0x22C92],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Flame_Armor_Sprite",
                addresses=[0x22C8C],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="HiPotion_Sprite",
                addresses=[0x22CAC],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Elixer_Sprite",
                addresses=[0x22CA6],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        #### Text Changes ####
        Attribute(
                name="Blacksmith_1",
                addresses=[0x1ED6C],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[11]
                ),
        Attribute(
                name="Blacksmith_2",
                addresses=[0x1ED6D],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[10]
                ),
        Attribute(
                name="Blacksmith_ITEM",
                addresses=[0x1ED6E],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Blacksmith_3",
                addresses=[0x1ED6F],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[12] 
                ),
        Attribute(
                name="Blacksmith_4",
                addresses=[0x1ED70],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[2] 
                ),
        Attribute(
                name="Blacksmith_5",
                addresses=[0x1ED71],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[33] 
                ),
        Attribute(
                name="Blacksmith_6",
                addresses=[0x1ED72],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32] 
                ),
        Attribute(
                name="Blacksmith_7",
                addresses=[0x1ED73],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32] 
                ),
        Attribute(
                name="Blacksmith_8",
                addresses=[0x1ED74],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32] 
                ),
        Attribute(
                name="Blacksmith_9",
                addresses=[0x1ED75],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32] 
                ),
        Attribute(
                name="Blacksmith_10",
                addresses=[0x1ED76],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32] 
                ),
        Attribute(
                name="Blacksmith_11",
                addresses=[0x1ED77],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32] 
                ),
        Attribute(
                name="Blacksmith_12",
                addresses=[0x1ED78],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32] 
                ),
        Attribute(
                name="Blacksmith_13",
                addresses=[0x1ED79],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32] 
                ),
        Attribute(
                name="Blacksmith_14",
                addresses=[0x1ED7a],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32] 
                ),
        Attribute(
                name="Blacksmith_15",
                addresses=[0x1ED7b],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32] 
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
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
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
        Attribute(
                name="Legend_Sword_Text_5",
                addresses=[0x1EE13],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32] 
                ),
        Attribute(
                name="Legend_Sword_Text_6",
                addresses=[0x1EE14],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[105] 
                ),
        Attribute(
                name="Legend_Sword_Text_7",
                addresses=[0x1EE15],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[115] 
                ),
        Attribute(
                name="Legend_Sword_Text_8",
                addresses=[0x1EE16],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32] 
                ),
        Attribute(
                name="Legend_Sword_Text_9",
                addresses=[0x1EE17],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[100] 
                ),
        Attribute(
                name="Legend_Sword_Text_10",
                addresses=[0x1EE18],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[111] 
                ),
        Attribute(
                name="Legend_Sword_Text_11",
                addresses=[0x1EE19],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[110] 
                ),
        Attribute(
                name="Legend_Sword_Text_12",
                addresses=[0x1EE1A],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[101] 
                ),
        Attribute(
                name="Legend_Sword_Text_13",
                addresses=[0x1EE1B],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[33] 
                ),
        Attribute(
                name="Ocarina_Text",
                addresses=[0x1e277],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1 
                ),    
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
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
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
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
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
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
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
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
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
        ### Bracelet Stuff ###
        Attribute(
                name="Bracelet_Control",
                addresses=[0x1f237],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[59]
                ),    
        Attribute(
                name="Bracelet_Text1",
                addresses=[0x1f25B],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[11
                                 ]
                ),
        Attribute(
                name="Bracelet_Text2",
                addresses=[0x1f25C],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[10
                                 ]
                ),
        Attribute(
                name="Bracelet_Text",
                addresses=[0x1f25D],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Bracelet_Text5",
                addresses=[0x1f25E],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[12]
                ),
        Attribute(
                name="Bracelet_Text6",
                addresses=[0x1f25F],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[2]
                ),
        Attribute(
                name="Bracelet_Text7",
                addresses=[0x1f260],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32] 
                ),
        Attribute(
                name="Bracelet_Text8",
                addresses=[0x1f261],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[5] 
                ),
        Attribute(
                name="Bracelet_Text9",
                addresses=[0x1f262],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0] 
                ),
        
        Attribute(
                name="Charm_Text1",
                addresses=[0x1f9C2],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[105] 
                ),
        Attribute(
                name="Charm_Text2",
                addresses=[0x1f9C3],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[116] 
                ),
        Attribute(
                name="Charm_Text3",
                addresses=[0x1f9C4],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[101] 
                ),
        Attribute(
                name="Charm_Text4",
                addresses=[0x1f9C5],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[109] 
                ),
        Attribute(
                name="Charm_Text5",
                addresses=[0x1f9C6],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[115] 
                ),
        Attribute(
                name="Charm_Text6",
                addresses=[0x1f9C7],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[63] 
                ),
        Attribute(
                name="Charm_Text7",
                addresses=[0x1f9C8],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32] 
                ),
        
        Attribute(
                name="Charm_Items_1",
                addresses=[0x1f9D7],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[11] 
                ),
        Attribute(
                name="Charm_Items_2",
                addresses=[0x1f9D8],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[10] 
                ),
        Attribute(
                name="Charm_Items_3",
                addresses=[0x1f9D9],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=None,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Charm_Items_4",
                addresses=[0x1f9Da],
                number_of_bytes=1,
                is_little_endian=False,
		possible_values=[12] 
                ),
        Attribute(
                name="Charm_Items_5",
                addresses=[0x1f9Db],
                number_of_bytes=1,
                is_little_endian=False,
		possible_values=[2] 
                ),
        Attribute(
                name="Charm_Items_6",
                addresses=[0x1f9Dc],
                number_of_bytes=1,
                is_little_endian=False,
		possible_values=[32] 
                ),
        Attribute(
                name="Charm_Items_7",
                addresses=[0x1f9Dd],
                number_of_bytes=1,
                is_little_endian=False,
		possible_values=[11] 
                ),
        Attribute(
                name="Charm_Items_8",
                addresses=[0x1f9De],
                number_of_bytes=1,
                is_little_endian=False,
		possible_values=[10] 
                ),
        Attribute(
                name="Charm_Items_9",
                addresses=[0x1f9Df],
                number_of_bytes=1,
                is_little_endian=False,
		min_value=0,
		max_value=100,
		min_max_interval=1
                ),
        Attribute(
                name="Charm_Items_10",
                addresses=[0x1f9e0],
                number_of_bytes=1,
                is_little_endian=False,
		possible_values=[12] 
                ),
        Attribute(
                name="Charm_Items_11",
                addresses=[0x1f9e1],
                number_of_bytes=1,
                is_little_endian=False,
		possible_values=[2] 
                ),
        Attribute(
                name="Charm_Items_12",
                addresses=[0x1f9e2],
                number_of_bytes=1,
                is_little_endian=False,
		possible_values=[32] 
                ),
        Attribute(
                name="Charm_Items_13",
                addresses=[0x1f9e3],
                number_of_bytes=1,
                is_little_endian=False,
		possible_values=[11]
                ),
        Attribute(
                name="Charm_Items_14",
                addresses=[0x1f9e4],
                number_of_bytes=1,
                is_little_endian=False,
		possible_values=[10] 
                ),
        Attribute(
                name="Charm_Items_15",
                addresses=[0x1f9e5],
                number_of_bytes=1,
                is_little_endian=False,
		min_value=0,
		max_value=100,
		min_max_interval=1 
                ),
        Attribute(
                name="Charm_Items_16",
                addresses=[0x1f9e6],
                number_of_bytes=1,
                is_little_endian=False,
		possible_values=[12] 
                ),
        Attribute(
                name="Charm_Items_17",
                addresses=[0x1f9e7],
                number_of_bytes=1,
                is_little_endian=False,
		possible_values=[2] 
                ),
        Attribute(
                name="Charm_Items_18",
                addresses=[0x1f9e8],
                number_of_bytes=1,
                is_little_endian=False,
		possible_values=[32] 
                ),
        Attribute(
                name="Charm_Items_19",
                addresses=[0x1f9e9],
                number_of_bytes=1,
                is_little_endian=False,
		possible_values=[11] 
                ),
        Attribute(
                name="Charm_Items_20",
                addresses=[0x1f9ea],
                number_of_bytes=1,
                is_little_endian=False,
		possible_values=[10] 
                ),
        Attribute(
                name="Charm_Items_21",
                addresses=[0x1f9eb],
                number_of_bytes=1,
                is_little_endian=False,
		min_value=0,
		max_value=100,
		min_max_interval=1  
                ),
        Attribute(
                name="Charm_Items_22",
                addresses=[0x1f9ec],
                number_of_bytes=1,
                is_little_endian=False,
		possible_values=[12] 
                ),
        Attribute(
                name="Charm_Items_23",
                addresses=[0x1f9ed],
                number_of_bytes=1,
                is_little_endian=False,
		possible_values=[2] 
                ),

        Attribute(
                name="Charm_Items_24",
                addresses=[0x1fA09],
                number_of_bytes=1,
                is_little_endian=False,
		possible_values=[11] 
                ),
        Attribute(
                name="Charm_Items_25",
                addresses=[0x1fA0a],
                number_of_bytes=1,
                is_little_endian=False,
		possible_values=[10] 
                ),
        Attribute(
                name="Charm_Items_26",
                addresses=[0x1fA0b],
                number_of_bytes=1,
                is_little_endian=False,
		min_value=0,
		max_value=100,
		min_max_interval=1  
                ),
        Attribute(
                name="Charm_Items_27",
                addresses=[0x1fA0c],
                number_of_bytes=1,
                is_little_endian=False,
		possible_values=[12] 
                ),
        Attribute(
                name="Charm_Items_28",
                addresses=[0x1fA0d],
                number_of_bytes=1,
                is_little_endian=False,
		possible_values=[2] 
                ),
        
]
Required_Rules = [
        Rule(
                description="Ocarina Sync",
                left_side=[ value("Ocarina_Reward"),value("Ocarina_Text"),value("Sonia_Item"),value("Ocarina_Cave_Sprite")
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
                left_side=[ value("Charmstone_Chest"),value("SPHINX_HINT")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Legend Sword Item",
                left_side=[ value("Legend_Sword"),value("Legend_Item"),value("Blacksmith_ITEM")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Bracelt Sync",
                left_side=[ value("Bracelet_Text"),value("Bracelet_Item")
                           ],
                rule_type="==",
                right_side=None
        ),

        Rule(
                description="Leather_Boots Sprite_Match",
                left_side=[ value("leather_boots"),value("Leather_Boots_Sprite")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Medecine Sprite_Match",
                left_side=[ value("medicine"),value("Medecine_Sprite")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Small_Spear Sprite_Match",
                left_side=[ value("Small_Spear_Sprite"),value("small_spear")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Chain_Mail Sprite_Match",
                left_side=[ value("Chailmail_Sprite"),value("chain_mail")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Wood_Shield Sprite_Match",
                left_side=[ value("Wood_Shield_Sprite"),value("wood_shield")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Excalibur Sprite_Match",
                left_side=[ value("Excalibur_Sprite"),value("excalibur")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Steel Shield Sprite_Match",
                left_side=[ value("SteelShield_Sprite"),value("steel_shield")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Knight Sword Sprite_Match",
                left_side=[ value("Knight_Sword_Sprite"),value("Knight_Sword")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Hard Armor Sprite_Match",
                left_side=[ value("Hard_Armor_Sprite"),value("Hard_Armor")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Potion Sprite_Match",
                left_side=[ value("Potion_Sprite_Pura"),value("Potion_Sprite_Pad"),
                            value("Potion_Sprite_Pura2"),value("Potion")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Charmstone Sprite_Match",
                left_side=[ value("Charm_sprite"),value("Charm_sprite_2"),
                            value("Charmstone_Purchase")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Ladder Sprite_Match",
                left_side=[ value("Ladder_Sprite"),value("Ladder_Boots")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Marine Sprite_Match",
                left_side=[ value("Marine_Sprite"),value("Marine_Boots")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Shield Sprite_Match",
                left_side=[ value("Shield_Sprite"),value("Shield_Magic_Shop")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Steel Armor Sprite_Match",
                left_side=[ value("Steel_Armor_Sprite"),value("Steel_Armor")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Shell Shield Sprite_Match",
                left_side=[ value("Shell_Shield_Sprite"),value("Shell_Shield")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Battle Spear Sprite_Match",
                left_side=[ value("Battle_Spear_Sprite"),value("Battle_Spear")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Knight_Armor_Sprite Sprite_Match",
                left_side=[ value("Knight_Armor_Sprite"),value("Knight_Armor")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Ceramic_Boots_Sprite Sprite_Match",
                left_side=[ value("Ceramic_Boots_Sprite"),value("Ceramic_Boots")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Knight_Shield_Sprite Sprite_Match",
                left_side=[ value("Knight_Shield_Sprite"),value("Knight_Shield")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="HolyWater_Sprite Sprite_Match",
                left_side=[ value("HolyWater_Sprite"),value("HolyWater_Sprite2"),
                            value("Holy_Water")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Flame_Shield_Sprite Sprite_Match",
                left_side=[ value("Flame_Shield_Sprite"),value("Flame_Shield")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Flame_Armor_Sprite Sprite_Match",
                left_side=[ value("Flame_Armor_Sprite"),value("Flame_Armor")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="HiPotion_Sprite Sprite_Match",
                left_side=[ value("HiPotion_Sprite"),value("Hi_Potion")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Elixer_Sprite Sprite_Match",
                left_side=[ value("Elixer_Sprite"),value("Elixer_Shop")
                           ],
                rule_type="==",
                right_side=None
        ),

        Rule(
                description="Charm_1_Match",
                left_side=[ value("Charm_Guy_1"),value("Charm_Items_3")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Charm_2_Match",
                left_side=[ value("Charm_Guy_2"),value("Charm_Items_9")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Charm_3_Match",
                left_side=[ value("Charm_Guy_3"),value("Charm_Items_15")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Charm_4_Match",
                left_side=[ value("Charm_Guy_4"),value("Charm_Items_21")
                           ],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Charm_5_Match",
                left_side=[ value("Charm_Guy_5"),value("Charm_Items_26")
                           ],
                rule_type="==",
                right_side=None
        ),

        

]

Optional_Rulesets = [
   
	
]
