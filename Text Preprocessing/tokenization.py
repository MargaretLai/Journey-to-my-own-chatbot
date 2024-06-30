from nltk.tokenize import word_tokenize, sent_tokenize

ecg_text = 'An electrocardiogram is used to record the electrical conduction through a person\'s heart. The readings can be used to diagnose cardiac arrhythmias.'

words = word_tokenize(ecg_text)
sentences = sent_tokenize(ecg_text)