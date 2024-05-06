# Diet-Tracker

## Project Objective
The objective of this project is to develop a comprehensive dietary tracking and management application that empowers users to effectively monitor and control their dietary habits. This application aims to assist users in achieving their personal health and fitness goals by providing them with the tools to log their dietary intake, analyze nutritional content, receive personalized dietary feedback, and track their progress towards set goals. The ultimate goal is to facilitate better nutritional awareness and healthier lifestyle choices through a user-friendly interface.

## Significance of the Project
In today's fast-paced world, where obesity and related health issues are prevalent, the Diet Tracker serves as a valuable resource for those seeking to take control of their dietary habits and weight management. By allowing users to track their caloric and macronutrient consumption, the application fosters awareness and informed decision-making, crucial for sustainable lifestyle changes. Additionally, the Diet Tracker's ability to provide personalized feedback empowers users to identify areas for improvement and make necessary adjustments to their diet and exercise routines.

One of the key novel aspects of the Diet Tracker is its integration of machine learning techniques for weight prediction and personalized plan generation. Unlike traditional calorie counting or generic diet plans, this application employs sophisticated algorithms to analyze the user's historical data and dietary habits, enabling accurate weight predictions and tailored recommendations. The weight prediction feature leverages machine learning models to identify patterns and relationships within the user's data, taking into account factors such as age, activity level, caloric intake, and macronutrient distribution. By employing advanced algorithms, the Diet Tracker can provide users with a projected weight trajectory, empowering them to make informed decisions and track their progress effectively.

Furthermore, the application's ability to generate customized weight loss and meal plans based on individual preferences and goals is a standout feature. By considering factors such as current weight, target weight, activity level, preferred diet type, and desired timeframe, the Diet Tracker tailors a comprehensive plan that maximizes the chances of successful weight management. This level of personalization sets the application apart from generic, one-size-fits-all approaches, ensuring that users receive a plan that aligns with their specific needs and preferences.

## Installation And Instruction To Use
### Installation
**For Windows and macOS:**
1. Ensure Python 3.8 or higher is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. The Diet Tracker application requires the following external libraries: NumPy, scikit-learn, joblib, and matplotlib. These libraries will be installed automatically during the setup process.
  
3. Clone the repository:
  ```bash
  git clone https://github.com/Sahilvp15/Diet-Tracker.git
  cd Diet-Tracker
```
### Usage Instructions
1. To start the application, ensure you are in the project's root directory, then execute the main script:
```bash
python main.py
```
This command initiates the application in the command line interface.
2. How to use the application:
- **Input Daily Diet Information**: Follow the prompts to enter daily diet data such as calories consumed, protein intake, etc.
- **Navigate the Menu:** Use the numbered menu to select different features like entering diet information, deleting an entry, or viewing diet data.
- **Diet Data and Feedback:** Access and review your entered diet data, get feedback on your nutritional intake compared to recommended values.
- **Predictions and Plans**: Use the application to predict future weight based on past data or to generate a weight loss plan tailored to your needs.

## Structure of the code
### Main.py
**Purpose**: Serves as the entry point for the application, orchestrating user interactions and managing the application flow.

**Main Functionalities**:
- **Initiates the user interface**: Manages the command line interface where users interact with the application.
- **Calls functions from functions.py based on user input**: Depending on the user's menu choice, different features are accessed.
- **print_menu()**: Prints a menu with the given options to navigate through various features like entering diet data, viewing diet reports, or receiving dietary advice.

### Functions.py
**Purpose**: Houses the core functionalities of the Diet Tracking App, from data handling to analysis and planning.

**Functions**:
- **Data Handling Functions**:
  - **load_data()**: Loads user diet data from a JSON file.
  - **save_data()**: Saves updated user data back to the JSON file.
- **User Input Handling Functions**:
  - **enter_diet_info()**: Allows the user to input new dietary information.
  - **delete_diet_info()**: Permits the deletion of a specific diet entry based on the date.
  - **display_data()**: Shows all stored diet entries in a readable format.
- **Analysis and Feedback Functions**:
  - **get_feedback()**: Analyzes the dietary data and provides nutritional feedback.
  - **predict_weight()**: Utilizes a machine learning model to predict future weight based on dietary intake.
- **Planning Functions**:
  - **recommend_weight_loss_plan()**: Generates a personalized weight loss plan.
  - **generate_meal_plan()**: Creates a detailed meal plan targeting specific macronutrient goals.
