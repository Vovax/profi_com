import psycopg2

db_con = psycopg2.connect(database='profireader_tests', user='pfuser', password='bAnach~tArski', host='db.profi')
print("Opened database successfully")
cur = db_con.cursor()

profi_db_con = psycopg2.connect(database='profireader', user='pfuser', password='bAnach~tArski', host='db.profi')
print("Opened 'Profireader' database successfully")
pro_cur = profi_db_con.cursor()
