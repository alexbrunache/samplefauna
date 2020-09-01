# Imports
import re
import json
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient
# from config import getSecret
from config import getGCPSecret

# Variables & Setup
client = FaunaClient(secret=getGCPSecret())
# client = FaunaClient(secret=getSecret())


# if __name__ == '__main__':
def getall(self):

    c = client.query(
        q.paginate(
            q.match(q.index('allFam')))
    )
    list1 = [c['data']]
    string = str(list1)
    pattern = '\d+'
    result = re.findall(pattern, string)

    return "First Name: " + str([client.query(q.get(q.ref(q.collection('person'), result[0])))['data']][0].get("firstName"))
    # print("First Name: " + str([client.query(q.get(q.ref(q.collection('person'), result[0])))['data']][0].get(
    # "firstName"))) 
