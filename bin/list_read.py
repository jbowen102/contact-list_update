import csv
import pandas as pd

def list_read(filename):
    """
    Function to read in CSV data from a contact list.
    Reads in the first row as the field names.
    Returns pandas DataFrame object with CSV contact list entries.
    The key for each Series in the DataFrame is the First+Last Name, First
    Name only, or Organization name.
    """
    with open(filename, 'r') as csvfile:
        print('Reading input data from CSV...')
        file_in = csv.reader(csvfile) #, dialect='excel')

        record_dict = {}
        i = 0

        for row in file_in:
            # print('Row %s:' % i)
            # print(row)

            if i == 0:
                field_list = row
                # firstn_field = row.index('First Name')
                # lastn_field = row.index('Last Name')

                # This row could be rearranged here and passed to pd.Series()
                # below.

            if i >= 1:
                record = pd.Series(row, index=field_list)
                # print('Record %s:' % i)
                # print(record)

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

            # if i >= 5:
            #     break
            i += 1

    # df = pd.DataFrame.from_dict(record_dict, orient='index')
    df = pd.DataFrame(record_dict)
    # print('Input CSV data as DataFrame:\n', df)

    # print('First record in DataFrame:')
    # print()
    return df.sort_index(axis=1)
    


# # list_read test
# filename = './input_data/Sample_iPhone_Export.csv'
# list_read(filename)
