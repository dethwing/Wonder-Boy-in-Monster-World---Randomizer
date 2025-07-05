# Wonder-Boy-in-Monster-World---Randomizer
Randomizer for the Genesis Classic, Wonder Boy 5 (Monster World 3)

First of all, I want to say huge thanks to both Mode8fx and PaddyCo for making this project possible.

In case you don't know, Mode8fx created the program "Simple Randomizer Maker" which is incredibly easy to use. All you need is the hex addresses and values and the program does the rest.
I've uploaded it as part of the repository, but you can also find it here : https://github.com/Mode8fx/SimpleRandomizerMaker

Update : To make certain things work, I needed to directly edit the SRM file. So use the one listed here, rather than the other one. 


In addition, I couldn't have made any progress without the ground work that PaddyCo laid out. He started this project over 4 years ago and provided me with the addresses for around 10 checks, along with all the values.
Using his framework and a hex editor, I was able to deduce all of the remaining checks.
You can find his work here : https://github.com/PaddyCo/mw3rando


With that out of the way, here's what this randomizer does and does not do.

There are currently 96 objcets randomized in the "Pool". They are :

(1). All 25 Shop Items. Non-Equippable items such as Keys cost billions of coins, and adjusting their prices causes the game to crash. So they cannot be found in Shops. All other equippable items can be found in shops. This includes Ocarina, Trident, Oasis Boots, Pygmy Items, Legend Items, and Spells. It does not include a Heart.

(2). The "Elder" items at the beginning of the game. These can be any item, except for a Heart.

(3). The "Sonia" item, left in the cave. This can be any item, except for a heart.

(4). The "Blacksmith" item (Legend Sword in Vanilla). This can be any item, except for a heart. 

(5). The Charmstone Items [For TWO Charmstones. One still gives you a heart]. These can be any items, except for a heart.

(5). 62 Chest items. This includes all 4 water money chests. (They have 1, 5, 6, and 8 Items respectively). This also includes the pyramid money chests. They have 8 items. 

Full List :

"Heart_Chests","Firestorm","Quake","bat_reward","Pygmy_Sword","Pygmy_Armor","Pygmy_Boots","Pygmy_Shield",                                        "Sun_Key","Moon_Key","Star_Key","Blue_Gem","Gold_Gem","Thunder","Return","Power","Shield_Magic_Chest","Old_Axe","Fire_Urn","Charmstone_Chest","Hard_Shield",
"Trident","Oasis_Boots","Amulet","Elixer_Chests","First_Money","Secret_Pyramid_1",
"Secret_Pyramid_2","Secret_Pyramid_3","Secret_Pyramid_4","Secret_Pyramid_5",
"Full_Health_1","Legend_Shield","Legend_Armor","Legend_Boots",
"Water_Money_Chest3_Item1","Water_Money_Chest3_Item2","Water_Money_Chest3_Item3","Water_Money_Chest3_Item4","Water_Money_Chest3_Item5",
Water_Money_Chest2_Item1","Water_Money_Chest2_Item2","Water_Money_Chest2_Item3","Water_Money_Chest2_Item4","Water_Money_Chest2_Item5","Water_Money_Chest2_Item6",
"Water_Money_Chest4_Item1","Water_Money_Chest4_Item2","Water_Money_Chest4_Item3","Water_Money_Chest4_Item4","Water_Money_Chest4_Item5","Water_Money_Chest4_Item6", "Water_Money_Chest4_Item7","Water_Money_Chest4_Item8",
'Pyramid_Item_1','Pyramid_Item_2','Pyramid_Item_3','Pyramid_Item_4','Pyramid_Item_5','Pyramid_Item_6','Pyramid_Item_7','Pyramid_Item_8'

*The Bracelet item is bugged, and does not work if you USE the bracelet before talking to the Elder Dragon. His item is completed random and may be a duplicate of something you already have.
*It will never be -needed- to beat the game, but it might be helpful. 

The item pool consists of a corresponding 96 items.

(1). All equipment except for the starting items. -- 29

(2). 3 Fire Storm, 3 Thunder, 3 Quake, 2 Shield, 2 Power, 1 Return -- 14 Spells

(3). 1 of each Potion, 2 Elixers. Both Hi-Potion and Elixer are guaranteed to take a shop-slot so you can refill before Biomeka. --- 6

(4). The Ocarina and Three Charmstones -- 4

(5). Non-Equippable Progression Items (Lamp, Amulet, 3 Keys, 2 Gems, Fire Urn, Bracelet) -- 9

(6). Thirteen Hearts -- 13

(7). Money, small heart, big heart, magic refil -- 21 

"Go-Mode" requirements --
   
      (a). Defeat the ice-bomber. Requires Bracelet and Both-Gems. 
   
      (b). Have access to Begonia. Requires Oasis Boots and Star-Key.
   
      (c). The Fire-Urn. Talk to the Blacksmith.

      (d). Legend Sword, Legend Shield, Legend Armor. (Technically you don't need Shield/Armor, but good luck without 'em)

      (e). In addition, I highly recomend you stock yourself with Power, Elixer, and Hi-Potion.
   
  

If you talk to the Dragon Elder after using the Bracelet to enter Childam, the door back to Purapill will not spawn. You may need to walk back. 


If you find any issues or logical progression problems, please reach out to me.


In addition to the random elements, many Quality of Life improvements are in place. In general, all items are cheaper than they would be in Vanilla, so less grinding is needed. 

Sonia's text synchs with her correpsonding item, so you can skip it if it's useless. The blacksmith's language is also synched, so you know what you're getting.

There are now 9 hints currently in the game. 

At the top of purapill stairs, on the first screen, the lady to the left will hint about the "Leap of Faith". This is the POWER chest.

The lady on the right will hint about the "Trident and Amulet Item". This is the OASIS BOOTS chest.

The wandering Dragon in Begonia will hint about the "Volcano item". This is the FIRE-URN chest. 

The second NPC in Alsedo [Left] hints about a "Sewer" item. This is the "FULL_HEAL" chest.

One NPC in each village will hint a "Charmstone" item. 

As many text speed ups are in place as I could find. The following texts can be skipped by holding C and mashing A : The Intro, Ocarina Activation, The Dwarf, The Sphinx, the Gems, the Ice Melting, and both Prince speaches.

Be very careful when skipping the text with the Sphinx! I'm not responsible if you skip a question! :-P

The Sphinx now contains FIVE random questions! Be careful!

Here's what you'll have to do to run the randomizer :

(1). Put the randomizer.py into the same folder as the SRM and the other python scripts. 

(2). Run the SRM executable. 

(3). Point it at the (Legally Aquired) rom you'll be using. Make sure you're using USA version, not Japanese! I cannot guarantee it will work the same [Though it might!]

(4). Open the output with your emulator. I use fusion, but it should work with any of them. 

(5). In addition to the rom, the program will output a spoiler log, with key items written in english. If you want to know what the other numbers mean, let me know. 

Have fun!
    
