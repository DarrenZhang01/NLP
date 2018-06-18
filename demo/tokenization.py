# Simple tokenization using NLTK
import nltk
text = "How are you today?"

tokenizer = nltk.tokenize.WhitespaceTokenizer()
print(tokenizer.tokenize(text))
