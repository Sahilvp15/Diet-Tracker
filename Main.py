# main.py
import functions

def print_menu():
    print("Diet Tracking Menu")
    print("------------------")
    print("1. Enter diet information for the day")
    print("2. Delete a diet entry")
    print("3. Display all data")
    print("4. Get feedback")
    print("5. Predict future weight")
    print("6. Get a weight loss plan")
    print("7. Get a meal plan")
    print("8. Exit")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-8): ")
        if not choice.isdigit() or int(choice) < 1 or int(choice) > 8:
            print("\nInvalid choice. Please enter a number from 1 to 8.")
            continue

        choice = int(choice)
        if choice == 1:
            functions.enter_diet_info()
        elif choice == 2:
            functions.delete_diet_info()
        elif choice == 3:
            functions.display_data()
        elif choice == 4:
            functions.get_feedback()
        elif choice == 5:
            print("\nPredicting weight using enhanced model...")
            print("Predicted weight:", functions.predict_weight())
        elif choice == 6:
            print("\nGenerating weight loss plan...")
            plan = functions.recommend_weight_loss_plan()
            print("\nRecommended Weight Loss Plan:")
            for key, value in plan.items():
                print(f"{key}: {value}")
        elif choice == 7:
            print("\nGenerating meal plan...")
            target_protein = float(input("Enter target protein (g): "))
            target_carbs = float(input("Enter target carbohydrates (g): "))
            target_fat = float(input("Enter target fat (g): "))
            meal_plan = functions.generate_meal_plan(target_protein, target_carbs, target_fat)
            print("\nMeal Plan:")
            for meal, details in meal_plan.items():
                print(f"\n{meal}:")
                for macronutrient, value in details.items():
                    print(f"{macronutrient}: {value:.2f}")
        elif choice == 8:
            print("\nExiting...")
            break
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
