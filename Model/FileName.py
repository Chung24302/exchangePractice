import time
import pandas as pd
import json
import os
def getTime():
    
    fileName_DATE = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime() )
    fileName_TIME = fileName_DATE[11:]
    fileName_DATE = fileName_DATE[:10]


    try:
        if not os.path.isfile('./Model/DB/exchange_Date_and_Time.json')   :
            print('create file')
            '''
            Json from Example:
                { 
                "DateAndTime":[ 

                    {"Order" : 1,
                    "Date" : "2022-01-01",
                    "Time" : "12:34:56" },

                    {"order" : 2,
                    "Date" : "2022-01-02",
                    "Time" : "13:24:56" }
                    ] 
               }

            '''
            #os.system('touch ./Model/DB/exchange_Date_and_Time.json')
            Default_dict = [{"Order" : 1, "Date" : fileName_DATE, "Time" : fileName_TIME }]
            with open('./Model/DB/exchange_Date_and_Time.json', mode='w') as fw:
                json.dump(Default_dict, fw )
            exit()

    except  FileExistsError:
        #pass
        print('except ERROR')
        
    with open('./Model/DB/exchange_Date_and_Time.json', 'r+') as fr:
        data = json.load(fr)
        newDate = {"Order" : len(data)+1, "Date" : fileName_DATE, "Time" : fileName_TIME }
        data.append(newDate)
        print(len(data))
        fr.seek(0)
        json.dump(data, fr)
        fr.close()

    with open('./Model/DB/exchange_Date_and_Time.json', 'r') as fr:
        data = json.load(fr)
        fr.close()

    if data[-2]['Date'] == fileName_DATE:
        print('same')
        same_day_counter = 0

        while data[same_day_counter-1]['Date'] == fileName_DATE:   
            print(data[same_day_counter-1]['Date'])
            same_day_counter -= 1
        print(same_day_counter)

    return fileName_DATE, fileName_TIME, same_day_counter+1