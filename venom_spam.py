import keyboard as k
import mouse as m
import time
import socket
from platform import platform
from random import choice
from datetime import datetime
from colorama import Fore, Style

windows = platform()

venom_version = '2.0 OpenSource'

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

random_filename_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', '1', '2', '3']
generator = ''

for i in range(6):
    generator = generator + choice(random_filename_keys)

logs_file = generator + ".txt" #Автоматически генерирует файл с логами. Вы увидите название файла для логов в консоли.
logs_file.lower()

current_time = datetime.now()
messages_send = 0

print(Fore.CYAN + "VENOM SPAM BOT 2.0 by idearivel" + Style.RESET_ALL)
print(Fore.WHITE + "Ознакомьтесь с инструкцией в README.txt !!!" + Style.RESET_ALL)

spam_message = input('Введите сообщение которое будет отправляться: ')

try:
    cooldown = float(input('Укажите задержку перед отправкой (рекомендуется не меньше 0.5): '))
except ValueError:
    print(Fore.RED + 'invalid value' + Style.RESET_ALL)
    time.sleep(3)
    exit()

try:
    messages_count = int(input('Сколько отправить сообщений? (рекомендуется не больше' + Fore.RED +  ' 1000 ' + Fore.WHITE + 'за раз): ' + Style.RESET_ALL))
except ValueError:
    print(Fore.RED + 'invalid value' + Style.RESET_ALL)
    time.sleep(3)
    exit()

try:
    if __name__ == "__main__":
        print(Fore.YELLOW + 'compatibility check in progress...' + Style.RESET_ALL)
        def spam():
            messages_send = 0
            time.sleep(3)
            print(Fore.GREEN + 'compatibility check successful' + Style.RESET_ALL)
            print('Logs file: ' + Fore.MAGENTA + logs_file + Style.RESET_ALL)

            for i in range(messages_count):
                time.sleep(cooldown)
                if k.is_pressed('alt'):
                    break
                m.click('left')
                k.write(spam_message)
                k.press('enter')
                if k.is_pressed('alt'):
                    break

                messages_send = messages_send + 1
                print(Fore.GREEN + 'СООБЩЕНИЕ Отправлено [', messages_send,'/',messages_count,']' + Style.RESET_ALL)
                
                logs_text = f"[{current_time}] [{windows}] [{local_ip}] SPAM COMPLETED [{messages_send}/{messages_count}]"
                with open(logs_file, "w") as file:
                    file.write(logs_text + '\n' + f'VERSION: {venom_version}')
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
except TypeError:
    print(Fore.RED + 'compatibility check failed' + Style.RESET_ALL)
except MemoryError:
    print(Fore.RED + 'out of memory' + Style.RESET_ALL)