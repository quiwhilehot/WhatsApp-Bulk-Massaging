from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote
import os
import random

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
# Создание папки на диске C, которую вы можете удалить после использования.

options.add_argument("--user-data-dir=c:/temp/")
# По сути, в папке "temp" вы можете найти все ваши данные WhatsApp.


os.system("")
os.environ["WDM_LOG_LEVEL"] = "0" 
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


print('''
WhatsApp Bulk Massaging PY
''' +style.GREEN)
print(style.RESET)

f = open("message.txt", "r", encoding="utf-8")
message = f.read()
f.close()

print(style.YELLOW + '\nВот ваше сообщение:')
print(style.GREEN + message)
print("\n" + style.RESET)
message = quote(message)

numbers = []
f = open("numbers.txt", "r")
for line in f.read().splitlines():
    if line.strip() != "":
        numbers.append(line.strip())
f.close()
total_number=len(numbers)
print(style.RED + 'Найдено ' + str(total_number) + ' номеров' + style.RESET)
delay = 30

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
print('Как только откроется окно браузера, войдите в свой WhatsApp аккаунт')
driver.get('https://web.whatsapp.com')
input(style.MAGENTA + "Как только завершится вход в аккаунт и вы увидете список ваших чатов, нажмите ENTER..." + style.RESET)

for idx, number in enumerate(numbers):
    number = number.strip()
    if number == "":
        continue
    print(style.YELLOW + '{}/{} => Отправка сообщения {}.'.format((idx+1), total_number, number) + style.RESET)
    try:
        url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
        sent = False
        for i in range(3):
            if not sent:
                driver.get(url)
                try:
                    click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='compose-btn-send']")))
                except Exception as e:
                    print(style.RED + f"\nОшибка отправки сообщения: {number}, retry ({i+1}/3)")
                    print("Убедитесь что ваш телефон и компьютер подключены к интернету")
                    print("Если появится предупреждение, пожалуйста, закройте его." + style.RESET)
                else:
                    sleep(1)
                    click_btn.click()
                    sent=True
                    driver.execute_script("window.stop();")  # Остановка загрузки страницы
                    sleep(3)
                    print(style.GREEN + 'Сообщение отправлено: ' + number + style.RESET)
                    next_delay = random.randint(3, 15)  #Установите значение задержки между отправкой сообщений
                    print(style.CYAN + 'Следующее сообщение будет отправлено через:', next_delay, 'секунд' + style.RESET)
                    sleep(next_delay)
    except Exception as e:
        print(style.RED + 'Ошибка отправки сообщения ' + number + str(e) + style.RESET)

driver.quit()
