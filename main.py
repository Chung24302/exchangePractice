from Model import FileName
from Model import extract
from Controller import downloadCSV
import json 
#os.system('rm ./Model/DB/exchange_Date_and_Time.json')
date, time, counter = FileName.getTime()
fileName = downloadCSV.DownloadAndRename(date, counter)
extract.extraction(fileName)