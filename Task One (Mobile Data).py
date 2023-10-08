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

print("Solution- using FOR Loop:\n")

for i in mobile_data['data']:
    phone_name = i.get('name')
    phone_price = i.get('price')
    phone_country = i.get('made')
    bdt_currency = mobile_data['exchange_rate'] * float(i.get('price')[:-4])

    print(f'{phone_name} is made in {phone_country}. The price is {phone_price} which is almost equal to {round(bdt_currency,2)} BDT')

print("\n")

print("Solution- using While Loop:\n")

i = 0
while i < len(mobile_data["data"][0:]):
    mobile_name = mobile_data["data"][i].get("name")
    mobile_price = mobile_data["data"][i].get("price")[:-4]
    mobile_made = mobile_data["data"][i].get("made")
    i += 1
    bd_rate = (mobile_data["exchange_rate"]) * float(mobile_price)
    print(f'{mobile_name} is made in {mobile_made}. The price is {mobile_price} USD which is almost equal to {round(bd_rate,2)} BDT')
