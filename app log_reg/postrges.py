import psycopg2

from config import host, user, password, db_name, port


connection = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,  # или другой адрес, если удалённый сервер
            port=port   # по умолчанию 5432
        )


def user_data_reg(User_name, User_password):
    try:
        connection = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,  # или другой адрес, если удалённый сервер
            port=port  # по умолчанию 5432
        )

        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO users (user_name, user_password)
                VALUES (%s, %s) RETURNING user_id;
                """,
                (User_name, User_password)
            )

            print(f'{cursor.fetchall()}')

            cursor.execute(
                'SELECT * FROM users;'
            )
            print(f'{cursor.fetchall()}')

            connection.commit()

    except Exception as ex:
        print(' [INFO]  Can`t establish connection to database', ex)
    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection closed')

def user_data_login(User_name, User_password):
    try:

        connection = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,  # или другой адрес, если удалённый сервер
            port=port  # по умолчанию 5432
        )

        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT * FROM users
                WHERE user_name=%s AND user_password=%s
                """,
                (User_name, User_password)
            )

            print(f'{cursor.fetchall()}')

            cursor.execute(
                'SELECT * FROM users;'
            )
            a = cursor.fetchall()
            print(f'{a}')

            if not a:
                print('не удалось залогиниться')
            else:
                print('login успешен')


    except Exception as ex:
        print(' [INFO]  Can`t establish connection to database', ex)
    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection closed')


