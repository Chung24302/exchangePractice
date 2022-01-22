import os
def DownloadAndRename(fileName_DATE, filesCounter ):
    exchange_rate_csv = 'https://rate.bot.com.tw/xrt/flcsv/0/day'
    dir_PATH = './Model/DB/exchange_rate_folder/'
    try:
        if not os.path.isdir(dir_PATH):
            os.mkdir('mkdir -p ./Model/DB/exchange_rate_folder/{EXTREACTED{DATA_ALL, DATA_BUY, DATA_SELL},ORIGINAL}')
    except  FileExistsError:
        print('Folder exist')
    dir_PATH = dir_PATH+'ORIGINAL/'
    cmd = 'wget '+ exchange_rate_csv + ' -O ' + dir_PATH + fileName_DATE +'.csv'

    if filesCounter < 0:
        fileName_DATE = fileName_DATE + '_' + str(abs(filesCounter))
        cmd = 'wget '+ exchange_rate_csv + ' -O ' + dir_PATH + fileName_DATE +'.csv'

    os.system(cmd)
    return fileName_DATE
