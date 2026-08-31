# Wonder-Boy-in-Monster-World---Randomizer
Randomizer for the Genesis Classic, Wonder Boy 5 (Monster World 3)

First of all, I want to say huge thanks to both Mode8fx and PaddyCo for making this project possible.

In case you don't know, Mode8fx created the program "Simple Randomizer Maker" which is incredibly easy to use. All you need is the hex addresses and values and the program does the rest.
I've uploaded it as part of the repository, but you can also find it here : https://github.com/Mode8fx/SimpleRandomizerMaker

Update : To make certain things work, I needed to directly edit the SRM file. So use the one listed here, rather than the one on Mode8FX's Git Hub. 


In addition, I couldn't have made any progress without the ground work that PaddyCo laid out. He started this project over 4 years ago and provided me with the addresses for around 10 checks, along with all the values.
Using his framework and a hex editor, I was able to deduce all of the remaining checks.
You can find his work here : https://github.com/PaddyCo/mw3rando


With that out of the way, here's what this randomizer does and does not do.

There are currently 107 Checks randomized in the "Pool". 
There are two kinds of items. Equipment [Anything that can be found on Equipment screen. Weapons, Armor, Shield, Boots, Spells, Other]
Non-Equipment. [Hearts, Money, Health/Magic Refills]

(1). All 25 Shop Items. Equipment Only

(2). The 2 "Elder" items at the beginning of the game. Equipment Only

(3). The "Sonia" item, left in the cave. Equipment Only

(4). The "Blacksmith" item (Legend Sword in Vanilla). Equipment Only

(5). The "Dragon" item (Bracelet in Vanilla). Equipment Only [The Only "Progression" items it can be is Blue Gem, Gold Gem, and Bracelet] 

(6). The 5 "Charmstone Guy" Items [For TWO Charmstones. One still gives you a heart]. Equipment Only

(7). Sphinx Quiz Bonus. Non-Progression Equipment Only

(8). 3 Initial Equipment items [Weapon/Armor/Boots]

(9). 3 Initial Hearts [Can be Hearts or Random Non-Progression Bonus Items]

(10). Four "Enemy Drop" items. 2nd Dungeon Bat, Three Yetis in Ice Castle Last Room. Can be anything

(11). 61 Chest items. Can be anything

The following checks have been swapped with multi-item chests to increase item balance.

Myconid <-> 5 Item Water Chest 

Gragg and Glagg <-> 6 Item Water Chest

Return Magic <-> 8 Item Water Chest 

This reduces the overall important of Trident and increases the value in other checks. 

The item pool consists of a corresponding 107 items.

One of each Weapon/Armor/Shield/Boots [32]

3 of each spell except for Shield and Return [14] 

5 Charmstones, 3 Elixers, 1 of Each Potion [12]

Progression Items, including Ocarina [10]

Hearts [14]

Money and Refills [24]

Jet Pack [1] (No, Really. I'm serious. But it only does something if you happen to start the game with it)



"Go-Mode" requirements --
   
      (a). Defeat the ice-bomber. Requires Bracelet and Both-Gems. 
   
      (b). Have access to Begonia. Requires Oasis Boots and Star-Key.
   
      (c). The Fire-Urn. 

      (d). Legend Sword, Legend Shield, Legend Armor. (Technically you don't need Shield/Armor, but good luck without 'em)

      (e). In addition, I highly recomend you stock yourself with Power, Thunder, Elixer, and Hi-Potion.
   
  
If you find any issues or logical progression problems, please reach out to me.

In addition to the random elements, many Quality of Life improvements are in place. In general, all items are cheaper than they would be in Vanilla, so less grinding is needed. 

Sonia's text synchs with her corresponding item, so you can skip it if it's useless. The blacksmith's language is also synched, so you know what you're getting.

There are now 9 hints currently in the game. 

At the top of Purapill stairs, on the first screen, the lady to the left will hint about the "Leap of Faith". This is the POWER chest.

The lady on the right will hint about the "Trident and Amulet Item". This is the OASIS BOOTS chest.

The wandering Dragon in Begonia will hint about the "Volcano item". This is the FIRE-URN chest. 

The second NPC in Alsedo [Left] hints about a "Sewer" item. This is the "FULL_HEAL" chest.

One NPC in each village will hint a "Charmstone" item. 

As many text speed ups are in place as I could find. The following texts can be skipped by holding C and mashing A : The Intro, Ocarina Activation, The Dwarf, The Sphinx, the Gems, the Ice Melting, and both Prince speaches.

Be very careful when skipping the text with the Sphinx! I'm not responsible if you skip a question! :-P

The Sphinx now contains 9/10 random questions! Be careful!

Here's what you'll have to do to run the randomizer :

(1). Put the randomizer.py into the same folder as the SRM and the other python scripts. 

(2). Run the SRM executable. 

(3). Point it at the (Legally Aquired) rom you'll be using. Make sure you're using USA version, not Japanese! I cannot guarantee it will work the same [Though it might!]

(4). Open the output with your emulator. I use fusion, but it should work with any of them. 

(5). In addition to the rom, the program will output a spoiler log, with key items written in english. If you want to know what the other numbers mean, let me know. 

Have fun!
    
