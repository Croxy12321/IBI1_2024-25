import xml.sax
import time

class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_element = ""
        self.namespace = ""
        self.term_id = ""
        self.name = ""
        self.is_a_count = 0
        self.max_terms = {
            "molecular_function": {"id": "", "name": "", "count": 0},
            "biological_process": {"id": "", "name": "", "count": 0},
            "cellular_component": {"id": "", "name": "", "count": 0}
        }

    def startElement(self, tag, attributes):
        self.current_element = tag
        if tag == "term":
            self.namespace = ""
            self.term_id = ""
            self.name = ""
            self.is_a_count = 0

    def characters(self, content):
        content = content.strip()
        if self.current_element == "id":
            self.term_id += content
        elif self.current_element == "name":
            self.name += content
        elif self.current_element == "namespace":
            self.namespace += content
        elif self.current_element == "is_a":
            self.is_a_count += 1

    def endElement(self, tag):
        if tag == "term" and self.namespace in self.max_terms:
            if self.is_a_count > self.max_terms[self.namespace]["count"]:
                self.max_terms[self.namespace] = {
                    "id": self.term_id,
                    "name": self.name,
                    "count": self.is_a_count
                }
        self.current_element = ""

start_time = time.time()

parser = xml.sax.make_parser()
handler = GOHandler()
parser.setContentHandler(handler)
parser.parse("C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical14/go_obo.xml")

for ns, data in handler.max_terms.items():
    print(f"{ns.title().replace('_', ' ')}: {data['id']}, {data['name']}, {data['count']} is_a terms")

end_time = time.time()
print(f"\nSAX parsing took: {end_time - start_time:.4f} seconds")

