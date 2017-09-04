import pandas as pd

# Short series
s1 = pd.Series(['', 'Justine', '', 'Henderson'],
        index=['Prefix', 'First Name', 'Middle Name', 'Last Name'])
s2 = pd.Series(['', 'Mathias', 'W', 'Little'],
        index=['Prefix', 'First Name', 'Middle Name', 'Last Name'])

dict1 = {'Henderson, Justine': s1,
	     'Little, Mathias': s2}

df1 = pd.DataFrame(dict1)

# Full-length series (iPhone export)
s3 = pd.Series(['', 'Justine', '', 'Henderson', '', 'The Sandwich Shop',
        '', '', '', '', '', '(949) 569-4371', '', '', '', '', '', '', '', '',
        '', '', '', '', '', '', '', 'cargocollective.com', '',
        '70 Bowman St. South Windsor, CT 06074', '', ''],
        index=['Prefix', 'First Name', 'Middle Name', 'Last Name', 'Suffix',
        'Organization', 'Department', 'Title', 'Nickname', 'Birthday',
        'Anniversary', 'Mobile', 'iPhone', 'Work', 'Home', 'Main', 'Home Fax',
        'Work Fax', 'Pager', 'Other', 'Home', 'Work', 'Email', 'Email', 'Email',
        'Email', 'Home Page', 'Home', 'Work', 'Home', 'Work', 'Note'])
s4 = pd.Series(['', 'Mathias', 'W', 'Little', 'Jr.', '', '', '', '',
        '1955-01-09', '', '(293) 799-2919', '', '', '', '', '', '', '', '',
        'euice@outlook.com', '', '', '', '', '', '', '', '',
        '17 Wilson Rd. Medford, MA 02155', '', ''],
        index=['Prefix', 'First Name', 'Middle Name', 'Last Name', 'Suffix',
        'Organization', 'Department', 'Title', 'Nickname', 'Birthday',
        'Anniversary', 'Mobile', 'iPhone', 'Work', 'Home', 'Main', 'Home Fax',
        'Work Fax', 'Pager', 'Other', 'Home', 'Work', 'Email', 'Email', 'Email',
        'Email', 'Home Page', 'Home', 'Work', 'Home', 'Work', 'Note'])

dict2 = {'Henderson, Justine': s3,
	     'Little, Mathias': s4}

df2 = pd.DataFrame(dict2)


# df2['Little, Mathias'] # returns the series associated with this label.
# df2['Little, Mathias']['Department'] # returns data in the Department field
# df2['Little, Mathias'][0] # returns data in first field (Prefix in this case)

# df2['Little, Mathias'][0] # returns data in first field (Prefix in this case)
# as string
# df2['Little, Mathias'][0:2] # returns slice with first two fields and indices
# together as series.

# df2['Little, Mathias']['Mod Date'] = '2017-09-04' # to add an entry into a
# new field.

# df2['Little, Mathias']['Prefix'] = 'Sir' # to overwrite data in existing field.
# df2['Little, Mathias'][0:1] = 'Sir' # to overwrite data in existing field.

# df2['Little, Mathias'].keys()[-1] # to see the last index

# df2.index.values # returns array with all indices listed. Can use len() on.


# http://pandas.pydata.org/pandas-docs/stable/dsintro.html#indexing-selection

# df = pd.DataFrame.from_dict(dict1, orient='index')

# Series label needs to be a valid Python name to be used for selection as attribute.
# http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe-column-attribute-access-and-ipython-completion


# obs
# Select record/series corresponding to label 'Brown, Joey'
# df.loc['Brown, Joey']
# df.loc[['Brown, Joey', 'Fields, Molly']]
# df.loc['Brown, Joey':'Fields, Molly'] # both start and stop indices returned

# Select record/series corresponding to integer 1
# df.iloc[1]

# Slice records/series
# df[1:3]
