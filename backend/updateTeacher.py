# UPDATE TEACHER RECORD

# INSTALL PYMYSQL FROM INTERNET

# STEP 1 - IMPORT PYMYSQL
import pymysql.cursors

def updateTeacher(t_id, t_first_name, t_last_name, t_email, t_phonenum, t_subject):
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
        query = "update teachers set first_name= %s, last_name= %s, email= %s, phonenum = %s, subject = %s where id = %s "

        try:
            # STEP - 5 TAKE INPUT FROM USER
            id =t_id
            first_name =t_first_name
            last_name =t_last_name
            email =t_email
            phonenum =t_phonenum
            subject = t_subject
    
        except Exception as e:
            print('INPUT ERROR ', e)
        else:
            try:
                # STEP 6 - CREATE cursor Object
                cursor = conn.cursor()

                # STEP 7 - EXECUTE THE Query
                noofrecoredupdated = cursor.execute(query, (first_name, last_name, email, phonenum, subject, int(id)))
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