# Create the indexing output folder if it does not exist
import os

if not os.path.exists('Retrieval_Output'):
    os.makedirs('Retrieval_Output')

# Define the path to the inverted index file
inverted_index_path = "D:/Projects/Kennedy Juma Projects/Information-Retrieval-and-Web-Search/Indexing_Output/inverted_index.txt"

# Define the word to search for
search_word = input('Enter a word to search:')

# Read in the contents of the inverted index file
with open(inverted_index_path, 'r') as f:
    inverted_index_lines = f.readlines()

# Search for the word in the inverted index
for line in inverted_index_lines:
    if line.startswith(search_word):
        docs = line.split(':')[1].strip().split()

        for doc in docs:
            if ':' in doc:
                doc_id, count = doc.split(':')
                #print(f"Document {doc_id} ID: {doc_id}, Frequency: {count}")


            else:
                doc_id = doc
                count = 1
                #print(f"Document {doc_id} ID: {doc_id}, Frequency: {count}")
                output_file = open("Retrieval_Output/output.txt", "w")

                output_string = f"Document {doc_id} ID: {doc_id}, Frequency: {count}"

                output_file.write(output_string)

                output_file.close()
        break
print(f"Done searching. Check output.txt in RetrievalSystem folder")