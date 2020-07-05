import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        user_input = input("Did you mean %s instead? Enter y(es) or n(o): " % get_close_matches(word, data.keys())[0])
        if user_input.lower() == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif user_input.lower() == "n":
            return "That word doesn't exist.  Try again."
        else:
            return "What didn't you understand about entering yes or no?"
    else:
        return "That word does not exist.  Please double check it."

word = input("Enter word: ").lower()

print(translate(word))
