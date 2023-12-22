#improved version of a code from a yt tutorial
#run the script to keep mouse moving. To exit press and hold 'f'
import pyautogui as pag
import random
import time
import keyboard

def afk_mouse():
    x = random.randint(600, 700)
    y = random.randint(200, 600)
    pag.moveTo(x, y, duration = 0.5)

def main():
        start_time = time.time()
        try:
            while not keyboard.is_pressed("f"):
                afk_mouse()
                time.sleep(2.4)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            elapsed_time = time.time() - start_time
            print(f"Script terminated. You were successfully AFK for {elapsed_time: .2f} seconds.")

            
if __name__ == "__main__":
    main()