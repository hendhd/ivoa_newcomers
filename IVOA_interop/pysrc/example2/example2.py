#!/usr/bin/env python3
# -*- coding=utf-8 -*- 

# A demo program to show as simple Cone Search

import pyvo

service=pyvo.dal.SCSService("http://vo.km3net.de/ant20_01/nu/cone/scs.xml?")
neutrinos=service.search(pos=(170,25), radius=30)

neutrinos.votable.to_xml("neutrinos.vot")
neutrinos.broadcast_samp("topcat")


