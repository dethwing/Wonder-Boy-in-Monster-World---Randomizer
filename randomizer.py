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
        ### TESTING ###
        
        ### Text Changes ###
        Attribute(
                name="Return_Hint_Text_1",
                addresses=[0x1e88b],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[70]
                ),
        Attribute(
                name="Return_Hint_Text_2",
                addresses=[0x1e88c],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[105]
                ),
        Attribute(
                name="Return_Hint_Text_3",
                addresses=[0x1e88d],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[110]
                ),
        Attribute(
                name="Return_Hint_Text_4",
                addresses=[0x1e88e],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[100]
                ),
        Attribute(
                name="Return_Hint_Text_5",
                addresses=[0x1e88f],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32]
                ),
        Attribute(
                name="Return_Hint_Text_6",
                addresses=[0x1e890],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[11]
                ),
        Attribute(
                name="Return_Hint_Text_7",
                addresses=[0x1e891],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[10]
                ),
        Attribute(
                name="Return_Hint_Text_8",
                addresses=[0x1e892],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[37]
                ),
        Attribute(
                name="Return_Hint_Text_9",
                addresses=[0x1e893],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[12]
                ),
        Attribute(
                name="Return_Hint_Text_10",
                addresses=[0x1e894],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[2]
                ),
        Attribute(
                name="Return_Hint_Text_11",
                addresses=[0x1e895],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32]
                ),
        Attribute(
                name="Return_Hint_Text_12",
                addresses=[0x1e896],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[105]
                ),
        Attribute(
                name="Return_Hint_Text_13",
                addresses=[0x1e897],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[110]
                ),
        Attribute(
                name="Return_Hint_Text_14",
                addresses=[0x1e898],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32]
                ),
        Attribute(
                name="Return_Hint_Text_15",
                addresses=[0x1e899],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[12]
                ),
        Attribute(
                name="Return_Hint",
                addresses=[0x1e89a],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[219,81,95,74,121]
                ),
        Attribute(
                name="Return_Hint_Text_17",
                addresses=[0x1e89b],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[46]
                ),
        Attribute(
                name="Return_Hint_Text_18",
                addresses=[0x1e89c],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[5]
                ),
        Attribute(
                name="Return_Hint_Text_19",
                addresses=[0x1e89d],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[9]
                ),
        Attribute(
                name="Return_Hint_Text_20",
                addresses=[0x1e89e],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[9]
                ),
        Attribute(
                name="Return_Hint_Text_21",
                addresses=[0x1e89f],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0]
                ),
        Attribute(
                name="Amulet_Hint_Text_1",
                addresses=[0x1fd29],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[76]
                ),
        Attribute(
                name="Amulet_Hint_Text_2",
                addresses=[0x1fd2a],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[111]
                ),
        Attribute(
                name="Amulet_Hint_Text_3",
                addresses=[0x1fd2b],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[111]
                ),
        Attribute(
                name="Amulet_Hint_Text_4",
                addresses=[0x1fd2c],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[107]
                ),
        Attribute(
                name="Amulet_Hint_Text_5",
                addresses=[0x1fd2d],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32]
                ),
        Attribute(
                name="Amulet_Hint_Text_6",
                addresses=[0x1fd2e],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[105]
                ),
        Attribute(
                name="Amulet_Hint_Text_7",
                addresses=[0x1fd2f],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[110]
                ),
        Attribute(
                name="Amulet_Hint_Text_8",
                addresses=[0x1fd30],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[32]
                ),
        Attribute(
                name="Amulet_Hint_Text_9",
                addresses=[0x1fd31],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[12]
                ),        
        Attribute(
                name="Amulet_Hint",
                addresses=[0x1fd32],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[219,81,95,74,121]
                ),
        Attribute(
                name="Amulet_Hint_Text_14",
                addresses=[0x1fd33],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[46]
                ),
        Attribute(
                name="Amulet_Hint_Text_15",
                addresses=[0x1fd34],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[5]
                ),
        Attribute(
                name="Amulet_Hint_Text_16",
                addresses=[0x1fd35],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[9]
                ),
        Attribute(
                name="Amulet_Hint_Text_17",
                addresses=[0x1fd36],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[9]
                ),
        Attribute(
                name="Amulet_Hint_Text_18",
                addresses=[0x1fd37],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0]
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
		max_value=200,
		min_max_interval=1,
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
		max_value=200,
		min_max_interval=1,
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
		max_value=4,
		min_max_interval=1,
                ),
        Attribute(
                name="Oasis_Price2",
                addresses=[0x1e19],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=176,
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
                min_value=20,
		max_value=40,
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
		max_value=25,
		min_max_interval=1,
                ),
        Attribute(
                name="Trident_Price2",
                addresses=[0x1dc5],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=100,
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
                min_value=1,
		max_value=13,
		min_max_interval=1,
                ),
        Attribute(
                name="PygmyBoots_Price2",
                addresses=[0x1e2d],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=136,
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
                min_value=1,
		max_value=33,
		min_max_interval=1,
                ),
        Attribute(
                name="PygmySword_Price2",
                addresses=[0x1dcd],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=52,
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
                min_value=1,
		max_value=27,
		min_max_interval=1,
                ),
        Attribute(
                name="PygmyArmor_Price2",
                addresses=[0x1ded],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=16,
		min_max_interval=1,
                ),
        Attribute(
                name="LegendBoots_Price1",
                addresses=[0x1e10],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=27,
		min_max_interval=1,
                ),
        Attribute(
                name="LegendBoots_Price2",
                addresses=[0x1e11],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=16,
		min_max_interval=1,
                ),
        Attribute(
                name="PygmyShield_Price1",
                addresses=[0x1e0c],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=46,
		min_max_interval=1,
                ),
        Attribute(
                name="PygmyShield_Price2",
                addresses=[0x1e0d],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=224,
		min_max_interval=1,
                ),
        Attribute(
                name="LegendSword_Price1",
                addresses=[0x1db0],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=77,
		min_max_interval=1,
                ),
        Attribute(
                name="LegendSword_Price2",
                addresses=[0x1db1],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=88,
		min_max_interval=1,
                ),
        Attribute(
                name="LegendShield_Price1",
                addresses=[0x1df0],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=78,
		min_max_interval=1,
                ),
        Attribute(
                name="LegendShield_Price2",
                addresses=[0x1df1],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=32,
		min_max_interval=1,
                ),
        Attribute(
                name="LegendArmor_Price1",
                addresses=[0x1dd0],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=92,
		min_max_interval=1,
                ),
        Attribute(
                name="LegendArmor_Price2",
                addresses=[0x1dd1],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=248,
		min_max_interval=1,
                ),
        Attribute(
                name="Charmstone_Price1",
                addresses=[0x1e53],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=0,
		max_value=1,
		min_max_interval=1,
                ),
        Attribute(
                name="Charmstone_Price2",
                addresses=[0x1e54],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=161,
		min_max_interval=1,
                ),
        Attribute(
                name="Charmstone_Price3",
                addresses=[0x1e55],
                number_of_bytes=1,
                is_little_endian=False,
                min_value=1,
		max_value=32,
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
                addresses=[0x1e268],
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
                name="Sonia_Text",
                addresses=[0x1e731],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0]
                ),
        Attribute(
                name="Ocarina_Sonia_Check",
                addresses=[0x1e5a7],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[48]                
                ),
        Attribute(
                name="Ocarina_Cave_Sprite",
                addresses=[0x27946],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[96]                
                ),
        Attribute(
                name="bat_spawn",
                addresses=[0x2ca05],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[48]
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
                possible_values=[48] 
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
        ###Elder###
        Attribute(
                name="elder_elixer",
                addresses=[0x1e07f],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,11,12,
                                 13,14,15,16,17,18,19,20,21,
                                 22,23,24,25,26,27,28,29,30,
                                 31,32,33,34,35,36,37,41,42,
                                 43,44,45,46,49,50,51,52,53,
                                 54,55,56,57,58,40]                                 
                ),
        Attribute(
                name="elder_firestorm",
                addresses=[0x1e08b],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,11,12,
                                 13,14,15,16,17,18,19,20,21,
                                 22,23,24,25,26,27,28,29,30,
                                 31,32,33,34,35,36,37,41,42,
                                 43,44,45,46,49,50,51,52,53,
                                 54,55,56,57,58,40]
                ),

        ###Legend Sword###
        Attribute(
                name="Legend_Sword",
                addresses=[0x1EE29],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0,8,16,24]
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
        #        possible_values=[48]
        #        ),
        #Attribute(
        #        name="Bracelet",
        #        addresses=[0x1F23C],
        #        number_of_bytes=1,
        #        is_little_endian=False,
        #        possible_values=[1]
        #        ),
        
        ###Ocarina###
        Attribute(
                name="Ocarina_Text",
                addresses=[0x1e277],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,11,12,
                                 13,14,15,16,17,18,19,20,21,
                                 22,23,24,25,26,27,28,29,30,
                                 31,32,33,34,35,36,37,41,42,
                                 43,44,45,46,49,50,51,52,53,
                                 54,55,56,57,58,40] 
                ),
        Attribute(
                name="Ocarina_Reward",
                addresses=[0x1e27c],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,11,12,
                                 13,14,15,16,17,18,19,20,21,
                                 22,23,24,25,26,27,28,29,30,
                                 31,32,33,34,35,36,37,41,42,
                                 43,44,45,46,49,50,51,52,53,
                                 54,55,56,57,58,40] 
                ),
        
        ###Shops###
        Attribute(
                name="leather_boots",
                addresses=[0x1e239],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46,40] 
                ),
        Attribute(
                name="medicine",
                addresses=[0x1e292],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46,40] 
                ),
        Attribute(
                name="small_spear",
                addresses=[0x1e1c1],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46,40] 
                ),
        Attribute(
                name="chain_mail",
                addresses=[0x1e1e5],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46,40] 
                ),
        Attribute(
                name="wood_shield",
                addresses=[0x1e215],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46,40] 
                ),        
       Attribute(
                name="Knight_Sword",
                addresses=[0x1e1b5],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,
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
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,
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
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,
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
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,
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
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,
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
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,
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
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,
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
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,
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
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,
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
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,
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
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,
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
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,
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
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,
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
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,
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
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,
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
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,
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
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,
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
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,
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
                possible_values=[0,1,2,3,4,5,6,7,8,9,10,
                                 11,12,13,14,15,16,17,18,
                                 19,20,21,22,23,24,25,26,
                                 27,28,29,30,31,32,33,34,
                                 35,36,37,         41,42,
                                 43,44,45,46] 
                ),

        ### Item Tier List ###
        ### PROGRESSION - 15 ###
        ### Tier 1 : Trident, Oasis, Bracelet, Lamp (133 - 154 - 177 - 186)                      - 4
        ### Tier 2 : Pygmy, Keys, Gems, Amulet (135/143/151/159 - 179/180/181 - 182/183 - 178)   - 10
        ### Tier 3 : Fire Urn (185)                                                              - 1

        ### NON-PROGRESSION - 17 ###
        ### Tier 1 : Legend Equipment (128/136/144/154)                                                      - 4
        ### Tier 2 : Spells, Elixer (160/161/162/163/164/165 - 170)                                          - 7
        ### Tier 3 : Heart, Charmstone (192 - 169)                                                           - 2
        ### Tier 4 : Healing Items (171/172/173/174)                                                         - 4

        
                ### Not currently in Use ###
        ### Tier 5 : Battle Spear, Flame Armor, Flame Shield, Ceramic Boots    (132,137,145,153)             - 4        
        ### Junk : Gradius, Cloth Boots, Leather Armor, Old Axe, Rapid Pad, Rod  (131,142,158,176,184,187)   - 6
        
        
                ### Sphere 0 Checks (3 Checks - 4 Prog.)###
        Attribute(
                name="Firestorm",
                addresses=[0xa752],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,154,177,179]
                ),
        Attribute(
                name="bat_reward",
                addresses=[0x2ca09],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,154,177,179]
                ),
        Attribute(
                name="Quake",
                addresses=[0xA738],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,154,177,179]
                ),

        ### Sphere 1 Checks (12 Checks - 14 Prog (No Urn))###


        ### Lamp Checks (3) ###
        Attribute(
                name="Hard_Shield",
                addresses=[0xA74E],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,154,    186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 160,161,162,163,164,165
                                 #131,142,158,176,184,187,
                                 #132,137,145,153
                                 ]
                ),
        Attribute(
                name="Trident",
                addresses=[0xA756],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,154,    186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 160,161,162,163,164,165
                                 #131,142,158,176,184,187,
                                 #132,137,145,153
                                 ]
                ),
        ### Elixer Chest can be accessed in 3 places. One is Sphere 1, and two are Sphere 2. ###
        ### I have chosen to treat it as a Sphere 1, though it can technically have it's own key###
        Attribute(
                name="Elixer_Chests",
                addresses=[0xA74C],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,154,177,186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 160,161,162,163,164,165
                                 #131,142,158,176,184,187,
                                 #132,137,145,153
                                 ]
                ),

        ### Trident Checks (6) ###
        Attribute(
                name="First_Money",
                addresses=[0xa75e],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[    154,177,186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 160,161,162,163,164,165
                                 #131,142,158,176,184,187,
                                 #132,137,145,153
                                ]
                ),        
        #Attribute(
        #        name="Water_Money_Chest2_Item1",
        #        addresses=[0xa784],
        #        number_of_bytes=1,
        #        is_little_endian=False,
        #        possible_values=[    154,177,186,
        #                         178,179,180,181,182,183,
        #                         135,143,151,159,
        #                         160,161,162,163,164,165
        #                         131,142,158,176,184,187,
        #                         132,137,145,153                                
        #                        ] 
        #        ),
        #Attribute(
        #        name="Water_Money_Chest2_Item2",
        #        addresses=[0xa786],
        #        number_of_bytes=1,
        #        is_little_endian=False,
        #        possible_values=[    154,177,186,
        #                         178,179,180,181,182,183,
        #                         135,143,151,159,
        #                         160,161,162,163,164,165
        #                         131,142,158,176,184,187,
        #                         132,137,145,153                                
        #                        ] 
        #        ),        
        #Attribute(
        #        name="Water_Money_Chest2_Item3",
        #        addresses=[0xa788],
        #        number_of_bytes=1,
        #        is_little_endian=False,
        #        possible_values=[    154,177,186,
        #                         178,179,180,181,182,183,
        #                         135,143,151,159,
        #                         160,161,162,163,164,165
        #                         131,142,158,176,184,187,
        #                         132,137,145,153                                
        #                        ] 
        #        ),
        
        #        ),
        #Attribute(
        #        name="Water_Money_Chest2_Item5",
        #        addresses=[0xa78c],
        #        number_of_bytes=1,
        #        is_little_endian=False,
        #        possible_values=[    154,177,186,
        #                         178,179,180,181,182,183,
        #                         135,143,151,159,
        #                         160,161,162,163,164,165
        #                         131,142,158,176,184,187,
        #                         132,137,145,153                                
        #                        ] 
        #        ),
        #Attribute(
        #        name="Water_Money_Chest2_Item6",
        #        addresses=[0xa78e],
        #        number_of_bytes=1,
        #        is_little_endian=False,
        #        possible_values=[    154,177,186,
        #                         178,179,180,181,182,183,
        #                         135,143,151,159,
        #                         160,161,162,163,164,165
        #                         131,142,158,176,184,187,
        #                         132,137,145,153                                
        #                        ] 
        #        ),        
        #Attribute(
        #        name="Water_Money_Chest3_Item1",
        #        addresses=[0xa790],
        #        number_of_bytes=1,
        #        is_little_endian=False,
        #        possible_values=[    154,177,186,
        #                         178,179,180,181,182,183,
        #                         135,143,151,159,
        #                         160,161,162,163,164,165
        #                         131,142,158,176,184,187,
        #                         132,137,145,153                                
        #                        ] 
        #        ),
        #Attribute(
        #        name="Water_Money_Chest3_Item2",
        #        addresses=[0xa792],
        #        number_of_bytes=1,
        #        is_little_endian=False,
        #        possible_values=[    154,177,186,
        #                         178,179,180,181,182,183,
        #                         135,143,151,159,
        #                         160,161,162,163,164,165
        #                         131,142,158,176,184,187,
        #                         132,137,145,153                                
        #                        ] 
        #        ),
        #Attribute(
        #        name="Water_Money_Chest3_Item3",
        #        addresses=[0xa794],
        #        number_of_bytes=1,
        #        is_little_endian=False,
        #        possible_values=[    154,177,186,
        #                         178,179,180,181,182,183,
        #                         135,143,151,159,
        #                         160,161,162,163,164,165
        #                         131,142,158,176,184,187,
        #                         132,137,145,153                                
        #                        ] 
        #        ),        
        #Attribute(
        #        name="Water_Money_Chest3_Item4",
        #        addresses=[0xa796],
        #        number_of_bytes=1,
        #        is_little_endian=False,
        #        possible_values=[    154,177,186,
        #                         178,179,180,181,182,183,
        #                         135,143,151,159,
        #                         160,161,162,163,164,165
        #                         131,142,158,176,184,187,
        #                         132,137,145,153                                
        #                        ] 
        #        ),
        #Attribute(
        #        name="Water_Money_Chest3_Item5",
        #        addresses=[0xa798],
        #        number_of_bytes=1,
        #        is_little_endian=False,
        #        possible_values=[    154,177,186,
        #                         178,179,180,181,182,183,
        #                         135,143,151,159,
        #                         160,161,162,163,164,165
        #                         131,142,158,176,184,187,
        #                         132,137,145,153                                
        #                        ]  
        #        
        #        ), 
        Attribute(
                name="Pygmy_Armor",
                addresses=[0xA72A],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[    154,177,186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 160,161,162,163,164,165
                                 #131,142,158,176,184,187,
                                 #132,137,145,153
                                ]
                ),
        Attribute(
                name="Pygmy_Sword",
                addresses=[0xA728],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[    154,177,186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 160,161,162,163,164,165
                                 #131,142,158,176,184,187,
                                 #132,137,145,153
                                ]
                ),
        Attribute(
                name="Amulet",
                addresses=[0xA754],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[    154,177,186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 160,161,162,163,164,165
                                 #131,142,158,176,184,187,
                                 #132,137,145,153
                                ]
                ),
        Attribute(
                name="Thunder",
                addresses=[0xA734],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[    154,177,186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 160,161,162,163,164,165
                                 #131,142,158,176,184,187,
                                 #132,137,145,153
                                ]
                ),

        ### Oasis Check (1) ###
        Attribute(
                name="Shield_Magic_Chest",
                addresses=[0xA730],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,    177,186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 160,161,162,163,164,165
                                 #131,142,158,176,184,187,
                                 #132,137,145,153
                                ]
                ),

        ### Bracelet Checks (3) ###
        Attribute(
                name="Pygmy_Boots",
                addresses=[0xA72E],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,154,177,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 160,161,162,163,164,165
                                 #131,142,158,176,184,187,
                                 #132,137,145,153
                                 ]
                ),
        Attribute(
                name="Blue_Gem",
                addresses=[0xA744],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,154,177,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 160,161,162,163,164,165
                                 #131,142,158,176,184,187,
                                 #132,137,145,153
                                 ]
                ),
        Attribute(
                name="Gold_Gem",
                addresses=[0xA746],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,154,177,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 160,161,162,163,164,165
                                 #131,142,158,176,184,187,
                                 #132,137,145,153
                                 ]
                ),
        

        
        ### Sphere 2 Checks (12 Checks - 15 Prog)###

        ### Trident + Amulet Checks ###
        Attribute(
                name="Oasis_Boots",
                addresses=[0xA732],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[    154,177,186,
                                     179,180,181,182,183,
                                 135,143,151,159,
                                 185,
                                 160,161,162,163,164,165,
                                 169,170,192,
                                 128,136,144,152]
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
                                 160,161,162,163,164,165,
                                 169,170,192,
                                 173,174]
                ),

        ### Trident + Oasis Check ###
        Attribute(
                name="Sun_Key",
                addresses=[0xA73C],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[        177,186,
                                 178,179,180,181,182,183,
                                 135,143,151,159,
                                 185,
                                 160,161,162,163,164,165,
                                 169,170,192,
                                 173,174]
                ),

        ### Trident + Sun Key Checks ###
        Attribute(
                name="Moon_Key",
                addresses=[0xA73A],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,    177,186,
                                 178,    180,181,182,183,
                                 135,143,151,159,
                                 185,
                                 160,161,162,163,164,165,
                                 169,170,192,
                                 173,174]
                ),
        Attribute(
                name="Secret_Pyramid_1",
                addresses=[0xa76a],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,    177,186,
                                 178,    180,181,182,183,
                                 135,143,151,159,
                                 185,
                                 160,161,162,163,164,165,
                                 169,170,192,
                                 173,174]
                ),
        Attribute(
                name="Secret_Pyramid_2",
                addresses=[0xa76c],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,    177,186,
                                 178,    180,181,182,183,
                                 135,143,151,159,
                                 185,
                                 160,161,162,163,164,165,
                                 169,170,192,
                                 173,174]
                ),
        Attribute(
                name="Secret_Pyramid_3",
                addresses=[0xa76e],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,    177,186,
                                 178,    180,181,182,183,
                                 135,143,151,159,
                                 185,
                                 160,161,162,163,164,165,
                                 169,170,192,
                                 173,174]
                ),
        Attribute(
                name="Secret_Pyramid_4",
                addresses=[0xa770],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,    177,186,
                                 178,    180,181,182,183,
                                 135,143,151,159,
                                 185,
                                 160,161,162,163,164,165,
                                 169,170,192,
                                 173,174]
                ),
        Attribute(
                name="Secret_Pyramid_5",
                addresses=[0xa772],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,    177,186,
                                 178,    180,181,182,183,
                                 135,143,151,159,
                                 185,
                                 160,161,162,163,164,165,
                                 169,170,192,
                                 173,174]
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
                                 160,161,162,163,164,165,
                                 169,170,192,
                                 128,136,144,152]
                ),

        ### Oasis + Moon Key Check ###
        Attribute(
                name="Pygmy_Shield",
                addresses=[0xA72C],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,    177,186,
                                 178,179,    181,182,183,
                                 135,143,151,159,
                                 185,
                                 160,161,162,163,164,165,
                                 169,170,192,
                                 173,174]
                ),

        ### Oasis + Star Key Check ###
        Attribute(
                name="Power",
                addresses=[0xA750],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[133,    177,186,
                                 178,179,180,    182,183,
                                 135,143,151,159,
                                 185,
                                 160,161,162,163,164,165,
                                 169,170,192,
                                 128,136,144,152]
                ),

        ### Sphere 3+ (3 Checks - Fire Urn, Legend Sword and non essentials only)###        
        Attribute(
                name="Old_Axe",
                addresses=[0xA758],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[185,
                                 160,161,162,163,164,165,169,
                                 128,136,144,152,
                                 173,174]
                ),
        
        
        Attribute(
                name="Fire_Urn",
                addresses=[0xA75A],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[185,
                                 160,161,162,163,164,165,169,
                                 128,136,144,152,
                                 173,174]
                ),        
        Attribute(
                name="Charmstone_Chest",
                addresses=[0xA740],
                number_of_bytes=1,
                is_little_endian=False,
                possible_values=[185,
                                 160,161,162,163,164,165,169,
                                 128,136,144,152,
                                 173,174]
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
                description="128+ Scaled are Different",
                left_side=[value("Firestorm"),value("Quake"),value("bat_reward"),value("Pygmy_Sword"),value("Pygmy_Armor"),
                           value("Pygmy_Boots"),value("Pygmy_Shield"),value("Sun_Key"),value("Moon_Key"),value("Star_Key"),
                           value("Blue_Gem"),value("Gold_Gem"),value("Thunder"),value("Return"),value("Power"),value("Shield_Magic_Chest"),
                           value("Old_Axe"),value("Fire_Urn"),value("Charmstone_Chest"),
                           value("Hard_Shield"),value("Trident"),value("Oasis_Boots"),value("Amulet"),
                           value("Elixer_Chests"),value("First_Money"),
                           value("Secret_Pyramid_1"),value("Secret_Pyramid_2"),value("Secret_Pyramid_3"),value("Secret_Pyramid_4"),value("Secret_Pyramid_5")
                           ],
                rule_type="!=",
                right_side=None
        ),

        Rule(
                description="0+ Scaled are Different",
                left_side=[value("leather_boots"),
                           value("medicine"),value("small_spear"),value("chain_mail"),value("wood_shield"),
                           value("Knight_Sword"),value("Hard_Armor"),value("Charmstone_Purchase"),value("Potion"),value("Ladder_Boots"),
                           value("excalibur"),value("steel_shield"),                           
                           value("Marine_Boots"),value("Shield_Magic_Shop"),value("Shell_Shield"),value("Steel_Armor"),
                           value("Ceramic_Boots"),value("Battle_Spear"),value("Knight_Armor"),value("Knight_Shield"),value("Holy_Water"),
                           value("Flame_Shield"),value("Flame_Armor"),value("Hi_Potion"),value("Elixer_Shop"),
                           value("elder_elixer"),value("elder_firestorm"),
                           value("Legend_Sword"),value("Ocarina_Reward")],
                rule_type="!=",
                right_side=None
        ),
        
