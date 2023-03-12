# !!! in progress !!! check if database tables exists, if not, then create (PostgreSQL)

import cfg
import event_report
# -----------------------------
import psycopg  # psycopg3.1.8

conn = psycopg.connect(**cfg.db_config)

cur = conn.cursor()
cur.execute('SELECT EXISTS(SELECT table_name FROM information_schema.tables WHERE table_name=%s)', ('lotto',))
table_exists = cur.fetchone()

print(table_exists)

cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS lotto;')
conn.commit()

cur = conn.cursor()
cur.execute('SELECT EXISTS(SELECT table_name FROM information_schema.tables WHERE table_name=%s)', ('lotto',))
table_exists = cur.fetchone()

print(table_exists)

cur.execute('''CREATE TABLE IF NOT EXISTS lotto(
            draw_id    INT    NOT NULL,
            draw_date   DATE        NOT NULL,
            draw_time   BOOLEAN     NOT NULL,
            ball_1      INT         NOT NULL,
            ball_2      INT         NOT NULL,
            ball_3      INT         NOT NULL,
            ball_4      INT         NOT NULL,
            ball_5      INT         NOT NULL,
            ball_6      INT         NOT NULL,
            special_results integer ARRAY    NOT NULL,
            balls_list   integer ARRAY[4]    NOT NULL,
            draw_sum    INT         NOT NULL,
            draw_avg    INT         NOT NULL,
            draw_median INT         NOT NULL,
            draw_odd    INT         NOT NULL,
            draw_even   INT         NOT NULL,
            draw_one_digit    INT   NOT NULL,
            draw_two_digit    INT   NOT NULL,
            prime_numbers_qty INT   NOT NULL,
            leap_year   BOOLEAN     NOT NULL,
            draw_date_sum INT       NOT NULL,
            birth_number INT        NOT NULL,
            master_number INT       NOT NULL,
         PRIMARY KEY(draw_id));''')
conn.commit()

conn.close()
