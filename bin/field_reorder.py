import csv
import pandas as pd


class MasterFields(object):
    """
    Class to store field order from a master list.
    "Master" fields should be ordered according to Thunderbird default import
    order.
    Reads in the first row as the field names.
    Data in any row but the first will be ignored.
    """
    def __init__(self, master_file='./master/TB_default_fields.csv'):
        with open(master_file, 'r') as csvfile:
            print('Reading master TB field order from CSV...')
            file_in = csv.reader(csvfile)
            self.field_list = file_in.__next__()

    def master_list(self):
        return self.field_list

    def master_dict(self, map_type):
        if map_type.lower() == 'iphone':
            self.map_dict = {'First Name': 'First Name',
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
            self.map_dict = {'First Name': 'First Name',
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

        return self.map_dict


def field_reorder(df_to_sort, master_file='./master/TB_default_fields.csv'):
    """
    Function to take in pandas DataFrame containing contact-data entries that
    need to be reordered relative to each other.
    The ordered_fields input should contain a list of correctly-ordered labels.
    Returns DataFrame with reordered fields conforming to ordered_fields.
    """

    # Create object to house TB master field order.
    TB_master = MasterFields(master_file)
    field_list = TB_master.master_list()

    # Look for fields unique to each type of export to infer the type.
    if 'iPhone' in df_to_sort.index:
        map_type = 'iPhone'
    elif 'Telex' in df_to_sort.index:
        map_type = 'Outlook'

    map_dict = TB_master.master_dict(map_type)

    # Ensure Thunderbird headings match hard-coded dict keys
    assert set(field_list) == set(map_dict.keys())

    # Create new list and populate with ordered df field names.
    print('Reordering fields...')
    sorted_index = []
    for TB_field in field_list:
        sorted_index += [map_dict[TB_field]]
    # sorted_index += ['Mod Date']
    # print(sorted_index)

    df_sorted = df_to_sort.reindex(index=sorted_index)
    # Replace NaNs with blanks
    return df_sorted.fillna('')


# # field_reorder test
# from list_read import list_read
# from list_combine import list_combine
# from list_write import list_write
# filename1 = './master/MyContacts-2017-08-10-210940-230_short_mod.csv'
# # filename2 = './input_data/2017-07-28_TSV_Contacts.csv'
# filename3 = './input_data/MyContacts-2017-08-10-210940-230.csv'
# df_current = list_read(filename1)
# df_in = list_read(filename3)
# df_comb = list_combine(df_current, df_in)
# df_sorted = field_reorder(df_comb)
# new_file = list_write(df_sorted, desc='iPhone_comb+sort_03')
