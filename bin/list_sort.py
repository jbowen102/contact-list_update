import csv
import pandas as pd
from list_read import list_read
# from list_write import list_write # circular reference


def master_field_dict(master_file='./current_master/TB_default_fields.csv'
                            map_type):
    """
    Function to read in field order from a master list and 'iPhone' or 'Outlook'
    as type of mapping to create.
    Fields should be ordered according to Thunderbird default import order.
    Reads in the first row as the field names.
    Data in any row but the first will be ignored.
    Returns a dict with mapping of Thunderbird heading names to Outlook or
    iPhone-export contact-list heading names.
    to .
    """

    with open(filename, 'r') as csvfile:
        print('Reading master field order from CSV...')
        file_in = csv.reader(csvfile)

        field_list = file_in.__next__()

        if map_type == 'iPhone':
            map_dict = {'First Name': 'First Name',
                        'Last Name': 'Last Name',
                        'Display Name': '',
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
                    	'Home Address': 'Home [Address]',
                    	'Work Address': 'Work [Address]',
                    	'Notes': 'Note',
                    	'Pager Number': 'Pager',
                    	'Home Address 2': '',
                    	'Home City': '',
                    	'Home State': '',
                    	'Home ZipCode': '',
                    	'Screen Name': '',
                    	'Home Country': '',
                    	'Work Address 2': '',
                    	'Work City': '',
                    	'Work State': '',
                    	'Work ZipCode': '',
                    	'Work Country': '',
                    	'Web Page 2': '',
                    	'Birth Year': '',
                    	'Birth Month': '',
                    	'Birth Day': ''}

        if map_type == 'Outlook':
            map_dict = {'First Name': 'First Name',
                        'Last Name': 'Last Name',
                        'Display Name': 'Title',
                        'Nickname': '',
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
                    	'Screen Name': '',
                    	'Home Country': 'Home Country/Region',
                    	'Work Address 2': 'Business Street 2',
                    	'Work City': 'Business City',
                    	'Work State': 'Business State',
                    	'Work ZipCode': 'Business Postal Code',
                    	'Work Country': 'Home Country/Region',
                    	'Web Page 2': '',
                    	'Birth Year': '',
                    	'Birth Month': '',
                    	'Birth Day': ''}


    elif map_type == 'iPhone':

    else:
        raise ValueError("map_type must be either 'iPhone' or 'Outlook'")


    # Ensure Thunderbird headings match hard-coded dict keys
    assert set(field_list) == set(map_dict.keys())



# # master_field_dict test
# # field_list = master_field_dict()
# # print(field_list)
# field_list = master_field_dict()
# print(field_list)
# new_file = list_write(field_list)


def list_sort(DF_to_sort, ordered_fields):
    """
    Function to take in pandas DataFrame containing contact-data entries that
    need to be reordered relative to each other.
    The ordered_fields input should contain a list of correctly-ordered labels.
    Returns DataFrame with reordered fields conforming to ordered_fields.
    """

    field_order = master_field_list()

    pass
