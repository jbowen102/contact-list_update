import time
import csv
import pandas as pd


class TimeStamp(object):

    def __init__(self):
        # Get date and time to put in filename
        # These are integers
        self.yr = time.localtime().tm_year
        self.mon = time.localtime().tm_mon
        self.day = time.localtime().tm_mday
        self.hr = time.localtime().tm_hour
        self.minute = time.localtime().tm_min
        self.sec = time.localtime().tm_sec

    def short_form(self):
        return '%.4i-%.2i-%.2i' % (self.yr, self.mon, self.day)

    def long_form(self):
        return ('%.4i-%.2i-%.2i' % (self.yr, self.mon, self.day) + '_' +
                '%.2i%.2i%.2i' % (self.hr, self.minute, self.sec))


class RecordSeries(object):
    def __init__(self, record_row, field_list):
        self.record_row = record_row
        self.field_list = field_list
        # Pad end of row with blank entries if field_list longer
        # (Outlook exports this way). Also add blank entry for
        # Mod Date column, if it didn't already exist.
        len_diff = len(self.field_list) - len(self.record_row)
        if len_diff > 0:
            self.record_row += [''] * len_diff
        self.record_series = pd.Series(self.record_row, index=self.field_list)

    def get_series(self):
        return self.record_series

    def set_date(self, date_str):
        self.record_series['Mod Date'] = date_str

    def name_map(self):
        "Returns a dict with series name as key and series as value"
        # Parse name for series.
        self.firstn = self.record_series.get('First Name', None).lower()
        self.lastn = self.record_series.get('Last Name', None).lower()
        self.org = self.record_series.get('Organization',
              self.record_series.get('Company', None)).lower()

        if self.firstn and self.lastn:
            self.name = self.lastn + ', ' + self.firstn
        elif self.firstn:
            self.name = self.firstn
        elif self.org:
            self.name = self.org
        else:
            raise ValueError('No first, last, or organization name for '
                                'record: %r' % self.record_series)

        return {self.name: self.record_series}


def field_list_mod(raw_field_list):
    """
    Takes in row with standard field names.
    Adds 'Mod Date' field to end if not present.
    Also modifies standard iPhone export field list to fix non-unique headings.
    Returns list with unique entries.
    """

    mod_field_list = raw_field_list[:]

    # Use 'iPhone' field existence to determine it's iPhone export.
    if 'iPhone' in raw_field_list:
        print('Type: iPhone')

        # If CSV doesn't already have date-modified column, add it.
        if not 'Mod Date' in raw_field_list:
            mod_field_list += ['Mod Date']

            # Assume file also has non-unique fields
            # Check that number of non-unique fields hasn't changed.
            assert mod_field_list.count('Home') == 4
            assert mod_field_list.count('Work') == 4
            assert mod_field_list.count('Email') == 4

            # Make columns unique.
            mod_field_list[mod_field_list.index('Work')] = 'Work [Phone]'
            mod_field_list[mod_field_list.index('Home')] = 'Home [Phone]'

            mod_field_list[mod_field_list.index('Home')] = 'Home [Email]'
            mod_field_list[mod_field_list.index('Work')] = 'Work [Email]'

            mod_field_list[mod_field_list.index('Email')] = 'Email [1]'
            mod_field_list[mod_field_list.index('Email')] = 'Email [2]'
            mod_field_list[mod_field_list.index('Email')] = 'Email [3]'
            mod_field_list[mod_field_list.index('Email')] = 'Email [4]'

            mod_field_list[mod_field_list.index('Home')] = 'Home [URL]'
            mod_field_list[mod_field_list.index('Work')] = 'Work [URL]'

            mod_field_list[mod_field_list.index('Home')] = 'Home [Address]'
            mod_field_list[mod_field_list.index('Work')] = 'Work [Address]'

        return mod_field_list


    elif 'Telex' in raw_field_list:
        print('Type: Outlook')

        # If CSV doesn't already have date-modified column, add it.
        if not 'Mod Date' in raw_field_list:
            mod_field_list += ['Mod Date']
        # Outlook fields already unique.

        return mod_field_list

    else:
        print('Unrecognized field format:\n%r' % raw_field_list)


def list_read(filename, start_line=2, end_line=None):
    """
    Function to read in CSV data from a contact list and store in a DataFrame.
    Inputs:
        filename: a string containing the file path and name
        start_line: the first numbered line of the CSV that should be included
        in the resulting DataFrame (defaults to 2, the first entry)
        end_line: the last numbered line of the CSV that should be included in
        the resulting DataFrame (defaults to None, the end)
    Reads in the first row as the field names.
    Returns pandas DataFrame object with CSV contact list entries.
    The key for each Series in the DataFrame is the First+Last Name, First
    Name only, or Organization name.
    """

    if end_line and not end_line >= start_line:
        raise ValueError('End value must be greater than or equal to '
                'start value.')

    with open(filename, 'r') as csvfile:
        print('Reading data from CSV...')
        file_in = csv.reader(csvfile)

        field_list = file_in.__next__()

        # Add 'Mod Date' field, make field names unique if necessary.
        field_list = field_list_mod(field_list)

        record_dict = {}
        i = 2

        for row in file_in:
            if i >= start_line:
                row_record_series = RecordSeries(row, field_list)

                # If there is no date in the Add/Mod Date column, add today's.
                row_series = row_record_series.get_series()
                if not row_series['Mod Date']:
                    date_now = TimeStamp()
                    row_record_series.set_date(date_now.short_form())

                record_dict.update(row_record_series.name_map())

            i += 1
            if end_line and i > end_line:
                break

    df = pd.DataFrame(record_dict)

    return df.sort_index(axis=1)
