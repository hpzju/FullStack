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

from sys import argv


for arg in argv:
    print(arg)

# terminal dependent argv parsing
# window:
#     cmd:
#         python ex13-argv.py  "str space" """string space""" '''string space'''
#     output:\
#         ex13-argv.py
#         str space
#         "string space"
#         '''string
#         space'''
#
# bash:
#     cmd:
#         python ex13-argv.py  "str space" """string space""" '''string space'''
#     output:
#         ex13-argv.py
#         str space
#         string space
#         string space
