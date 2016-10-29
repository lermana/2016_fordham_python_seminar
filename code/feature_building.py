import stock_data

import pandas



def get_feature_table():
    """one giant function: our feature_building work exported from Jupyter"""
    data = stock_data.get_all_closing_prices("../stock_csvs/")

    closing_prices =  data.ix[:, data.columns.get_level_values(1).isin({"close"})]
    closing_returns =  (closing_prices.shift(-1) - closing_prices) / closing_prices

    opening_prices =  data.ix[:, data.columns.get_level_values(1).isin({"open"})]
    opening_returns =  (opening_prices.shift(-1) - opening_prices) / opening_prices

    dataframes = []
    for column_pair in closing_returns.columns:
        tic = column_pair[0]
        dataframes.append(
            pandas.concat({tic: 
                pandas.concat({'intra':
                              (data[tic].close - data[tic].open)
                                  / data[tic].open
                              }, axis=1)}, axis=1))

    intra_rets = dataframes[0].join(dataframes[1:])


    high =  data.ix[:, data.columns.get_level_values(1).isin({"high"})]
    high_returns =  (high.shift(-1) - high) / high

    low =  data.ix[:, data.columns.get_level_values(1).isin({"loww"})]
    low_returns =  (low.shift(-1) - low) / low

    volume =  data.ix[:, data.columns.get_level_values(1).isin({"volume"})]
    volume_returns =  (volume.shift(-1) - volume) / volume


    corrs = stock_data.get_max_corrs(closing_returns)

    dataframes = []
    for column_pair in closing_returns.columns:
        tic = column_pair[0]
        top_corr = corrs.ix[tic, 'most correlated other stock']
        dataframes.append(
            pandas.concat({tic: 
                pandas.concat({top_corr: 
                              closing_prices[top_corr].close}, axis=1)}, axis=1))


    all_corrs = dataframes[0].join(dataframes[1:])


    dataframes = []
    for column_pair in closing_returns.columns:
        tic = column_pair[0]
        
        dataframes.append(pandas.concat({
                              tic: opening_returns[tic].join(
                                  closing_returns[tic]).join(
                                      high_returns[tic]).join(
                                          low_returns[tic]).join(
                                              intra_rets[tic]).join(
                                                  volume_returns[tic]).join(
                                                        all_corrs[tic])
                    }, axis=1))


    feature_table = dataframes[0].join(dataframes[1:])
    return feature_table



