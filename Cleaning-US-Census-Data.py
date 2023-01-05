import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

# load all files into one dataframe to analyse
states_filename = glob.glob('states*.csv')

df_list = []
for filename in states_filename:
    df = pd.read_csv(filename)
    df_list.append(df)
us_census = pd.concat(df_list)

# use regex to convert income to correct format
us_census.Income = pd.to_numeric(us_census.Income.str.replace('$', '', regex=False))
us_census.Income = us_census.Income.round(2)

# separate genderpop column to male and female
gender_split = us_census.GenderPop.str.split('M_', expand=True)
us_census['MalePop'] = pd.to_numeric(gender_split[0])
us_census['FemalePop'] = pd.to_numeric(gender_split[1].str.replace('F', '', regex=False))
drop_col = ['GenderPop', 'Unnamed: 0']
us_census = us_census.drop(
  labels = drop_col,
  axis=1
)

# present graph showing female population and income
plt.scatter(us_census['FemalePop'], us_census['Income'])
plt.title('Female Population per State vs Income')
plt.xlabel('Population of Women per State')
plt.ylabel("Income (in US Dollars)")
plt.show()
plt.clf() #clear current figure

# replace na values in women column
us_census = us_census.fillna(value={"FemalePop":us_census.TotalPop - us_census.MalePop})

# drop duplicates
us_census = us_census.drop_duplicates()

plt.scatter(us_census['FemalePop'], us_census['Income'])
plt.title('Female Population per State vs Income')
plt.xlabel('Population of Women per State')
plt.ylabel("Income (in US Dollars)")
plt.show()
plt.clf()

#Histogram of Races
races = ['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']
for race in races:
  us_census[race] = pd.to_numeric(us_census[race].str.replace('%', '', regex=False))
  us_census[race] = round(us_census[race], 2)

# fill gaps in race columns
us_census = us_census.fillna(value={"Pacific":1-us_census.White - us_census.Black - us_census.Native - us_census.Asian - us_census.Hispanic })

for race in races:
  plt.hist(us_census[race])
  plt.title("Histogram of the Percentage of {} People per State".format(race))
  plt.xlabel('Percentage')
  plt.ylabel('Frequency')
  plt.show()
  plt.clf()
