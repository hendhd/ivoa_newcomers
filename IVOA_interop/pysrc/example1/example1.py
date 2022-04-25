#!/usr/bin/env python3
# -*- coding=utf-8 -*- 

# A demo program to show how a TAP query in PyVO works. 

import pyvo
import astropy 
import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")


service = pyvo.dal.TAPService ("http://cdsarc.cds.unistra.fr/saadavizier.tap/tap")
result = service.search("SELECT TOP 1 * FROM obscore")

result.votable.to_xml("result.vot")

