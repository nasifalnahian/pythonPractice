food = ["rice", "egg", "cookies", "cake", "meat"]
fruits = ["apple", "banana", "orange", "nuts", "dates", "mango"]
fast_food = ["burger", "pizza", "sandwich"]
search = input("enter your search product : ")
if search in food:
    print("yes its a food item")
elif search in fruits:
    print("yes its a fruits item")
elif search in fast_food:
    print("yes its a fast_food item")
else:
    print("not found")
