import spacy
from spacy import displacy
from subprocess import call

try:
    NER = spacy.load("it_core_news_md")
except OSError:
    print("SpaCy model not found. Downloading...")
    call(["python", "-m", "spacy", "download", "it_core_news_md"])
    NER = spacy.load("it_core_news_md")


input_file = "../output/Antipasti/Bicchierini alla birra con crema al parmigiano.txt"
with open(input_file, "r", encoding='utf-16') as f:
    text = ''.join(f.readlines())


def pinpoint_spacy(sentence):
    """
    Function to pinpoint the entities in a sentence using spaCy.
    """
    doc = NER(sentence)
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_, spacy.explain(ent.label_))
    return [ent for ent in doc.ents if ent.label_ == "GPE"]


print(pinpoint_spacy(text))
