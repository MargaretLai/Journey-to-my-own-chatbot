from nltk import RegexpParser

pos_tagged_text = []

chunk_grammar  = "AZ: {<JJ><NN>}"
chunk_parser = RegexParser(chunk_grammar)

result = chunk_parser.parse(pos_tagged_text)