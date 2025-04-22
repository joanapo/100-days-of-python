import requests
import datetime

APP_ID = "YOUR_APP_ID"
API_KEY = "YOUR_API_KEY"

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "YOUR_SHEETY_API_ENDPOINT"

GENDER = "YOUR_GENDER"
WEIGHT_KG = "YOUR WEIGHT INT"
HEIGHT_CM = "YOUR HEIGHT INT"
AGE = "YOUR AGE INT"


query = input("Enter what exercise you did today: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

nutritionix_params = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=nutritionix_params, headers=headers)
result = response.json()

auth_header = {
    "Authorization": "YOUR AUTH KEY"
}

today = datetime.datetime.now()

for exercise in result["exercises"]:
    data = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=data, headers=auth_header)
    print(f"Google Sheet amended. \nWorkout details: "
          f"\nDate: {data['workout']['date']},"
          f"\nTime: {data['workout']['time']},"
          f"\nExercise: {data['workout']['exercise']},"
          f"\nDuration: {data['workout']['duration']},"
          f"\nCalories: {data['workout']['calories']}."
          f"\nGood job!")