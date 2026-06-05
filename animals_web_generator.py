import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

def get_animal_data(animals_data):
    """
    Iterate through the animals_data and get
    the following information for each one:
    - Name
    - Diet
    - The first location from the list of locations
    - Type
    """
    output = ""  # define an empty string
    for animal_obj in animals_data:
        # append information to each string
        output += serialize_animal(animal_obj)
    return output

def serialize_animal(animal_obj):
    output = ""
    name = animal_obj.get("name")
    diet = animal_obj["characteristics"].get("diet")
    location = animal_obj["locations"][0]
    animal_type = animal_obj["characteristics"].get("type")
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
    with open(template_path, "r") as fileobj:
        template = fileobj.read()
        return template

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