# MapReduce with Python

Find a few answers from a large dataset.

## Description

The quest is simple. Use MapReduce algortihm to find the answer for the following questions.

1. Find the # of flights each airline made so far  from 1987 until recent.
2. Find the mean departure delay per origination airport.
3. What day the delays are the worst?

## Hints

MapReduce algorithm is designed to be seperated. Use this to your advantage. 

1. Make 3 functions: `Mapper`, `Sorter`, `Reducer`.
2. Use threading or multiprocessing while you are mapping or sorting different files.
3. For things you multiprocessed, write down the results into temporary files.
4. Use `functools.reduce`, `itertools.groupby` and builtin `map` function.

## Dataset

You will be working on `Airline On-Time Performance Dataset`. Dataset is availabe at my Google Drive. Use your **school ID** to access to the [folder](https://drive.google.com/drive/folders/1145wIkSlzA61CdHS4hZZFgF6ZzIbaVJM?usp=sharing). 

The data consists of flight arrival and departure details for all commercial flights within the USA, from October 1987 to April 2008. It has a total file size of 1.6 GB (compressed, and 12 GB when uncompressed), with the number of records a little over 123 million records.

Each row represents an individual flight record with details of that flight in the row. The information are:

| No  | Name              | Data Type | Description                                                               |
| --- | ----------------- | --------- | ------------------------------------------------------------------------- |
| 1   | Year              | int64     | 1987-2008                                                                 |
| 2   | Month             | int64     | 1-12                                                                      |
| 3   | DayofMonth        | int64     | 1-31                                                                      |
| 4   | DayOfWeek         | int64     | 1 (Monday) - 7 (Sunday)                                                   |
| 5   | DepTime           | float64   | actual departure time (local, hhmm)                                       |
| 6   | CRSDepTime        | float64   | scheduled departure time (local, hhmm)                                    |
| 7   | ArrTime           | float64   | actual arrival time (local, hhmm)                                         |
| 8   | CRSArrTime        | float64   | scheduled arrival time (local, hhmm)                                      |
| 9   | UniqueCarrier     | string    | unique carrier code                                                       |
| 10  | FlightNum         | float64   | flight number                                                             |
| 11  | TailNum           | string    | plane tail number                                                         |
| 12  | ActualElapsedTime | float64   | in minutes                                                                |
| 13  | CRSElapsedTime    | float64   | in minutes                                                                |
| 14  | AirTime           | float64   | in minutes                                                                |
| 15  | ArrDelay          | float64   | arrival delay, in minutes                                                 |
| 16  | DepDelay          | float64   | departure delay, in minutes                                               |
| 17  | Origin            | string    | origin IATA airport code                                                  |
| 18  | Dest              | string    | destination IATA airport code                                             |
| 19  | Distance          | float64   | in miles                                                                  |
| 20  | TaxiIn            | float64   | taxi in time, in minutes                                                  |
| 21  | TaxiOut           | float64   | taxi out time in minutes                                                  |
| 22  | Cancelled         | int64     | was the flight cancelled?                                                 |
| 23  | CancellationCode  | string    | reason for cancellation (A = carrier, B = weather, C = NAS, D = security) |
| 24  | Diverted          | int64     | 1 = yes, 0 = no                                                           |
| 25  | CarrierDelay      | float64   | in minutes                                                                |
| 26  | WeatherDelay      | float64   | in minutes                                                                |
| 27  | NASDelay          | float64   | in minutes                                                                |
| 28  | SecurityDelay     | float64   | in minutes                                                                |
| 29  | LateAircraftDelay | float64   | in minutes                                                                |

You can find more information about this dataset in the website of [Statistical Computing](http://stat-computing.org/dataexpo/2009/). Find out more information on [Airline On-Time Performance Data](https://www.transtats.bts.gov/DatabaseInfo.asp?QO_VQ=EFD&QO_anzr=Nv4yv0r%20b0-gvzr%20cr4s14zn0pr%20Qn6n) from [Bureau of Transportation Statistics (BTS)](https://www.transtats.bts.gov/).

## How to work on this Assignment?

1. Download this repository with [`git clone`](https://git-scm.com/docs/git-clone).
2. [Create a virtual environment](https://github.com/metinsenturk/class-materials/tree/main/contents/create-virtual-environment) and activate this environment everytime you need to use it.
3. Install [requirements.txt](requirements.txt) file using `pip install -r requirements.txt`.
4. Run the notebook.

## Questions

The repository should be self descriptive and it should guide you through assignment. Let me know if you have any questions.

