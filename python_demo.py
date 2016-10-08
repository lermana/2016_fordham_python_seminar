# September 18, 2016
# Here is a Python demo

# Note: any statements that start with a pound sign (like this one) are considered 'comments' and will not be run by the computer as code


# ----------------- OVERVIEW -----------------

# A simple problem: We have a folder that is full of .csv files. 
# Each csv file contains stock data for the company whose ticker can be found in the file name (table_$ticker.csv)
# Our goal is to:
#	1) extract closing prices by date for each stock
# 	2) combine all the data into one table (complete with headers) 
#	3) and write it to a new csv file

# About the data: 
	# Gathered from https://quantquote.com/historical-stock-data, under 'Free Data'
	# Daily stock price data for the S&P 500 stocks that ranges from January 1998 - August 2013
	# These stocks presumably were the members of the S&P 500 as of August 9th 2013
	# Columns: date (YYYYMMDD), time (empty / not relevant), open, high, low, close, volume
	# Note: prices & volumes here are adjusted for splits & dividends

# This is not necessarily the data we will be using for the rest of the seminar

# This might seem a little intense to those of you who are new to programming and/or Python
# It is TOTALLY OK if some or a lot of this is confusing
# Everything here will be thoroughly fleshed out during the seminar

# That said, *MOST* (300 out of 350 lines) of this document is just a text explanation of what the code is doing

# ****** TO RUN THIS CODE: see instructions at bottom (you can search for 'to run')

# please feel free to contact me with any questions: https://www.linkedin.com/in/abelerman


# ----------------- UNDERSTANDING THE PROBLEM -----------------

# Let's try writing some pseudo code:

# create container to store stock data
# for file in directory:
# 	open file
#	extract contents
#	add contents to container
#   next file
# write contents of container to a .csv file


# ----------------- ADDITIONAL INFO -----------------

# This will be covered in much more detail in the seminar, but here are some Python basics:
	# You seperate statements by putting them on different lines
	# Use a colon (:) to denote the start of an indented block of code
	# Use indentations to control flow (if statements, for loops, etc.)
	# Keep things as simple and elegenat as possible

# For anybody who is interested, you can find the official Python style guide at:
	# https://www.python.org/dev/peps/pep-0008/
	# This is long but good to eventually at least kinda go through if you want to know Python well

# There are MANY different ways to implement our pseudo code in Python
# And this one is probably not the best
# Alternative methods & expansions to this method will be reviewed in the seminar

# The 'best' method for doing anything depends on the specifics for each situation, including:
	# type and size of data
	# speed requirements
	# further appications (will other programs need to use this code?)
	# time alotted to complete project
	# your skill level

# It's OK to change your mind after you build something! 
# ...though you may not always get the time to do something again ;)
# So you always want to do things as nicely as is possible

# If you feel that you can make this program better, please go ahead! 
# You might want to save changes in a new file...


# ----------------- DATASTRUCTURES -----------------

# In this program, we make heavy use of:


# list
	# created with square brackets: your_list = [] (this creates an empty list, can add items later)
	# mutable (changeable) container
	# can hold objects of any type 
	# preserves order
	# finding items within it: your_list[4] gets 5th item in a list named 'your_list'
	# fast appends - O(1)


# tuple
	# created with parentheses: your_tuple = (items, seperated, by, commas)
	# an immutable (unchangeable) container
	# can hold objects of any type
	# preserves order
	# finding items within it: same as list
	# takes up less memory than a list
	

# DataFrame
	# accessed via import of the pandas package
	# created with: new_dataframe = pandas.DataFrame(your_data)
	# tabular data structure: provides nice access to columns, is great for analysis
	# the DataFrame object comes with a whole lot of functionality (methods), like:
		# set_index: define an index for the table, which allows for easy joins
		# join: combine multiple dataframes based on index
		# to_csv: write the DataFrame to a .csv file


# ----------------- WHAT WE WILL BE DOING -----------------

# A more detailed rundown than before of what we will be writing:

# Create a master list to hold all of our data
# Use a 'for' loop to iterate through .csv files in the folder 'daily'
	# Create a list to store data for this file / ticker
	# Extract ticker from filename & retain
	# In each file, we are going to iterate through each line (again with a for loop)
		# Retain the contents of each line (date & price) in a tuple
		# Then append said tuple to our list
		# Repeat this process for other lines
	# Create DataFrame out of list
	# Append this stock's DataFrame to our master list
	# Repeat this process for other files
# Create DataFrame out of our master list
# Format DataFrame columns
# Write to csv


# ----------------- PROGRAM CONTENTS -----------------

# This program contains 4 main functions:

# 1) get_ticker
		# extracts a ticker from a filename of format 'table_$ticker.csv'
		# to do this we use the split function
			# this is built into python; no importing required
			# given a string 'samplestring', you use it as such: samplestring.split(character)
			# this will return, as a list, the sample string split on the character you pass (in quotes) to it
			# note: to denote strings in Python, you can use single or double quotes

# 2) get_closing_prices
		# this is what will, for each file:
			# open the file (and read file using Python's csv package; function is csv.reader)
			# extract the stock data
			# return data as a DataFrame

