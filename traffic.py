print()
print("         ===========================================")
print("             What Does the Traffic Light Say? ")
print("                Enter a Color Below (👇)")
print()
print("             ▂▃▅▇█▓▒░  N A M E  ░▒▓█▇▅▃▂")
print("                 Aayush Singh")
print("                 From Nepal 🇳🇵")
print("         ===========================================")
print()

user = input("Enter traffic light colour (Red / Yellow / Green): ")
x = user.lower()

match x:
    case 'red':
        print("\n           🚦 Light: RED")
        print("           🛑 Action: STOP!")
    case 'yellow':
        print("\n           🚦 Light: YELLOW")
        print("           ⚠️ Action: SLOW DOWN!")
    case 'green':
        print("\n           🚦 Light: GREEN")
        print("           ✅ Action: GO!")
    case _:
        print("\n           ❌ Invalid color. Please enter red, yellow, or green.")
