# Imports
import re
import json
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient
from flask import Flask

app = Flask(__name__)


@app.route('/')
def getall():
    # if __name__ == '__main__':
    # Variables & Setup
    client = FaunaClient(secret="fnAD0lh0uaACAIcRCRWTWllmNND-WpAZwgEicUVk")
    c = client.query(
        q.paginate(
            q.match(q.index('allFam')))
    )
    list1 = [c['data']]
    string = str(list1)
    pattern = '\d+'
    result = re.findall(pattern, string)
    index = (len(result))

    # for j in range(0, index, 1):
    #    print(result[j])dd
    #    i = result[j]
    #    c = client.query(q.get(q.ref(q.collection('person'), i)))
    #    list2 = [c['data']]
    #    print(list2)
    #    print("First Name:", list2[0].get("firstName"))
    #    print("Last Name:", list2[0].get("lastName"))

    return "First Name: " + str([client.query(q.get(q.ref(q.collection('person'), result[0])))['data']][0].get("firstName"))
