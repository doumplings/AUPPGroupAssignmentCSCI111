import pymysql.cursors

def getTeacher(teacher_id):
    conn = None
    try:

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
        query = "select * from teachers where id = %s"

        try:
            # STEP - 5 TAKE INPUT FROM USER
            id = teacher_id

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
                    print('INVALID TEACHER ID')
            finally:
                # STEP 9 - CLOSE CONNECTION
                conn.close()