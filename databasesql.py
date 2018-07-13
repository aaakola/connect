# custom module "DATABASESQL" that creates functions that contain sql statements that can be used to stores and retrieves data from
# A database

#this is an independent Module That will be imported in the logic.py but with sql statements


#Author:Akola Arthur Alaali

#Contact Information
#Email:arthurstaurtleo@hotmail.com
 #    :arthurstaurtleo@gmail.com

#phone:+256758855695
#created On:19th June 2018 and Modified On:20th June 2018


import sqlite3 as sql,sys

#sqlite inbuilt functions connect(),cursor(),commit()

FNAME= "smschat.db"

def init():
    db = sql.connect(FNAME)

    cur=db.cursor()
     
    stmt = """ create table if not exists user_details(
    User_id int primary key not null,
    Username varchar(25) not null,
    Time_sent_in_seconds real not null
    )"""
    cur.execute(stmt)
    db.commit()
    
    db = sql.connect(FNAME)
    cur=db.cursor()
    
    messages =""" create table if not exists messages(
    message_to int primary key not null,
    message_from varchar(25) not null,
    Text varchar(100),
    Time_sent_human_form varchar(30) not null,
    Time_sent_in_seconds real not null
    )"""
    
    cur.execute(messages)
    db.commit()
    
    
    return db, cur

def add_user(db,cur,new_id,uname,Time_sent_in_seconds):
    cur=db.cursor()
    stmt="""
    insert into user_details values(?,?,?)
    """
    try:
        cur.execute( stmt, (new_id,uname,Time_sent_in_seconds))
        db.commit()
        return True
    except:
        print "Unable to add User to the Database"
        print ""
        print "The User_Id Entered Already Exists In The System"#
        return False
        
def read_user(db,cur):#,uname not required
    cur.execute("select Username from user_details")
    users_in=cur.fetchall()
    
    return [user_in[0] for user_in in users_in]
    
    #print returned_users
    #print users_in
    
    #return users_in
    
def read_all_users(db,cur):#,uname not required
    cur.execute("select Username from user_details")
    all_users_in=cur.fetchall()#thi
    
    print all_users_in
    
    return  all_users_in  #[ user_in[0] for user_in in users_in]
        

    
def save_message(db,cur,message_to,message_from,Text,Time_sent_human_form):#*read_all_user()  
    
    cur=db.cursor()#points to a pointer in the database file
    
    msg="""
    insert into messages values(?,?,?,?,?)
    """
    
    msg=cur.execute( msg, (message_to,message_from,Text,time.acstime(),time.time()) )
    db.commit()   
   # print msg

#def read_inbox(db,cur,user_id):
    
 #   cur.execute("""select User_id,Time_sent_in_seconds from user_details where User_id = ?""",(user_id,))
  #  specific_user_id=cur.fetchall()
    
   # cur.execute("select message_from,Text,Time_sent_human_form from messages where User_id = ?",(user_id,))
    #message_for_user_id = cur.fetchall()
    
    
def get_inbox(db, cur, uid):
    cur.execute("select last_fetch_time from users_details where ID = ?",(uid,))
    last_fetch_time = cur.fetchone()
    if not last_fetch_time:
        return []
        
    last_fetch_time = last_fetch_time[0]

    t=time.time()
    cur.execute("""
        select time_sent_human_form,message_from,message from messages where 
        (message_to = ?) and (message_time_in_seconds > ?)""",
        (uid,last_fetch_time)
    )
    messages = cur.fetchall()
    
    cur.execute("update users_details set last_fetch_time=? where ID=?",(t,uid))
    db.commit()
    return messages
    
    
    
    
    
    
    
    
    
    
    #if (Time_sent_in_seconds

    
#def read_msg_data:
    

db,cur=init()

#add_user(db,cur,"1011","Mush",0.0)

read_user(db,cur)#,"daisy"

#users =read_user(*init())
#print users

#db,cur=init()

#save_message(db,cur,10013,"bug","Thank You,we..","Wed Jun 20 10:42:19 2018")

#db,cur =init()
#read_inbox(db,cur,10012)

def g():
    for i in range(20):
        yield i

print g().next()#

