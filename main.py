import gui
import board
import digitalio
from adafruit_debouncer import Button
import macro.macro

lcd = board.DISPLAY
LCD_w = 320
LCD_h = 240

cursor = 0

def set_displayed_menu(menu):
    global displayed_menu
    displayed_menu = menu

applications = {
    "USB Macro": [set_displayed_menu, macro.macro.create_menu()],
}
displayed_menu = applications

down = digitalio.DigitalInOut(board.SWITCH_DOWN)
down = Button(down)
press = digitalio.DigitalInOut(board.SWITCH_PRESS)
press = Button(press)
up = digitalio.DigitalInOut(board.SWITCH_UP)
up = Button(up)
b3 = digitalio.DigitalInOut(board.BUTTON_3)
b3 = Button(b3)
b1 = digitalio.DigitalInOut(board.BUTTON_1)

def refresh_screen():
    global screen
    global cursor
    # Stop cursor from going further than the displayed menu
    if cursor >= len(displayed_menu):
        cursor = len(displayed_menu) - 1
    
    # Stop cursor from going less than the displayed menu
    if cursor < 0:
        cursor = 0

    screen = gui.draw_vertical_menu(displayed_menu, cursor)

refresh_screen()
while True:
    up.update()
    down.update()
    press.update()
    b3.update()

    if down.pressed:
        cursor += 1
        refresh_screen()

    if up.pressed:
        cursor -= 1
        refresh_screen()

    if press.pressed:
        item = gui.get_item_at_index(displayed_menu, cursor)
        item[1][0](item[1][1])

        cursor = 0
        refresh_screen()
    
    if b3.pressed: # Home screen
        displayed_menu = applications
        cursor = 0
        refresh_screen()
    
    if b1.value:
        lcd.show(screen)