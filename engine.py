import libtcodpy as libtcod

from entity import Entity
from input_handlers import handle_keys

def main():
    screen_width = 80 #set screen width and height as integers
    screen_height = 50

    player = Entity(int(screen_width / 2), int(screen_height / 2), '@', libtcod.white)
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), '@', libtcod.yellow)
    entities = [npc, player]

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD) #set a font

    libtcod.console_init_root(screen_width, screen_height, 'py rogue', False) #actually generate the window

    con = libtcod.console_new(screen_width, screen_height)

    key = libtcod.Key() #holds keyboard and mouse input in variables
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed(): #a loop that keeps the game running esentially
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse) #updates key and mouse with user inputs

        libtcod.console_set_default_foreground(con, libtcod.white)
        libtcod.console_put_char(con, player_x, player_y, '@', libtcod.BKGND_NONE)
        libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
        libtcod.console_flush() #updates the screen constantly

        libtcod.console_put_char(con, player_x, player_y, ' ', libtcod.BKGND_NONE)

        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            player_x += dx
            player_y += dy

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

if __name__ == '__main__':
    main()
