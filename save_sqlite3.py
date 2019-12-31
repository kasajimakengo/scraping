import sqlite3

conn = sqlite3.connect('top_cities.db')

c = conn.cursor()

# c.execute("""
#     CREATE TABLE cities(
#         rank integer,
#         city text,
#         population integer
#     )
# """ )

c.execute('INSERT INTO cities VALUES (?, ?, ?)', (1, '上海', 24150000))

c.execute('INSERT INTO cities VALUES (:rank, :city, :population)', {'rank': 2, 'city': 'カラチ', 'population': 23500000})
c.executemany('INSERT INTO cities VALUES (:rank, :city, :population)', [
    {'rank': 3, 'city': '北京', 'population': 21516000},
    {'rank': 4, 'city': '天津', 'population': 14722100},
    {'rank': 5, 'city': 'インスタンブル', 'population': 14160467},
])

conn.commit()

c.execute('SELECT * FROM cities')
for row in c.fetchall():
    print(row)

conn.close()