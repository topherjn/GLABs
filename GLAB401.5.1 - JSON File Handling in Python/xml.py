import xml.etree.ElementTree as ET

# Sample XML data
xml_data = """
<bookstore>
    <book>
        <title>Python Programming</title>
        <author>John Doe</author>
        <price>29.95</price>
    </book>
    <book>
        <title>Web Development</title>
        <author>Jane Smith</author>
        <price>19.99</price>
    </book>
</bookstore>
"""

# Parse the XML data
root = ET.fromstring(xml_data)

# Navigating XML Trees and Extracting Information
for book_element in root.findall("book"):
    title = book_element.find("title").text
    author = book_element.find("author").text
    price = float(book_element.find("price").text)
    
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Price: ${price:.2f}\n")

# Programmatically Modify XML Documents
for book_element in root.findall("book"):
    price_element = book_element.find("price")
    current_price = float(price_element.text)
    
    # Increase the price by 10%
    new_price = current_price * 1.10
    price_element.text = str(new_price)

# Create a new book element and add it to the XML
new_book_element = ET.Element("book")
new_title_element = ET.Element("title")
new_title_element.text = "Data Science"
new_author_element = ET.Element("author")
new_author_element.text = "Alice Johnson"
new_price_element = ET.Element("price")
new_price_element.text = "39.99"
new_book_element.append(new_title_element)
new_book_element.append(new_author_element)
new_book_element.append(new_price_element)
root.append(new_book_element)

# Serialize the modified XML to a string
modified_xml = ET.tostring(root, encoding="utf-8").decode()

# Print the modified XML
print("Modified XML:")
print(modified_xml)

# Using XPath to Query XML Data
print("\nUsing XPath:")
titles = root.findall(".//title")
for title in titles:
    print(f"Title: {title.text}")
