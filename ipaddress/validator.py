#!/usr/bin/env python3
import ipaddress
ipcheck = input("Give an ip:")

IPValidated = False

def validator(ipcheck):
    try:
        ipaddress.ip_address(ipcheck)
    except ValueError:
        print("ValueError")
    else:
        print("ip set: "+ipcheck)
validator(ipcheck)
