import pandas as pd

def list_add(df_current, df_input):
    """
    Function that takes in a pandas DataFrame of contacts and adds any new
    contacts that appear in a second DataFrame of contacts.
    Returns pandas DataFrame object with contacts.
    The key for each Series in the DataFrame is the First+Last Name, First
    Name only, or Organization name.
    """

    # print(df_current.keys())

    # Create copy of master dataframe and add
    df_out = df_current.copy()


    # Series containing today's date for entries that are new or modified.
    # mod_date = pd.Series(['2017-09-04'], index=['Mod Date'])


    for ser_key in df_input.keys():

        # ser_key = df_input.keys()[s]
        # print(ser_key)

        # If any series key is not already in df_current, add it now.
        # Known issue: Editing a name will cause a duplicate to be added.
        if not ser_key in df_current.keys():

            # Add new Series from the input list to the output.
            # Update the date-modified field.
            # new_entry_series = df_input[ser_key]
            # new_entry_series.append(mod_date)
            # df_out[ser_key] = new_entry_series

            df_out[ser_key] = df_input[ser_key]
            df_out[ser_key]['Mod Date'] = '2017-09-04'
            print('Added %s to output df' % ser_key)

    return df_out.sort_index(axis=1)
    print(df_out.keys())


# list_read test
from list_read import list_read
from list_write import list_write
from list_sort import master_field_list
filename1 = './master/Sample_iPhone_Export_2.csv'
df_current = list_read(filename1)
filename2 = './input_data/Sample_iPhone_Export_3.csv'
df_input = list_read(filename2)
df_out = list_add(df_current, df_input)

# input('>>')
# fields = master_field_list(filename1)
list_write(df_out, new_filename=None)
