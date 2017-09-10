import csv
import pandas as pd
from list_read import list_read
# from list_write import list_write # circular reference


def master_field_list(filename='./current_master/TB_default_fields.csv'):
    """
    Function to read in field order from a master list.
    Fields should be ordered according to Thunderbird default import order.
    Reads in the first row as the field names.
    Data in any row but the first will be ignored.
    Returns list object with field names as strings.
    """
    with open(filename, 'r') as csvfile:
        print('Reading master field order from CSV...')
        file_in = csv.reader(csvfile)

        i = 0
        for row in file_in:

            # Make sure not to read data from any rows except first.
            if i >= 1:
                break
            i += 1

            field_list = row

        return field_list


# # master_field_list test
# # field_list = master_field_list()
# # print(field_list)
# field_list = master_field_list()
# print(field_list)
# new_file = list_write(field_list)


def iPhone_field_map():
    """
    Function that returns a dict with mapping of iPhone-export contact-list
    heading names to Thunderbird heading names.
    """


def list_sort(DF_to_sort, ordered_fields):
    """
    Function to take in pandas DataFrame containing contact-data entries that
    need to be reordered relative to each other.
    The ordered_fields input should contain a list of correctly-ordered labels.
    Returns DataFrame with reordered fields conforming to ordered_fields.
    """

    field_order = master_field_list()

    pass
