import time
from xml.dom.minidom import parse

start_time = time.time()
dom_tree = parse("C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical14/go_obo.xml")
collection = dom_tree.documentElement
terms = collection.getElementsByTagName("term")
max_terms = {
    "molecular_function": {"id": "", "name": "", "count": 0},
    "biological_process": {"id": "", "name": "", "count": 0},
    "cellular_component": {"id": "", "name": "", "count": 0}
}
for term in terms:
    namespace = term.getElementsByTagName("namespace")[0].firstChild.nodeValue
    term_id = term.getElementsByTagName("id")[0].firstChild.nodeValue
    name = term.getElementsByTagName("name")[0].firstChild.nodeValue
    is_a_count = len(term.getElementsByTagName("is_a"))

    if namespace in max_terms and is_a_count > max_terms[namespace]["count"]:
        max_terms[namespace] = {"id": term_id, "name": name, "count": is_a_count}
for ns, data in max_terms.items():
    print(f"{ns.title().replace('_', ' ')}: {data['id']}, {data['name']}, {data['count']} is_a terms")

end_time = time.time()
print(f"\nDOM parsing took: {end_time - start_time:.4f} seconds")

# 记得写一句注释说明：# SAX was faster（或相反）
