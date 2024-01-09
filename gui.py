import time
import board
import digitalio
import displayio
import terminalio
from adafruit_display_text import label

font = terminalio.FONT

LCD_w = 320
LCD_h = 240

def get_item_at_index(menu_items: dict, index: int):
    #print(menu_items.items())
    for item in enumerate(menu_items.items()):
        if index == item[0]:
            return(item[1])

def draw_vertical_menu(menu_items: dict, cursor: int):
    screen = displayio.Group()
    color_bitmap = displayio.Bitmap(LCD_w, LCD_h, 1) #Width, Height, Colours
    color_palette = displayio.Palette(1)
    color_palette[0] = 0x333366
    bg = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    screen.append(bg)
    
    for item in enumerate(menu_items.items()):
        if cursor == item[0]:
            text_color = 0xFFFF00
        else:
            text_color = 0xFFFFFF
            
        screen.append(label.Label(font, text=item[1][0], color=text_color, x=10, y=item[0] * 15 + 15))

    return(screen)