# 3) get_all_closing_prices
		# this will go through the folder it is passed
		# and for each file call get_closing_prices
		# collect a list of DataFrames (where each DataFrame contains one stock's data)
		# join all the DataFrames into one master DataFrame
		# and return the master DataFrame

# 4) main
		# this is a function that gets called if the file is run via command line execution (i.e. as a script)
		# it will call get_all_closing_prices, passing the directory: 'quantquote_daily_sp500_83986/daily/'
		# and then write data to csv: 'sp500_1998_2013_closingprices.csv'


# Note: the triple-quote statements right below the function definition are called docstrings
	# these lines are descriptions of what each function will do
	# these are kind of like comments, except if you enter help(function) from the interpreter, docstring gets returned


# ----------------- PROGRAM STRUCTURE -----------------

# personally, I like to kinda follow what's called a 'functional programming' style
# I say 'kinda' because Python is not a true functional language and therefore I don't try to force it to be
# but I do like to use certain functional features anyway

# for example, using subroutines
# these are functions within functions, which you will see below
# there are two main reasons for this: logical structure & garbage collection

# 1) logical structure
	# this, to me, means two things:
	# it is easy for you to keep track of your ideas
		# as in, what are you trying to do, and how are you trying to do it
	# and it also makes it easy for somebody else to understand your code
	# this helps with debugging, additions, and also just general clarity of mind
	# which can help you code faster & also code smarter 

# 2) garbage collection
	# when you create a new object (like a list or DataFrame), it takes up space
	# especially once it's been filled with lots of information
	# when you have lots of these objects lying around, they can take up memory, and slow you down
	# variables and objects that are created within a function generally stay within the confines of that function
	# which means they are generally discarded as soon as that function has reached the end of its process
	# which leaves you with less clutter

# --
# additionally, the if __name__ == '__main__' condition at the end:
	# this line allows for the main function to be executed from the command line with a simple command
	# see below


# ----------------- TO RUN -----------------

# this is a .py file (also called a module), which can be used in two ways


# **** PREREQUISITE: set up your data

# this function must be run from the folder in which 
	# the 'quantquote_daily_sp500_83986' folder lives
		# in which the 'daily' folder lives
			# in which the stock data .csv files live

# in other words, your setup should look something like:

#		/Users/your_name/fordham/python_seminar/quantquote_daily_sp500_83986/daily/lots of table_$ticker.csv files

# where this program is in 'python_seminar'
# feel free to change this setup around if you feel comfortable


# --
# **** METHOD 1: command line script

# this is the EASIEST way to do it
# navigate via command line to correct directory
# type: python python_demo.py 
# press: enter


# --
# **** METHOD 2: import module and call functions

# via interpreter:

	# if you start the Python interpreter (typing Python and pressing enter at the command line)
	# while you are in the directory in which this file is stored
	# you can enter 'import python_demo' and then use these functions
		# for example: ticker = python_demo.get_ticker('table_ticker.csv')
		# or, you can give the module an alias: import python_demo as demo
		# ticker = demo.get_ticker('table_ticker.csv')

# via other modules:
	
	# you can write other modules (.py files) that say 'import python_demo' at the top
	# and use these functions in them, just like you would at the command line

# if you install this module (mildly complicated but not horribly so)
# then it makes it really easy to use these functions from anywhere 
# we will cover this later

# so you'd get the master DataFrame by calling get_all_closing_prices
# and then writing that DataFrame to csv
# as is done in main


# ----------------- OUR CODE -----------------

import os
import csv
import pandas as pd



def get_ticker(file):
	"""returns stock ticker as string"""
	return file.split('_')[1].split('.')[0]


def get_closing_prices(file):
	"""returns DataFrame; columns 'date' & 'ticker'; ticker contains closing prices"""
	
	def get_data(file):
		"""returns a list of (date, closing_price) tuples"""
		data = []
		with open('quantquote_daily_sp500_83986/daily/' + file) as f:
			csvreader = csv.reader(f)
			for row in csvreader:
				data.append((row[0], row[5]))
		return data

	def format_data(data, ticker):
		"""returns DataFrame with correct columns"""
		df = pd.DataFrame(data, columns=['date', ticker])
		return df.set_index('date', drop=True)

	return format_data(get_data(file), get_ticker(file))


def get_all_closing_prices(folder):
	"""return list of get_closing_prices lists"""
	
	def get_list_of_prices(folder):
		"""get list of DataFrames"""
		all_stocks = []
		for file in os.listdir(folder):
			all_stocks.append(get_closing_prices(file))
		return all_stocks

	def get_dataframe(data):
		"""inner join list of dataFrames on date"""
		return data[0].join(data[1:], how='outer')

	return get_dataframe(get_list_of_prices(folder))


def main():
	"""function that is called when file is run from command line"""
	data = get_all_closing_prices('quantquote_daily_sp500_83986/daily/')
	data.to_csv('sp500_1998_2013_closingprices.csv')


if __name__ == '__main__':
	main()
