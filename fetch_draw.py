import cfg
import event_report
# --------------------
import requests
import json
import os
import pandas as pd
import csv
from datetime import datetime


# store and update raw data in csv and json format

def file_exist():
    pass


def file_update():
    pass


# update database -> from module database
# for database parse only json file

def db_update():
    pass


# if file exist, check last draw system id, if mach then update, if not exist create

def get():
    try:

        with open(cfg.config['DRAW_CONFIG'], 'r', encoding=cfg.config['ENCODING']) as j_file:
            j_draw_config = json.load(j_file)
            j_draw_config['query_strings']['game'] = 'Lotto'  # !!! temporary default Lotto
            print(j_draw_config['query_strings'])
            # print(json.dumps(j_draw_config, indent=2))

        with open(cfg.config['REQUESTS_JSON'], 'r', encoding=cfg.config['ENCODING']) as j_file:
            j_requests = json.load(j_file)
            # print(json.dumps(j_requests, indent=2))

        response = requests.get(j_draw_config['base_url'], headers=j_requests['headers'],
                                params=j_draw_config['query_strings'])

        print(response.status_code)  # !!! catch in event log

        print(response.json())

        print(json.dumps(response.json(), indent=2))

        # !!! dump response to file, for parse testing

        with open('draw_test.json', 'w+', encoding="utf-8") as j_file:
            json.dump(response.json(), j_file, indent=4)
            j_file.truncate()  # remove remaining part

        event_report.event_log(event='[UPDATE]', message='Fetch draw')
    except Exception:
        event_report.event_log(event='[ERROR]')


# get()


with open('draw_test.json', 'r', encoding=cfg.config['ENCODING']) as j_file:
    j_draw_config = json.load(j_file)

    # print(j_draw_config['items'])

print(json.dumps(j_draw_config['items'], indent=4))
print()

print(len(j_draw_config['items']))

draws = list()
lotto = dict()

draws_csv = list()

for i in range(len(j_draw_config['items'])):
    print('Lotto: ', j_draw_config['items'][i]['results'][0])

    date_time_object = datetime.strptime(j_draw_config['items'][i]['results'][0]['drawDate'],
                                         cfg.config['date_time_format'])
    draw_date = date_time_object.strftime(cfg.config['date_store_format'])
    draw_time = date_time_object.strftime(cfg.config['time_store_format'])

    # Lotto.update({'drawSystemId': j_draw_config['items'][i]['results'][0]['drawSystemId']})

    draws.append({'drawSystemId': j_draw_config['items'][i]['results'][0]['drawSystemId'],
                  'drawDate': j_draw_config['items'][i]['results'][0]['drawDate'],
                  'resultsJson': j_draw_config['items'][i]['results'][0]['resultsJson']
                  })

    draws_csv.append([j_draw_config['items'][i]['results'][0]['drawSystemId'],
                      draw_date, draw_time, *j_draw_config['items'][i]['results'][0]['resultsJson']])

lotto['Lotto'] = draws
# print('LottoPlus: ', j_draw_config['items'][i]['results'][1])


print(json.dumps(lotto, indent=4))

print(lotto)

print(draws_csv)

j_lotto = json.dumps(lotto, indent=4)

with open("lotto.json", "w") as f:
    f.write(j_lotto)

with open('lotto.csv', 'w') as f:
    write = csv.writer(f)
    write.writerows(draws_csv)


df = pd.DataFrame(draws_csv)

print('DataFrame:\n', df)


with open('lotto_pd.csv', 'w') as f:
    df.to_csv(f)
