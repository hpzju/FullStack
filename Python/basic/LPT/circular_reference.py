#!/usr/bin/env python

##################################################
# {circular reference example}
##################################################
# {License_info}
##################################################
# Author: {hubert_hao}
# Copyright: Copyright {2019}, {project_name}
# Credits: [{credit_list}]
# License: {license}
# Version: {mayor}.{minor}.{rel}
# Maintainer: {maintainer}
# Email: {contact_email}
# Status: {dev_status}
##################################################

import gc
import ctypes


def ref_count(address):
    return ctypes.c_long.from_address(address).value


def gc_check(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            print(f"found: {hex(object_id)}")
            return True
    print(f"not found: {hex(object_id)}")
    return False


class A(object):
    def __init__(self):
        self.b = B(self)
        print(f"""Constructor A:
        a {hex(id(self))} : {ref_count(id(self))}
        b {hex(id(self.b))} : {ref_count(id(self.b))}
         """)

    def __del__(self):
        print(f"""Destructor A:
        a {hex(id(self))} : {ref_count(id(self))}
        b {hex(id(self.b))} : {ref_count(id(self.b))}
         """)


class B(object):
    def __init__(self, a):
        self.a = a
        print(f"""Constructor B:
        b {hex(id(self))} : {ref_count(id(self))}
        a {hex(id(self.a))} : {ref_count(id(self.a))}
         """)

    def __del__(self):
        print(f"""Destructor B:
        b {hex(id(self))} : {ref_count(id(self))}
        a {hex(id(self.a))} : {ref_count(id(self.a))}
         """)


if __name__ == '__main__':

    a = A()
    print("A() executed")
    print("-"*40)

    b = B(a)
    print("B() executed")
    print("-"*40)

    a.b = b
    print("a.b = b executed")
    print("+"*40)

    id_a = id(a)
    id_b = id(b)

    print(f"""in a:
    a {hex(id(a))} : {ref_count(id(a))}
    b {hex(id(a.b))} : {ref_count(id(a.b))}
     """)
    print(f"""in b:
    b {hex(id(b))} : {ref_count(id(b))}
    a {hex(id(b.a))} : {ref_count(id(b.a))}
     """)
    # del b
    # print("*"*40)
    # del a

    del a
    print("del a executed")
    print("*"*40)
    del b
    print("del b executed")
    print("*"*40)

    gc_check(id_b)
    gc_check(id_a)

    gc.collect()
    print("GC executed")
    print("=" * 40)

    gc_check(id_b)
    gc_check(id_a)