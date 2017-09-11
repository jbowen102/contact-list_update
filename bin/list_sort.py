import pandas as pd


def master_field_list(master_file='./master/TB_default_fields.csv'):
    """
    Function to read in field order from a master list.
    "Master" fields should be ordered according to Thunderbird default import
    order.
    Reads in the first row as the field names.
    Data in any row but the first will be ignored.
    Returns list with ordered field names
    """
    with open(master_file, 'r') as csvfile:
        print('Reading master field order from CSV...')
        file_in = csv.reader(csvfile)

        field_list = file_in.__next__()
        return field_list


def master_field_dict(map_type):
    """
    Function to read in field order from a master list and 'iPhone' or 'Outlook'
    as type of mapping to create.
    "Master" fields should be ordered according to Thunderbird default import
    order.
    Reads in the first row as the field names.
    Data in any row but the first will be ignored.
    Returns a dict with mapping of Thunderbird heading names to Outlook or
    iPhone-export contact-list heading names.
    """

    if map_type.lower() == 'iphone':
        map_dict = {'First Name': 'First Name',
                    'Last Name': 'Last Name',
                    'Display Name': '[TB_Display Name]',
                    'Nickname': 'Nickname',
                    'Organization': 'Organization',
                    'Department': 'Department',
                    'Job Title': 'Title',
                    'Primary Email': 'Home [Email]',
                    'Secondary Email': 'Work [Email]',
                	'Mobile Number': 'Mobile',
                	'Home Phone': 'Home [Phone]',
                	'Work Phone': 'Work [Phone]',
                	'Fax Number': 'Work Fax',
                	'Web Page 1': 'Home Page',
                	'Home Address': '[TB_Home Address]',
                	'Work Address': '[TB_Work Address]',
                	'Notes': 'Note',
                	'Pager Number': 'Pager',
                	'Home Address 2': '[TB_Home Address 2]',
                	'Home City': '[TB_Home City]',
                	'Home State': '[TB_Home State]',
                	'Home ZipCode': '[Home ZipCode]',
                	'Screen Name': '[TB__Screen Name]',
                	'Home Country': '[TB_Home Country]',
                	'Work Address 2': '[TB_Work Address 2]',
                	'Work City': '[TB_Work City]',
                	'Work State': '[TB_Work State]',
                	'Work ZipCode': '[TB_Work ZipCode]',
                	'Work Country': '[TB_Work Country]',
                	'Web Page 2': '[TB_Web Page 2]',
                	'Birth Year': '[TB_Birth Year]',
                	'Birth Month': '[TB_Birth Month]',
                	'Birth Day': '[TB_Birth Day]',
                    'Custom 1': '[TB_Custom 1]',
                    'Custom 2': '[TB_Custom 2]',
                    'Custom 3': '[TB_Custom 3]',
                    'Custom 4': '[TB_Custom 4]'}

    elif map_type.lower() == 'outlook':
        map_dict = {'First Name': 'First Name',
                    'Last Name': 'Last Name',
                    'Display Name': 'Title',
                    'Nickname': '[TB_Nickname]',
                    'Organization': 'Company',
                    'Department': 'Department',
                    'Job Title': 'Job Title',
                    'Primary Email': 'E-mail Address',
                    'Secondary Email': 'E-mail 2 Address',
                	'Mobile Number': 'Mobile Phone',
                	'Home Phone': 'Home Phone',
                	'Work Phone': 'Business Phone',
                	'Fax Number': 'Business Fax',
                	'Web Page 1': 'Web Page',
                	'Home Address': 'Home Street',
                	'Work Address': 'Business Street',
                	'Notes': 'Notes',
                	'Pager Number': 'Pager',
                	'Home Address 2': 'Home Street 2',
                	'Home City': 'Home City',
                	'Home State': 'Home State',
                	'Home ZipCode': 'Home Postal Code',
                	'Screen Name': '[TB_Screen Name]',
                	'Home Country': 'Home Country/Region',
                	'Work Address 2': 'Business Street 2',
                	'Work City': 'Business City',
                	'Work State': 'Business State',
                	'Work ZipCode': 'Business Postal Code',
                	'Work Country': 'Home Country/Region',
                	'Web Page 2': '[TB_Web Page 2]',
                	'Birth Year': '[TB_Birth Year]',
                	'Birth Month': '[TB_Birth Month]',
                	'Birth Day': '[TB_Birth Day]',
                    'Custom 1': '[TB_Custom 1]',
                    'Custom 2': '[TB_Custom 2]',
                    'Custom 3': '[TB_Custom 3]',
                    'Custom 4': '[TB_Custom 4]'}

    else:
        raise ValueError("map_type must be either 'iPhone' or 'Outlook'")

    return map_dict

# # master_field_dict test
# map_dict = master_field_dict(map_type='iPhone')
# for k in map_dict:
#     print('%s\t-\t%s' % (k, map_dict[k]))


def list_sort(df_to_sort, df_type, master_file='./master/TB_default_fields.csv'):
    """
    Function to take in pandas DataFrame containing contact-data entries that
    need to be reordered relative to each other.
    The ordered_fields input should contain a list of correctly-ordered labels.
    Returns DataFrame with reordered fields conforming to ordered_fields.
    """

    field_list = master_field_list(master_file)
    map_dict = master_field_dict(df_type)
    # Ensure Thunderbird headings match hard-coded dict keys
    assert set(field_list) == set(map_dict.keys())

    # Create new list and populate with ordered df field names.
    sorted_index = []
    for TB_field in field_list:
        sorted_index += [map_dict[TB_field]]
    print(sorted_index)

    df_sorted = df_to_sort.reindex(index=sorted_index)
    return df_sorted


# list_sort test
import csv
from list_read import list_read
from list_write import list_write
filename1 = './master/MyContacts-2017-08-10-210940-230_short_mod.csv'
df_in = list_read(filename1)
df_sorted = list_sort(df_in, df_type='iPhone')
new_file = list_write(df_sorted, desc='iPhone_sort_1')
