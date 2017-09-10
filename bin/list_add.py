from hashlib import md5
import pandas as pd
from list_write import date_time_str


def series_compare(input_ser, current_ser):
    """
    Function that takes in two pandas Series objects with contact info and
    compares them by taking the md5 hash of the concatenation of all entries.
    Returns Boolean True if Series are different and False if equivalent.
    """

    input_str = '|'.join(input_ser.values)
    curr_str = '|'.join(current_ser.values)
    input_str_rec = input_str.encode('utf-8')
    curr_str_rec = curr_str.encode('utf-8')
    input_str_hash = md5(input_str_rec).hexdigest()
    curr_str_hash = md5(curr_str_rec).hexdigest()
    # print('\tCurrent: %s' % curr_str_rec)
    # print('\t    New: %s' % input_str_rec)

    return (not input_str_hash == curr_str_hash)


def list_add(df_current, df_input):
    """
    Function that takes in a pandas DataFrame of contacts and adds any new
    contacts that appear in a second DataFrame of contacts.
    Returns pandas DataFrame object with contacts.
    The key for each Series in the DataFrame is the First+Last Name, First
    Name only, or Organization name.
    """

    # Create copy of current dataframe
    df_out = df_current.copy()

    new_rec = []
    mod_rec = []

    for ser_key in df_input.keys():

        # If any series key is not already in df_current, add it now.
        # Known issue: Editing a name will cause the new one to be added in
        # addition to old one, not replacing.
        if not ser_key in df_current.keys():
            df_out[ser_key] = df_input[ser_key]
            df_out[ser_key]['Mod Date'] = date_time_str('short')
            new_rec += [ser_key]
            print('+ Added %s' % ser_key)
            continue

        # Compare new and current records
        str_mod = series_compare(df_input[ser_key], df_out[ser_key])

        # If the two series are not exactly the same, use the new one.
        if str_mod:
            df_out[ser_key] = df_input[ser_key]
            df_out[ser_key]['Mod Date'] = date_time_str('short')
            mod_rec += [ser_key]
            print('^ Modified %s' % ser_key)

    print('\n' + '#' * 10 + 'Update finished' + '#' * 10)
    print('\tEntries added (%d)' % len(new_rec))
    print('\tEntries modified (%d)' % len(mod_rec))
    return df_out.sort_index(axis=1)


# list_read test
from list_read import list_read
from list_write import list_write
from list_sort import master_field_list
# filename1 = './master/Sample_iPhone_Export_2.csv'
filename1 = './master/MyContacts-2017-08-10-210940-230_short_mod.csv'
# filename1 = './master/2017-07-12_TSV_Contacts.csv'
df_current = list_read(filename1)

# filename2 = './input_data/Sample_iPhone_Export_3.csv'
filename2 = './input_data/MyContacts-2017-08-10-210940-230.csv'
# filename2 = './input_data/2017-07-28_TSV_Contacts.csv'
df_input = list_read(filename2)

df_out = list_add(df_current, df_input)
list_write(df_out, desc='iPhone_test_11')
