# SEARCH RECORDS EXAMPLE

# INSTALL PYMYSQL FROM INTERNET

# STEP 1 - IMPORT PYMYSQL
import pymysql.cursors


# STEP 2 - Connect to MYSQL database
def getStudent(student_id):
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
        query = "select * from student where id = %s"

        try:
            # STEP - 5 TAKE INPUT FROM USER
            id = student_id

        except Exception as e:
            print('INPUT ERROR ', e)
        else:
            try:
                # STEP 6 - CREATE cursor Object
                cursor = conn.cursor()

                # STEP 7 - EXECUTE THE Query
                cursor.execute(query, id)

            except Exception as e:
                print('RECORD FETCHING PROBLEM ', e)
            else:
                if cursor.rowcount > 0:
                    # STEP 8 - DISPLAY RECORDS
                    # Fetch Each Record In Dictionary Format
                    
                    for record in cursor:
                        return record
                else:
                    return 'INVALID ID'
            finally:
                # STEP 9 - CLOSE CONNECTION
                conn.close()
