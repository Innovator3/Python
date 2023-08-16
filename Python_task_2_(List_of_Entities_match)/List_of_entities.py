def find_entities_in_text(text, person_info):
    entities = []
    for key, value in person_info.items():
        value_lower = value.lower()
        text_lower = text.lower()
        start = 0
        while start < len(text_lower):
            start = text_lower.find(value_lower, start)
            if start == -1:
                break
            end = start + len(value_lower)
            entities.append([start, end, value])
            start = end
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
