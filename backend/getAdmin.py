# SEARCH RECORDS EXAMPLE

# INSTALL PYMYSQL FROM INTERNET

# STEP 1 - IMPORT PYMYSQL
import pymysql.cursors


# STEP 2 - Connect to MYSQL database
def getAdmin(uid, password):
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
        query = "SELECT admin_id, admin_password FROM admin WHERE admin_id = %s AND admin_password = %s"

        try:
            # STEP - 5 TAKE INPUT FROM USER
            admin = [uid, password]

        except Exception as e:
            print('INPUT ERROR ', e)
        else:
            try:
                # STEP 6 - CREATE cursor Object
                cursor = conn.cursor()

                # STEP 7 - EXECUTE THE Query
                cursor.execute(query, admin)

            except Exception as e:
                print('RECORD FETCHING PROBLEM ', e)
            else:
                if cursor.rowcount > 0:
                    # STEP 8 - DISPLAY RECORDS
                    # Fetch Each Record In Dictionary Format
                    for record in cursor:
                        print(" ----------- ")
                        print("admin_id ", record['admin_id'])
                        print("admin_password ", record['admin_password'])
                    return "FOUND"
                    
                else:
                    print('INVALID admin - NO RECORD FOUND')
                    return "NOTFOUND"
            finally:
                # STEP 9 - CLOSE CONNECTION
                conn.close()

