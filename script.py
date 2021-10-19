# Import modules
import pandas as pd
import numpy as np

# Read dataset into a variable named car_eval
car_eval = pd.read_csv('car_eval_dataset.csv')

# Output the first five rows of car_eval
print(car_eval.head())

# Create a table of frequencies of all the cars reviewed by manufacturer_country
print(car_eval['manufacturer_country'].value_counts())

# What is the modal category?
modal_category = car_eval['manufacturer_country'].value_counts()[0]

# Output the modal category
print('\nThe modal category = {}'.format(modal_category))

# Which country appears 4th most frequently?
print('\nThe 4th most frequently appeared country is United States\n')

# Calculate a table of proportions for countries that appear in manufacturer_country in the dataset
print(car_eval['manufacturer_country'].value_counts(normalize=True))

# What percentage of cars were manufactured in Japan?
print('\n22.8% of cars were manufactured in Japan\n')

# Print out a list of the possible values for buying_cost variable in car_eval
print(car_eval['buying_cost'].unique())

# Create a new list, named  buying_cost_categories, that contains the unique values in buying_cost variable, ordered from lowest to highest
buying_cost_categories = ['low', 'med', 'high', 'v-high']

# Convert buying_cost to type 'category'
car_eval['buying_cost'] = pd.Categorical(car_eval['buying_cost'], buying_cost_categories, ordered=True)

# Calculate the median of the buying_cost variable into a variable called median_category_num
median_category_num = np.median(car_eval['buying_cost'].cat.codes)

# Output median_category_num
print('\nMedian of buying_cost variable is {}'.format(median_category_num))

# Display the median category of buying_cost variable
print('\nMedian category of buying_cost variable is {}\n'.format(buying_cost_categories[int(median_category_num)]))

# Calculate a table of proportions for the luggage variable of car_eval and print the result
print('{}\n'.format(car_eval['luggage'].value_counts(normalize=True)))

# Calculate a table of proportions for the luggage variable of car_eval including NaN values and print the result
print(car_eval['luggage'].value_counts(dropna=False, normalize=True))

# Are there any missing values in this column?
print('\nThere is no missing value in the luggage column of \'car_eval\' dataset\n')

# Calculate a table of proportions for the luggage variable using a different method (since there is no missing value in that column) of car_eval and print the result
print(car_eval['luggage'].value_counts() / len(car_eval['luggage']))

# Find the count of cars that have 5 or more doors in the dataset into a variable called frequency
frequency = (car_eval['doors'] == '5more').sum()

# Output frequency
print('\nThe count of cars that have 5 or more doors is {}\n'.format(frequency))

# Find the proportion of cars that have 5+ doors. Save the result in a variable called proportion
proportion = (car_eval['doors'] == '5more').mean()

# Output proportion
print('The proportion of cars that have 5+ doors is {}'.format(proportion))