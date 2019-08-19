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


if __name__ == '__main__':
    print(f"int_info: {sys.int_info}")

    a = 2**1000

    print(f"2**1000 size: {sys.getsizeof(a)} Bytes")

    print(f"0 size: {sys.getsizeof(0)} Bytes")
    print(f"1 size: {sys.getsizeof(1)} Bytes")

    string = 'abcdefghij'
    print(f"'{string}' size: {sys.getsizeof(string)} Bytes")