# Wonder-Boy-in-Monster-World---Randomizer
Randomizer for the Genesis Classic, Wonder Boy 5 (Monster World 3)

First of all, I want to say huge thanks to both Mode8fx and PaddyCo for making this project possible.

In case you don't know, Mode8fx created the program "Simple Randomizer Maker" which is incredibly easy to use. All you need is the hex addresses and values and the program does the rest.
I've uploaded it as part of the repository, but you can also find it here : https://github.com/Mode8fx/SimpleRandomizerMaker

In addition, I couldn't have made any progress without the ground work that PaddyCo laid out. He started this project over 4 years ago and provided me with the addresses for around 10 checks, along with all the values.
Using his framework and a hex editor, I was able to deduce [MOST] of the remaining checks.
You can find his work here : https://github.com/PaddyCo/mw3rando

With that out of the way, here's what this randomizer does and does not do. [So Far].

1. All shop items are randomized, and all are guaranteed to be different. In addition, they are price-scaled, so you can be relatively sure of buying things in progression. The reason the sprite looks weird is because they are changed so that shop will sell you an item, even if you had the base item. [Example: If you have leather boots, and the leather boots are set to Ladder Boots, it still won't sell it you. That's why I had to change it]. In addition, Marine boots are guaranteed to be in one of the 4 shops available to you from Purapill and Lillypad. The reason is that they are needed for the Quake check. More on that later. Finally, Hi Potion and Elixer will be somewhere in the last 2 shop areas [Chilldam and Begonia] so you can be sure of restocking your health before trying Biomeke [AKA impossible final boss].
2. MOST chest items are randomized. This includes all Magic [Except for the all magic secret chest in the Pyramid], the Charmstone Chest, all Pygmys, keys, gems, fire urn, amulet, and axe. It also includes things like Oasis boots, Trident, and even Hard Shield! It does NOT include Heart Chests [If you switch one, you switch them all, and you'd be stuck on 3 hearts for the game!] and Money Chests [No luck finding them in code yet], and Elixer Chests [Same as Heart, they're all linked together]. 
3. Items in chests are scaled by progression. For instance, of the first 3 "Free" checks [Myconid, Bat, Quake], you are guaranteed to get 3 of Trident/Bracelet/Oasis Boots/Lamp. And items progress from there.
4. The bracelet check is NOT randomized, but you will probably get it before you talk to him. I have the address for it, but there's some complications I haven't worked out yet that prevents him from giving it you.
5. The Ocarina check is NOT randomized. You MUST talk to Ellanora and Sonia to spawn it. Although I could randomize it, it won't spawn if you already have the ocarina, and that would make things messy. [To do?]
6. The Legendary Sword check is NOT randomized. I haven't found the address yet. Unforunately, the value for LS is 0...which of course appears thousands of times in code.
7. I made the executive decision to pull Charmstones from the pool. As Monk would say, You'll thank me later.


   If you find any issues or logical progression problems, please reach out to me.

Here's what you'll have to do to run the randomizer :
(1). Run the SRM executable. 
(2). Put the randomizer.py into the same folder as the SRM. 
(3). Run the SRM and point it at the rom you'll be using. Make sure you're using USA version, not Japanese!
(4). You shouldn't need any of the optional settings unless you're doing research on addresses. These are cheat-modes to let you get to certain areas easier and quicker.
(5). Open the output with your emulator. I use fusion, but it should work with any of them. 
(6). It's possible the game will freeze on the title screen. [It did for me, but not for Artega]. If you have problems go to Options -> Set Config -> And click disable SRAM and Fix Checksums. 
(7). Currently the Inn save functions do NOT save your game. Apologies, I don't know why that is. Make sure you save state after you save at an inn, so you don't lose your progress if you die!!!!

Have fun!
    
