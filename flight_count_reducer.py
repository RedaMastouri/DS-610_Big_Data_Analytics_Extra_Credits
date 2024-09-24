# Reducer.py

import sys
current_flight = None
flight_counts = 0

for line in sys.stdin:
    try:
        flight, counts = line.strip().split("\t",1)
        counts = int(counts)
    except ValueError as e:
        continue
    if flight != current_flight:
        if current_flight:
            print "%s\t%d" %(current_flight, flight_counts)
        current_flight = flight
        flight_counts = 0
    flight_counts += counts
    
if current_flight:
    print "%s\t%d" %(current_flight, flight_counts)
