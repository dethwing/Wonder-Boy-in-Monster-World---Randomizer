# Wonder-Boy-in-Monster-World---Randomizer
Randomizer for the Genesis Classic, Wonder Boy 5 (Monster World 3)

First of all, I want to say huge thanks to both Mode8fx and PaddyCo for making this project possible.

In case you don't know, Mode8fx created the program "Simple Randomizer Maker" which is incredibly easy to use. All you need is the hex addresses and values and the program does the rest.
I've uploaded it as part of the repository, but you can also find it here : https://github.com/Mode8fx/SimpleRandomizerMaker

In addition, I couldn't have made any progress without the ground work that PaddyCo laid out. He started this project over 4 years ago and provided me with the addresses for around 10 checks, along with all the values.
Using his framework and a hex editor, I was able to deduce [MOST] of the remaining checks.
You can find his work here : https://github.com/PaddyCo/mw3rando

With that out of the way, here's what this randomizer does and does not do. [So Far].

1. All shop items are randomized. Non-Equippable Progression items (Keys, Gems, etc) have prices in the billions, so are not available. Equippable Progression items (Trident, Oasis Boots, Pygmy....) are available.

      Forced Logic : All Shop Items are different. The Potion shop-item in Purapill and Lillpad is the same item, so it will appear twice.
   
      Forced Logic : Marine boots will appear by Lillypad at the latest. Needed for Quake chest.
   
      Forced Logic : Hi Potion and Elixer will be available. "Needed" for final boss.
   
      Optional Logic : Scale price by region, prevent certain items from appearing.
   
3. (Almost) all chests are randomized. Exceptions include: Heart Chests, Pyramid Money. This includes the Bat and Legend Sword. Total Checks : 42

      Forced Logic : All chests are different. Exception: Elixer and some magic chests duplicate the same item as they are the same items.
   
      Forced Logic : Available items incldue 15 Progression Items (4*Pygmy, 3*Key, 2*Gem, Fire Urn, Lamp, Bracelet, Amulet, Trident, Oasis Boots)
                     and 10 Non-Progression Items (All Magic except for Shield, Heart, Elixer, and non-Sword Legend Items)
   
      Forced Logic : Complicated, but in general, the fewer requirements for a check, the more likely it is to be progression.
   
      Optional Logic : None at this time.

4. Elder (The first person you talk to) items are randomized. They can be anything in the game.
   
      Forced Logic : Both items are different.
   
      Optional Logic : Customize your start from fully random, or require equipment, spells, etc.

5. "Go-Mode" requires 7 items --
   
      (a). Defeat the ice-bomber. Requires Bracelet and Both-Gems. The Axe is not required, nor do you need to open the chest. (Though you probably should....)
   
      (b). Have access to Begonia. Requires Oasis Boots (Or enough Health/Refills to skip them) and the Star-Key.
   
      (c). The Fire-Urn. The Old Axe is NOT required and is not in the pool.

      (d). Legend Sword.
   
      (d). After this,talk to the blacksmith, so you can go to the final area. 

      If you talk to the Elder after using the Bracelet to enter Childam, the door back to Purapill will not spawn. You may need to walk back. 


   If you find any issues or logical progression problems, please reach out to me.

Here's what you'll have to do to run the randomizer :

(1). Run the SRM executable. 

(2). Put the randomizer.py into the same folder as the SRM. 

(3). Run the SRM and point it at the rom you'll be using. Make sure you're using USA version, not Japanese!

(4). Use the optinal settings to customize your experience. Be aware the more you use, the longer it will take to generate. It may also crash. If you receieve the message "Maybe it was a bad seed?" try again.

(5). Open the output with your emulator. I use fusion, but it should work with any of them. 

Have fun!
    
