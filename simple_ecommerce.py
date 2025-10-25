# simple_ecommerce.py
# Run with: python simple_ecommerce.py

products = {
    1: {"name": "T-shirt", "price": 499},
    2: {"name": "Jeans", "price": 899},
    3: {"name": "Shoes", "price": 1299},
    4: {"name": "Watch", "price": 799},
    5: {"name": "Cap", "price": 199},
}

cart = {}

def show_products():
    print("\n🛍️ Available Products:")
    for pid, info in products.items():
        print(f"{pid}. {info['name']} - ₹{info['price']}")
    print()

def add_to_cart():
    try:
        pid = int(input("Enter product ID to add: "))
        if pid in products:
            qty = int(input("Enter quantity: "))
            cart[pid] = cart.get(pid, 0) + qty
            print(f"✅ {products[pid]['name']} added to cart (Qty: {cart[pid]}).")
        else:
            print("❌ Invalid Product ID.")
    except ValueError:
        print("⚠️ Please enter valid numbers.")

def view_cart():
    if not cart:
        print("\n🛒 Your cart is empty.\n")
        return
    print("\n🛒 Your Cart:")
    total = 0
    for pid, qty in cart.items():
        name = products[pid]["name"]
        price = products[pid]["price"]
        subtotal = price * qty
        total += subtotal
        print(f"{name} (x{qty}) - ₹{subtotal}")
    print(f"-------------------------\nTotal: ₹{total}\n")

def remove_from_cart():
    try:
        pid = int(input("Enter product ID to remove: "))
        if pid in cart:
            del cart[pid]
            print("🗑️ Item removed from cart.")
        else:
            print("❌ Item not found in cart.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def checkout():
    if not cart:
        print("\nCart is empty. Add items before checkout!\n")
        return
    view_cart()
    confirm = input("Do you want to confirm purchase? (y/n): ").lower()
    if confirm == "y":
        print("\n🎉 Order placed successfully! Thank you for shopping.\n")
        cart.clear()
    else:
        print("❌ Checkout cancelled.\n")

def main():
    print("🧑‍💻 Welcome to PythonShop!")
    while True:
        print("""
======== MENU ========
1. Show Products
2. Add to Cart
3. View Cart
4. Remove Item
5. Checkout
6. Exit
======================
""")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            show_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            remove_from_cart()
        elif choice == "5":
            checkout()
        elif choice == "6":
            print("👋 Thanks for visiting PythonShop!")
            break
        else:
            print("❌ Invalid choice! Please enter 1–6.")

if __name__ == "__main__":
    main()
