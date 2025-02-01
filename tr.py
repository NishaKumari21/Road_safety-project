import time

print("HAVE A SAFE JOURNEY!!")
def traffic_light():
    # while True:
        light_choice = input("Enter 'r' for Red, 'y' for Yellow, 'g' for Green: ").strip().lower()
        if light_choice == 'r':
            print("🛑 RED LIGHT - STOP")
            time.sleep(5)
        elif light_choice == 'y':
            print("⚠️ YELLOW LIGHT - GET READY")
            time.sleep(2)
        elif light_choice == 'g':
            print("✅ GREEN LIGHT - GO")
            time.sleep(5)
        else:
            print("Invalid choice! Please enter 'r', 'y', or 'g'.")

def helpline():
    print("India:")
    print("National Road Safety Helpline: 1033")
    print("Traffic Police Helpline: 100 (Police Emergency)")
    print("Ambulance/Medical Emergency: 102")
    print("Fire Emergency: 101")
    print("Road Transport: 1800-180-4321")

while True:
    a = input("1.HELP 2.SAFETY_TIPS 3.CONTINUE YOUR JOURNEY! (or type 'exit' to quit): ")

    if a == "1":
        helpline()
    elif a == "2":
        print("Here are the safety tips:")
        print("1. Always wear your seatbelt 🦺")
        print("2. Follow speed limits ⚡")
        print("3. Avoid distractions 📱🚫")
        print("4. Obey traffic signals 🛑🚦")
        print("5. Maintain a safe following distance 🚗↔️🚗")
        print("6. Use turn signals 🔄💡")
        print("7. Drive defensively 🛣️👀")
        print("8. Don’t drink and drive 🍻❌🚗")
        print("9. Use headlights properly 💡🚘")
        print("10. Check blind spots 👀⚠️")
        print("11. Adjust driving to weather 🌧️❄️🌫️")
        print("12. Stop for school buses 🚌🛑")
        print("13. Maintain your vehicle 🛠️🚗")
        print("14. Be cautious at intersections ⛔🚦")
        print("15. Yield to pedestrians 🚶‍♂️🚶‍♀️")
        print("16. Plan your route ahead 🗺️🚘")
    elif a == "3":
        traffic_light()
    elif a == "exit" or "Exit":
        print("Thank you! Have a safe journey!")
        break  
    else:
        print("Invalid choice! Please enter '1', '2', or '3' (or 'exit' to quit).")
