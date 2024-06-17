import requests
from telethon import events


async def currency(event: events, client):

    base_url = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json'

    response = requests.get(base_url)

    json = response.json()
    usd_byn = round(json['usd']['byn'], 3)
    usd_rub = round(json['usd']['rub'], 3)
    usd_eur = round(json['usd']['eur'], 3)
    usd_cny = round(json['usd']['cny'], 3)
    usd_uah = round(json['usd']['uah'], 3)
    usd_kzt = round(json['usd']['kzt'], 3)
    usd_btc = json['usd']['btc']
    usd_eth = round(json['usd']['eth'], 7)

    chat = await event.get_chat()

    await client.send_message(chat, f'<pre>USD / BYN = {usd_byn}</pre>\n'
                                    f'<pre>USD / RUB = {usd_rub}</pre>\n'
                                    f'<pre>USD / EUR = {usd_eur}</pre>\n'
                                    f'<pre>USD / CNY = {usd_cny}</pre>\n'
                                    f'<pre>USD / UAH = {usd_uah}</pre>\n'
                                    f'<pre>USD / KZT = {usd_kzt}</pre>\n'
                                    f'<pre>USD / BTC = {usd_btc}</pre>\n'
                                    f'<pre>USD / ETH = {usd_eth}</pre>', parse_mode='HTML')
