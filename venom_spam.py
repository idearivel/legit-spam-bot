import keyboard as k
import mouse as m
import time
from colorama import Fore, Style

messages_send = 0
messages_count = int(input('Сколько отправить ВЕНОМОВ?: '))

if __name__ == "__main__":
    print(Fore.YELLOW + 'compatibility check successful')
    def spam():
        messages_send = 0
        time.sleep(3)
        for i in range(messages_count):
            time.sleep(0.5)
            m.click('left')
            if k.is_pressed('alt'):
                break
            k.press('v')
            if k.is_pressed('alt'):
                break
            k.press('e')
            if k.is_pressed('alt'):
                break
            k.press('n')
            if k.is_pressed('alt'):
                break
            k.press('o')
            if k.is_pressed('alt'):
                break
            k.press('m')
            if k.is_pressed('alt'):
                break
            k.press('enter')    

            messages_send = messages_send + 1
            print(Fore.GREEN + 'VENOM Отправлен [', messages_send,'/',messages_count,']' + Style.RESET_ALL)
            if k.is_pressed('alt'):
                break
    spam()
else:
    print(Fore.RED + 'compatibility check failed' + Style.RESET_ALL)