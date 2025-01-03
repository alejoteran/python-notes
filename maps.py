items = [
    {
        'product' : 'camisa',
        'price' : 100
    },
    {
        'product' : 'pantalon',
        'price' : 200
    },
    {
        'product' : 'tennis',
        'price' : 300
    }
]

prices = list(map(lambda item : item['price'], items))
print(f'precios -> {prices}')

def add_tax(item):
    new_item = item.copy()
    new_item['tax'] = new_item['price'] * 0.19
    return new_item

new_items = list(map(add_tax, items))

print(f'new items -> {new_items}')
print(f'old items -> {items}')