mobile_data = {
'status': True,
'data': [
    {'name': 'Xiaomi Note 5','price': '300 USD', 'made': 'China'},
    {'name': 'Samsung Note 6','price': '200 USD', 'made': 'USA'},
    {'name': 'Iphone 5','price': '180.5 USD', 'made': 'Japan'},
    {'name': 'Pixel 5','price': '89.60 USD', 'made': 'Russia'},
    {'name': 'Techno 5','price': '110 USD', 'made': 'Uk'},
    {'name': 'Huawei 5','price': '350 USD', 'made': 'Malaysia'},
],
    'exchange_rate': 107.25
}

for i in mobile_data['data']:
    phone_name = i.get('name')
    phone_price = i.get('price')
    phone_country = i.get('made')
    bdt_currency = mobile_data['exchange_rate'] * float(i.get('price')[:-4])

    print(f'{phone_name} is made in {phone_country}. The price is {phone_price} which is almost equal to {round(bdt_currency,2)} BDT')
