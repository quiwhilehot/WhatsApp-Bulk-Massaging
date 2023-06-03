# Скрипт массовой рассылки WhatsApp

## Описание
Этот скрипт позволяет отправлять массовые сообщения в WhatsApp с помощью Python. Он использует библиотеку Selenium для автоматизации процесса отправки. Скрипт поддерживает теги WhatsApp, кодировку UTF-8 и различные функции отправки сообщений, такие как отправка смайлов.

## Возможности
- Отправка массовых сообщений в WhatsApp с использованием вашей учетной записи
- Поддержка тегов WhatsApp для форматирования сообщений
- Кодировка UTF-8 для многоязычных сообщений
- Отправка текстовых сообщений, включая ссылки и смайлы

## Системные требования
- Python 3.6 или выше
- Браузер Chrome (рекомендуется последняя версия)

## Установка
1. Клонируйте репозиторий.
2. Установите необходимые библиотеки, выполнив следующую команду: `pip install -r requirements.txt`
## Использование
1. Подготовьте ваше сообщение и номера телефонов:
- Отредактируйте файл `message.txt` с вашим желаемым сообщением.
- Добавьте номера телефонов в файл `numbers.txt`, по одному номеру на каждой строке.
2. Запустите скрипт: `main.py`
3. В строке `next_delay = random.randint(3, 15)` вы можете задать собственные значения задержки между отправкой сообщений
4. Следуйте инструкциям в терминале:
- Войдите в свою учетную запись WhatsApp, отсканировав QR-код в открытом окне браузера.
- После входа в аккаунт нажмите ENTER, чтобы начать отправку сообщений.
5. Расслабьтесь и наблюдайте, пока скрипт отправляет сообщения на указанные номера телефонов.

## Отказ от ответственности
Пожалуйста, используйте этот скрипт ответственно и уважайте условия использования WhatsApp. Отправка незапрошенных или спам-сообщений строго запрещена и может привести к приостановке вашей учетной записи.

Благо дарим [тут](https://oplata.qiwi.com/form?invoiceUid=b41f76b2-3a89-475f-995d-64c9f7eb1e94)

# WhatsApp Bulk Messaging Script

## Description
This script allows you to send bulk messages on WhatsApp using Python. It utilizes the Selenium library to automate the sending process. The script supports WhatsApp tags, UTF-8 encoding, and various messaging features like sending emojis.

## Features
- Send bulk messages on WhatsApp using your own account
- Supports WhatsApp tags for formatting messages
- UTF-8 encoding for multilingual messaging
- Send text messages, including links and emojis

## System Requirements
- Python 3.6 or higher
- Chrome browser (latest version recommended)

## Installation
1. Clone the repository.
2. Install the required libraries by running the following command: `pip install -r requirements.txt`

## Usage
1. Prepare your message and phone numbers:
- Edit the `message.txt` file with your desired message.
- Add the phone numbers to the `numbers.txt` file, one number per line.
2. Run the script: `main.py`
3. In the line `next_delay = random.randint(3, 15)` you can set your own values for the delay between sending messages.
4. Follow the instructions in the terminal:
- Enter your WhatsApp account by scanning the QR code in the opened browser window.
- Once logged in, press ENTER to start sending messages.
5. Sit back and relax while the script sends your messages to the specified phone numbers.

## Disclaimer
Please use this script responsibly and respect the terms of service of WhatsApp. Sending unsolicited or spam messages is strictly prohibited and may result in account suspension.
