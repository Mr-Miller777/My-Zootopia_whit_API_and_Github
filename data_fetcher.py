import os
import requests
from dotenv import load_dotenv
import animals_web_generator



def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
        ...
      },
      'locations': [
        ...
      ],
      'characteristics': {
        ...
      }
    },
    """
    load_dotenv()
    api_key = os.getenv("API_KEY")
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {'X-Api-Key': api_key}

    response = requests.get(url, headers=headers)

    if response.status_code == requests.codes.ok:
        # Die Daten als JSON-Dictionary ausgeben
        animals_data = response.json()

        if len(animals_data) == 0:
            return f"<h2>The animal '{animal_name}' does not exist.</h2>"
        else:
            return ''.join(animals_web_generator.serialize_animal(animal_obj) for animal_obj in animals_data)
    else:
        print(f'Fehler: {response.status_code} - {response.text}')
