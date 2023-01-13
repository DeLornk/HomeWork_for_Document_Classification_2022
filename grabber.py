from telethon import TelegramClient
import csv

# Remember to use your own values from my.telegram.org!
api_id = 0
api_hash = ''
client = TelegramClient('test_session', api_id, api_hash)

async def main():
    csvfile = open('results.csv', 'w')
    fieldnames = ['date', 'text']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    channel = await client.get_entity('Sputnik_results')
    print(channel)

    i = 1

    for message in await client.get_messages('Sputnik_results', limit=10000):
        print('-----------------')

        if message.text != "":
            print(f'Сообщение {i}\nDate: {message.date}')
            print(message.text)
            writer.writerow({'date': message.date, 'text': message.text})
            i += 1
            print()
        else:
            print("Пустое сообщение")

with client:
    client.loop.run_until_complete(main())