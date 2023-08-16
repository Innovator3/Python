def common_characters(str1, str2):
    common_chars = set(str1) & set(str2)
    return common_chars




def calculate_similarity(string1, string2):
    total_characters = set(string1) | set(string2)
    similarity = len(common_chars_set) / len(total_characters)
    return similarity

string1 = "hello"
string2 = "hola"


common_chars_set = common_characters(string1, string2)
print("Common characters:", common_chars_set)  

similarity = calculate_similarity(string1, string2)
print("Similarity:", similarity)