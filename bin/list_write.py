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


# # list_write test
# from field_reorder import master_field_list
# comment the above line out if using list_write in field_reorder
# # Reads in the unsorted fields
# fields = master_field_list('./input_data/Sample_iPhone_Export.csv')
# # fields = master_field_list() # gets correct master list
# # Data will not re-sort to the master list yet.
# from list_read import list_read
# filename = './input_data/Sample_iPhone_Export.csv'
# data = list_read(filename, start_line=3, end_line=10)
# new_file = list_write(data, fields)

# # list_combine test
# from list_read import list_read
# from list_combine import list_combine
# # from list_write import list_write
# from field_reorder import MasterFields
# # filename1 = './master/Sample_iPhone_Export_2.csv'
# # filename1 = './master/MyContacts-2017-08-10-210940-230_short_mod_dates.csv'
# filename1 = './master/MyContacts-2017-08-10-210940-230_short_mod.csv'
# # filename1 = './master/2017-07-12_TSV_Contacts.csv'
# df_current = list_read(filename1)
# # filename2 = './input_data/Sample_iPhone_Export_3.csv'
# filename2 = './input_data/MyContacts-2017-08-10-210940-230.csv'
# # filename2 = './input_data/2017-07-28_TSV_Contacts.csv'
# df_input = list_read(filename2)
# df_out = list_combine(df_current, df_input)
# new_file = list_write(df_out, desc='iPhone_test_16')
