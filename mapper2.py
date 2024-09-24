# mapper2.py


'''
writing structured MapReduce Python code by computing 
the average departure delay for each origination airport. 
First,let’s take a look at the mapper.
Write the following code into a file called mapper2.py:
 0>> Year': 'int64',
    'Month': 'int64',
    'DayofMonth': 'int64',
    'DayOfWeek': 'int64',
    'DepTime': 'float64',
    'CRSDepTime': 'float64',
    'ArrTime': 'float64',
    'CRSArrTime': 'float64',
    'UniqueCarrier': 'string',
    'FlightNum': 'float64',
    'TailNum': 'string',
    'ActualElapsedTime': 'float64',
    'CRSElapsedTime': 'float64',
    'AirTime': 'float64',
    'ArrDelay': 'float64',
 15>>   'DepDelay': 'float64',   << DepartureDelay
 16>>   'Origin': 'string',      << Origination
    'Dest': 'string',
    'Distance': 'float64',
    'TaxiIn': 'float64',
    'TaxiOut': 'float64',
    'Cancelled': 'int64',
    'CancellationCode': 'string',
    'Diverted': 'int64',
    'CarrierDelay': 'float64',
    'WeatherDelay': 'float64',
    'NASDelay': 'float64',
    'SecurityDelay': 'float64',
    'LateAircraftDelay': 'float64'
'''
import sys
import csv
SEP = "\t" 

class Mapper(object):
    def __init__(self, stream, sep=SEP):
        self.stream = stream
        self.sep = sep
    def emit(self, key, value):
        sys.stdout.write("{}{}{}\n".format(key, self.sep, value))
    def map(self):
        for row in self:
            self.emit(row[16], row[15]) #computing the average departure delay for each airport
    def __iter__(self):
        reader = csv.reader(self.stream) 
        for row in reader:
            yield row

            
if __name__== '__main__':
    mapper = Mapper(sys.stdin) 
    mapper.map()
