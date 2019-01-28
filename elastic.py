import requests
import json
import os
from elasticsearch import Elasticsearch

directory = 'extra1'
res = requests.get('http://localhost:9200')
# print (res.content)
es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])
#
no = 1

for filename in os.listdir(directory):
    if filename.endswith(".json"):
        print(filename)
        filename = directory + '/' + filename
        f = open(filename)
        docket_content = f.read()

        es.index(index='wikibooks_java', ignore=400, doc_type='docket', id=no, body=json.loads(docket_content))

        no = no + 1

# Practice Push
# # ElasticSearch settings
# ES_CLUSTER = 'http://localhost:9200/'
# ES_INDEX = 'test'
# ES_TYPE = 'doc'
# es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
# e1={
#     "first_name":"nitin",
#     "last_name":"panwar",
#     "age": 27,
#     "about": "Love to play cricket",
#     "interests": ['sports','music'],
# }
#
# e2={
#     "first_name" :  "Jane",
#     "last_name" :   "Smith",
#     "age" :         32,
#     "about" :       "I like to collect rock albums",
#     "interests":  [ "music" ]
# }
# e3={
#     "first_name" :  "Douglas",
#     "last_name" :   "Fir",
#     "age" :         35,
#     "about":        "I like to build cabinets",
#     "interests":  [ "forestry" ]
# }
#
# # print(e1)
#
# res = es.index(index='megacorp',doc_type='employee',id=1,body=e1)
#
# res=es.index(index='megacorp',doc_type='employee',id=2,body=e2)
# # print(res['created'])
# res = es.index(index='megacorp',doc_type='employee',id=3,body=e3)
# print(res['result'])
#
#
# # res=es.get(index='megacorp',doc_type='employee',id=3)
# # print(res)
# # print(res['_source'])
#
# # res=es.delete(index='megacorp',doc_type='employee',id=3)
# # print(res['result'])
#
# #
# res= es.search(index='megacorp',body={'query':{'match_all':{}}})
# print('Got %d hits' %res['hits']['total'])
#
# res= es.search(index='megacorp',body={'query':{'match':{'first_name':'nitin'}}})
# print(res['hits']['hits'])
#
# # print(es.search(index="ecommerce", body={"query": {"match_phrase": {"name": "Zend"}}}))
# # json_docs = []
# # for filename in os.listdir('/Users/janit/ASU/CSE 591/Assignment 2/extra'):
# #     if filename.endswith('.json'):
# #         with open('extra/'+filename) as open_file:
# #             json_docs.append(json.load(open_file))
# #
# # es.bulk(ES_INDEX, ES_TYPE, json_docs)