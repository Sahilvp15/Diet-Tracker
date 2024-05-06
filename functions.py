import numpy as np
import json
import os
import datetime
import joblib
from joblib import dump
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, VotingRegressor
from sklearn.ensemble import VotingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR
import matplotlib.pyplot as plt

# Load the updated data
def load_data(file_path='user_data.json'):
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        return []

def save_data(data, file_path='user_data.json'):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Function to validate date input
def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%m/%d/%Y")
        return True
    except ValueError:
        return False

def enter_diet_info():
    user_data = load_data()

    # Date input with validation
    date_str = input("\nEnter date (mm/dd/yyyy): ")
    while not validate_date(date_str):
        print("Invalid date format. Please enter the date in the format mm/dd/yyyy.")
        date_str = input("Enter date (mm/dd/yyyy): ")

    # Age input with validation
    age = input("Enter your age: ")
    while not age.isdigit() or int(age) <= 0 or int(age) > 120:
        print("Invalid input. Age must be a positive number less than 120.")
        age = input("Enter your age: ")

    # Activity level input with validation
    activity_level = input("Enter your activity level (1-5): ")
    while not activity_level.isdigit() or int(activity_level) < 1 or int(activity_level) > 5:
        print("Invalid activity level. Please enter a number between 1 and 5.")
        activity_level = input("Enter your activity level (1-5): ")

    # Caloric intake input with validation
    calories = input("Enter calories consumed: ")
    while not calories.replace('.', '', 1).isdigit() or float(calories) <= 0:
        print("Invalid input. Please enter a valid number for calories.")
        calories = input("Enter calories consumed: ")

    # Protein input with validation
    protein = input("Enter protein (g): ")
    while not protein.replace('.', '', 1).isdigit() or float(protein) <= 0:
        print("Invalid input. Please enter a valid number for protein.")
        protein = input("Enter protein (g): ")

    # Carbohydrates input with validation
    carbs = input("Enter carbohydrates (g): ")
    while not carbs.replace('.', '', 1).isdigit() or float(carbs) <= 0:
        print("Invalid input. Please enter a valid number for carbohydrates.")
        carbs = input("Enter carbohydrates (g): ")

    # Fat input with validation
    fat = input("Enter fat (g): ")
    while not fat.replace('.', '', 1).isdigit() or float(fat) <= 0:
        print("Invalid input. Please enter a valid number for fat.")
        fat = input("Enter fat (g): ")

    # Weight input with validation
    weight = input("Enter current weight (kg): ")
    while not weight.replace('.', '', 1).isdigit() or float(weight) <= 0:
        print("Invalid input. Please enter a valid number for weight.")
        weight = input("Enter current weight (kg): ")

    # Append the new entry
    user_data.append({
        "date": date_str,
        "age": int(age),
        "activity_level": int(activity_level),
        "calories": float(calories),
        "protein": float(protein),
        "carbs": float(carbs),
        "fat": float(fat),
        "weight": float(weight)
    })

    save_data(user_data)
    print("\nDiet information recorded successfully.")

def delete_diet_info():
    user_data = load_data()  # Load the existing data

    if not user_data:
        print("\nNo data available to delete.")
        return

    # Display existing entries with dates for user to choose
    print("\nExisting Entries:")
    for entry in user_data:
        print(f"Date: {entry['date']}")

    # Ask user for the date they want to delete
    date_str = input("\nEnter the date of the entry to delete (mm/dd/yyyy): ")

    # Check if the date exists in the data
    found = False
    for i, entry in enumerate(user_data):
        if entry['date'] == date_str:
            found = True
            break

    if found:
        # Remove the entry
        del user_data[i]
        save_data(user_data)  # Save the updated data back to the file
        print(f"Entry for {date_str} deleted successfully.")
    else:
        print("No entry found for the specified date.")

def display_data():
    user_data = load_data()
    if not user_data:
        print("\nNo data to display.")
        return

    print("\nDiet Data:")
    for info in user_data:
        print(f"\nDate: {info['date']}")
        print(f"Age: {info['age']}")
        print(f"Activity Level: {info['activity_level']}")
        print(f"Calories: {info['calories']}")
        print(f"Protein: {info['protein']} g")
        print(f"Carbohydrates: {info['carbs']} g")
        print(f"Fat: {info['fat']} g")
        print(f"Weight: {info['weight']} kg")
        print("-" * 20)

def get_feedback():
    # Load the user data
    user_data = load_data()

    # Check if there is any data to provide feedback
    if not user_data:
        print("\nNo data to provide feedback.")
        return

    # Calculate macronutrient percentages
    total_calories = sum(info['calories'] for info in user_data)
    total_protein = sum(info['protein'] for info in user_data)
    total_carbs = sum(info['carbs'] for info in user_data)
    total_fat = sum(info['fat'] for info in user_data)

    if total_calories == 0:  # Prevent division by zero if total_calories is zero
        print("Insufficient data to calculate macronutrient percentages.")
        return

    protein_percent = (total_protein * 4 * 100) / total_calories
    carbs_percent = (total_carbs * 4 * 100) / total_calories
    fat_percent = (total_fat * 9 * 100) / total_calories

    print("\nDiet Feedback:")
    print(f"\nAverage calories per day: {total_calories / len(user_data):.2f}")
    print(f"Protein intake: {protein_percent:.2f}% (Recommended: 10-35%)")
    print(f"Carbohydrate intake: {carbs_percent:.2f}% (Recommended: 45-65%)")
    print(f"Fat intake: {fat_percent:.2f}% (Recommended: 20-35%)")

    if protein_percent < 10 or protein_percent > 35:
        print("\nConsider adjusting your protein intake to meet the recommended range.")
    if carbs_percent < 45 or carbs_percent > 65:
        print("\nConsider adjusting your carbohydrate intake to meet the recommended range.")
    if fat_percent < 20 or fat_percent > 35:
        print("\nConsider adjusting your fat intake to meet the recommended range.")

