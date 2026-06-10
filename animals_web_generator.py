import json


def load_data(file_path):
    """ Loads a JSON file with error handling for missing files. """
    try:
        with open(file_path, "r") as handle:
            return json.load(handle)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' contains invalid JSON.")
        sys.exit(1)


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


def main():
    animals_data = load_data('animals_data.json')
    output = get_animal_data(animals_data)
    template = read_template('animals_template.html')
    animals_text = add_animals_to_template(template, output)
    write_animals_file(animals_text)


if __name__ == '__main__':
    main()