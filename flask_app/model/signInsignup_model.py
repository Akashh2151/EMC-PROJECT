import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

class SignupModel:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="roott",
                database="emc_project",
                port="3306"
            )
            print("Connection successful")
        except mysql.connector.Error as err:
            print("Error:", err)



    def register_user(self, username, email, password):
        try:
            cursor = self.con.cursor()

        # Check if user already exists
            query_check = "SELECT * FROM users WHERE username = %s"
            cursor.execute(query_check, (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                return {"message": "Username already taken"}

        # Hash the password using pbkdf2:sha256 method
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Insert new user
            query_insert = "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)"
            values = (username, email, hashed_password)
            cursor.execute(query_insert, values)
            self.con.commit()

            cursor.close()
            response = {"message": "Registration successful"}
            return response
        except mysql.connector.Error as err:
            print("Error:", err)
            response = {"message": "An error occurred during registration"}
            return response

 




    def login_user(self, username, password):
        try:
            cursor = self.con.cursor(dictionary=True)
            query = "SELECT * FROM users WHERE username = %s"
            cursor.execute(query, (username,))
            user = cursor.fetchone()
            cursor.close()

            if user and check_password_hash(user["password_hash"], password):
                response = {"message": "Login successful"}
            else:
                response = {"message": "Invalid credentials"}

            return response
        except mysql.connector.Error as err:
            print("Error:", err)
            response = {"message": "An error occurred during login"}
            return response



    def close_connection(self):
        if hasattr(self, 'con') and self.con.is_connected():
            self.con.close()
            print("Connection closed")
