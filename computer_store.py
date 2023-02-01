processing_price = 0
current_price = input()

while current_price != 'special' and current_price != 'regular':
    current_price = float(current_price)
    if current_price < 0:
        print('Invalid price!')
        current_price = input()
        continue
    processing_price += current_price
    current_price = input()
if not processing_price:
    print('Invalid order!')
    exit()
taxes = processing_price * 0.2
total_price = processing_price + taxes
if current_price == 'special':
    total_price *= 0.9
print(f'''Congratulations you've just bought a new computer!
Price without taxes: {processing_price:.2f}$
Taxes: {taxes:.2f}$
-----------
Total price: {total_price:.2f}$''')
