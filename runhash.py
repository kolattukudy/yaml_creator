import hashlib
import os
import glob

# Regular imports
from copy import deepcopy

# Yaml loaders and dumpers
from ruamel.yaml.main import \
    round_trip_load as yaml_load, \
    round_trip_dump as yaml_dump

# Yaml commentary
from ruamel.yaml.comments import \
    CommentedMap as OrderedDict, \
    CommentedSeq as OrderedList

# For manual creation of tokens
from ruamel.yaml.tokens import CommentToken
from ruamel.yaml.error import CommentMark
# Globals
# Number of spaces for an indent 
INDENTATION = 2 
# Used to reset comment objects
tsRESET_COMMENT_LIST = [None, [], None, None]


"""
resource_string = OrderedDict({
            "auth": OrderedList([OrderedDict({"type": "s3","id": "falkonry"}),
                [OrderedDict({"filename": file_name,"url": "s3://falkonry-platform-one-dev/"+file_name})],
                [OrderedDict({"validation": OrderedList([OrderedDict({
                    "type": "sha256",
                    "value": hash})
                ])
            })]])
        })
"""
def create_yaml_string(file_name,hash):
    resource_string = OrderedDict({
                "resource": OrderedList([OrderedDict({

                    "auth": OrderedDict({
                        "type": "s3",
                        "id": "falkonry",
                        "region": "us-west-2"}),
                   
               "filename": file_name,
                "url": "s3://falkonry-platform-one-dev/"+file_name,
                "validation": OrderedDict({
                    "type": "sha256",
                    "value": hash})
                
            
        })])
        })
    return yaml_dump(resource_string)



def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha256()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       for byte_block in iter(lambda: file.read(4096),b""):
            # update the hash object
            h.update(byte_block)

   # return the hex representation of digest
   return h.hexdigest()


file_list=glob.glob("tilingcontainerwhls/*")
#file_list = [os.path.basename(x) for x in glob.glob("tilingcontainerwhls/*")]

myfile = open('harden.txt', 'w')

for file in file_list:
  hash = hash_file(file)
  yaml_string=create_yaml_string(os.path.basename(file),hash)
  print(yaml_string)
  myfile.write(yaml_string)
myfile.close()
  
