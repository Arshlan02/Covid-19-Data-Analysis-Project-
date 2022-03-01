In this Project, a tiny data set related to the Covid-19 pandemic is taken and analyzed in a very Easy To Understand (ETU) language.
Here, I learn how to work on a real project of Data Analysis with Python. 

At first I created number of questions given below regarding with the project and then I solved that questions with the help of Python. It is a project of Data Analysis with Python or you can say, Data Science with Python.


Questions:

Q. 1) Show the number of Confirmed, Deaths and Recovered cases in each Region.
Q. 2) Remove all the records where the Confirmed Cases is Less Than 10.
Q. 3) In which Region, maximum number of Confirmed cases were recorded ?
Q. 4) In which Region, minimum number of Deaths cases were recorded ?
Q. 5) How many Confirmed, Deaths & Recovered cases were reported from India till 29 April 2020 ?
Q. 6-A ) Sort the entire data wrt No. of Confirmed cases in ascending order.
Q. 6-B ) Sort the entire data wrt No. of Recovered cases in descending order.


The commands that I used in this project :

* import pandas as pd -- To import Pandas library
* pd.read_csv - To import the CSV file in Jupyter notebook
* df.count() - It counts the no. of non-null values of each column.
* df.isnull().sum() - It detects the missing values from the dataframe.
* import seaborn as sns - To import the Seaborn library.
* import matplotlib.pyplot as plt - To import the Matplotlib library.
* sns.heatmap(df.isnull()) - It will show the all columns & missing values in them in heat map form.
* plt.show() - To show the plot.
* df.groupby(‘Col_name’) - To form groups of all unique values of the column.
* df.sort_values(by= ['Col_name'] ) - Sort the entire dataframe by the values of the given column.     
* df[df.Col_1 = = ‘Element1’] - Filtering – We are accessing all records with Element1 only of Col_1.

