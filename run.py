import time
import csv
from os import listdir
from os.path import exists as path_exists
from hashlib import md5
import pandas as pd
from bin import list_read as lr
from bin import list_combine as lc
from bin import field_reorder as fr
from bin import list_write as lw


class InputDirectoryError(Exception):
    pass


def combine_prog():
    print('*' * 10, 'Combine program', '*' * 10)
    current_filename = input("Enter the filepath of current master list to "
                "add entries to:\n>>> ")
    df_current = lr.list_read(current_filename)

    input_filename = input("\nEnter the filepath of new import list or press "
        "Enter to use default\n (whatever lone file is in the 'input_files' "
        "directory):\n>>> ")

    if input_filename == "":
        avail_input_files = listdir('./input_data/')
        if len(avail_input_files) == 1:
            df_input = lr.list_read('./input_data/' + avail_input_files[0])
        else:
            raise InputDirectoryError("There must be exactly one file in the 'input_data' dir.")
    elif path_exists(input_filename):
        df_input = lr.list_read(input_filename)
    else:
        raise InputDirectoryError("Invalid response. Start over.")

    df_out = lc.list_combine(df_current, df_input)

    desc = input("Enter a description for output-file name (like 'iPhone' or "
                "'Outlook') or press Enter for none:\n>>> ")
    new_file = lw.list_write(df_out, desc)


def reformat_prog():
    print('\t', '*' * 10, 'Reformat program', '*' * 10)
    master_filename = input("Enter the filepath of master field list to use"
                " (TB import format) or press Enter to use default\n"
                "\t('master/TB_default_fields.csv'):\n>>> ")
    reorder_filename = input("Enter the filepath of list to reorder "
                "according to the TB field format or press Enter to use default\n"
                "(whatever lone file is in the 'input_files' directory):\n>>> ")

    if reorder_filename == "":
        avail_input_files = listdir('./input_data/')
        if len(avail_input_files) == 1:
            df_to_reorder = lr.list_read('./input_data/' + avail_input_files[0])
        else:
            raise InputDirectoryError("There must be exactly one file in the 'input_data' dir.")
    elif path_exists(reorder_filename):
        df_to_reorder = lr.list_read(reorder_filename)
    else:
        raise InputDirectoryError("Invalid response. Start over.")

    if master_filename:
        df_out = fr.field_reorder(df_to_reorder, master_filename)
    else:
        df_out = fr.field_reorder(df_to_reorder)

    desc = input("Enter a description for output-file name (like 'iPhone' "
                "or 'Outlook') or press Enter for none:\n>>> ")
    new_file = lw.list_write(df_out, desc)


while True:
    prog = input(
        "Type 'cr' to run Combine program then Reformat (std iPhone workflow).\n"
        "Type 'r' to run Reformat program only (std Outlook workflow).\n"
        "Type 'c' to enter the Combine program only.\n"
        "Type 'h' for help.\n"
        "Type 'q' to quit.\n>>> ")

    if prog.lower() == 'cr':
        combine_prog()
        reformat_prog()
        break

    elif prog.lower() == 'r':
        reformat_prog()
        break

    elif prog.lower() == 'c':
        combine_prog()
        break

    elif prog.lower() == 'h':
        print("\nCombine program (typically only used with iPhone exports):\n"
        "\t-The Combine program is used to update a CSV master list of contacts with "
        "newly-added or modified entries \n"
        "\t\tfound in an input CSV file recently exported.\n"
        "\t-The formats supported are iPhone- and Outlook-generated CSV exports.\n"
        "\t-Intent is to accept and combine input and master lists in SOURCE format, not TB format.\n"
        "\t-Before running, check input CSV for anomolies. Correct in input "
        "file or on source device (and re-export) \n"
        "\t\tbefore proceeding with program.\n"
        "\t-Place a copy of input file in 'input_data' directory.\n"
        "\t-Ensure the most recent master list CSV is in the 'master' directory.\n"
        "\t-Program will ask for name of input and master lists (which do not "
        "need to be in the program directories).\n"
        "\t-Program will combine to make a new master list with the union of records "
        "found in the two files. \n"
        "\t-Any new records found in input file will be added to master list, and "
        "any that have been modified \n"
        "\t\tsince last combine will replace the previous versions in the master list.\n"
        "\t-New master list will be written to new file in output_data directory.\n"
        "\t-After verifying that output CSV is valid, manually copy new master list "
        "to master dir for future use.\n"
        "\t-(The Assumption is that contacts will not be deleted from Outlook. "
        "No combining needed, because \n"
        "\t\tinput list always should include previously-seen records.)\n"

        "\nReformat program (used with both iPhone and Outlook exports):\n"
        "\t-The Reformat program accepts either input data type (iPhone or Outlook export).\n"
        "\t-Place a copy of input file in 'input_data' directory.\n"
        "\t-The input data is then reformatted according to TB master field list.\n"
        "\t-Its fields are renamed and reordered according to the TB convention.\n"
        "\t-New reformatted list will be written to new file in output_data directory.\n\n")


    elif prog.lower() == 'q':
        quit()

    else:
        print("Invalid response. Only inputs accepted are 'cr', 'r', 'c', 'h', "
                                                                "or 'q'.")
