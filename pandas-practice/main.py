import pandas as pd   #a way of saying "import the pandas library and give it the nickname pd"
#pandas is an open source python library that provides data manipulation and analysis tools for working with structured data
# Pandas has two primary data structures: Series (1-dimensional) and DataFrame (2-dimensional like full spreadsheet or SQL table)
# Whenever we start working with pandas, what we usually do first is load data
#CSV - Comma Separated Values
#Pandas has a built-in function called pd.read_csv('data.csv'), pd.read_excel('data.xlsx), pd.DataFrame()
# that makes it easy to load data from a CSV, excel or file/DataFrame(dictionary) into a DataFrame(2-dimensional data structure)
#When working with Large machine learning libraries, it will already have dataframes loaded for you
#####################################################################################################################

#Dataframe is a 2-dimensional,  tabular data structure with labeled axes (rows and columns). Python Native spreadsheet  
#   - Key Features: 1) Label based indexing  2) Column-wise and row-wise operation 3) Support for mixed data types 4) Fast, vectorized operations (built on NumPy)

######################################################################################################################

df= pd.read_csv('orders.csv')  # Load data from a CSV file into a DataFrame  #read_csv is a function in pandas that reads a CSV file and converts it into a DataFrame
print(df)  # Print the DataFrame to see the loaded data  #Automaticaly assigns indeces to each row starting that gets loaded in


#working with pandas is best done in a jupyter notebook environment as it allows for interactive data exploration and visualization, therefore the rest of the code will be in a jupyter notebook