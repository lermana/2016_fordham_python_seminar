import os
import csv
import datetime
import pandas
import itertools



def get_ticker(file):
    """returns stock ticker as string"""
    return file.split('_')[1].split('.')[0]


def get_closing_prices(file):
    """returns DataFrame; columns 'date' & 'ticker'; ticker contains closing prices"""
    ticker = get_ticker(file)
    df = pandas.read_csv('../stock_csvs/' + file, 
                         names=['date', 'time', 'open', 'high', 'loww', 'close', 'volume'])
    
    df['date'] = df['date'].apply(lambda date: datetime.datetime.strptime(str(date), '%Y%m%d'))

    return pandas.concat({ticker: df.set_index('date', drop=True)}, axis=1)


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


def get_max_corrs(returns):
    """fuck you"""
    
    corr_mat = returns.corr()
    max_corrs = []
    
    for col in corr_mat.columns:
        maximum = corr_mat[col[0]].sort_values(by='close', 
                                                ascending=False).ix[1]
        max_corrs.append((col[0],
                          maximum.name[0],
                          maximum.values[0]))

    max_corrs_df = pandas.DataFrame(max_corrs, 
                                    columns=['stock', 
                                            'most correlated other stock', 
                                            'correlation']).set_index('stock',
                                                                      drop=True)
    return max_corrs_df


def main():
    """function that is called when file is run from command line"""
    data = get_all_closing_prices('../stock_csvs/')
    data.to_csv('../output/all_stock_data.csv')


if __name__ == '__main__':
    main()

















