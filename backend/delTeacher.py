
# STEP 1 - IMPORT PYMYSQL
import pymysql.cursors


# STEP 2 - Connect to MYSQL database]
def deleteTeacher(teacher_id):
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
        query = "delete from teachers where id = %s"

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
                noofrecoreddelete = cursor.execute(query, (int(id)))
            except Exception as e:
                print('DELETE PROBLEM ', e)
            else:
                if noofrecoreddelete > 0:
                    conn.commit()
                    return True
                    # STEP 8 - Commit Database
                    
                else:
                    return False
            finally:
                conn.close()

