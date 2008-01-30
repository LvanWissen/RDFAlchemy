#!/usr/bin/env python
# encoding: utf-8
"""
orm.py

Created by Philip Cooper on 2007-11-23.
Copyright (c) 2007 Openvest. All rights reserved.
"""

from rdfalchemy import rdfObject, rdflibAbstract

import logging
log=logging.getLogger('rdfAlchemy')

def allsub(cl):
    "return all subclasses of the given class"
    sub = set(cl.__subclasses__())
    for onesub in cl.__subclasses__():
        sub |= allsub(onesub)
    return sub
    

def mapper(*classes):
    """Map the classes given to allow descriptors with ranges to the proper Class of that type
    default if no args is to map all subclasses(recursivly) of rdfObject
    
    preforms the mapping
    
    returns a dict of {rdf_type: mapped_class} for further processing"""
    if not classes:
        classes = allsub(rdfObject)
    class_dict = dict([(str(cl.rdf_type), cl) for cl in classes])
    for cl in classes:  # for each class
        for v in cl.__dict__.values():  # for each desciptor
            if isinstance(v,rdflibAbstract) and v.range_type:  #if its a descriptor with a range
                try:
                    v._mappedClass = class_dict[str(v.range_type)] 
                except KeyError:
                    log.warn("No Class Found\nFailed to map %s range of %s"%(v,v.range_type))
    return class_dict

#def mapBase(baseclass):
#    """This maps all classes below baseclass as in mapper()
#    AND puts the dict of {rdf_type: mapped_class}  in an baseclass.type2class attribute"""
#    baseclass.type2class = mapper(allsub(baseclass))
    