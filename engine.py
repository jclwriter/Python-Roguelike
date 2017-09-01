import libtcodpy as libtcod

def main():
    screen_width = 80 #set screen width and height as integers
    screen_height = 50

    player_x = int(screen_width / 2) #no matter what the screen width/height are, the player will always be in the middle of the screen
    player_y = int(screen_height / 2)

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD) #set a font
    libtcod.console_init_root(screen_width, screen_height, 'py rogue', False) #actually generate the window

    key = libtcod.key() #holds keyboard and mouse input in variables
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed(): #a loop that keeps the game running esentially
        libtcod.console_set_default_foreground(0, libtcod.white) #set the foreground color
        libtcod.console_put_char(0, player_x, player_y, '@', libtcod.BKGND_NONE) #place a character on screen
        libtcod.console_flush() #updates the screen constantly

        key = libtcod.console_check_for_keypress() #adds a check for a key press, stores it in a variable

        if key.vk == libtcod.KEY_ESCAPE: #if a key press is the escape button, ends the loop
            return True

if __name__ == '__main__':
    main()
