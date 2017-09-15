import csv
import pandas as pd
from bin.list_read import TimeStamp


def list_write(df_out, desc=None):
    """
    Takes a pandas DataFrame object and file description as input.
    Description is optional. Default is date and time.
    Writes new file. Returns nothing.
    If there is a file with the same name in the output_data directory,
    it will be overwritten!
    """

    if desc:
        desc = '_' + desc

    fields = df_out.index.values

    date_time_now = TimeStamp()
    new_filename = './output_data/' + date_time_now.long_form() + desc + '.csv'

    # If data is only one row, modify the iterable so it writes correctly.
    if isinstance(df_out[0:1], str):
        df_out = [df_out, []]

    # Create new CSV file to write to
    with open(new_filename, 'w+', newline='') as new_file:
        new_file_csv = csv.writer(new_file)

        print('Writing data to CSV...')

        # write field names as first row
        new_file_csv.writerow(fields)

        for ser_key in df_out.keys():
            new_file_csv.writerow(df_out[ser_key])

        return new_filename
