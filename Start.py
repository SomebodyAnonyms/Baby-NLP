import spacy
from collections import Counter

Spacy_analyzer = spacy.load("en_core_web_sm")

Text = input("Enter your text: ")
Spacy_text = Spacy_analyzer(Text)

Sentences = [str(i) for i in Spacy_text.sents]
Words = []
Dependency = []
Parse_label = []
Part_of_speech = []
Lemma = []
Words_filtered = []
for i in Spacy_text:
    Words.append(i.text)
    Dependency.append((i.text, i.head.text, [child for child in i.children]))
    Parse_label.append((i, i.dep_))
    Part_of_speech.append((i, i.pos_))
    Lemma.append((str(i), i.lemma_))
    if not i.is_stop: Words_filtered.append(i)
Words_frequency = Counter(Words_filtered).most_common()
Morphology = None
Entities = [(i.text, i.label_, spacy.explain(i.label_), i.kb_id_) for i in Spacy_text.ents]
Sentiment = None
Categories = None

print(Sentences)
print(Words)
print(Words_filtered)
print(Words_frequency)
print(Dependency)
print(Parse_label)
print(Part_of_speech)
print(Lemma)
print(Morphology)
print(Entities)
print(Sentiment)
print(Categories)
