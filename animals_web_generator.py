import data_fetcher


def get_animal_from_user():
    while True:
            animal = input("Enter a name of an animal: ").strip()
            if not animal:
                print("Animal name cannot be empty.")
            else:
                return animal


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
    animal_name = get_animal_from_user()
    data = data_fetcher.fetch_data(animal_name)
    template = read_template('animals_template.html')
    animals_text = add_animals_to_template(template, data)
    write_animals_file(animals_text)


if __name__ == '__main__':
    main()