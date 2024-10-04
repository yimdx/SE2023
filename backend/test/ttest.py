from flask import Flask, request

import pymysql

# Database configuration
DB_HOST = 'localhost'
DB_USER = 'your_username'
DB_PASSWORD = 'your_password'
DB_NAME = 'your_database_name'

app = Flask(__name__)

def connect_to_database():
    """Connect to the MySQL database."""
    connection = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_NAME)
    return connection

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')

        # Connect to the database
        connection = connect_to_database()
        cursor = connection.cursor()

        # Query the database based on user input
        if name and age:
            query = "SELECT * FROM users WHERE name = %s AND age = %s"
            cursor.execute(query, (name, age))
        elif name:
            query = "SELECT * FROM users WHERE name = %s"
            cursor.execute(query, (name,))
        elif age:
            query = "SELECT * FROM users WHERE age = %s"
            cursor.execute(query, (age,))
        else:
            query = "SELECT * FROM users"
            cursor.execute(query)

        # Fetch the results
        results = cursor.fetchall()

        # Close the database connection
        cursor.close()
        connection.close()

        # Render the results
        output = ''
        if results:
            for row in results:
                output += f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}\n"
        else:
            output = "No results found."

        return output

    # Render the form for user input
    return '''
        <form method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name"><br><br>
            <label for="age">Age:</label>
            <input type="text" id="age" name="age"><br><br>
            <input type="submit" value="Submit">
        </form>
    '''
if __name__ == '__main__':
    app.run()


    '''
    @netshop.route("/merchant/goodsList", methods=['GET', 'POST'])
def goodsList():
    #"userName" needs to be cached after login
    formName = getGoodsList()
    mutex.acquire()
    transaction = f"SELECT * FROM {formName}"
    print(f"###########{transaction}###########")
    cursor.execute(transaction)
    result = cursor.fetchall()

    mutex.release()
    return jsonify(result=result),200
    '''