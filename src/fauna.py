# Imports
import re
import json
from faunadb import query as q
from faunadb.objects import Ref
from src.config import client


def getfam():
    c = client.query(
        q.paginate(
            q.match(q.index('allFam')))
    )
    list1 = [c['data']]
    string = str(list1)
    pattern = '\d+'
    result = re.findall(pattern, string)

    return "First Name: " + str(
        [client.query(q.get(q.ref(q.collection('person'), result[0])))['data']][0].get("firstName"))


def getfamlastname():
    c = client.query(
        q.paginate(
            q.match(q.index('allFam')))
    )
    list1 = [c['data']]
    string = str(list1)
    pattern = '\d+'
    result = re.findall(pattern, string)

    return "Last Name: " + str(
        [client.query(q.get(q.ref(q.collection('person'), result[0])))['data']][0].get("lastName"))
