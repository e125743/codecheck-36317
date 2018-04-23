#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import os
import sys
import codecs
import sqlite3
from contextlib import closing
import json

dbname = 'test.db'

with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()
    print ('Content-type: text/html; charset=UTF-8')
    print ("\r\n\r\n")
    if ( os.environ['REQUEST_METHOD'] == "GET" ):
        select_sql = 'select * from recipes'
        c.execute(select_sql)
        data = c.fetchcall()
        print(json.dumps(data))
    #elif ( os.environ['REQUEST_METHOD'] == "POST" ):
