#trying to learn python data structure
#such a shoping list
shoplist = ['apple','mango','carrot','banana']

print(f"i have {len(shoplist)} items to purchase") #string formatting
print("these items are:", end = ' ')
for item in shoplist:
    print(item, end = ' ')

print("\ni also have to buy rice")
shoplist.append("rice") #new value added to shoplist
print(f"my shopping list is now {shoplist}")

print("sorting the shoplist")
shoplist.sort()
print(f"sorted shoplist: {shoplist}")

print(f"First item to buy in shoplist: {shoplist[0]}")
first_index = shoplist[0]
del shoplist[0]
print(f"I bought the {first_index}")
print(f"remaining items to buy: {shoplist}")
