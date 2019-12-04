import time
import csv
from hashlib import md5
import pandas as pd
from bin import list_read as lr
from bin import list_combine as lc
from bin import field_reorder as fr
from bin import list_write as lw


while True:
    prog = input("Type 'r' to enter the Reformat program.\n"
        "Type 'c' to enter the Combine program.\n"
        "Type 'h' for help.\n"
        "Type 'q' to quit.\n>>> ")

    if prog.lower() == 'r':
        print('\t', '*' * 10, 'Reformat program', '*' * 10)
        master_filename = input("Enter the filepath of master field list to use"
                    " (TB import format) or press Enter to use default "
                    " ('master/TB_default_fields.csv'):\n>>>")
        reorder_filename = input('Enter the filepath of list to reorder '
                    'according to the TB field format:\n>>>')

        df_to_reorder = lr.list_read(reorder_filename)

        if master_filename:
            df_out = fr.field_reorder(df_to_reorder, master_filename)
        else:
            df_out = fr.field_reorder(df_to_reorder)

        desc = input("Enter a description for output-file name (like 'iPhone '"
                    "or 'Outlook') or press Enter for none:\n>>>")
        new_file = lw.list_write(df_out, desc)
        break

    elif prog.lower() == 'c':
        print('*' * 10, 'Combine program', '*' * 10)
        current_filename = input('Enter the filepath of current master list to '
                    'add entries to:\n>>>')
        df_current = lr.list_read(current_filename)

        input_filename = input('\nEnter the filepath of newly-exported list:\n>>>')
        df_input = lr.list_read(input_filename)

        df_out = lc.list_combine(df_current, df_input)

        desc = input("Enter a description for output-file name (like iPhone or "
                    "'Outlook') or press Enter for none:\n>>>")
        new_file = lw.list_write(df_out, desc)
        break

    elif prog.lower() == 'h':
        print('No help available yet')

    elif prog.lower() == 'q':
        quit()

    else:
        print("Invalid response. Only inputs accepted are 'r', 'c', 'h', or 'q'.")
