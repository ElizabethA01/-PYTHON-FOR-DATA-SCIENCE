<html><head></head><body>#!/usr/bin/env python
# coding: utf-8

# # Analyze Wage Data with Python
# 
# - [View Solution Notebook](./solutions.html)
# - [View Project Page](https://www.codecademy.com/projects/practice/analyze-wage-data-with-python)

# ## Task Group 1 - Import and Clean

# ### Task 1
# 
# Display the first five lines of `df_wages`.

# In[86]:


import pandas as pd

df_wages = pd.read_csv(&#39;wages.csv&#39;)

# Preview the data
df_wages.head()


# ### Task 2
# 
# Rename the `Occupation title (click on the occupation title to view its profile)` column to `Occupation title`. 

# In[87]:


col_wrapper = {&#39;Occupation title (click on the occupation title to view its profile)&#39;:&#39;Occupation title&#39;}
df_wages = df_wages.rename(
    mapper=col_wrapper,
    axis=1)

# show output
df_wages.head()


# ### Task 3
# 
# Drop any redundant or otherwise unnecessary columns from `df_wages`. Make a note of why these columns are suitable for dropping!

# In[88]:


dropped = [&#39;Year&#39;, &#39;Index&#39;]
df_wages = df_wages.drop(
    labels = dropped,
    axis=1
)

# show output
df_wages.head()


# ### Task 4
# 
# Display column information including names, # non-null entries, and data types.

# In[89]:


df_wages.info()


# ## Task Group 2 - Column Transformations

# ### Task 5
# 
# Use pandas to split the information in the `Occupation title` column into new columns `Industry`, `Level`, and `Occupation`. 

# In[90]:


df_wages[&#39;Industry&#39;] = df_wages[&#39;Occupation title&#39;].str.split(pat=&#39;-&#39;, expand=True)[0]
df_wages[&#39;Level&#39;] = df_wages[&#39;Occupation title&#39;].str.split(pat=&#39;-&#39;, expand=True)[1]
df_wages[&#39;Occupation&#39;] = df_wages[&#39;Occupation title&#39;].str.split(pat=&#39;-&#39;, expand=True)[2]


# show output
df_wages[[&#39;Occupation title&#39;, &#39;Industry&#39;, &#39;Level&#39;, &#39;Occupation&#39;]].head()


# ### Task 6
# 
# Remove any leading and trailing whitespaces in the columns `Industry`, `Level`, and `Occupation`.

# In[100]:


df_wages[&#39;Industry&#39;] = df_wages[&#39;Industry&#39;].str.strip()
df_wages[&#39;Level&#39;] = df_wages[&#39;Level&#39;].str.strip()
df_wages[&#39;Occupation&#39;] = df_wages[&#39;Occupation&#39;].str.strip()


# ### Task 7
# 
# Replace the `&#39;$&#39;` character in the columns `Average hourly wage`, `Industry average`, and `Similar occupation average` with an empty character `&#39;&#39;` (no space between the single quotes!).

# In[92]:


df_wages[&#39;Average hourly wage&#39;] = df_wages[&#39;Average hourly wage&#39;].str.replace(pat=&#39;$&#39;, repl=&#39;&#39;, regex=False)
df_wages[&#39;Industry average&#39;] = df_wages[&#39;Industry average&#39;].str.replace(pat=&#39;$&#39;, repl=&#39;&#39;, regex=False)
df_wages[&#39;Similar occupation average&#39;] = df_wages[&#39;Similar occupation average&#39;].str.replace(pat=&#39;$&#39;, repl=&#39;&#39;, regex=False)
# show output
df_wages[[&#39;Average hourly wage&#39;, &#39;Industry average&#39;, &#39;Similar occupation average&#39;]].head()


# ### Task 8
# 
# Convert the data types of the columns `Average hourly wage`, `Industry average`, and `Similar occupation average` from `object` to `float`.

# In[93]:


df_wages[&#39;Average hourly wage&#39;] = df_wages[&#39;Average hourly wage&#39;].astype(float)
df_wages[&#39;Industry average&#39;]= df_wages[&#39;Industry average&#39;].astype(float)
df_wages[&#39;Similar occupation average&#39;] = df_wages[&#39;Similar occupation average&#39;].astype(float)

# show output
df_wages.info()


# ## Task Group 3 - Comparison to Industry Average

# ### Task 9
# 
# Calculate the difference between the average hourly wage and the industry average. Assign the difference to a new column `Industry wage difference`.

# In[94]:


df_wages[&#39;Industry wage difference&#39;] = df_wages[&#39;Average hourly wage&#39;] - df_wages[&#39;Industry average&#39;]

# show output
df_wages[[&#39;Occupation&#39;, &#39;Average hourly wage&#39;, &#39;Industry average&#39;, &#39;Industry wage difference&#39;]].head()


# ### Task 10
# 
# Divide `Industry wage difference` by `Industry average` to convert the difference to a percent change. (You might want to multiply by `100` at the end to display as a percentage).
# 
# Assign the result to new column called `Industry wage pctchg`. 

# In[95]:


df_wages[&#39;Industry wage pctchg&#39;] = df_wages[&#39;Industry wage difference&#39;]/df_wages[&#39;Industry average&#39;] * 100

# show output
df_wages[[&#39;Industry&#39;, &#39;Occupation&#39;,&#39;Level&#39;, &#39;Average hourly wage&#39;, &#39;Industry average&#39;, &#39;Industry wage pctchg&#39;]].head()


# ### Task 11
# 
# Sort `df_wages` by the `Industry wage pctchg` column from *highest* to *lowest*. Assign the result to the variable `highest_industry_pctchg`.

# In[96]:


highest_industry_pctchg = df_wages.sort_values(by=&#39;Industry wage pctchg&#39;, ascending=False)

# show output
highest_industry_pctchg[[&#39;Industry&#39;, &#39;Occupation&#39;,&#39;Level&#39;, &#39;Industry wage pctchg&#39;]].head(10)


# ## Task Group 4 - Computer Jobs

# ### Task 12
# 
# Use the separate `Industry` column you created in Task 5 to investigate occupations in the **&#39;Computer and Mathematical Occupations&#39;** industry. Filter `df_wages` for this specific industry and create a new DataFrame named `cs_math_occupations`.

# In[102]:


cs_math_occupations = df_wages[df_wages[&#39;Industry&#39;] == &#39;Computer and Mathematical Occupations&#39;]


# ### Task 13
# 
# Sort `cs_math_occupations` by `Average hourly wage` from highest to lowest, and display the results.

# In[104]:


cs_math_occupations.sort_values(by=&#39;Average hourly wage&#39;, ascending=False)

<script type="text/javascript" src="https://external-production.codecademy.com/assets/relay.js"></script></body></html>