- **Machine Learning Model Handling Functions**:
  - **save_model()**, **load_model()**: Functions to manage the serialization and retrieval of machine learning models.
  - **log_prediction()**: Logs the details of weight predictions for monitoring and analysis.

### user_data.json
**Purpose**: Acts as the data store for the application, holding user-specific dietary entries in a structured JSON format.

**Functionality**:
- Stores each user's dietary data, including date, caloric intake, macronutrients, and weight.
- Accessed by `load_data()` and modified by `save_data()` to maintain and update user entries.

### rf_model.pkl
**Purpose**: Contains the serialized machine learning model used for predicting future weight.

**Functionality**:
- Holds the RandomForestRegressor model trained on historical dietary data.
- Utilized by `predict_weight()` to generate weight predictions based on new dietary inputs.

### Flow chart
                             +-------------------+
                             |    main.py        |
                             |                   |
                             | + Calls functions |
                             +---------+---------+
                                       |
                                       v
                             +---------+---------+
                             |   functions.py    |
                             |                   |
                             | + Manages data    |
                             | + Performs        |
                             |   calculations    |
                             | + Predicts        |
                             |   outcomes        |
                             +---------+---------+
                                       |
                                       v
                             +---------+---------+
                             | user_data.json    |
                             |                   |
                             | + Stores user     |
                             |   diet entries    |
                             | + Read/Write      |
                             |   operations      |
                             +-------------------+



## Functionalities and Test Results
- ### Diet Tracking Menu
![Screenshot 2024-04-23 094634](https://github.com/dravyaaa/Diet-Tracker/assets/107662465/e714b144-25aa-4bd5-8c5c-65b453f778cf)

- ### Diet Information for a day
![Screenshot 2024-04-23 094719](https://github.com/dravyaaa/Diet-Tracker/assets/107662465/4786d646-bd98-4a0f-9b02-6ff37c3cacc4)

- ### Data
![Screenshot 2024-04-23 094806](https://github.com/dravyaaa/Diet-Tracker/assets/107662465/bbd1ede9-ea6a-4d5f-94df-88a929faeab3)

- ### Feedback
![Screenshot 2024-04-23 094826](https://github.com/dravyaaa/Diet-Tracker/assets/107662465/573f4d21-eeb7-45b2-90c7-2f79be2c3a55)

- ### Deletion
![Screenshot 2024-04-23 094842](https://github.com/dravyaaa/Diet-Tracker/assets/107662465/26423632-f961-4618-bbbb-3dc71c3ff354)

- ### Weight Prediction
![Screenshot 2024-04-23 094901](https://github.com/dravyaaa/Diet-Tracker/assets/107662465/93fbfbb0-c011-4496-84f6-08bf71eba0e5)

- ### Weight Loss plan
![image](https://github.com/dravyaaa/Diet-Tracker/assets/43622669/75fd6693-cb67-4b0f-aaf7-21c758d8918a)


- ### Meal Plan
![image](https://github.com/dravyaaa/Diet-Tracker/assets/43622669/19716186-d6f2-4913-afc0-cf8f254999bf)



## Discussion and Conclusion
- **Project Issues**: While the code includes some input validation mechanisms, such as checking for valid date formats and numeric inputs, there is room for improvement in terms of comprehensive error handling and input validation. Robust error handling and input validation mechanisms would improve the application's resilience to unexpected inputs or edge cases, enhancing the overall user experience and preventing potential errors or crashes.

- **Limitations**: The models require detailed and continuous input of dietary and weight data over time to optimize predictions and recommendations effectively. In the early stages of data collection, the model's predictions may not be as reliable due to insufficient data, which could lead to less effective or generic dietary advice. This limitation could be particularly impactful for new users or those who cannot consistently input their dietary information. Enhancing the model's ability to provide valuable insights with limited data through more sophisticated predictive algorithms or incorporating external datasets could help mitigate this limitation.

- **Application of Course Learnings**: The project effectively demonstrates the application of various machine learning concepts taught in the course, such as regression models, ensemble methods, and data preprocessing techniques. By implementing models like RandomForestRegressor and GradientBoostingRegressor, the project provides practical experience in handling real-world data and predicting outcomes based on historical inputs. The use of ensemble learning to combine predictions from multiple models showcases an advanced technique to improve prediction accuracy. Additionally, the project's structure encourages understanding the full machine learning workflow from data collection and preprocessing to model training, evaluation, and deployment, aligning well with the course curriculum that covers these areas comprehensively. This hands-on application solidifies theoretical knowledge by addressing practical challenges and solutions in data science and machine learning.

