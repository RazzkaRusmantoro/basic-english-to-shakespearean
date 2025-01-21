import spacy
import json
import re

nlp = spacy.load("en_core_web_sm")

# Load the translation dictionary
with open("data/word_mapping.json", "r") as file:
    translation_dict = json.load(file)

def translation(text):
    doc = nlp(text)

    transformed_tokens = []

    for token in doc:
        # Check if token is in the dictionary and replace it
        if token.text.lower() in translation_dict:
            transformed_token = translation_dict[token.text.lower()]
        else:
            transformed_token = token.text

        transformed_tokens.append(transformed_token)

    transformed_text = ' '.join(transformed_tokens)

    # Clean up extra spaces
    transformed_text = re.sub(r'\s([,!.?;])', r'\1', transformed_text)
    transformed_text = re.sub(r'\s+-\s+', '-', transformed_text)
    transformed_text = re.sub(r"'\s", "'", transformed_text)

    # Capitalize the first letter of sentences
    transformed_text = re.sub(r'([.!?])\s*(\w)', lambda m: m.group(1) + ' ' + m.group(2).upper(), transformed_text)

    # Capitalize starting letter of overall text
    transformed_text = transformed_text[0].upper() + transformed_text[1:]

    return transformed_text.strip()
