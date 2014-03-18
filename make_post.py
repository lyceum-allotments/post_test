import httplib, urllib
from multiprocessing import Process

headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}


conn = httplib.HTTPConnection("localhost:8000")

def request_location():
    params =  urllib.urlencode({'name': name, 'request_loc' : True})
    conn.request("POST", "/cgi-bin/test.py", params, headers)
    response = conn.getresponse()
    data = response.read()
    return data

def set_location(location):
    params =  urllib.urlencode({'name': name, 'set_loc' : location})
    conn.request("POST", "/cgi-bin/test.py", params, headers)
    response = conn.getresponse()
    data = response.read()


def test_location():
    old_location = request_location()
    while(True):
        new_location = request_location()
        if not old_location == new_location:
            print 
            print "location update!"
            print new_location
            old_location = new_location


p = Process(target=test_location)


name = raw_input("Enter name: ").lower()
p.start()

command = raw_input("Enter command: ").lower().split()


while(command[0] != "exit"):
    if command[0] == "request_location":
        print request_location()
    if command[0] == "set_location":
        set_location(command[1])
    command = raw_input("Enter command: ").lower().split()

p.terminate()
conn.close()
