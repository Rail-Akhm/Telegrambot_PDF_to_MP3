from gtts import gTTS
import pdfplumber
from pathlib import Path
import telebot
import pathlib
import os
bot = telebot.TeleBot('5433694283:AAHH0l4FmOBm6jgmGdMLpqhThp0tlYgzTyk')

if (os.path.isfile('C:/Users/railakhm/PycharmProjects/telegrambot/audio.pdf')):
    os.remove('C:/Users/railakhm/PycharmProjects/telegrambot/audio.pdf')

if (os.path.isfile('C:/Users/railakhm/PycharmProjects/telegrambot/audio.mp3')):
    os.remove('C:/Users/railakhm/PycharmProjects/telegrambot/audio.mp3')

@bot.message_handler(commands = ['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name}, это мой первый телеграм-бот) Закинь PDF файл и получишь MP3'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(content_types=['document'])
def handle_docs(message):
    try:

        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = 'C:/Users/railakhm/PycharmProjects/telegrambot/' + message.document.file_name;
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        path = pathlib.Path("C:/Users/railakhm/PycharmProjects/telegrambot/")
        for i, path in enumerate(path.glob('*.pdf')):
            path.rename('audio' + '.pdf')



        bot.reply_to(message, f"Я получил твой документ, щас скину MP3")
        bot.reply_to(message, f"Обрабатываю твой файл...")
    except Exception as e:
        bot.reply_to(message, e)

    if __name__ == '__main__':
        main()

    mp3 = open('audio.mp3', 'rb')
    bot.send_audio(message.chat.id, mp3, "получай свой аудио файл:")


def pdf_to_mp3(file_path='test.pdf', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix =='.pdf':

        print(f'Твой файл: {Path(file_path).name}')
        print(f'Обрабатываю твой файл')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)

        text = text.replace('\n','')

        my_audio = gTTS(text=text, lang='ru', slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')
        return f' {file_name} mp3 сделан! \n  Получай)'


def main():
    print(pdf_to_mp3(file_path=('C:/Users/railakhm/PycharmProjects/telegrambot/audio.pdf')))

bot.polling(none_stop=True)
