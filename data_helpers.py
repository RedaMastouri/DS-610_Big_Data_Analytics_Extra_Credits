from concurrent.futures import ThreadPoolExecutor
from functools import partial
from multiprocessing import Pool

import pandas as pd

AIRLINE_DTYPES = {
    'Year': 'int64',
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
    'DepDelay': 'float64',
    'Origin': 'string',
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
    'LateAircraftDelay': 'float64',
}


def read_airline_files(data_files, num_of_files=22, processing='single') -> pd.DataFrame:
    """
    Read all files into one single dataframe.

    Notes:
    This function will work only if you have a large amount of RAM
    on your computer. For example, anything above 30 GB should work.

    If you have less RAM, you can limit the number of files to load
    with this function with the parameter. First 8 files consumes 
    13 GB memory space.

    For more information on this issue, check out the stackoverflow
    answer: https://datascience.stackexchange.com/a/27794/61094.
    Another nice answer on this issue is the following:
    https://stackoverflow.com/a/60616527/5159551

    Parameters:

    data_files:
        List of data files 
    num_of_files:
        How many files from the data folder you want to
        load to. Range is (0, 22].
    processing:
        Defines if multiprocessing is used while reading
        files. Use `single` for serial, `multi` for 
        multiprocessing, and `thread` for multithreading.

    Use following to see actual memory usage the returned 
    dataframe.

    >>> df.info(verbose=False, memory_usage="deep")
    """
    if num_of_files not in range(1, 23):
        raise ValueError('Incorrect number of files.')

    # partial function
    par_func = partial(
        pd.read_csv,
        compression='bz2',
        encoding='ISO-8859-1',
        engine='c',
        low_memory=False,
        dtype=AIRLINE_DTYPES,
    )

    # run partial function for all file paths and concat the dataframe
    if processing == 'single':
        df = pd.concat(
            map(par_func, data_files[:num_of_files]), ignore_index=True)
    elif processing == 'multi':
        with Pool() as pool:
            df_list = pool.map(par_func, data_files[:num_of_files])
            df = pd.concat(df_list, ignore_index=True)
            del df_list
    elif processing == 'thread':
        with ThreadPoolExecutor() as executor:
            df_list = executor.map(par_func, data_files[:num_of_files])
            df = pd.concat(df_list, ignore_index=True)
            del df_list
    else:
        raise ValueError('Incorrect value for processing.')

    return df


def read_airline_file(data_file, **read_csv_kwargs) -> pd.DataFrame:
    """
    Read a single file into dataframe.
    """
    return pd.read_csv(
        filepath_or_buffer=data_file,
        compression='bz2',
        encoding='ISO-8859-1',
        engine='c',
        low_memory=False,
        dtype=AIRLINE_DTYPES,
        **read_csv_kwargs
    )


def read_csv_with_multiprocessing(files, pool_kwargs) -> pd.DataFrame:
    """
    Read multiple CSV files into a single dataframe
    with multiprocessing.
    """
    with Pool(**pool_kwargs) as pool:
        df_list = pool.map(pd.read_csv, files)
        combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df
