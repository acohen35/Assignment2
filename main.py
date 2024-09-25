import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


resources = data.resources
recipes = data.recipes
sandwich_maker = SandwichMaker(resources)
cashier = Cashier()


cashier.machine_resources = resources

def main():
    while True:
        choice = input("What would you like? (small/medium/large/off/report): ").lower()
        if choice == "off":
            break
        elif choice == "report":
            cashier.report()
        elif choice in recipes:
            if sandwich_maker.check_resources(recipes[choice]["ingredients"]):
                payment = cashier.process_coins()
                if cashier.transaction_result(payment, recipes[choice]["cost"]):
                    sandwich_maker.make_sandwich(choice, recipes[choice]["ingredients"])
                    print(f"{choice.capitalize()} sandwich is ready. Bon Appétit!")
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()