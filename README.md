# Wonder-Boy-in-Monster-World---Randomizer
Randomizer for the Genesis Classic, Wonder Boy 5 (Monster World 3)

First of all, I want to say huge thanks to both Mode8fx and PaddyCo for making this project possible.

In case you don't know, Mode8fx created the program "Simple Randomizer Maker" which is incredibly easy to use. All you need is the hex addresses and values and the program does the rest.
I've uploaded it as part of the repository, but you can also find it here : https://github.com/Mode8fx/SimpleRandomizerMaker

Update : To make certain things work, I needed to directly edit the SRM file. So use the one listed here, rather than the other one. 


In addition, I couldn't have made any progress without the ground work that PaddyCo laid out. He started this project over 4 years ago and provided me with the addresses for around 10 checks, along with all the values.
Using his framework and a hex editor, I was able to deduce [MOST] of the remaining checks.
You can find his work here : https://github.com/PaddyCo/mw3rando


With that out of the way, here's what this randomizer does and does not do. [So Far].

There are currently 66 objcets randomized in the "Pool". They are :

(1). All 25 Shop Items. Non-Equippable items such as Keys cost billions of coins, and adjusting their prices causes the game to crash. So they cannot be found in Shops. All other equippable items can be found in shops.
This includes Trident, Oasis Boots, Pygmy Items, Legend Items, and Spells. It does not include a Heart.

(2). The "Elder" items at the beginning of the game. These can be any item, except for a Heart.

(3). The "Sonia" item, left in the cave. This can be any item, except for a heart.

(4). The "Blacksmith" item (Legend Sword in Vanilla). This can be any item, except for a heart. 

(5). 37 Chest items: 
("Firestorm"),("Quake"),("bat_reward"),("Pygmy_Sword"),("Pygmy_Armor"),
("Pygmy_Boots"),("Pygmy_Shield"),("Sun_Key"),("Moon_Key"),("Star_Key"),
("Blue_Gem"),("Gold_Gem"),("Thunder"),("Return"),("Power"),
("Shield_Magic_Chest"),("Old_Axe"),("Fire_Urn"),("Charmstone_Chest"),("Hard_Shield"),
("Trident"),("Oasis_Boots"),("Amulet"),("Elixer_Chests"),("First_Money"),
("Secret_Pyramid_1"),("Secret_Pyramid_2"),("Secret_Pyramid_3"),("Secret_Pyramid_4"),("Secret_Pyramid_5"),
("Water_Money_Chest3_Item1"),("Water_Money_Chest3_Item2"),("Water_Money_Chest3_Item3"),("Water_Money_Chest3_Item4"),("Water_Money_Chest3_Item5"),
("Full_Health_1"),("Full_Health_2"),

The item pool consists of a corresponding 66 items, forcing each "Check" to be different. They are :

(1). All equipment except for the starting items. -- 29

(2). All Spells -- 6

(3). Potions and Elixer -- 5 [Elixer and Hi-Potion can only appear in Shops. This so you can be properly equipped for the final battle]

(4). The Ocarina and Charmstone -- 2

(5). Non-Equippable Progression Items (Lamp, Amulet, 3 Keys, 2 Gems, Fire Urn, Bracelet) -- 9

(6). A Heart -- 1

(7). Money, small heart, big heart, magic refil -- 14

Some notes on Item Restrictions :

(1). Ocarina must appear in the first 8 checks, by the Sonia Item.

(2). Leather Boots must appear in the first 14 checks, before leaving Purapil. 

(3). Return Magic, Trident, Oasis Boots, Bracelet, and Lamp (The most important Items) are never behind more than one progression item. (So they cannot be in the pyramid, or in Poseidon's Area for instance).

(4). Amulet, Keys, and Gems are never behind more than TWO progression items. (So they cannot be Legend Sword, Blacksmith, or either Pygmy Check). 

(5). The three pygmy checks (Fire-Urn and Charmstone and the 2nd Health) are restricted to increase the chances you'll need Pygmy items. It's roughly 50-50 you'll need to do one of them.

9 other Chest items are randomized for fun, but will never have progression items in them. The Legend Chests, and the 2nd Money-Chest Near Alsedo. These will have some random combination of money, small hearts, Heart, and even an extra Charmstone. 


"Go-Mode" requires 7 items --
   
      (a). Defeat the ice-bomber. Requires Bracelet and Both-Gems. The Old-Axe is not needed, nor is it in the Pool. 
   
      (b). Have access to Begonia. Requires Oasis Boots (Or enough Health/Refills to skip them) and the Star-Key.
   
      (c). The Fire-Urn. Talk to the Blacksmith.

      (d). Legend Sword. (You technicallty don't need the other Legend Items, but good luck vs Biomeka without them! I personally would never try it without booth Legend Armor and Legend Shield). 
   
  

      If you talk to the Elder after using the Bracelet to enter Childam, the door back to Purapill will not spawn. You may need to walk back. 


   If you find any issues or logical progression problems, please reach out to me.


In addition to the random elements, many Quality of Life improvements are in place. In general, all items are cheaper than they would be in Vanilla, so less grinding is needed. 

Sonia's text synchs with her correpsonding item, so you can skip it if it's useless. The blacksmith's language is also synched, so you know what you're getting.

There are THREE hints currently in the game. 

At the top of purapill stairs, on the first screen, the lady to the left will hint about the "Sphinx Item". This is the CHARMSTONE chest.

The lady on the right will hint about the "Poseidon item". This is the OASIS BOOTS chest.

The wandering Dragon in Begonia will hint about the "Volcano item". This is the FIRE-URN chest. 

As many text speed ups are in place as I could find. The following texts can be skipped by holding C and mashing A : The Intro, Ocarina playing, The Dwarf, The Sphinx, the Gems, the Ice Melting, and both Prince speaches.

Be very careful when skipping the text with the Sphinx! I'm not responsible if you skip a question! :-P

Here's what you'll have to do to run the randomizer :

(1). Put the randomizer.py into the same folder as the SRM and the other python scripts. 

(2). Run the SRM executable. 

(3). Point it at the (Legally Aquired) rom you'll be using. Make sure you're using USA version, not Japanese! I cannot guarantee it will work the same [Though it might!]

(4). Be Patient. Sometimes it takes a while, sometime it crashes. If you receieve the message "Maybe it was a bad seed?" try again. If it gets over 50,000 atttempts, I'd recomend trying again. 

(5). Open the output with your emulator. I use fusion, but it should work with any of them. 

(6). In addition to the rom, the program will output a spoiler log, with key items written in english. If you want to know what the other numbers mean, let me know. 

Have fun!
    
