# SEARCH RECORDS EXAMPLE

# INSTALL PYMYSQL FROM INTERNET

# STEP 1 - IMPORT PYMYSQL
import pymysql.cursors


# STEP 2 - Connect to MYSQL database
def addStudent(id, first_name, last_name, email, phonenum, dob):
    conn = None
    try:
        # STEP 2 - CONNECT WITH MYSQL DATABASE
        # cursorclass = pymysql.cursors.DictCursor
        # RECORD WILL FETCH IN DICTIONARY FORMAT
        # IF WE NOT MENTION IT - IT WILL TAKE TUPLE
        conn = pymysql.connect(host='127.0.0.1',
                user='root', password='abc123', db='csdb',
                charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    except Exception as ex:
        print('PROBLEM WITH Database Connection', ex)
    else:
        print('Database Connection SUCCESS')

    # STEP 3 - CHECK Connection is Establish or not
    if conn is not None:
        # STEP 4 Create Query
        query = "INSERT INTO student(id, first_name, last_name, email, phonenum, dob) VALUES(%s,%s,%s,%s,%s,%s)"

        try:
            # STEP - 5 TAKE INPUT FROM USER
            student = [id, first_name, last_name, email, phonenum, dob]

        except Exception as e:
            print('INPUT ERROR ', e)
        else:
            try:
                # STEP 6 - CREATE cursor Object
                cursor = conn.cursor()

                # STEP 7 - EXECUTE THE Query
                noofrecoredinsert = cursor.execute(query, student)

            except Exception as e:
                print('RECORD FETCHING PROBLEM ', e)
            else:
                if noofrecoredinsert > 0:
                    conn.commit()
                    return 'RECORD INSERTED'
                    
                else:
                    return 'RECORD NOT INSERTED'
            finally:
                # STEP 9 - CLOSE CONNECTION
                conn.close()

