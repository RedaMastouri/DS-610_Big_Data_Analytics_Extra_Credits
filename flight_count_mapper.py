# Mapper.py

import sys, io
import re
'''
Let's keep in mind that MapReduce is just a fancy for-loop
'''
reload(sys)
sys.setdefaultencoding('utf-8')

for line in sys.stdin:
    try:
        article_id, content = unicode(line.strip()).split('\t', 1)
    except ValueError as e:
        continue
    flight_list = re.split("\W*\s+\W*", content, flags=re.UNICODE)
    for flight in flight_list:
        print >> sys.stderr, "reporter:counter:flight_tracker,total_flight,%d" %1
        print "%s\t%d" %(flight.lower(), 1)
