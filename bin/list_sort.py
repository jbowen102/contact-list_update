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
        map_dict = {'First Name': '01.First Name',
                    'Last Name': '02.Last Name',
                    'Display Name': '03.',
                    'Nickname': '04.Nickname',
                    'Organization': '05.Organization',
                    'Department': '06.Department',
                    'Job Title': '07.Title',
                    'Primary Email': '08.Home [Email]',
                    'Secondary Email': '09.Work [Email]',
                	'Mobile Number': '10.Mobile',
                	'Home Phone': '11.Home [Phone]',
                	'Work Phone': '12.Work [Phone]',
                	'Fax Number': '13.Work Fax',
                	'Web Page 1': '14.Home Page',
                	'Home Address': '15.Home [Address]',
                	'Work Address': '16.Work [Address]',
                	'Notes': '17.Note',
                	'Pager Number': '18.Pager',
                	'Home Address 2': '19.',
                	'Home City': '20.',
                	'Home State': '21.',
                	'Home ZipCode': '22.',
                	'Screen Name': '23.',
                	'Home Country': '24.',
                	'Work Address 2': '25.',
                	'Work City': '26.',
                	'Work State': '27.',
                	'Work ZipCode': '28.',
                	'Work Country': '29.',
                	'Web Page 2': '30.',
                	'Birth Year': '31.',
                	'Birth Month': '32.',
                	'Birth Day': '33.',
                    'Custom 1': '34.',
                    'Custom 2': '35.',
                    'Custom 3': '36.',
                    'Custom 4': '37.'}

    elif map_type.lower() == 'outlook':
        map_dict = {'First Name': '01.First Name',
                    'Last Name': '02.Last Name',
                    'Display Name': '03.Title',
                    'Nickname': '04.',
                    'Organization': '05.Company',
                    'Department': '06.Department',
                    'Job Title': '07.Job Title',
                    'Primary Email': '08.E-mail Address',
                    'Secondary Email': '09.E-mail 2 Address',
                	'Mobile Number': '10.Mobile Phone',
                	'Home Phone': '11.Home Phone',
                	'Work Phone': '12.Business Phone',
                	'Fax Number': '13.Business Fax',
                	'Web Page 1': '14.Web Page',
                	'Home Address': '15.Home Street',
                	'Work Address': '16.Business Street',
                	'Notes': '17.Notes',
                	'Pager Number': '18.Pager',
                	'Home Address 2': '19.Home Street 2',
                	'Home City': '20.Home City',
                	'Home State': '21.Home State',
                	'Home ZipCode': '22.Home Postal Code',
                	'Screen Name': '23.',
                	'Home Country': '24.Home Country/Region',
                	'Work Address 2': '25.Business Street 2',
                	'Work City': '26.Business City',
                	'Work State': '27.Business State',
                	'Work ZipCode': '28.Business Postal Code',
                	'Work Country': '29.Home Country/Region',
                	'Web Page 2': '30.',
                	'Birth Year': '31.',
                	'Birth Month': '32.',
                	'Birth Day': '33.',
                    'Custom 1': '34.',
                    'Custom 2': '35.',
                    'Custom 3': '36.',
                    'Custom 4': '37.'}

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
