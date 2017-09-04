import csv
import pandas as pd

def list_read(filename, start_line=2, end_line=None):
    """
    Function to read in CSV data from a contact list.
    Inputs:
        filename: a string containing the file path and name
        start_line: the first numbered line of the CSV that should be included
        in the resulting DataFrame (defaults to 2, the first entry)
        end_line: the last numbered line of the CSV that should be included in
        the resulting DataFrame (defaults to None, the end)
    Reads in the first row as the field names.
    Returns pandas DataFrame object with CSV contact list entries.
    The key for each Series in the DataFrame is the First+Last Name, First
    Name only, or Organization name.
    """
    with open(filename, 'r') as csvfile:
        print('Reading input data from CSV...')
        file_in = csv.reader(csvfile)

        # Get field names before entering loop (no influence from start/end
        # line specified)
        field_list = file_in.__next__()
        # If CSV doesn't already have date-modified fields, add now.
        if not 'Mod Date' in field_list:
            field_list += ['Mod Date']
            add_mod_field = True
        else:
            add_mod_field = False

        record_dict = {}
        i = 2

        for row in file_in:
            # print('Row %s:' % i)
            # print(row)

            if i >= start_line:

                # Add blank entry to row if Mod Date field didn't already exist.
                if add_mod_field:
                    row += ['']
                record = pd.Series(row, index=field_list)
                # print('Record %s:' % i)
                # print(record)

                # Parse name for series.
                firstn = record['First Name']
                lastn = record['Last Name']
                org = record['Organization']

                if firstn and lastn:
                    name = lastn + ', ' + firstn
                elif firstn:
                    name = firstn
                elif org:
                    name = org
                else:
                    raise ValueError('No first, last, or organization name for'
                                        'record %i' % i)

                record_dict.update({name: record})

            i += 1
            if end_line and i > end_line:
                break

    # df = pd.DataFrame.from_dict(record_dict, orient='index')
    df = pd.DataFrame(record_dict)
    # print('Input CSV data as DataFrame:\n', df)

    # print('First record in DataFrame:')
    # print()
    return df.sort_index(axis=1)



# # # list_read test
# filename = './input_data/Sample_iPhone_Export.csv'
# list_read(filename)
