import os
import re
import string
from nltk.stem.porter import PorterStemmer

# Initialize the stemmer and stop words list
stemmer = PorterStemmer()
#stop_words = set(['a', 'an', 'the', 'and', 'or', 'in', 'on', 'at', 'to', 'of', 'for', 'by', 'with', 'is', 'are', 'was', 'were', 'be', 'been'])

# Open the stopword file and read its contents
with open("D:/Projects/Kennedy Juma Projects/Information-Retrieval-and-Web-Search/project1/stopwordlist.txt", "r") as f:
    stopword_list = f.read().splitlines()

# Remove any leading or trailing whitespaces from the stopword list
stopword_list = [word.strip() for word in stopword_list]

# Print the stopword list to verify that it was read correctly
#print(stopword_list)

# Create the indexing output folder if it does not exist
if not os.path.exists('Indexing_Output'):
    os.makedirs('Indexing_Output')

# Define the paths to the input and output files
input_path = "D:/Projects/Kennedy Juma Projects/Information-Retrieval-and-Web-Search/Text_Parser_output"
output_path = "D:/Projects/Kennedy Juma Projects/Information-Retrieval-and-Web-Search/Indexing_Output"

# Define the regular expression for finding words in the documents
word_regex = re.compile(r'\b\w+\b')

# Define dictionaries to store the forward index and inverted index
forward_index = {}
inverted_index = {}

# Define a function to preprocess a given document and return a list of stemmed words
def preprocess_document(doc):
    # Convert the document to lower case
    doc = doc.lower()

    # Remove all punctuation and numbers from the document
    doc = doc.translate(str.maketrans('', '', string.punctuation + string.digits))

    # Tokenize the document into individual words
    words = word_regex.findall(doc)

    # Remove stop words from the document
    words = [word for word in words if word not in stopword_list]

    # Stem the words using the Porter stemmer
    words = [stemmer.stem(word) for word in words]

    return words

# Loop through all the input files and build the forward and inverted indices
for filename in os.listdir(input_path):
    # Read in the contents of the file
    with open(os.path.join(input_path, filename), 'r') as f:
        doc = f.read()

    # Preprocess the document to get a list of stemmed words
    words = preprocess_document(doc)

    # Update the forward index with the list of words for this document
    doc_id = os.path.splitext(filename)[0]
    forward_index[doc_id] = words

    # Update the inverted index with the list of documents for each word
    for word in words:
        if word not in inverted_index:
            inverted_index[word] = {}
        if doc_id not in inverted_index[word]:
            inverted_index[word][doc_id] = 0
        inverted_index[word][doc_id] += 1

# Write the forward index to a file
with open(os.path.join(output_path, "forward_index.txt"), 'w') as f:
    for doc_id, words in forward_index.items():
        word_counts = {}
        for word in words:
            if word not in word_counts:
                word_counts[word] = 0
            word_counts[word] += 1
        output_str = f"{doc_id}:"
        for word, count in word_counts.items():
            output_str += f" {word}:{count}"
        output_str += "\n"
        f.write(output_str)
print("Done writing to forward_indexing.txt")

# Write the inverted index to a file
with open(os.path.join(output_path, "inverted_index.txt"), 'w') as f:
    for word, docs in inverted_index.items():
        output_str = f"{word}:"
        for doc_id, count in docs.items():
            output_str += f" {doc_id}:{count}"
        output_str += "\n"
        f.write(output_str)
print("Done writing to inverted_indexing.txt")

