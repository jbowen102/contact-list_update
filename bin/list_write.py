import time
import csv
import pandas as pd
from list_sort import master_field_list
# comment the above line out if using list_write in list_sort

def date_time_str(form):
    """
    Inputs:
        form - 'short' for date only, 'long' for date and time.
    Returns string
    """
    # get date and time to put in filename
    # These are integers
    yr = time.localtime().tm_year
    mon = time.localtime().tm_mon
    day = time.localtime().tm_mday
    hr = time.localtime().tm_hour
    minute = time.localtime().tm_min
    sec = time.localtime().tm_sec

    date_str = '%.4i-%.2i-%.2i' % (yr, mon, day)
    date_time_str = ('%.4i-%.2i-%.2i' % (yr, mon, day) + '_' +
                     '%.2i%.2i%.2i' % (hr, minute, sec))

    # print('Date and time:')
    # print(date_time_str)
    if form == 'short':
        return date_str
    if form == 'long':
        return date_time_str
    else:
        raise ValueError("Input either 'short' or 'long'")


def list_write(data, new_filename=None):
    """
    Takes a pandas DataFrame object, field list, and filename as input.
    New filename input is optional. Default is date and time.
    Writes new file. Returns nothing.
    If there is a file with the same name in the output_data directory,
    it will be overwritten!
    """

    fields = data.index.values

    # Create new file name if none passed in to function
    if not new_filename:
        new_filename = './output_data/' + date_time_str('long') + '.csv'

    # If data is only one row, modify the iterable so it writes correctly.
    if isinstance(data[0:1], str):
        data = [data, []]

    # Create new CSV file to write to
    with open(new_filename, 'w+', newline='') as new_file:
        new_file_csv = csv.writer(new_file)

        print('Writing data to CSV...')

        # write field names as first row
        new_file_csv.writerow(fields)

        for ser_key in data.keys():

            # type(data[ser_key])
            # print(data[ser_key])
            new_file_csv.writerow(data[ser_key])


# # list_write test
# # Reads in the unsorted fields
# fields = master_field_list('./input_data/Sample_iPhone_Export.csv')
# # fields = master_field_list() # gets correct master list
# # Data will not re-sort to the master list yet.
# from list_read import list_read
# filename = './input_data/Sample_iPhone_Export.csv'
# data = list_read(filename, start_line=3, end_line=10)
# list_write(data, fields)
