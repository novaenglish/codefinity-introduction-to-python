# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

apple_count = shelf.count("apples")
print(f"Number of Apples: {apple_count}")

banana_index = shelf.index("bananas")
print(f"First Banana Index: {banana_index}")

if shelf.count("apples") < 5:
    print("Apples need to be restocked." )
else:
    print("Apples are suffiently stocked.")

grape_count = shelf.count("grapes")
if shelf.count("grapes") == 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are suffiently stocked.")

if "oranges" in shelf:
    print(f"Oranges are at index: {shelf.index("oranges")}")
else:
    print("Oranges are out of stock.")


    

