# import env
import pyautogui
import keyboard
import minescript
import time

pyautogui.PAUSE = 0.1
delay = 0.1

reference_slot = {}

def get_position():
    x,y = pyautogui.position()
    minescript.echo(f"{x}, {y}")
def buy_sugar_cane():
    pyautogui.press("esc")
    minescript.execute("/shop Farming")
    time.sleep(delay)
    pyautogui.click(962, 407) # sugar cane position
    pyautogui.click(966, 468) # buy stack
    for _ in range(0,8):
        pyautogui.click(1015, 407) # add a stack

    pyautogui.click(970, 350) # buy sugar cane
    pyautogui.click(970, 350) # buy sugar cane
def buy_gun_powder():
    minescript.execute("/shop Mobs")
    time.sleep(delay)
    pyautogui.click(741, 405)  # gunpowder position
    pyautogui.click(954, 478)  # buy stacks 
    pyautogui.click(1120, 407) # add 32 stacks
    pyautogui.click(971, 355) # buy
    pyautogui.click(971, 355) # buy
def convert_to_paper():
    minescript.press_key_bind("key.use", True)
    time.sleep(delay)
    pyautogui.keyDown("shift")
    pyautogui.click(622, 406) # select paper recipe
    pyautogui.click(1316, 412) # Craft item

    for _ in range(3):
        pyautogui.press("space")
        pyautogui.click(1316, 412) # Craft item

    # pyautogui.press("space")
    # pyautogui.click(1316, 412) # Craft item
    # pyautogui.press("space")
    # pyautogui.click(1316, 412) # Craft item

    pyautogui.keyUp("shift")

def craft_fireworks():
    short_delay = 0.01
    time.sleep(0.1)

    pyautogui.keyDown("shift")

    pyautogui.PAUSE = 0.01
    for x in range(9):
        for y in range(4):
            px = 966 + (x * 56) # slot x
            py = 552 + (y * 56) # slot y
            pyautogui.moveTo(px, py)
            pyautogui.mouseDown()
            time.sleep(short_delay)
            pyautogui.mouseUp()
            time.sleep(short_delay)

        pyautogui.moveTo(1318, 405) # craft item
        pyautogui.mouseDown()
        time.sleep(short_delay)
        pyautogui.mouseUp()
        time.sleep(0.02)  # Give the game time to update result

    # Final output click
    pyautogui.moveTo(1318, 405) # Craft Item
    pyautogui.mouseDown()
    time.sleep(short_delay)
    pyautogui.mouseUp()

    pyautogui.keyUp("shift")
    pyautogui.PAUSE = 0.1
def sell_fireworks():
    minescript.execute("/sellall FIREWORK_ROCKET")
def empty_inventory():
    slots = [(979, 556), (1022, 553), (1079, 555), (1138, 558), (1187, 561), (1244, 560), (1288, 556), (1346, 557), (1405, 553), (979, 603), (1036, 610), (1088, 609), (1130, 605), (1182, 603), (1239, 610), (1302, 607), (1368, 607), (1393, 608), (975, 650), (1034, 658), (1088, 660), (1129, 663), (1191, 666), (1239, 667), (1288, 662), (1344, 662), (1404, 664), (965, 725), (1036, 726), (1084, 728), (1140, 732), (1187, 727), (1241, 727), (1305, 735), (1349, 732), (1402, 727)] # Slot positions
    time.sleep(delay)
    minescript.execute("/sellall GUNPOWDER")
    minescript.execute("/sellall SUGAR_CANE")
    minescript.player_set_orientation(2523.6243, -13.499759) # Trash position
    minescript.press_key_bind("key.inventory",True)
    pyautogui.PAUSE = 0.01
    for x,y in slots:
        pyautogui.moveTo(x,y)
        pyautogui.keyDown("ctrl")
        pyautogui.press("tab")
        pyautogui.keyUp("ctrl")
    minescript.player_set_orientation(2699.1167, 23.700203) # Crafting table
    pyautogui.PAUSE = 0.1

def main():
    if minescript.player_inventory() != []:
        empty_inventory()
        pyautogui.press("esc")
    buy_sugar_cane()
    pyautogui.press("esc")
    buy_gun_powder()
    pyautogui.press("esc")
    convert_to_paper()
    minescript.press_key_bind("key.use", True)
    craft_fireworks()
    pyautogui.press("esc")
    sell_fireworks()
    pyautogui.press("esc")

def exit_program():
    exit()

keyboard.add_hotkey("ctrl+t", get_position)

while True:
    keyboard.wait("f12")
    minescript.echo("works")
    main()

