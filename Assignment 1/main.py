### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,
            "ham": 4,
            "cheese": 4,
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,
            "ham": 6,
            "cheese": 8,
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,
            "ham": 8,
            "cheese": 12,
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,
    "ham": 18,
    "cheese": 24,
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        print("Please insert coins.")
        dollars = int(input("how many large dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))
        total = dollars * 1.0 + half_dollars * 0.5 + quarters * 0.25 + nickels * 0.05
        return total

    def transaction_result(self, coins, cost):
        if coins < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        else:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            return True

    def make_sandwich(self, sandwich_size, ingredients):
        for item in ingredients:
            self.machine_resources[item] -= ingredients[item]
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")


### Main program ###

machine = SandwichMachine(resources)

while True:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

    if choice == "off":
        break
    elif choice == "report":
        for item in machine.machine_resources:
            unit = "slice(s)" if item != "cheese" else "ounce(s)"
            print(f"{item.capitalize()}: {machine.machine_resources[item]} {unit}")
    elif choice in recipes:
        sandwich = recipes[choice]
        ingredients = sandwich["ingredients"]
        cost = sandwich["cost"]

        if machine.check_resources(ingredients):
            coins_inserted = machine.process_coins()
            if machine.transaction_result(coins_inserted, cost):
                machine.make_sandwich(choice, ingredients)
    else:
        print("Invalid option. Please choose small, medium, large, report, or off.")
