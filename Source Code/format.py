# Raul Luna, Jr
# Team #13
# CS 440 - Code Project
# September 26, 2014
# Create multiple .csv files for the business data input. All these figures will be created by the group with having reasonable
# figures according to the time of year in 2013. The business data set will consist of the follow data set:
# Ice Cream Sales
# Residental Sales in Chicago
# Coffee / Hot Chocolate
# Propane / Propane Accessories
# Soup

# libs
import calendar
import random

# Create the .csv of ice cream sales for the selected year
# @param year
# @param month_list
# @param sales_list
# @param d_file
def create_data( year, month_list, sales_list, d_file):
	# Find the number of days in each month for the year 2013 and output to a text file as Month, # of days
	# Ex. January, 31
	for i in range( len( month_list)):
		# Determine the number of days in each month
		x = calendar.monthrange( year, i+1)		# second parameter corresponds to the month number which will start at 1, not 0
		num_weekday, num_day = x				# separate the tuple so we can save the number of days in the month only
		#day_list.append( num_day)				# insert the number of days in the month into a list
		for j in range( num_day):
			# Populate sales for each day in current month and write into the output file
			#d_file.write( month_list[i] + "," + str( j+1) + "," + str( year) + "\t" + str( hot_dogs_sales( i+1, num_day)) + "\n")
			# Need format to be day-month-year
			d_file.write( str( j+1) + "-" + month_list[i] + "-" + str( year) + "\t" + str( hot_dogs_sales( i+1, num_day)) + "\n")


	# Generated the number of ice cream sales for now. Maybe later, we can input the actual figures from an API
	#ice_cream_sales( months, days, ice_cream_sales_list)

# Generated the number of ice cream sales in the Chicago area (statically allocated currently). Maybe later, we can input the actual figures from an API
# @param month_list		the list of months ( January - December)
# @param day_list		the list of the number of days (1 - 28/31)
# @param sale_list		reference list of ice cream sales that corresponds to a month
def ice_cream_sales( month, days):
	# Months corresponding outside of summer
	if( month <= 5 and month >= 9):
		# Random number between both parameters
		return random.randint( 500, 50000)
	# Months corresponding during the summer
	else:
		return random.randint( 2000, 100000)

# Generated the number of residental sales in the Chicago area (statically allocated currently). Maybe later, we can input the actual figures from an API
# @param month_list		the list of months ( January - December)
# @param day_list		the list of the number of days (1 - 28/31)
# @param sale_list		reference list of residental sales that corresponds to a month
def residental_sales( month, days):
	# Months corresponding from January and February
	if( month < 3 ):
		# Random number between both parameters
		return random.randint( 50, 150)
	# Months corresponding from March thru June
	elif( month >= 3 and month < 7):
		# Random number between both parameters
		return random.randint( 300, 500)
	# Months corresponding from July thru October
	elif( month >= 7 and month < 11):
		# Random number between both parameters
		return random.randint( 200, 300)
	# Months corresponding from November and December
	else:
		# Random number between both parameters
		return random.randint( 100, 200)

# Generated the number of hot drinks sales in the Chicago area (statically allocated currently). Maybe later, we can input the actual figures from an API
# @param month_list		the list of months ( January - December)
# @param day_list		the list of the number of days (1 - 28/31)
# @param sale_list		reference list of hot drinks sales that corresponds to a month
def hot_drinks_sales( month, days):
	# Months corresponding from January and February
	if( month < 3):
		# Random number between both parameters
		return random.randint( 60000, 70000)
	# Months corresponding from March thru June
	elif( month >= 3 and month < 7):
		# Random number between both parameters
		return random.randint( 40000, 50000)
	# Months corresponding from July thru October
	elif( month >= 7 and month < 11):
		# Random number between both parameters
		return random.randint( 60000, 70000)
	# Months corresponding from November and December
	else:
		# Random number between both parameters
		return random.randint( 90000, 100000)

# Generated the number of hot dogs sales in the Chicago area (statically allocated currently). Maybe later, we can input the actual figures from an API
# @param month_list		the list of months ( January - December)
# @param day_list		the list of the number of days (1 - 28/31)
# @param sale_list		reference list of hot dogs sales that corresponds to a month
def hot_dogs_sales( month, days):
	# Months corresponding from January and February
	if( month < 3):
		# Random number between both parameters
		return random.randint( 85000, 90000)
	# Months corresponding from March thru June
	elif( month >= 3 and month < 7):
		# Random number between both parameters
		return random.randint( 90000, 100000)
	# Months corresponding from July thru October
	elif( month >= 7 and month < 11):
		# Random number between both parameters
		return random.randint( 90000, 100000)
	# Months corresponding from November and December
	else:
		# Random number between both parameters
		return random.randint( 85000, 90000)
# main
def main():

	# List of months
	months = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    # List of number of days in a month for the selected year (dynamic)
	days = []

	# List of the number of ice cream sales for the selected year
	ice_cream_sales_list = []

	# List of the number of residental sales for the selected year
	residental_sales_list = []

	# List of the number of coffee / hot chocolate sales for the selected year
	hot_drinks_sale_list = []

	# List of the number of hot dog sales for the selected year
	hot_dogs_sale_list = []

	# Create .csv file to export
	#ice_cream_data = open('ice_cream_sales_data.csv', 'w')

	# Create .csv file to export
	#residental_data = open('residental_data.csv', 'w')

	# Create .csv file to export
	#hot_drinks_data = open('hot_drinks_data.csv', 'w')

	# Create .csv file to export
	hot_dogs_data = open('hot_dogs_data.tsv', 'w')

	# Create .csv files for all data sets
	#create_data( 2013, months, ice_cream_sales_list, ice_cream_data)
	#create_data( 2013, months, residental_sales_list, residental_data)
	#create_data( 2013, months, hot_drinks_sale_list, hot_drinks_data)
	create_data( 2013, months, hot_drinks_sale_list, hot_dogs_data)

main()