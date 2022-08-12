"""
This script uses the sqlite3 library to communicate with the database. If
there are any updates that require communication with the database it should
be added here
"""
import sqlite3 as db


def get_surf_location_and_regions():
    """
    Connects to the database and retrieves the information such as the surf
    location and its region

    return (list): List containing tuples with surf location and region
    """
    connection = db.connect('SurfDatabase.db')
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM SurfTable"
    )
    table_info = cursor.fetchall()
    connection.close()
    return table_info
