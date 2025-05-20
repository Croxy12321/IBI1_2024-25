import xml.sax  # Import SAX module for event-driven XML parsing
import time     # Import time module to measure execution time

# Define a custom handler class 
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        # Initialize variables 
        self.current_element = ""
        self.namespace = ""
        self.term_id = ""
        self.name = ""
        self.is_a_count = 0

        # Create a dictionary to store the term with the most is_a tags in each category
        self.max_terms = {
            "molecular_function": {"id": "", "name": "", "count": 0},
            "biological_process": {"id": "", "name": "", "count": 0},
            "cellular_component": {"id": "", "name": "", "count": 0}
        }

    # Triggered when a tag starts
    def startElement(self, tag, attributes):
        self.current_element = tag
        # Reset term data when a new <term> begins
        if tag == "term":
            self.namespace = ""
            self.term_id = ""
            self.name = ""
            self.is_a_count = 0

    # Triggered when characters inside a tag are read
    def characters(self, content):
        content = content.strip()  # Remove leading and trailing whitespace
        # Accumulate data based on which element is being read
        if self.current_element == "id":
            self.term_id += content
        elif self.current_element == "name":
            self.name += content
        elif self.current_element == "namespace":
            self.namespace += content
        elif self.current_element == "is_a":
            self.is_a_count += 1  # count occurrences; content not needed

    # Triggered when a tag ends
    def endElement(self, tag):
        # When </term> ends, check if it has the most is_a in its category
        if tag == "term" and self.namespace in self.max_terms:
            if self.is_a_count > self.max_terms[self.namespace]["count"]:
                self.max_terms[self.namespace] = {
                    "id": self.term_id,
                    "name": self.name,
                    "count": self.is_a_count
                }
        # Reset current element tracker
        self.current_element = ""


start_time = time.time()  # Record start time

parser = xml.sax.make_parser()      # Create SAX parser
handler = GOHandler()               # Instantiate our custom handler
parser.setContentHandler(handler)   # Assign the handler to the parser

# Parse the XML file
parser.parse("C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical14/go_obo.xml")

# Output results 
for ns, data in handler.max_terms.items():
    print(f"{ns.title().replace('_', ' ')}: {data['id']}, {data['name']}, {data['count']} is_a terms")

end_time = time.time()  # Record end time
print(f"\nSAX parsing took: {end_time - start_time:.4f} seconds")

# SAX was faster
