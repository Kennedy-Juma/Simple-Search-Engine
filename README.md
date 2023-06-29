****ABOUT THE PROJECT****
This project includes two main components: the Text Parser and the Indexer. The purpose of the Text Parser is to preprocess a given text corpus, extract individual words and their corresponding document IDs, and output the results to a file called parser_output.txt. The Indexer takes the output of the Text Parser and constructs a forward index and an inverted index for the text corpus.

****TEXT PARSER****
The Text Parser is implemented in the file TextParser.py. It takes a path to a directory containing text files as input and produces a file called parser_output.txt as output. This output file is stored in Text_Parser_output directory. The output file contains one line per word occurrence in the input text files, with each line consisting of a document ID, a word ID, and a frequency count. The parser also removes any stop words and applies a stemming algorithm (Porter stemmer) to the remaining words.

****INDEXER****
The Indexer is implemented in the file IndexConstruction.py. It takes the parser_output.txt file from the Text Parser as the input and produces two index files: a forward index(forward_index.txt) and an inverted index(inverted_index.txt). The forward index contains one line per document, with each line consisting of a document ID and a list of word IDs and their corresponding frequencies in that document. The inverted index contains one line per word, with each line consisting of a word ID and a list of document IDs and their corresponding frequencies in which the word occurs. The indexing algorithm used is the vector space model.

****RETRIEVAL SYSTEM****
This is a simple retrieval system that allows you to search through a collection of documents for a specific word or phrase. The program searches through the inverted index file for the specified word or phrase, and return a list of the documents that contain that word or phrase, along with their frequencies.

****How to run the code****
To run the Text Parser, open a command prompt and type python TextParser.py.

To run the Indexer, open a command prompt and type python IndexConstruction.py.

To run the Retrieval, open a command prompt and type python RetrievalSystem.py.

Note: -Please make sure that you have read and write permissions to the input and output directories.
	  -Change the directory path containing the parser files to where your files are located in both the two .py files.
****OUTPUT****
After running the Text Parser a parser_output.txt file will be produced in Text_Parser_output directory.On running the IndexConstruction.py, two index files will be produced in the Indexing_Output directory: forward_index.txt and inverted_index.txt. The forward_index.txt file contains the forward index, and the inverted_index.txt file contains the inverted index.

****Required Libraries****
Before running the TextParser.py and IndexConstruction.py, install the following packages:
nltk: pip install nltk