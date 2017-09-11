import pandas as pd

# Short series
s1 = pd.Series(['', 'Justine', '', 'Henderson'],
        index=['Prefix', 'First Name', 'Middle Name', 'Last Name'])
s2 = pd.Series(['', 'Mathias', 'W', 'Little'],
        index=['Prefix', 'First Name', 'Middle Name', 'Last Name'])

dict1 = {'Henderson, Justine': s1,
	     'Little, Mathias': s2}

df1 = pd.DataFrame(dict1)

# Full-length series (iPhone export format)
s3 = pd.Series(['', 'Justine', '', 'Henderson', '', 'The Sandwich Shop',
        '', '', '', '', '', '(949) 569-4371', '', '', '', '', '', '', '', '',
        '', '', '', '', '', '', '', 'cargocollective.com', '',
        '70 Bowman St. South Windsor, CT 06074', '', ''],
        index=['Prefix', 'First Name', 'Middle Name', 'Last Name', 'Suffix',
        'Organization', 'Department', 'Title', 'Nickname', 'Birthday',
        'Anniversary', 'Mobile', 'iPhone', 'Work [Phone]', 'Home [Phone]',
        'Main', 'Home Fax', 'Work Fax', 'Pager', 'Other', 'Home [Email]',
        'Work [Email]', 'Email [1]', 'Email [2]', 'Email [3]', 'Email [4]',
        'Home Page', 'Home [URL]', 'Work [URL]', 'Home [Address]',
        'Work [Address]', 'Note'])
s4 = pd.Series(['', 'Mathias', 'W', 'Little', 'Jr.', '', '', '', '',
        '1955-01-09', '', '(293) 799-2919', '', '', '', '', '', '', '', '',
        'euice@outlook.com', '', '', '', '', '', '', '', '',
        '17 Wilson Rd. Medford, MA 02155', '', ''],
        index=['Prefix', 'First Name', 'Middle Name', 'Last Name', 'Suffix',
        'Organization', 'Department', 'Title', 'Nickname', 'Birthday',
        'Anniversary', 'Mobile', 'iPhone', 'Work [Phone]', 'Home [Phone]',
        'Main', 'Home Fax', 'Work Fax', 'Pager', 'Other', 'Home [Email]',
        'Work [Email]', 'Email [1]', 'Email [2]', 'Email [3]', 'Email [4]',
        'Home Page', 'Home [URL]', 'Work [URL]', 'Home [Address]',
        'Work [Address]', 'Note'])

dict2 = {'Henderson, Justine': s3,
	     'Little, Mathias': s4}

df2 = pd.DataFrame(dict2)


# df2['Little, Mathias']
# Returns the series associated with this label.

# df2['Little, Mathias']['Department']
# Returns data in the Department field

# df2['Little, Mathias'][0]
# Returns data in first field (Prefix in this case) as string

# df2['Little, Mathias'][0:2]
# Returns slice with first two fields and indices together as series.

# df2['Little, Mathias']['Mod Date'] = '2017-09-04'
# To assign a new value to an existing field or assign a value in a new field.

# df2['Little, Mathias']['Prefix'] = 'Sir'
# To overwrite data in existing field.

# df2['Little, Mathias'][0:1] = 'Sir'
# To overwrite data in existing field.

# df2[0:1]
# Returns a dataframe with the first entry of all series.

# df2['Little, Mathias'].keys()[-1]
# To see the last index

# s3.values returns np array with all values in that series (similar to .keys())

# df2.index.values
# Returns array with all indices listed. Can use len() on.

# df2.loc['Note'] = 'text here'
# Assigns new values to all columns at the specified index.

# df2.reindex(index=[])
# Allows new list of indices to be specified (reorder an existing index list.
# Can remove indices too). Can assign new column list.

# df2.index = []
# Allows a new list of indices to be specified. The data is not reordered (use
# .reindex() for this). It just overwrites all the index names in place.

# http://pandas.pydata.org/pandas-docs/stable/dsintro.html#indexing-selection

# Series label needs to be a valid Python name to be used for selection as attribute.
# http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe-column-attribute-access-and-ipython-completion


# df.loc['Brown, Joey']
# df.loc[['Brown, Joey', 'Fields, Molly']]
# Select record/series corresponding to labels.

# df.iloc[1]
# Select record/series corresponding to integer 1

# df[1:3]
# Slice records/series
