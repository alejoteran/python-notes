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

new_items = list(map(lambda item : {
    'product' : item['product'],
    'price' : item['price'],
    'tax' : item['price'] * 0.19
}, items))

print(f'new items -> {new_items}')