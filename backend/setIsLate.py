# UPDATE STUDENT RECORD

# INSTALL PYMYSQL FROM INTERNET

# STEP 1 - IMPORT PYMYSQL
import pymysql.cursors

def isLate(st_id):
# STEP 2 - Connect to MYSQL database
    conn = None
    try:
        # STEP 2 - CONNECT WITH MYSQL DATABASE
        # conn = pymysql.connect(host='127.0.0.1',
        #         user='root', password='abc123', db='pythondb',
        #         charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

        conn = pymysql.connect(host='127.0.0.1',
                            user='root', password='abc123', db='csdb')
    except Exception as ex:
        print('PROBLEM WITH Database Connection', ex)
    else:
        print('Database Connection SUCCESS')

    # STEP 3 - CHECK Connection is Establish or not
    if conn is not None:
        # STEP 4 Create Query
        query = "update student set late=True where id = %s "

        try:
            # STEP - 5 TAKE INPUT FROM USER
            id = st_id
            
    
        except Exception as e:
            print('INPUT ERROR ', e)
        else:
            try:
                # STEP 6 - CREATE cursor Object
                cursor = conn.cursor()

                # STEP 7 - EXECUTE THE Query
                noofrecoredupdated = cursor.execute(query, int(id))
            except Exception as e:
                print('INSERT PROBLEM ', e)
            else:
                if noofrecoredupdated > 0:
                    
                    # STEP 8 - Commit Database
                    conn.commit()
                    print('record updated')
                    return 'RECORD UPDATED'
                else:
                    print('invalid Id record not updated')
                    return 'INVALID ID'
            finally:
                conn.close()