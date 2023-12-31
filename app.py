from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    # connection = psycopg2.connect(host=os.getenv("PGHOST"), user=os.getenv("PGUSER"), password=os.getenv("PGPASSWORD"), port=os.getenv("PGPORT"), dbname=os.getenv("PGDATABASE"))
    connection_string = os.getenv("DATABASE_URL", "dbname=duckspotting")
    print('Connecting to', connection_string)
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM mytable;")
    results = cursor.fetchall()
    connection.close()

    return f"{results}"

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
