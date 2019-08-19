#!/usr/bin/env python

##################################################
# {Description}
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

import sys


def int_interning(start=-5, end=256):

    g1 = (i for i in range(start, end + 1))
    g2 = (i for i in range(start, end + 1))

    intered = list(filter(lambda t: id(t[0]) == id(t[1]), zip(g1, g2)))

    return (intered[0][0], intered[-1][0])


def str_intering_check(string):
    if id(string) == id(str(string)):
        print(f"'{string}' is interned")
        return True
    else:
        print(f"'{string}' is not interned")
        return False


if __name__ == '__main__':

    low, up = int_interning(-1000, 1000)
    print(f"int interning range:[{low},{up}]")

    a = "hello  world"
    b = "strang long string djf;lasj97erwwwwwwwwwww" \
        "werqafasdfasdfasssssssssssssasfwqerqwegsdgsdgd" \
        "dfasdfsafsadfasdfasfadsfffffffffffagdqwrewerqr" \
        "944rpuetojdgfpwup349rsdufpouep98rrewoijasfl"
    c = "strang long string djf;lasj97erwwwwwwwwwww" \
        "werqafasdfasdfasssssssssssssasfwqerqwegsdgsdgd" \
        "dfasdfsafsadfasdfasfadsfffffffffffagdqwrewerqr" \
        "944rpuetojdgfpwup349rsdufpouep98rrewoijasfl"

    str_intering_check(a)
    str_intering_check(b)
    str_intering_check(c)

    sys.intern(b)
    print(f"interning '{b}'")
    print(f"b is c: {id(b) == id(c)}")

