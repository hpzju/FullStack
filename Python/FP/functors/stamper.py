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

from datetime import datetime


def stamper(fmt='%Y-%m-%d %H:%M:%S'):
    while True:
        yield datetime.strftime(datetime.now(), fmt)


if __name__ == "__main__":
    stampit = stamper('%H:%M:%S %f')
    print(stampit)
    for index, stamp in enumerate(stampit):
        print(f"{stamp}: {index}")
        if index > 100:
            break
