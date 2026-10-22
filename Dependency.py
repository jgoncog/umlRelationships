class Document:
    def __init__(self, content: str):
        self.content = content


class Printer:
    
    def print_doc(self, doc: Document):
        print(f"Printing: {doc.content}")



doc = Document("Hello World")
printer = Printer()


printer.print_doc(doc)  
