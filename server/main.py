import pymysql

# MySQL Connection 연결 하는 법
conn = pymysql.connect(host='localhost', user='*****', password='****', db='test', charset='utf8', )

curs = conn.cursor(pymysql.cursors.DictCursor)

# ==== select example ====
sql = "select * from users"
curs.execute(sql)

# 데이타 Fetch
rows = curs.fetchall()
print(rows)

conn.close()