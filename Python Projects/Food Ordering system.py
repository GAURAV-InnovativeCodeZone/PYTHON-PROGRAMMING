# Project : 02 => Food Ordering System
# This System created by Gaurav Panwar

print("\n●----------🙏 ●● Welcome To Restaurant ●● 🙏----------●\n")
menu = {
    "Burger": 50,
    "Pizza": 120,
    "Noodle": 30,
    "Momos": 30,
    "Coffee": 60,
    "Tea": 20,
    "Pasta": 40,
}
print("FOOD MENU")
print(
    " Burger : 50 \n Pizza  : 120 \n Noodle : 30 \n Momos  : 30 \n Coffee : 60 \n Tea    : 20 \n Pasta  : 40 \n\n"
)

total_order = 0

item_1 = input("Enter the name of item that you want to order : ")

if item_1 in menu:
    total_order += menu[item_1]
    print(f"Your item {item_1} has been added to your order list.")
else:
    print(f"SORRY! Ordered item {item_1} is not available yet.")

another_order = input("\nDo you want to order another item ? (Yes/No):")

if another_order == "Yes":
    item_2 = input("\nOK! Enter the name of another item : ")
    if item_2 in menu:
        total_order += menu[item_2]
        print(f"Your item {item_2} has been added to your order list.")
    else:
        print("SORRY! Ordered item {item_2} is not available.")

print(
    f"\nThe total amount of items that you ordered is {total_order}. So you have to pay {total_order} Rs only.\n"
)

print("\n●---------------🙏 ●● THANK YOU ●● 🙏---------------●\n")
