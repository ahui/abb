#!/usr/bin/python
# coding=utf-8

def sbv0(adict,reverse=False):
    return sorted(adict.iteritems(), key=lambda (k,v): (v,k), reverse=reverse)

def sbv1(d,reverse=False):
    L = [(k,v) for (k,v) in d.iteritems()]
    return sorted(L, key=lambda x: x[1] , reverse=reverse)

def sbv2(d,reverse=False):
    return sorted(d.items(), key=lambda x: x[1] , reverse=reverse)

def sbv3(d,reverse=False):
    L = ((k,v) for (k,v) in d.iteritems())
    return sorted(L, key=lambda x: x[1] , reverse=reverse)

def sbv4(d,reverse=False):
    return sorted(d.iteritems(), key=lambda x: x[1] , reverse=reverse)

from operator import itemgetter
def sbv5(d,reverse=False):
    return dict(sorted(d.iteritems(), key=itemgetter(0), reverse=reverse))

D = dict(zip(range(100),range(10)))
#D = {"100":1,"200":9,"300":2}
print D
print sbv5(D, reverse=False)
print D
#from profile import run
#run("for ii in xrange(1000):  sbv0(D, reverse=True)")
#run("for ii in xrange(1000):  sbv1(D, reverse=True)")
#run("for ii in xrange(1000):  sbv2(D, reverse=True)")
#run("for ii in xrange(1000):  sbv3(D, reverse=True)")
#run("for ii in xrange(1000):  sbv4(D, reverse=True)")
#run("for ii in xrange(10000):  sbv5(D, reverse=True)")
