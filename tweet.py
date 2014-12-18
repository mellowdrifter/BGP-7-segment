#!/usr/bin/python
'''Be sure to touch v4_count and v6_count if they don't exist'''

import urllib2
from xml.etree import ElementTree
from twitter import *

# Variables
v6_token = "xxx"
v6_token_key = "xxx"
v6_con_secret = "xxx"
v6_con_secret_key = "xxx"
v4_token = "xxx"
v4_token_key = "xxx"
v4_con_secret = "xxx"
v4_con_secret_key = "xxx"
t6 = Twitter(auth=OAuth(v6_token, v6_token_key, v6_con_secret, v6_con_secret_key))
t4 = Twitter(auth=OAuth(v4_token, v4_token_key, v4_con_secret, v4_con_secret_key))
v4_path = "/path/to/v4_count"
v6_path = "/path/to/v6_count"
xml_path = "/path/to/bgp/bgp.xml"

# Pull last delta
with open(v4_path) as f:
   try:
       old_v4 = int(f.readline())
   except:
       old_v4 = 0
with open(v6_path) as f:
   try:
       old_v6 = int(f.readline())
   except:
       old_v6 = 0

# Pull current values
with open(xml_path) as f:
   tree = ElementTree.parse(f)
   rootElem = tree.getroot()
   ipv4_element = rootElem.find("ipv4")
   ipv6_element = rootElem.find("ipv6")
   ipv4 = ipv4_element.text.strip(' \n\t')
   ipv6 = ipv6_element.text.strip(' \n\t')

# Work out deltas and create delete strings
ipv4_delta = int(ipv4) - old_v4
ipv6_delta = int(ipv6) - old_v6

if ipv4_delta < 0:
   delta4 = "This is " + str(-ipv4_delta) + " less routes than the last update"
elif ipv4_delta > 0:
   delta4 = "This is " + str(ipv4_delta) + " more routes than the last update"
else:
   delta4 = "No change in the amount of routes from the last update"

if ipv6_delta < 0:
   delta6 = "This is " + str(-ipv6_delta) + " less routes than the last update"
elif ipv6_delta > 0:
   delta6 = "This is " + str(ipv6_delta) + " more routes than the last update"
else:
   delta6 = "No change in the amount of routes from the last update"
   
c4 = "I currently see " + str(ipv4) + " IPv4 routes" + ". " + delta4
c6 = "I currently see " + str(ipv6) + " IPv6 routes" + ". " + delta6

with open(v4_path, "w") as f:
   f.write(ipv4)
with open(v6_path, "w") as f:
   f.write(ipv6)

# Tweet
t6.statuses.update(status=c6)
t4.statuses.update(status=c4)
