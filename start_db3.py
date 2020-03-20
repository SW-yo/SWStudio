import sqlite3

conn = sqlite3.connect('my_database.db')

data = []
cur = conn.execute('select avg(random_val) from data_table group by id % 100')
for row in cur:
    data.append((int(row[0] * 10)))


import collections

hist_data = collections.Counter(data)

import kame

hist_kame = kame.Kame()

hist_kame.home()
hist_kame.clear()
hist_kame.histogram(hist_data, 10)