def save_model(model, filename='model.pkl'):
    joblib.dump(model, filename)

def load_model(filename='model.pkl'):
    return joblib.load(filename)

def log_prediction(date, actual, predicted):
    with open('predictions_log.txt', 'a') as file:
        file.write(f"{date}: Actual Weight - {actual}, Predicted Weight - {predicted}\n")


# Predict weight using the trained model
def predict_weight():
    # Load and prepare data
    user_data = load_data()
    data = np.array([[d['age'], d['activity_level'], d['calories'], d['protein'], d['carbs'], d['fat'], d['weight']] for d in user_data])
    X, y = data[:, :-1], data[:, -1]

    # Train model
    model = RandomForestRegressor(max_depth=3, n_estimators=50, random_state=42)
    model.fit(X, y)
    dump(model, 'rf_model.pkl')  # Save the model

    # Get the last entry's data
    last_entry = user_data[-1]
    next_day_data = [last_entry['age'] + 1] + [last_entry[feature] for feature in ['activity_level', 'calories', 'protein', 'carbs', 'fat']]
    prediction = model.predict([next_day_data])[0]

    # Plot results
    dates = [datetime.datetime.strptime(d['date'], "%m/%d/%Y") for d in user_data]
    plt.figure(figsize=(10, 5))
    plt.plot(dates, y, 'bo-', label='Historical Weights')
    plt.plot(dates[-1] + datetime.timedelta(days=1), prediction, 'ro', label='Predicted Weight')
    plt.xlabel('Date')
    plt.ylabel('Weight')
    plt.title('Weight Prediction and Progress')
    plt.legend()
    plt.grid(True)
    plt.show()

    log_prediction(user_data[-1]['date'], last_entry['weight'], prediction)

    return prediction


def create_weight_loss_plan(current_weight, target_weight, activity_level, preferred_diet, timeframe):

    np.random.seed(42)
    X_train = np.random.rand(100, 5) * 100  # 100 samples, 5 features
    y_train = np.random.rand(100) * 2000 + 1200  # 100 samples, target between 1200 and 3200 calories

    # Encode preferred diet from text to a numeric value
    diet_types = {'vegan': 1, 'low-carb': 2, 'high-protein': 3, 'balanced': 4}
    diet_code = diet_types.get(preferred_diet.lower(), 0)  # default to 0 if not found

    # Define models
    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    gb = GradientBoostingRegressor(n_estimators=100, random_state=42)
    svr = SVR(kernel='linear')

    # Create ensemble
    ensemble = VotingRegressor(estimators=[('rf', rf), ('gb', gb), ('svr', svr)])

    # Fit ensemble model
    ensemble.fit(X_train, y_train)

    # Generate feature vector for prediction
    feature_vector = [current_weight, target_weight, activity_level, diet_code, timeframe]

    # Predict daily calorie intake and macronutrient distribution
    daily_calories = ensemble.predict([feature_vector])[0]

    # Create plan
    weight_loss_plan = {
        'Daily Calories': daily_calories,
        'Protein (g)': daily_calories * 0.15 / 4,  # Example calculation
        'Carbs (g)': daily_calories * 0.55 / 4,
        'Fat (g)': daily_calories * 0.30 / 9,
        'Duration (weeks)': timeframe
    }

    return weight_loss_plan


def recommend_weight_loss_plan():
    current_weight = float(input("Enter your current weight (kg): "))
    target_weight = float(input("Enter your target weight (kg): "))
    activity_level = int(input("Enter your daily activity level (1-5): "))
    preferred_diet = input("Enter your preferred diet (Balanced, low-carb, high-protein, vegan): ")
    timeframe = int(input("Enter the timeframe to achieve the target weight (in weeks): "))

    plan = create_weight_loss_plan(current_weight, target_weight, activity_level, preferred_diet, timeframe)
    return plan

def generate_meal_plan(target_protein, target_carbs, target_fat):
    # Load user data
    user_data = load_data()

    # Prepare data
    data = np.array([[d['protein'], d['carbs'], d['fat'], d['calories']] for d in user_data])
    X, y = data[:, :-1], data[:, -1]

    # Define models
    lr = LinearRegression(n_jobs=-1)
    dt = DecisionTreeRegressor()
    nn = MLPRegressor(hidden_layer_sizes=(10, 10), max_iter=5000)  # Deep neural network

    # Create ensemble
    ensemble = VotingRegressor(estimators=[('lr', lr), ('dt', dt), ('nn', nn)])

    # Fit ensemble model
    ensemble.fit(X, y)

    # Generate meal plan using the ensemble model
    target_macros = [target_protein, target_carbs, target_fat]
    predicted_meal_calories = ensemble.predict([target_macros])[0]

    meal_plan = {
        'Breakfast': {
            'Calories': predicted_meal_calories * 0.25,
            'Protein': target_protein * 0.25,
            'Carbs': target_carbs * 0.25,
            'Fat': target_fat * 0.25
        },
        'Lunch': {
            'Calories': predicted_meal_calories * 0.35,
            'Protein': target_protein * 0.35,
            'Carbs': target_carbs * 0.35,
            'Fat': target_fat * 0.35
        },
        'Dinner': {
            'Calories': predicted_meal_calories * 0.40,
            'Protein': target_protein * 0.40,
            'Carbs': target_carbs * 0.40,
            'Fat': target_fat * 0.40
        }
    }

    return meal_plan