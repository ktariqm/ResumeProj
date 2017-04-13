'''
Created on Apr 12, 2017

@author: khurr
'''
# def add(a,b):
#     return a+b
# 
# def addFixedValue(a):
#         y = 5
#         return y +a
# 
# print add(1,2)
# print addFixedValue(1)

# This was the solution on StackOverflow http://stackoverflow.com/questions/20199126/reading-json-from-a-file
# import json
#
# with open('strings.json') as json_data:
#     d = json.load(json_data)
#     print(d)


# import os

# currdir = os.getcwd()
# print (currdir)
# 
# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)


import json
import sys

try:
    passed_filename = str(sys.argv[1])
    with open(passed_filename) as json_data:
        resume_data = json.load(json_data)
        print(json.dumps(resume_data, indent=4))

except IOError:
    print "Record not found."


    #print(resume_data)
