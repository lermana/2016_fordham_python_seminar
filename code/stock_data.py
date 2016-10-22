import os
import csv
import datetime
import pandas as pd



def get_ticker(file):
	"""returns stock ticker as string"""
	return file.split('_')[1].split('.')[0]


def get_closing_prices(file):
	"""returns DataFrame; columns 'date' & 'ticker'; ticker contains closing prices"""
	ticker = get_ticker(file)
	df = pd.read_csv('../stock_csvs/' + file, 
						names=['date', 'time', 'open', 'high', 'low', 'close', 'volume'])
	
	dates = df['date'].apply(lambda date: datetime.datetime.strptime(str(date), '%Y%m%d'))
	df['date'] = dates

	return pd.concat({ticker: df.set_index('date', drop=True)}, axis=1)


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
	data = get_all_closing_prices('../stock_csvs/')
	data.to_csv('../output/all_stock_data.csv')


if __name__ == '__main__':
	main()

