### Legend Chests ###           
        Rule(
                description="Legends are Different",
                left_side=[value("Legend_Boots"),value("Legend_Shield"),value("Legend_Armor")],
                rule_type="!=",
                right_side=None
        ),

### Ocarina ####
        Rule(
                description="Ocarina Logic",
                left_side=[value("Ocarina_Text"),value("Ocarina_Reward")],
                rule_type="==",
                right_side=None
        ),
        Rule(
                description="Ocarina Logic 2",
                left_side=[value("elder_elixer"),value("elder_firestorm"),value("Ocarina_Reward"),value("leather_boots"),
                           value("medicine"),value("small_spear"),value("chain_mail"),value("wood_shield")],
                rule_type="count",
                right_side=("==",40,"==",1)
        ),

### Legend Sword ###        
        Rule(
                description="Legend Sword Logic",
                left_side=[ value("Old_Axe"),value("Fire_Urn"),value("Charmstone_Chest"),value("Star_Key"),
                            value("Power"),value("Oasis_Boots")     
                           ],
                rule_type="count",
                right_side=("==",128,"==",1)
        ),

### Marine Boots ###
        Rule(
                description="Marine Logic",
                left_side=[value("elder_elixer"),value("elder_firestorm"),value("Ocarina_Reward"),
                           value("leather_boots"),
                           value("medicine"),value("small_spear"),value("chain_mail"),value("wood_shield"),
                           value("Knight_Sword"),value("Hard_Armor"),value("Charmstone_Purchase"),value("Potion"),value("Ladder_Boots"),
                           value("Marine_Boots"),value("Shield_Magic_Shop"),value("Shell_Shield"),value("Steel_Armor"),
                           ],
                rule_type="count",
                right_side=("==",27,"==",1)
        ),

