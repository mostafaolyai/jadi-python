

price = int(input())

if price > 50000:
    print(price* 0.8)
elif 20000 < price < 50000:
    print(price* 0.9)
elif 20000 > price:
    print(price)