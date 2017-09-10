from hashlib import md5 # delete later
import csv
import pandas as pd

def list_read(filename, start_line=2, end_line=None):
    """
    Function to read in CSV data from a contact list and store in a DataFrame.
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

    if end_line and not end_line >= start_line:
        raise ValueError('End value must be greater than or equal to '
                'start value')

    with open(filename, 'r') as csvfile:
        print('Reading input data from CSV...')
        file_in = csv.reader(csvfile)

        # Get field names before entering loop
        field_list = file_in.__next__()

        # If CSV doesn't already have date-modified fields, add now.
        if not 'Mod Date' in field_list:
            field_list += ['Mod Date']
            add_mod_field = True
            # print('Added Mod Date field. Number of indices:', len(field_list))
        else:
            add_mod_field = False

        record_dict = {}
        i = 2

        for row in file_in:
            # print('Row %d of length %d:' % (i, len(row)))
            # print(row)

            if i >= start_line:

                # Pad end of row with blank entries if field_list longer
                # (Outlook exports this way). Also adds blank entry for
                # Mod Date field, if it didn't already exist.
                len_diff = len(field_list) - len(row)
                if len_diff > 0:
                    row += [''] * len_diff

                # print('Row %d in CSV. Length: %d' % (i, len(row)))
                record = pd.Series(row, index=field_list)
                # print('Record %s:' % i)
                # print(record.values)

                # Parse name for series.
                firstn = record.get('First Name', None).lower()
                lastn = record.get('Last Name', None).lower()
                org = record.get('Organization',
                      record.get('Company', None)).lower()

                if firstn and lastn:
                    name = lastn + ', ' + firstn
                elif firstn:
                    name = firstn
                elif org:
                    name = org
                else:
                    raise ValueError('No first, last, or organization name for '
                                        'record %i' % i)

                # rec_str = '|'.join(record.values)
                # rec_str_enc = rec_str.encode('utf-8')
                # rec_hash = md5(rec_str_enc).hexdigest()
                # print('md5 hash of series %d: %s' % (i, rec_hash))

                record_dict.update({name: record})

            i += 1
            if end_line and i > end_line:
                break

    df = pd.DataFrame(record_dict)
    # print('Input CSV data as DataFrame:\n', df)

    return df.sort_index(axis=1)


# # list_read test
# # filename = './input_data/Sample_iPhone_Export.csv'
# # filename1 = './master/2017-07-12_TSV_Contacts.csv'
# filename1 = './master/MyContacts-2017-08-10-210940-230_shortened.csv'
# list_read(filename1, end_line=7)
# print('\n' + '-'*80 + '\n')
# filename2 = './input_data/MyContacts-2017-08-10-210940-230.csv'
# list_read(filename2, end_line=7)
