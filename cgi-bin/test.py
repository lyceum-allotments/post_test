#! /usr/bin/python2
import cgi 
import json
import cgitb

cgitb.enable()

form = cgi.FieldStorage()

fp = open("locations.json", "r")
loc_string = fp.read()

print "Content-Type: text/html"
print 

if "request_loc" in form:
    print loc_string
elif "set_loc" in form:
    locations = json.loads(loc_string)
    locations[form["name"].value] = form["set_loc"].value
    fp = open("locations.json", "w")
    fp.write(json.dumps(locations))

fp.close()