### Health ###
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
				description="Starter_0",
				left_side=[value("elder_elixer"),value("elder_firestorm")],
				rule_type="!=",
				right_side=0,
			),
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
				description="No_0",
				left_side=[value("leather_boots"),
                           value("medicine"),value("small_spear"),value("chain_mail"),value("wood_shield"),
                           value("Knight_Sword"),value("Hard_Armor"),value("Charmstone_Purchase"),value("Potion"),value("Ladder_Boots"),
                           value("excalibur"),value("steel_shield"),                           
                           value("Marine_Boots"),value("Shield_Magic_Shop"),value("Shell_Shield"),value("Steel_Armor"),
                           value("Ceramic_Boots"),value("Battle_Spear"),value("Knight_Armor"),value("Knight_Shield"),value("Holy_Water"),
                           value("Flame_Shield"),value("Flame_Armor"),value("Hi_Potion"),value("Elixer_Shop")],
				rule_type="!=",
				right_side=0,
			),
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
                                            13,6,20,
                                            21,45,12,2,27,
                                            32,33,34,35,36,37,11,26,
                                            19,1,42,
                                            18,25,10,31,46,5,17,7,4,9,15,24,23,
                                            0,16,8,41
                                            ]

			),
                        Rule(
				description="Second Area",
				left_side=[value("medicine"),value("small_spear"),value("chain_mail"),value("wood_shield")],
				rule_type="!=",
				right_side=[
                                        
                                            21,45,12,2,27,
                                            32,33,34,35,36,37,11,26,
                                            19,1,42,
                                            18,25,10,31,46,5,17,7,4,9,15,24,23,
                                            0,16,8,41,
                                            
                                            9,15,24,23,16,8]

			),
                        Rule(
				description="Third Area",
				left_side=[value("Knight_Sword"),value("Hard_Armor"),value("Charmstone_Purchase"),
                                           value("Potion"),value("Ladder_Boots")],
				rule_type="!=",
				right_side=[43,3,30,14,29,28,22,44,

                                            
                                            32,33,34,35,36,37,11,26,
                                            19,1,42,
                                            18,25,10,31,46,5,17,7,4,9,15,24,23,
                                            0,16,8,41
                                            ]

			),
                        Rule(
				description="Fourth Area",
				left_side=[value("Marine_Boots"),value("Shield_Magic_Shop"),
                                           value("Shell_Shield"),value("Steel_Armor")],
				rule_type="!=",
				right_side=[43,3,30,14,29,28,22,44,
                                            13,6,20,

                                            
                                            19,1,42,
                                            18,25,10,31,46,5,17,7,4,9,15,24,23,
                                            0,16,8,41
                                            ]

			),
                        Rule(
				description="Fifth Area",
				left_side=[value("excalibur"),value("steel_shield")],
				rule_type="!=",
				right_side=[43,3,30,14,29,28,22,44,
                                            13,6,20,
                                            21,45,12,2,27,

                                            
                                            18,25,10,31,46,5,17,7,4,9,15,24,23,
                                            0,16,8,41
                                            ]

			),
                        Rule(
				description="Sixth Area",
				left_side=[value("Ceramic_Boots"),value("Battle_Spear"),value("Knight_Armor"),
                                           value("Knight_Shield"),value("Holy_Water")],
				rule_type="!=",
				right_side=[43,3,30,14,29,28,22,44,
                                            13,6,20,
                                            21,45,12,2,27,
                                            32,33,34,35,36,37,11,26,

                                            
                                            0,16,8,41
                                            ]

			),
                        Rule(
				description="Seventh Area",
				left_side=[value("Flame_Shield"),value("Flame_Armor"),
                                           value("Hi_Potion"),value("Elixer_Shop")],
				rule_type="!=",
				right_side=[43,3,30,14,29,28,22,44,
                                            13,6,20,
                                            21,45,12,2,27,
                                            32,33,34,35,36,37,11,26,
                                            19,1,42,

                                            
                                            ]

			),
                ],
                must_be_enabled=None,
		must_be_disabled=None,
        ),
        Ruleset(
		name="Test",
		description="Speed for Test",
		rules=[
                        Rule(
				description="Starter_1",
				left_side=[value("elder_elixer")],
				rule_type="==",
				right_side=0,
			),
                        Rule(
				description="Starter_2",
				left_side=[value("elder_firestorm")],
				rule_type="==",
				right_side=24,
			),
                        Rule(
				description="Myconid",
				left_side=[value("Firestorm")],
				rule_type="==",
				right_side=133,
			),
                        Rule(
                                description="Ocarina",
				left_side=[value("Ocarina_Reward")],
				rule_type="==",
				right_side=27,
			),
                        Rule(
				description="medecine",
				left_side=[value("medicine")],
				rule_type="==",
				right_side=40,
			),

                        
                ],
                must_be_enabled=None,
		must_be_disabled=None,
	),
	Ruleset(
		name="Hints",
		description="Text Changes for Hints",
		rules=[                        
                        Rule(
				description="Sphinx Hint1",
				left_side=[(value("Star_Key"),"=",128),(value("SPHINX_HINT"),"=",0)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint2",
				left_side=[(value("Star_Key"),"=",133),(value("SPHINX_HINT"),"=",5)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint3",
				left_side=[(value("Star_Key"),"=",177),(value("SPHINX_HINT"),"=",49)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint4",
				left_side=[(value("Star_Key"),"=",186),(value("SPHINX_HINT"),"=",58)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint5",
				left_side=[(value("Star_Key"),"=",178),(value("SPHINX_HINT"),"=",50)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint6",
				left_side=[(value("Star_Key"),"=",180),(value("SPHINX_HINT"),"=",52)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint7",
				left_side=[(value("Star_Key"),"=",181),(value("SPHINX_HINT"),"=",53)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint8",
				left_side=[(value("Star_Key"),"=",182),(value("SPHINX_HINT"),"=",54)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint9",
				left_side=[(value("Star_Key"),"=",183),(value("SPHINX_HINT"),"=",55)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint10",
				left_side=[(value("Star_Key"),"=",135),(value("SPHINX_HINT"),"=",7)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint11",
				left_side=[(value("Star_Key"),"=",143),(value("SPHINX_HINT"),"=",15)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint12",
				left_side=[(value("Star_Key"),"=",151),(value("SPHINX_HINT"),"=",23)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint13",
				left_side=[(value("Star_Key"),"=",159),(value("SPHINX_HINT"),"=",31)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint14",
				left_side=[(value("Star_Key"),"=",185),(value("SPHINX_HINT"),"=",57)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint15",
				left_side=[(value("Star_Key"),"=",160),(value("SPHINX_HINT"),"=",32)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint16",
				left_side=[(value("Star_Key"),"=",161),(value("SPHINX_HINT"),"=",33)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint17",
				left_side=[(value("Star_Key"),"=",162),(value("SPHINX_HINT"),"=",34)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint18",
				left_side=[(value("Star_Key"),"=",163),(value("SPHINX_HINT"),"=",35)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint19",
				left_side=[(value("Star_Key"),"=",164),(value("SPHINX_HINT"),"=",36)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint20",
				left_side=[(value("Star_Key"),"=",165),(value("SPHINX_HINT"),"=",37)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint21",
				left_side=[(value("Star_Key"),"=",169),(value("SPHINX_HINT"),"=",41)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint22",
				left_side=[(value("Star_Key"),"=",170),(value("SPHINX_HINT"),"=",42)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint23",
				left_side=[(value("Star_Key"),"=",192),(value("SPHINX_HINT"),"=",64)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint24",
				left_side=[(value("Star_Key"),"=",136),(value("SPHINX_HINT"),"=",8)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint25",
				left_side=[(value("Star_Key"),"=",144),(value("SPHINX_HINT"),"=",16)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Sphinx Hint26",
				left_side=[(value("Star_Key"),"=",152),(value("SPHINX_HINT"),"=",24)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint1",
				left_side=[(value("Oasis_Boots"),"=",128),(value("POSS_HINT"),"=",0)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint2",
				left_side=[(value("Oasis_Boots"),"=",154),(value("POSS_HINT"),"=",26)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint3",
				left_side=[(value("Oasis_Boots"),"=",177),(value("POSS_HINT"),"=",49)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint4",
				left_side=[(value("Oasis_Boots"),"=",186),(value("POSS_HINT"),"=",58)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint5",
				left_side=[(value("Oasis_Boots"),"=",179),(value("POSS_HINT"),"=",51)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint6",
				left_side=[(value("Oasis_Boots"),"=",180),(value("POSS_HINT"),"=",52)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint7",
				left_side=[(value("Oasis_Boots"),"=",181),(value("POSS_HINT"),"=",53)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint8",
				left_side=[(value("Oasis_Boots"),"=",182),(value("POSS_HINT"),"=",54)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint9",
				left_side=[(value("Oasis_Boots"),"=",183),(value("POSS_HINT"),"=",55)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint10",
				left_side=[(value("Oasis_Boots"),"=",135),(value("POSS_HINT"),"=",7)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint11",
				left_side=[(value("Oasis_Boots"),"=",143),(value("POSS_HINT"),"=",15)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint12",
				left_side=[(value("Oasis_Boots"),"=",151),(value("POSS_HINT"),"=",23)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint13",
				left_side=[(value("Oasis_Boots"),"=",159),(value("POSS_HINT"),"=",31)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint14",
				left_side=[(value("Oasis_Boots"),"=",185),(value("POSS_HINT"),"=",57)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint15",
				left_side=[(value("Oasis_Boots"),"=",160),(value("POSS_HINT"),"=",32)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint16",
				left_side=[(value("Oasis_Boots"),"=",161),(value("POSS_HINT"),"=",33)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint17",
				left_side=[(value("Oasis_Boots"),"=",162),(value("POSS_HINT"),"=",34)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint18",
				left_side=[(value("Oasis_Boots"),"=",163),(value("POSS_HINT"),"=",35)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint19",
				left_side=[(value("Oasis_Boots"),"=",164),(value("POSS_HINT"),"=",36)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint20",
				left_side=[(value("Oasis_Boots"),"=",165),(value("POSS_HINT"),"=",37)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint21",
				left_side=[(value("Oasis_Boots"),"=",169),(value("POSS_HINT"),"=",41)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint22",
				left_side=[(value("Oasis_Boots"),"=",170),(value("POSS_HINT"),"=",42)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint23",
				left_side=[(value("Oasis_Boots"),"=",192),(value("POSS_HINT"),"=",64)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint24",
				left_side=[(value("Oasis_Boots"),"=",136),(value("POSS_HINT"),"=",8)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint25",
				left_side=[(value("Oasis_Boots"),"=",144),(value("POSS_HINT"),"=",16)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Poseidon Hint26",
				left_side=[(value("Oasis_Boots"),"=",152),(value("POSS_HINT"),"=",24)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Amulet Hint1",
				left_side=[(value("First_Money"),"=",178),(value("Pygmy_Armor"),"=",178),
                                           (value("Pygmy_Sword"),"=",178),(value("Amulet"),"=",178),(value("Thunder"),"=",178)
                                           ,(value("Amulet_Hint"),"=",219)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Amulet Hint2",
				left_side=[(value("Shield_Magic_Chest"),"=",178),(value("Sun_Key"),"=",178),(value("Power"),"=",178),
                                           (value("Amulet_Hint"),"=",74)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Amulet Hint3",
				left_side=[(value("Star_Key"),"=",178),(value("Moon_Key"),"=",178),(value("Secret_Pyramid_1"),"=",178),
                                           (value("Secret_Pyramid_2"),"=",178),(value("Secret_Pyramid_3"),"=",178),(value("Secret_Pyramid_4"),"=",178),
                                           (value("Secret_Pyramid_5"),"=",178),(value("Pygmy_Shield"),"=",178),
                                           (value("Amulet_Hint"),"=",95)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Amulet Hint5",
				left_side=[(value("Hard_Shield"),"=",178),(value("Elixer_Chests"),"=",178),(value("Trident"),"=",178),
                                           (value("Amulet_Hint"),"=",81)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Amulet Hint6",
				left_side=[(value("Pygmy_Boots"),"=",178),(value("Blue_Gem"),"=",178),(value("Gold_Gem"),"=",178),
                                           (value("Amulet_Hint"),"=",121)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Return_Hint1",
				left_side=[(value("First_Money"),"=",165),(value("Pygmy_Armor"),"=",165),
                                           (value("Pygmy_Sword"),"=",165),(value("Amulet"),"=",165),(value("Thunder"),"=",165),
                                           (value("Oasis_Boots"),"=",165),(value("Return"),"=",165),
                                           (value("Return_Hint"),"=",219)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Return_Hint2",
				left_side=[(value("Shield_Magic_Chest"),"=",165),(value("Sun_Key"),"=",165),(value("Power"),"=",165),
                                           (value("Amulet_Hint"),"=",74)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Return_Hint3",
				left_side=[(value("Star_Key"),"=",165),(value("Moon_Key"),"=",165),(value("Secret_Pyramid_1"),"=",165),
                                           (value("Secret_Pyramid_2"),"=",165),(value("Secret_Pyramid_3"),"=",165),(value("Secret_Pyramid_4"),"=",165),
                                           (value("Secret_Pyramid_5"),"=",165),(value("Pygmy_Shield"),"=",165),(value("Charmstone_Chest"),"=",165),
                                           (value("Return_Hint"),"=",95)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Return_Hint5",
				left_side=[(value("Hard_Shield"),"=",165),(value("Elixer_Chests"),"=",165),(value("Trident"),"=",165),
                                           (value("Return_Hint"),"=",81)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Return_Hint6",
				left_side=[(value("Pygmy_Boots"),"=",165),(value("Blue_Gem"),"=",165),(value("Gold_Gem"),"=",165),(value("Old_Axe"),"=",165),
                                           (value("Return_Hint"),"=",121)],
				rule_type="count",
				right_side=("==",True,"!=",1)
			),
                        Rule(
				description="Return_Hint7",
				left_side=[(value("Fire_Urn"),"=",165),(value("Return_Hint"),"=",121)],
				rule_type="count",
				right_side=("==",True,"!=",222)
			),


                        
                        
                ],
                must_be_enabled=None,
		must_be_disabled=None,
	),
	
]
