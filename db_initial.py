# !!! in progress !!! check if database tables exists, if not, then create (PostgreSQL)

import cfg
import event_report
# -----------------------------
import psycopg  # psycopg3.1.8

print(psycopg.__version__)

print(cfg.db_config)

#conn = psycopg.connect(**cfg.db_config)

# cur = conn.cursor()

# sql = 'DROP TABLE IF EXISTS draws;'

# cur.execute(sql)

# sql = '''CREATE TABLE IF NOT EXISTS draws(
#             draws_id    INT         GENERATED ALWAYS AS IDENTITY,
#             draw_date   DATE        NOT NULL,
#             leap_year   BOOLEAN     NOT NULL,
#             draw_date_sum INT       NOT NULL,
#             birth_number INT        NOT NULL,
#             master_number INT       NOT NULL,
#             balls_csv   CHAR(17)    NOT NULL,
#             ball_1      INT         NOT NULL,
#             ball_2      INT         NOT NULL,
#             ball_3      INT         NOT NULL,
#             ball_4      INT         NOT NULL,
#             ball_5      INT         NOT NULL,
#             ball_6      INT         NOT NULL,
#             draw_sum    INT         NOT NULL,
#             draw_avg    INT         NOT NULL,
#             draw_median INT         NOT NULL,
#             draw_odd    INT         NOT NULL,
#             draw_even   INT         NOT NULL,
#             draw_one_digit    INT   NOT NULL,
#             draw_two_digit    INT   NOT NULL,
#             prime_numbers_qty INT   NOT NULL,
#          PRIMARY KEY(draws_id));'''
