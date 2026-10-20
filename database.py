import mysql.connector


def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vasanyamu1*#",
        database="ml_dataset_management"
    )

    return connection