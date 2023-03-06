import cfg
import event_report
# --------------------
import os
import requests
import json
import pandas as pd
from datetime import datetime


# file names for game data: lotto_orig.json, lotto.json, lotto_plus.json, lotto.cvs, lotto_plus.cvs
# function save_json_cvs() only for Lotto (lotto_orig.json include Lotto and LottoPlus, exclude some fields,
# e.g specialResults

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

def get(game=cfg.config['default_game']):

    main_json = os.path.isfile('lotto_orig.json')

    try:

        with open(cfg.config['DRAW_CONFIG'], 'r', encoding=cfg.config['ENCODING']) as j_file:
            request_data = json.load(j_file)

            request_data['query_strings']['game'] = game

            # print(request_data['query_strings'])

        with open(cfg.config['REQUESTS_JSON'], 'r', encoding=cfg.config['ENCODING']) as j_file:
            j_requests = json.load(j_file)

        response = requests.get(request_data['base_url'], headers=j_requests['headers'],
                                params=request_data['query_strings'])

        # Check response.status_code, if not 200, raise Exception

        if response.status_code != 200:
            message = 'Game "' + game + '" - Cannot fetch json data, status code: ' + str(response.status_code)
            raise event_report.CustomError(message)

        last_game_id = response.json()
        last_game_id = last_game_id['items'][0]['drawSystemId']

        print(last_game_id)

        print(response.json())

        # !!! dump response to file, for parse testing

        if main_json == True:

            request_data['query_strings']['size'] = last_game_id

            print(request_data['query_strings'])

            response = requests.get(request_data['base_url'], headers=j_requests['headers'],
                                    params=request_data['query_strings'])

            # Check response.status_code, if not 200, raise Exception

            if response.status_code != 200:
                message = 'Game "' + game + '" - Cannot fetch json data, status code: ' + str(response.status_code)
                raise event_report.CustomError(message)

            with open('lotto_orig.json', 'w', encoding="utf-8") as j_file:
                json.dump(response.json(), j_file, indent=4)
                j_file.truncate()  # remove remaining part

        event_report.event_log(event='[UPDATE]', message='Fetch draw')
    except event_report.CustomError as ce:
        event_report.event_log(event='[ERROR]', subject=str(ce)[1:-1])
    except Exception as e:
        event_report.event_log(event='[ERROR]', subject=str(e))


get()


def save_json_cvs():
    pass
#
#
# with open('draw_test.json', 'r', encoding=cfg.config['ENCODING']) as j_file:
#     j_draw_config = json.load(j_file)
#
#     # print(j_draw_config['items'])

# print(json.dumps(j_draw_config['items'], indent=4))

# print(len(j_draw_config['items']))

# draw_lotto_list = list()
# draw_lotto_dict = dict()
#
# draw_lotto_plus_list = list()
# draw_lotto_plus_dict = dict()
#
# draw_lotto_csv = list()
# draw_lotto_plus_csv = list()
#
# for i in range(len(j_draw_config['items'])):
#     date_time_object = datetime.strptime(j_draw_config['items'][i]['results'][0]['drawDate'],
#                                          cfg.config['date_time_format'])
#     draw_date = date_time_object.strftime(cfg.config['date_store_format'])
#     draw_time = date_time_object.strftime(cfg.config['time_store_format'])
#
#     draw_lotto_list.append({'drawSystemId': j_draw_config['items'][i]['results'][0]['drawSystemId'],
#                             'drawDate': j_draw_config['items'][i]['results'][0]['drawDate'],
#                             'resultsJson': j_draw_config['items'][i]['results'][0]['resultsJson']
#                             })
#
#     draw_lotto_csv.append([j_draw_config['items'][i]['results'][0]['drawSystemId'],
#                            draw_date, draw_time, *j_draw_config['items'][i]['results'][0]['resultsJson']])
#
#
#     date_time_object = datetime.strptime(j_draw_config['items'][i]['results'][1]['drawDate'],
#                                          cfg.config['date_time_format'])
#     draw_date = date_time_object.strftime(cfg.config['date_store_format'])
#     draw_time = date_time_object.strftime(cfg.config['time_store_format'])
#
#     draw_lotto_plus_list.append({'drawSystemId': j_draw_config['items'][i]['results'][1]['drawSystemId'],
#                             'drawDate': j_draw_config['items'][i]['results'][1]['drawDate'],
#                             'resultsJson': j_draw_config['items'][i]['results'][1]['resultsJson']
#                             })
#
#     draw_lotto_plus_csv.append([j_draw_config['items'][i]['results'][1]['drawSystemId'],
#                            draw_date, draw_time, *j_draw_config['items'][i]['results'][1]['resultsJson']])
#
#
#
# draw_lotto_dict['Lotto'] = draw_lotto_list
#
# draw_lotto_plus_dict['LottoPlus'] = draw_lotto_plus_list

# print(draw_lotto_dict)
#
# j_lotto = json.dumps(draw_lotto_dict, indent=4)
#
# with open("lotto.json", "w") as f:
#     f.write(j_lotto)
#
# columns = ['Draw Id', 'Date', 'Time', '1', '2', '3', '4', '5', '6']
# df = pd.DataFrame(data=draws_csv, columns=columns)
#
# print(df)
#
# with open('lotto_pd.csv', 'w') as f:
#     df.to_csv(f, header=columns)
