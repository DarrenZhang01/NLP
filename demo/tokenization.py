# Simple tokenization using NLTK
import nltk
text = "How are you today?"
# White space tokenization
tokenizer = nltk.tokenize.WhitespaceTokenizer()
print("\n")
print("Below is the WhitespaceTokenizer for text")
print(tokenizer.tokenize(text))

text1 = "What's your name?"
# Tree bank word tokenization
tokenizer1 = nltk.tokenize.TreebankWordTokenizer()
print("Below is the TreebankWordTokenizer for text1")
print(tokenizer1.tokenize(text1))

print("Below is the WhitespaceTokenizer for text1")
print(tokenizer.tokenize(text1))

# Word punctuation tokenization
tokenizer2 = nltk.tokenize.WordPunctTokenizer()
print("Below is the WordPunctTokenizer for text1")
print(tokenizer2.tokenize(text1))
