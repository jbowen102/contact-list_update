from hashlib import md5
import pandas as pd


def field_list_compare(input_arr, current_arr):
    """
    Function that takes in two NumPy arrays, each with a list of column names
    from a contact list. Compares the two (using md5 hash), returns True if
    equivalent, False if different.
    """

    # Exclude Mod Date field
    if 'Mod Date' in input_arr:
        input_str = '|'.join(input_arr[:-1])
    else:
        input_str = '|'.join(input_arr)

    if 'Mod Date' in current_arr:
        curr_str = '|'.join(current_arr[:-1])
    else:
        curr_str = '|'.join(current_arr)

    input_str_rec = input_str.encode('utf-8')
    curr_str_rec = curr_str.encode('utf-8')
    input_str_hash = md5(input_str_rec).hexdigest()
    curr_str_hash = md5(curr_str_rec).hexdigest()

    return (input_str_hash == curr_str_hash)


def series_compare(input_ser, current_ser):
    """
    Function that takes in two pandas Series objects with contact info and
    compares them by taking the md5 hash of the concatenation of all entries.
    Returns Boolean True if Series are different and False if equivalent.
    """

    # Exclude Mod Date field
    if 'Mod Date' in input_ser.index:
        input_str = '|'.join(input_ser.values[:-1])
    else:
        input_str = '|'.join(input_ser.values)

    if 'Mod Date' in current_ser.index:
        curr_str = '|'.join(current_ser.values[:-1])
    else:
        curr_str = '|'.join(current_ser.values)

    input_str_rec = input_str.encode('utf-8')
    curr_str_rec = curr_str.encode('utf-8')
    input_str_hash = md5(input_str_rec).hexdigest()
    curr_str_hash = md5(curr_str_rec).hexdigest()

    return (not input_str_hash == curr_str_hash)


def list_combine(df_current, df_input):
    """
    Function that takes in a pandas DataFrame of contacts and adds any new
    contacts that appear in a second DataFrame of contacts.
    Returns pandas DataFrame object with contacts.
    The key for each Series in the DataFrame is the First+Last Name, First
    Name only, or Organization name.
    """

    # Check that new and current field lists are the same
    same_fields = field_list_compare(df_input.index.values,
                                    df_current.index.values)
    if not same_fields:
        raise ValueError('Cannot combine lists. Field list different.')

    # Create copy of current DataFrame
    df_out = df_current.copy()
    new_rec = []
    mod_rec = []

    for ser_key in df_input.keys():

        # If any series key is not already in df_current, add it now.
        # Known issue: Editing a name will cause the new one to be added in
        # addition to old one, not replacing.
        if not ser_key in df_current.keys():
            df_out[ser_key] = df_input[ser_key]
            new_rec += [ser_key]
            print('+ Added %s' % ser_key)
            continue

        # Compare new and current records
        # If the two series are not exactly the same, use the new one.
        str_mod = series_compare(df_input[ser_key], df_current[ser_key])
        if str_mod:
            df_out[ser_key] = df_input[ser_key]
            mod_rec += [ser_key]
            print('^ Modified %s' % ser_key)

    print('\n' + '#' * 10 + 'Update finished' + '#' * 10)
    print('\tEntries added (%d)' % len(new_rec))
    print('\tEntries modified (%d)' % len(mod_rec))
    return df_out.sort_index(axis=1)
