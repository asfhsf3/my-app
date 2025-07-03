import json
import sys
import os

accounts_file = "accounts.json"

# إنشاء ملف الحسابات لو مش موجود
if not os.path.exists(accounts_file):
    with open(accounts_file, "w") as f:
        json.dump({}, f)

# تحميل الحسابات من الملف
with open(accounts_file, "r") as f:
    user_accounts = json.load(f)

def save_accounts():
    with open(accounts_file, "w") as f:
        json.dump(user_accounts, f)

def register():
    print("\n🔐 Create your account:")
    username = input("Choose a username: ")
    if username in user_accounts:
        print("⚠️ Username already exists.")
        return register()

    password = input("Choose a password: ")
    user_accounts[username] = password
    save_accounts()
    print("✅ Account created successfully!\n")

def login():
    attempts = 3
    while attempts > 0:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in user_accounts and user_accounts[username] == password:
            print("✅ Login successful, welcome!")
            return True
        else:
            attempts -= 1
            print(f"❌ Incorrect. You have {attempts} attempts left.")
            if attempts == 0:
                print("⛔ You have been locked out.")
                sys.exit()

def main_menu():
    print("\n🌍 Welcome to the World of Travel & Fun Tools!")
    print("1️⃣ World Travel")
    print("2️⃣ Multiplication Table")
    print("3️⃣ Smart Calculator (Functions)")
    print("4️⃣ Simple Calculator")
    print("5️⃣ Even/Odd Separator")

    choice = input("👉 Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        print("Which continent do you want to visit?")
        print("1. Europe")
        print("2. Asia")
        print("3. Africa")
        continent = input("Enter your choice (1/2/3): ")

        if continent == "1":
            europe = ["France", "Germany", "Italy", "Spain", "Finland", "United Kingdom"]
            country = input("Choose a country (France, Germany, Italy, Spain, Finland, United Kingdom): ")
            if country in europe:
                print(f"🏰 Welcome to {country}!")
            else:
                print("❌ Invalid country! Please choose from the list.")

        elif continent == "2":
            asia = ["Japan", "China", "India", "Thailand", "Indonesia", "Korea"]
            country = input("Choose a country (Japan, China, India, Thailand, Indonesia, Korea): ")
            if country in asia:
                print(f"🗻 Welcome to {country}!")
            else:
                print("❌ Invalid country! Please choose from the list.")

        elif continent == "3":
            africa = ["Egypt", "Nigeria", "South Africa", "Ghana", "Kenya", "Morocco"]
            country = input("Choose a country (Egypt, Nigeria, South Africa, Ghana, Kenya, Morocco): ")
            if country in africa:
                print(f"🏜️ Welcome to {country}!")
            else:
                print("❌ Invalid country! Please choose from the list.")

        else:
            print("❌ Invalid continent selection.")

    elif choice == "2":
        num = int(input("Enter a number: "))
        print(f"\n📊 Multiplication Table of {num}:")
        for i in range(11):
            print(f"{num} x {i} = {num*i}")

    elif choice == "3":
        def add(a, b): return a + b
        def sub(a, b): return a - b
        def mul(a, b): return a * b
        def div(a, b): return "Error" if b == 0 else a / b

        print("🧮 Choose operation:")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
        op = input("Enter: ")
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if op == "1":
            print("Result:", add(a, b))
        elif op == "2":
            print("Result:", sub(a, b))
        elif op == "3":
            print("Result:", mul(a, b))
        elif op == "4":
            print("Result:", div(a, b))
        else:
            print("❌ Invalid choice.")

    elif choice == "4":
        op = input("Enter operator (+, -, x, /): ")
        a = int(input("First number: "))
        b = int(input("Second number: "))

        if op == "+":
            print("Result:", a + b)
        elif op == "-":
            print("Result:", a - b)
        elif op == "x":
            print("Result:", a * b)
        elif op == "/":
            if b != 0:
                print("Result:", a / b)
            else:
                print("Error: Cannot divide by zero.")
        else:
            print("❌ Invalid operator.")

    elif choice == "5":
        numbers = list(range(1, 21))
        evens = [n for n in numbers if n % 2 == 0]
        odds = [n for n in numbers if n % 2 != 0]
        print("🟦 Even numbers:", evens)
        print("🟥 Odd numbers:", odds)

    else:
        print("❌ Invalid choice. Please restart the program.")

# ====== تشغيل البرنامج ======
print("👋 Welcome!")
have_account = input("Do you have an account? (yes/no): ").lower()

if have_account == "yes":
    login()
elif have_account == "no":
    register()
    login()
else:
    print("Invalid input. Please restart the program.")
    sys.exit()

main_menu()
