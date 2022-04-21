# -*- coding: utf-8 -*-

"""

Azure Functions HTTP Trigger Python Sample

"""


import os
import platform
import sys
import json

postreqdata = json.loads(open(os.environ['req']).read())
with open(os.environ['res'], 'w') as response:
    response.write("hello world from "+postreqdata['name'])

### dump 
#print("Python Version = '{0}'".format(platform.python_version()))  
#print(sys.version_info)
#for e in os.environ:
#    print ("{}->{}".format(e, os.environ[e]))
