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

# line comment
print("line comment")   # comment after line

print("inline # pound char")   # comment after line

print("inline '#' pound char")   # comment after line

"""
this can be used as block comments

no code generated during execution

args: 

*args:

default_kwargs:

**kwargs:
"""

for ns in dir():
    print(f"{ns}: {eval(ns)}")
