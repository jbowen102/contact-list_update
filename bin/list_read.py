from hashlib import md5 # delete later
import csv
import pandas as pd


def field_list_mod(raw_field_list):
    """
    Function to modify the standard iPhone export field list to fix non-unique
    headings. Takes in list with standard entries.
    Returns list with unique entries.
    """

    mod_field_list = raw_field_list[:]

    # Check that number of non-unique fields hasn't changed.
    assert mod_field_list.count('Home') == 4
    assert mod_field_list.count('Work') == 4
    assert mod_field_list.count('Email') == 4

    # Add descriptors to Work and Home Phone
    mod_field_list[mod_field_list.index('Work')] = 'Work [Phone]'
    mod_field_list[mod_field_list.index('Home')] = 'Home [Phone]'

    # Add descriptors to Home and Work Email
    mod_field_list[mod_field_list.index('Home')] = 'Home [Email]'
    mod_field_list[mod_field_list.index('Work')] = 'Work [Email]'

    # Add descriptors to Emails 1, 2, 3, 4
    mod_field_list[mod_field_list.index('Email')] = 'Email [1]'
    mod_field_list[mod_field_list.index('Email')] = 'Email [2]'
    mod_field_list[mod_field_list.index('Email')] = 'Email [3]'
    mod_field_list[mod_field_list.index('Email')] = 'Email [4]'

    # Add descriptors to Home and Work URLs
    mod_field_list[mod_field_list.index('Home')] = 'Home [URL]'
    mod_field_list[mod_field_list.index('Work')] = 'Work [URL]'

    # Add descriptors to Home and Work Addresses
    mod_field_list[mod_field_list.index('Home')] = 'Home [Address]'
    mod_field_list[mod_field_list.index('Work')] = 'Work [Address]'

    return mod_field_list


def create_series(record_row, field_list):
    """
    Function that takes a contact-list record and field list as inputs
    and creates a pandas Series with the list's column headings as the index.
    Also parses the record's name
    Returns 1-dict with the record name as key and record series as value.
    """

    # Pad end of row with blank entries if field_list longer
    # (Outlook exports this way). Also adds blank entry for
    # Mod Date column, if it didn't already exist.
    len_diff = len(field_list) - len(record_row)
    if len_diff > 0:
        record_row += [''] * len_diff

    # print('Row %d in CSV. Length: %d' % (i, len(row)))
    record = pd.Series(record_row, index=field_list)
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

    return {name: record}


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
        # field_list = file_in.__next__()
        field_list = file_in.__next__()

        # If CSV doesn't already have date-modified column, add it.
        if not 'Mod Date' in field_list:
            field_list += ['Mod Date']

        # Use 'iPhone' field to determine it's iPhone export.
        # Make columns unique. Outlook fields already unique.
        if 'iPhone' in field_list:
            print('Type: iPhone')
            field_list = field_list_mod(field_list)
        elif 'Telex' in field_list:
            print('Type: Outlook')

        record_dict = {}
        i = 2

        for row in file_in:
            # print('Row %d of length %d:' % (i, len(row)))
            # print(row)

            if i >= start_line:

                name_record_dict = create_series(row, field_list)
                record_dict.update(name_record_dict)

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
