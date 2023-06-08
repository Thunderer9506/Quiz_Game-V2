import requests
response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()
question_data = response.json()["results"]