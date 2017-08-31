# Python-Roguelike
creating a roguelike in python

Tentative Production Steps to get the engine running:

Creating the screen:
1. import libtcod
2. define screen width/height variables
3. declare font using libtcod
4. generate the actual screen using width/height variables
5. create a loop that will keep the game running
6. add a keypress to get out of the game by pressing escape that exits the loop

Putting a character on screen:
1. Set a foreground color
2. put a character on the screen
3. use libtcod flush to present everything on the screen

Player movement:
1. create x and y variables
2. get rid of step 2 from the last group
3. place a symbol in the middle of the screen, cast player position to int from float
4. add variables that hold keyboard and mouse input
5. add a function that captures key/mouse events
6. Put player movement in a separate file

input_handlers file:
1. use the key value captured earlier, store it, move the last step 4 to here instead
2. create statements that compare the input to keyboard input and move accordingly
3. also remove the key_escape check, replace it using 'if exit'
4. call input_handlers in engine.py
