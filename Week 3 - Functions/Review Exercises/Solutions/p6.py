def bulk_price(list_price, items):
    totalCost = list_price * 0.9 + list_price * 0.8 # adds the price of the first 2 shoes
    totalCost = totalCost + (list_price * 0.7) * (items - 2) # adds the price of the rest of the shoes
    return totalCost

list_price = float(input())
items = int(input())

print(bulk_price(list_price, items))