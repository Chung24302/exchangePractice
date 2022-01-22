import pandas as pd
def extraction(fileName):
    ORI_Path = './Model/DB/exchange_rate_folder/ORIGINAL/'
    csvfileName = ORI_Path+fileName
    ORI_data = pd.read_csv(csvfileName+'.csv', index_col=False)
    data = ORI_data[['幣別', '現金', '即期', '現金.1','即期.1']]
    data.columns = ['幣別', '現金_本行賣出','即期_本行賣出', '現金_本行買入','即期_本行買入']
    data_Sell = data[['幣別', '現金_本行賣出','即期_本行賣出']]
    data_Buy = data[['幣別','現金_本行買入','即期_本行買入']]

    output_file_Path = './Model/DB/exchange_rate_folder/EXTREACTED/'
    fileName = fileName+'.json'
    data.to_json(output_file_Path + 'DATA_ALL/' + fileName, orient='table', index=False)
    data_Sell.to_json(output_file_Path + 'DATA_SELL/' + fileName, orient='table', index=False)
    data_Buy.to_json(output_file_Path + 'DATA_BUY/' + fileName, orient='table', index=False)