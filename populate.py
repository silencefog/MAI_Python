import cx_Oracle
import csv
import io

# drops symbols from a number and turns a tring to an int
def clearNumber(phone):
    rem = " +()-"
    for char in rem:
        phone = phone.replace(char, "")
    numPh = int(phone)
    return numPh

path_to_oracle_lib = "your path
cx_Oracle.init_oracle_client(lib_dir=path_to_oracle_lib)

conn = cx_Oracle.connect(your_user, your_password, 'db202009151316_high')

cursor = conn.cursor()

cursor.execute("CREATE TABLE PHONES(name VARCHAR2(100),phnumber VARCHAR2(40),phnumber_int NUMBER)")

path = "your path to csv"
with io.open(path, encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    first = True
    for r in reader:
        if first:
            first = False
            continue
        res = clearNumber(r[4])
        cursor.execute("INSERT INTO PHONES(name, phnumber, phnumber_int) VALUES(:name, :phnumber, :phnumber_int)", [r[3], r[4], res])
        conn.commit()

cursor.execute("SELECT * FROM PHONES")
result = cursor.fetchall()
print(result)

conn.close()
