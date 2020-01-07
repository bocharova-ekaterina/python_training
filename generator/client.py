from model.client import Client
import random
import string
import os.path
import json
import getopt
import sys

try:
    opts, args=getopt.getopt(sys.argv[1:], "n:f:", ["number of client", "file"])
except getopt.GetoptError as error:
    getopt.usage()
    sys.exit(2)


n=5
f="data/clients.json"


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10 + string.punctuation
    return prefix + " ".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


testdata = [Client(firstname="", lastname="", address="", home="", mobile="", work="", email="",email2="", email3="")] +[
            Client(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20),
            home=random_string("home", 10), mobile=random_string("mobile", 10), work=random_string("work", 10),
            email=random_string("email", 20), email2=random_string("email2", 20), email3=random_string("email3", 20))
            for i in range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
