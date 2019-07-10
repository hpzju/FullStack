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

script, filename = argv

print(f"reading {filename}......")

with open(filename) as fo:
    for index, line in enumerate(fo):
        print(f"{index+1:0>3}: {line}", end="")