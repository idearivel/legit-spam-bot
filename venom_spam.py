import keyboard as k
import mouse as m
import time
from datetime import datetime
from colorama import Fore, Style
current_time = datetime.now()

print(Fore.CYAN + "VENOM SPAM BOT 1.3 by idearivel" + Style.RESET_ALL)
cooldown = float(input('Укажите задержку перед отправкой (рекомендуется не меньше 0.25): '))
messages_send = 0
messages_count = int(input('Сколько отправить ВЕНОМОВ?: '))

try:
    if __name__ == "__main__":
        print(Fore.YELLOW + 'compatibility check in progress...' + Style.RESET_ALL)
        def spam():
            messages_send = 0
            time.sleep(3)
            for i in range(messages_count):
                time.sleep(cooldown)
                m.click('left')
                if k.is_pressed('alt'):
                    break
                k.press('v')
                if k.is_pressed('alt'):
                    break
                k.press('e')
                if k.is_pressed('altsggdggdg'):
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
                print(Fore.YELLOW + 'compatibility check successful' + Style.RESET_ALL)
                print(Fore.GREEN + 'VENOM Отправлен [', messages_send,'/',messages_count,']' + Style.RESET_ALL)
                if k.is_pressed('alt'):
                    break
    else:
        print(Fore.RED + 'compatibility check failed' + Style.RESET_ALL)
    spam()
except NameError:
    print(Fore.RED + 'compatibility check failed' + Style.RESET_ALL)
except KeyError:
    print(Fore.RED + 'compatibility check failed' + Style.RESET_ALL)
except ValueError:
    print(Fore.RED + 'compatibility check failed' + Style.RESET_ALL)