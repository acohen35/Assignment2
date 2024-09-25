class Cashier:
    def __init__(self):
        self.machine_resources= None

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        large_dollars = int(input("How many large dollars ($1)?: "))
        half_dollars = int(input("How many half dollars ($0.5)?: "))
        quarters = int(input("How many quarters?: "))
        nickels = int(input("How many nickels?: "))

        return (large_dollars * 1.00) + (half_dollars * 0.50) + (quarters * 0.25) + (nickels * 0.05)

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        else:
            change = (coins - cost)
            if change > 0:
                print(f"Here is ${change:.2f} in change.")
            return True

    def report(self):
        """"Prints current resource levels."""
        if self.machine_resources:
            for item, quantity in self.machine_resources.items():
                print(f"{item.capitalize()}: {quantity}")
        else:
            print("Resource data not available.")