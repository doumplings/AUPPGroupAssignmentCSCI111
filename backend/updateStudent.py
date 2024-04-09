# UPDATE STUDENT RECORD

# INSTALL PYMYSQL FROM INTERNET

# STEP 1 - IMPORT PYMYSQL
import pymysql.cursors

def updateStudent(st_id, st_first_name, st_last_name, st_email, st_phonenum, st_dob):
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
        query = "update student set first_name= %s, last_name= %s, email= %s, phonenum = %s, dob = %s where id = %s "

        try:
            # STEP - 5 TAKE INPUT FROM USER
            id = st_id
            first_name = st_first_name
            last_name = st_last_name
            email = st_email
            phonenum = st_phonenum
            dob = st_dob
    
        except Exception as e:
            print('INPUT ERROR ', e)
        else:
            try:
                # STEP 6 - CREATE cursor Object
                cursor = conn.cursor()

                # STEP 7 - EXECUTE THE Query
                noofrecoredupdated = cursor.execute(query, (first_name, last_name, email, int(phonenum), dob, int(id)))
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