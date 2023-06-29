import re
import os
from nltk.stem import PorterStemmer

# Set up the Porter Stemmer
ps = PorterStemmer()

# Create dictionaries to store the mappings
word_to_id = {}
file_to_id = {}

# Define the tokenizer function
def tokenizer(text):
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    # Split on non-alphanumeric characters and convert to lowercase
    tokens = re.findall(r'\w+', text.lower())
    # Ignore words with numbers
    tokens = [token for token in tokens if not any(char.isdigit() for char in token)]
    return tokens

# Define the function to build the word dictionary
def build_word_dictionary(tokens):
    # Iterate over the tokens
    for token in tokens:
        # Stem the token
        stemmed_token = ps.stem(token)
        # Add the token to the word dictionary if it's not already there
        if stemmed_token not in word_to_id:
            word_to_id[stemmed_token] = len(word_to_id) + 1

# Define the function to build the file dictionary
def build_file_dictionary(file_path):
    # Add the file to the file dictionary if it's not already there
    if file_path not in file_to_id:
        file_to_id[file_path] = len(file_to_id) + 1

# Define the main function to parse the documents
def parse_documents(data_directory):
    # Iterate over the files in the data directory
    for file_name in os.listdir(data_directory):
        # Read in the file
        with open(os.path.join(data_directory, file_name), 'r') as file:
            text = file.read()
        # Tokenize the text
        tokens = tokenizer(text)
        # Build the word dictionary
        build_word_dictionary(tokens)
        # Build the file dictionary
        build_file_dictionary(file_name)
        # Print out the tokens and document IDs
        print_tokens_and_document_ids(tokens, file_name)

# Define the function to print out the tokens and document IDs
def print_tokens_and_document_ids(tokens, file_name):
    # Create the folder if it does not exist
    if not os.path.exists('Text_Parser_output'):
        os.makedirs('Text_Parser_output')
    # Get the document ID from the file dictionary
    document_id = file_to_id[file_name]
    # Print out the tokens and document ID in the required format
    with open('Text_Parser_output/parser_output.txt', 'a') as f:
        for token in tokens:
            token_id = word_to_id[ps.stem(token)]
            f.write(token + '\t' + str(token_id) + '\n')
        f.write(file_name + '\t' + str(document_id) + '\n')

# Run the parser on the TREC data
folder_path = 'D:/Projects/Kennedy Juma Projects/Information-Retrieval-and-Web-Search/project1/ft911'
parse_documents(folder_path)
print("Done writing to parser_output.txt")