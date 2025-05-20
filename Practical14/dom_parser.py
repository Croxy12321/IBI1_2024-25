import time
from xml.dom.minidom import parse  # Import DOM parser from xml.dom.minidom

# Record start time
start_time = time.time()

# Parse the XML file and build a DOM tree in memory
dom_tree = parse("C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical14/go_obo.xml")

# Get the root element (e.g., <obo>)
collection = dom_tree.documentElement

# Get all <term> elements under the root
terms = collection.getElementsByTagName("term")

# Dictionary to store the term with the highest number of <is_a> elements in each namespace
max_terms = {
    "molecular_function": {"id": "", "name": "", "count": 0},
    "biological_process": {"id": "", "name": "", "count": 0},
    "cellular_component": {"id": "", "name": "", "count": 0}
}

# Iterate through all <term> elements
for term in terms:
    # Extract values from child elements
    namespace = term.getElementsByTagName("namespace")[0].firstChild.nodeValue
    term_id = term.getElementsByTagName("id")[0].firstChild.nodeValue
    name = term.getElementsByTagName("name")[0].firstChild.nodeValue
    is_a_count = len(term.getElementsByTagName("is_a"))  # Count <is_a> elements

    # If this term has more <is_a> than the current maximum for its namespace, update the record
    if namespace in max_terms and is_a_count > max_terms[namespace]["count"]:
        max_terms[namespace] = {"id": term_id, "name": name, "count": is_a_count}

# Print results
for ns, data in max_terms.items():
    print(f"{ns.title().replace('_', ' ')}: {data['id']}, {data['name']}, {data['count']} is_a terms")

end_time = time.time() # Record end time
print(f"\nDOM parsing took: {end_time - start_time:.4f} seconds")

# SAX was faster
