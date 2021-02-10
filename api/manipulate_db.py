from web_crawler import return_data
from time import time, sleep
from datetime import datetime
from web_crawler import return_data
import mysql.connector

# connecting to our news database
db = mysql.connector.connect(
    host="db4free.net",
    user="malikovy_admin",
    password="b3fc6f72",~
    database="malikovy_news"
)

mycursor = db.cursor()

#mysql help queries
#////////
# mycursor.execute("CREATE TABLE Article (article_title MEDIUMTEXT, article_image MEDIUMTEXT, article_id int PRIMARY KEY AUTO_INCREMENT, article_text LONGTEXT)")
# mycursor.execute("DROP TABLE ArticleTest")
#////////

def manipulate_db():
    # store data return
    data = return_data()
    print(data)

    print(f"\nINITIAL DATA REFRESH AT{datetime.now()}\n"*3)
    # delete old data
    mycursor.execute("DELETE FROM Article")
    db.commit()
    for res in data:
        # destructure the web crawler data
        title, image, id_num, text = res
        # insert new data
        mycursor.execute("INSERT INTO Article (article_title, article_image, article_text) VALUES (%s, %s, %s)", (title, image, text))
        db.commit()
    
            

manipulate_db()
