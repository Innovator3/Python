import re

def find_entities_in_text(text, person_info):
    entities = []
    for key, value in person_info.items():
        matches = re.finditer(value.lower(), text.lower())
        for match in matches:
            entities.append([match.start(), match.end(), value])
    entities.sort()
    return entities

story = "My name is N.R.Bhargav, and at present, I'm working in Hallmark Global Technologies in Kakinada city. Kakinada is famous for Sweets and cinema roads. My Favourite part of Kakinada is the beach"
person = {
    "name": "N.R.Bhargav",
    "company": "Hallmark Global Technologies",
    "city": "Kakinada",
    "favourite": "Beach",
}

result = find_entities_in_text(story, person)
print(result)
