import os
import requests
from dotenv import load_dotenv


def get_animal_from_user():
    while True:
            animal = input("Enter a name of an animal: ").strip()
            if not animal:
                print("Animal name cannot be empty.")
            else:
                return animal


def get_data_from_api(api_key, animal):

    url = f"https://api.api-ninjas.com/v1/animals?name={animal}"
    headers = {'X-Api-Key': api_key}

    response = requests.get(url, headers=headers)

    if response.status_code == requests.codes.ok:
        # Die Daten als JSON-Dictionary ausgeben
        animals_data = response.json()
        return (animals_data)
    else:
        print(f'Fehler: {response.status_code} - {response.text}')


def get_animal_data(animals_data):
    """
    Iterate through the animals_data and get
    the following information for each one:
    - Name
    - Diet
    - The first location from the list of locations
    - Type
    """
    return ''.join(serialize_animal(animal_obj) for animal_obj in animals_data)


def serialize_animal(animal_obj):
    """Creates an HTML list item string for a single animal, safely accessing nested data."""
    output = ""
    name = animal_obj.get("name")

    # Safe access to characteristics dictionary
    characteristics = animal_obj.get("characteristics", {})
    diet = characteristics.get("diet")
    animal_type = characteristics.get("type")

    # Safe access to locations list (take the first location if it exists)
    locations = animal_obj.get("locations", [])
    location = locations[0] if locations else None

    output += '<li class = "cards_item">'
    if name is not None:
        output += f'<div class="card__title">Name: {name}</div>\n'
    output += '<p class="card__text">'
    if diet is not None:
        output += f'<strong>Diet:</strong> {diet}<br/>\n'
    if location is not None:
        output += f'<strong>Location:</strong> {location}<br/>\n'
    if animal_type is not None:
        output += f'<strong>Type:</strong> {animal_type}<br/>\n'
    output += '</p>'
    output += '</li>'
    output += '\n'  # Empty print for spacing
    return output


def read_template(template_path):
    """Reads an HTML template file with error handling."""
    try:
        with open(template_path, "r") as fileobj:
            return fileobj.read()
    except FileNotFoundError:
        print(f"Error: The template file '{template_path}' was not found.")


def add_animals_to_template(template, output):
    animals_text = template.replace("__REPLACE_ANIMALS_INFO__", output)
    return animals_text


def write_animals_file(animals_text):
    with open("animals.html", "w") as fileobj:
        fileobj.write(animals_text)
    print("Website was successfully generated to the file animals.html.")


def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    animal = get_animal_from_user()
    animals_data = get_data_from_api(api_key, animal)
    output = get_animal_data(animals_data)
    template = read_template('animals_template.html')
    animals_text = add_animals_to_template(template, output)
    write_animals_file(animals_text)


if __name__ == '__main__':
    main()