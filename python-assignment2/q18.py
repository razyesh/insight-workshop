"""
18. Find a package in the Python standard library for dealing with
JSON. Import the library module and inspect the attributes of the
module. Use the help function to learn more about how to use the
module. Serialize a dictionary mapping 'name' to your name and 'age'
to your age, to a JSON string. Deserialize the JSON back into
Python.
"""

import json


def serialize_json(sample_dict):
    """Serializing JSON Data"""
    return json.dumps(sample_dict, indent=4)


def deserialize_json(sample_json):
    """De-serializing JSON Data"""
    return json.loads(sample_json)


result = serialize_json({'name':'Rajesh Pudasaini', 'age':21})
print("Serialize Json: ", result)
result = deserialize_json(result)
print("Deserialize Json: ", result)