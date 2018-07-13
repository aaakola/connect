#Program that uses database to store username, IDs and messages of different users that are registered in the system.
#
#Written by:
#   Mushabe Daisy
#
#Contacts:
#   +256-751-300-440
#   mushdaisy71@gmail.com


import sqlite3 as sql,sys
FNAME = "user_details.db"
db = sql.connect(FNAME)

def init ():
    cur=db.cursor()
    stmt="""create table if not exists users_details(
    ID int primary key not null,
    username varchar(30) not null,
    last_fetch_time real not null
    )"""
    cur.execute(stmt)
    db.commit()
    
    cur=db.cursor()
    stmt="""create table if not exists messages(
    message_to int primary key not null,
    message_from varchar(30) not null,
    message text not null,
    time_sent_human_form varchar(5) not null,
    time_sent_in_seconds real not null
    )"""
    cur.execute(stmt)
    db.commit()
    return db,cur
    
def write_user_details(db,cur, uname,uid, last_fetch_time=0):
    cur=db.cursor()
    stmt="""
    insert into users_details values(?,?,?)
    """
    try:
        cur.execute(stmt,(uname,uid, last_fetch_time))
        db.commit()
        return True
    except:
        return False
    
def read_user_details(db,cur):
    cur.execute("select username from users_details")
    rows = cur.fetchall()
    return [row[0] for row in rows]

def get_inbox(db, cur, uid):
    cur.execute("select last_fetch_time from users_details where ID = ? ", uid)
    last_fetch_time = fetchone()
    if not last_fetch_time:
        return []
    
users = read_user_details(*init())     
print users    
