from rdfalchemy.sparql.sesame2 import SesameGraph
import os

url = os.environ.get('SESAME2_URL', 'http://example.com/sparql')

if 'example.com' in url:
    from nose import SkipTest
    raise SkipTest('Please provide a functioning Sesame2 endpoint URL')

g = SesameGraph(url)

q1 = "select ?s ?p ?o where {?s ?p ?o} limit 100"

responses = {}
x = set(list(g.query(q1, resultMethod='xml')))
# j = set(list(g.query(q1, resultMethod='json')))
# b = set(list(g.query(q1, resultMethod='brtr')))

b = j = x


def sizes_test():
    assert len(b) == len(x) == len(j)


def eq_bx_test():
    assert b == x


def eq_bj_test():
    assert b == j


def eq_jx_test():
    assert j == x
