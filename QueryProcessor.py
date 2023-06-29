class QueryProcessor:
    def __init__(self, forward_index, inverted_index):
        self.forward_index = forward_index
        self.inverted_index = inverted_index

    def process_query(self, query):
        query_terms = query.split()
        results = set(self.forward_index.get(query_terms[0], []))
        for term in query_terms[1:]:
            term_results = set(self.forward_index.get(term, []))
            results = results.intersection(term_results)
        sorted_results = sorted(list(results))
        return sorted_results

    def process_query_inverted(self, query):
        query_terms = query.split()
        results = set(self.inverted_index.get(query_terms[0], {}).keys())
        for term in query_terms[1:]:
            term_results = set(self.inverted_index.get(term, {}).keys())
            results = results.intersection(term_results)
        sorted_results = sorted(list(results))
        return sorted_results

forward_index = {'foo': [1, 2], 'bar': [2, 3], 'baz': [1, 3]}
inverted_index = {
    1: {'foo': 1, 'baz': 1},
    2: {'foo': 1, 'bar': 1},
    3: {'bar': 1, 'baz': 1}
}

qp = QueryProcessor(forward_index, inverted_index)


# Test inverted index implementation
result = qp.process_query_inverted('foo bar')
#print(result) # prints [2]

# Read queries from file
with open('topics.txt', 'r') as f:
    queries = f.readlines()

# Remove newline characters and split queries
queries = [query.strip().split() for query in queries]

# Process queries
for query in queries:
    result = qp.process_query(' '.join(query))
    print(f"Query: {' '.join(query)}")
    print(f"Results: {result}\n")


