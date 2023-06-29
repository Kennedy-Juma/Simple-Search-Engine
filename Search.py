# Define the path to the inverted index file
inverted_index_path = "D:/Projects/Kennedy Juma Projects/Information-Retrieval-and-Web-Search/Indexing_Output/inverted_index.txt"
forward_index_path = "D:/Projects/Kennedy Juma Projects/Information-Retrieval-and-Web-Search/Indexing_Output/forward_index.txt"
topics = "D:/Projects/Kennedy Juma Projects/Information-Retrieval-and-Web-Search/topics.txt"
# Read in the contents of the forward index file
with open(forward_index_path, 'r') as f:
    forward_index = f.readlines()

# Read in the contents of the inverted index file
with open(inverted_index_path, 'r') as f:
    inverted_index = f.readlines()

#query = 'This is a sample query'

with open('topics.txt', 'r') as f:
    queries = f.read()
    terms = queries.split()
    #print(terms)

with open('stopwordlist.txt', 'r') as f:
    stopwords = f.read()


import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Preprocess the query terms
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

preprocessed_terms = []
for term in terms:
    # Remove non-alphabetic characters
    term = re.sub(r'[^a-zA-Z]', '', term)
    # Convert to lowercase
    term = term.lower()
    # Remove stop words
    if term not in stop_words:
        # Stem the term
        term = stemmer.stem(term)
        preprocessed_terms.append(term)
#print(preprocessed_terms)

import os
import re
import math
from collections import defaultdict
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Define the path to the collection directory
collection_dir = "/path/to/collection"

# Define the path to the inverted index file
inverted_index_path = inverted_index

# Define the path to the stop words file
stop_words_path = stop_words

# Define the path to the query file
query_path = topics

# Define the path to the output file
output_path = "Retrieval_Output/output.txt"

# Define the number of top results to retrieve
num_results = 10

# Load the stop words
stop_words = set()
with open('stopwordlist.txt', "r") as f:
    for line in f:
        stop_words.add(line.strip())

# Define the Porter stemmer
stemmer = PorterStemmer()

# Preprocess a query term
def preprocess_query_term(term):
    # Remove non-alphabetic characters
    term = re.sub(r'[^a-zA-Z]', '', term)
    # Convert to lowercase
    term = term.lower()
    # Remove stop words
    if term not in stop_words:
        # Stem the term
        term = stemmer.stem(term)
        return term
    else:
        return None

# Preprocess a query
def preprocess_query(query):
    # Tokenize the query into individual terms
    terms = query.split()
    # Preprocess each query term
    preprocessed_terms = [preprocess_query_term(term) for term in terms]
    # Remove None values (stop words, etc.)
    preprocessed_terms = [term for term in preprocessed_terms if term is not None]
    return preprocessed_terms

# Calculate the TF-IDF weight of a term in a document
def calculate_tf_idf(term, doc_id, term_freq, doc_lengths, num_docs):
    tf = term_freq[term][doc_id]
    idf = math.log(num_docs / len(term_freq[term]))
    return tf * idf / doc_lengths[doc_id]

# Calculate the length of a document vector
def calculate_doc_length(doc_vector):
    return math.sqrt(sum([weight**2 for weight in doc_vector.values()]))

# Calculate the cosine similarity between two vectors
def calculate_cosine_similarity(query_vector, doc_vector):
    dot_product = sum([query_vector[term] * doc_vector[term] for term in query_vector if term in doc_vector])
    query_length = math.sqrt(sum([weight**2 for weight in query_vector.values()]))
    doc_length = calculate_doc_length(doc_vector)
    if query_length > 0 and doc_length > 0:
        return dot_product / (query_length * doc_length)
    else:
        return 0.0

# Read in the collection and preprocess the documents
doc_terms = defaultdict(list)
doc_lengths = defaultdict(float)
num_docs = 0
for filename in os.listdir("D:/Projects/Kennedy Juma Projects/Information-Retrieval-and-Web-Search/Indexing_Output"):
    with open(os.path.join("D:/Projects/Kennedy Juma Projects/Information-Retrieval-and-Web-Search/Indexing_Output", filename), "r") as f:
        # Read in the document text
        text = f
print(text)
