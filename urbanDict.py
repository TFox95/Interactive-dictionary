from udpy import UrbanClient
from decypher import decypher

#client = UrbanClient()

#defs =  client.get_definition("PAWG")

#for d in defs:
    #print(d.definition)

#    output = d.definition
#    decypher(output)
def urbansearch():
    term = input("What 'slang' do you want to search?")
    client = UrbanClient()
    defs = client.get_definition(term)
    for item in defs:
        output = item.definition
        decypher(output)
urbansearch()
