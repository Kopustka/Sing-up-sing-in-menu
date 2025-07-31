import psycopg2
from config import host, user, password, db_name, port

# Note: Here a global connection is created but inside functions
# you create new connections separately. This can be optimized.

# Function to register a new user in the database
def user_data_reg(User_name, User_password):
    try:
        # Create a new connection to the PostgreSQL database
        connection = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,  # Hostname or IP of the DB server (could be remote)
            port=port   # Default PostgreSQL port is 5432
        )

        # Use a context manager to get a cursor for executing SQL commands
        with connection.cursor() as cursor:
            # Insert a new user into the "users" table with username and password
            cursor.execute(
                """
                INSERT INTO users (user_name, user_password)
                VALUES (%s, %s) RETURNING user_id;
                """,
                (User_name, User_password)
            )
            # Fetch and print the returned user_id (newly created)
            print(f'{cursor.fetchall()}')

            # Optional: fetch and print all users in the table (for debug)
            cursor.execute('SELECT * FROM users;')
            print(f'{cursor.fetchall()}')

            # Commit changes to make sure the insert is saved
            connection.commit()

    except Exception as ex:
        # Print an error message if something went wrong
        print(' [INFO]  Can`t establish connection to database', ex)

    finally:
        # Always close the connection to free resources
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection closed')


# Function to check if user credentials exist in the database for login
def user_data_login(User_name, User_password):
    try:
        # Establish a new connection to the PostgreSQL database
        connection = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )

        # Use cursor to execute the SELECT query
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT * FROM users
                WHERE user_name=%s AND user_password=%s
                """,
                (User_name, User_password)
            )

            # Fetch all matching rows
            a = cursor.fetchall()
            print(f'Retrieved rows: {a}')

            # If no rows found, login failed
            if not a:
                print('Login failed: invalid username or password')
                return False
            else:
                print('Login successful')
                return True

            # The code below is unreachable due to return statements above,
            # you can remove or move it if needed
            cursor.execute('SELECT * FROM users;')
            print(f'{cursor.fetchall()}')

    except Exception as ex:
        # Handle any errors during DB connection or query execution
        print(' [INFO]  Can`t establish connection to database', ex)

    finally:
        # Close the database connection
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection closed')
