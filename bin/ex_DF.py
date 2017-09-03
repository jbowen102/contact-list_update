import pandas as pd

# Short series
s1 = pd.Series(['', 'Joey', '', 'Brown'],
        index=['Prefix', 'First Name', 'Middle Name', 'Last Name'])
s2 = pd.Series(['', 'Molly', '', 'Fields'],
        index=['Prefix', 'First Name', 'Middle Name', 'Last Name'])

# Full-length series
s3 = pd.Series(['', 'Joey', '', 'Brown'],
        index=['Prefix', 'First Name', 'Middle Name', 'Last Name'])
s4 = pd.Series(['', 'Joey', '', 'Brown'],
        index=['Prefix', 'First Name', 'Middle Name', 'Last Name'])

s5 =

dict1 = {'Brown, Joey': s1,
	     'Fields, Molly': s2}

# df = pd.DataFrame.from_dict(dict1, orient='index')

df2 = pd.DataFrame(dict1)


# http://pandas.pydata.org/pandas-docs/stable/dsintro.html#indexing-selection

# df.Prefix
# df2.
# Addressing the records this way causes problems because business names
# have spaces.
# Series label needs to be a valid Python name to be used for selection as attribute.
# http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe-column-attribute-access-and-ipython-completion

# This give error:
# df['Brown, Joey']
# This works, so only column can be used:
# df['Prefix']

# Select record/series corresponding to label 'Brown, Joey'
# df.loc['Brown, Joey']
# df.loc[['Brown, Joey', 'Fields, Molly']]
# df.loc['Brown, Joey':'Fields, Molly'] # both start and stop indices returned

# Select record/series corresponding to integer 1
# df.iloc[1]

# Slice records/series
# df[1:3]
