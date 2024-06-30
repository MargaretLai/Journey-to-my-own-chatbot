# Text Normalization is not needed every time
''' Types of normalzation: 
        - Upper or lowercasing
        - Stopword removal
        - Stemming – bluntly removing prefixes and suffixes from a word
        - Lemmatization – replacing a single-word token with its root
'''

# Upper or lowercasing
brands = 'Salvation Army, YMCA, Boys & Girls Club of America'

brands_lower = brands.lower()
brands_upper = brands.upper()



# Stopword removal
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))    # Create a set of stop words

survey_text = 'A YouGov study found that American\'s like Italian food more than any other country\'s cuisine.'

tokenized_text = word_tokenize(survey_text)
tokenized_text_no_stop = [word for word in tokenized_text if word not in stop_words]



# Stemming (stemming is the text preprocessing normalization task concerned with bluntly removing word affixes (prefixes and suffixes).)
from nltk.stem import PorterStemmer

populated_island = 'Java is an Indonesian island in the Pacific Ocean. It is the most populated island in the world, with over 140 million people.'

stemmer = PorterStemmer()
tokenized = word_tokenize(populated_island)
stemmed_words = [stemmer.stem(word) for word in tokenized]



# Lemmatization (a method for casting words to their root forms.)
from nltk.stem import WordNetLemmatizer

populated_island = 'Indonesia was founded in 1945. It contains the most populated island in the world, Java, with over 140 million people.'

lemmatizer = WordNetLemmatizer()

tokenized_island = word_tokenize(populated_island)

lemmatized_island = [lemmatizer.lemmatize(word) for word in tokenized_island]   #lemmatize() treats every word as a noun

# To improve the performance of lemmatization, find the part of speech for each word in string
from nltk.corpus import wordnet
from collections import Counter

def get_part_of_speech(word):
  probable_part_of_speech = wordnet.synsets(word)
  
  pos_counts = Counter()

  pos_counts["n"] = len(  [ item for item in probable_part_of_speech if item.pos()=="n"]  ) # noun
  pos_counts["v"] = len(  [ item for item in probable_part_of_speech if item.pos()=="v"]  ) # verb
  pos_counts["a"] = len(  [ item for item in probable_part_of_speech if item.pos()=="a"]  )
  pos_counts["r"] = len(  [ item for item in probable_part_of_speech if item.pos()=="r"]  )
  
  most_likely_part_of_speech = pos_counts.most_common(1)[0][0]
  return most_likely_part_of_speech

lemmatized_pos = [lemmatizer.lemmatize(word, get_part_of_speech(word)) for word in tokenized_string]
