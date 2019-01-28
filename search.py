from pprint import pprint

from numpy import require

import requests
from elasticsearch import Elasticsearch

res = requests.get('http://localhost:9200')
es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

# res = es.search(index='myindex', body={'query': {'match': {'heading':'Collection'}}})
# pprint(res)


# res = es.search(index='myindex', body={
#     'query': {
#         'bool': {
#             'must': [{
#                 'match': {
#                     'heading': 'collection'
#                 }
#             }]
#         },
#
#     }
# })
#
# pprint((res['hits']['hits']))


# res = es.search(index='myindex', body={
#   "query": {
#           "term": {
#             "content": "collection"
#           }
#         },
#         # {
#         #   "term": {
#         #     "status": "normal"
#         #   }
#         # }
#     })
#
# pprint(len(res['hits']['hits']))
#
result = es.search(index= 'myindex', body={
    "query": {
        "query_string": {
            "query" : "implement deep copy add copy constructors associated class. copy constructor takes instance 'this' single argument copies values it. work, pretty straightforward safe. EDIT: note don't accessor methods read fields. access fields directly source instance type instance copy constructor. Obvious overlooked."
        }
    }
})

pprint(result['hits']['hits'])


# result = es.search(index= 'myindex', body={
#     "query": {
#         "query_string" : {
#             "fields" : ["content", "heading"],
#             "query" : "for OR for each"
#         }
#     }
# })

pprint(len(result['hits']['hits']))