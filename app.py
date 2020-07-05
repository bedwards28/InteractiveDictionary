import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        return "Did you mean %s instead?" % get_close_matches(word, data.keys())[0]
    else:
        return "That word does not exist.  Please double check it."

word = input("Enter word: ").lower()

print(translate(word))
