# This is a joint project between Daisy, Arthur and Tom
#
# The logic defined here implements an SMS-like python command-line application
# in which a server stores and forwards messages to clients(the storage is volatile)
# ie the messages are lost whenever the server restarts and this includes when a
# change is made to it)
#
# the main lesson to be learned here is how to ocrrdinate data between one server
# and two or more clients, as this is what happens in real word
#
# Contacts:
#   Arthur +256-758-855-695 <athurstaurtleo@hotmail.com>
#   Daisy  +256-751-300-440 <mushdaisy71@gmail.com>

import time, random, json, sms_data

jencode = json.JSONEncoder().encode
jdecode = json.JSONDecoder().decode

class CustomRequest:
    def __init__(self, request):
        payload = request.form.get("json-payload","{}")
        self.json = jdecode(payload)


def generate_ID():
    """
    generate a randon numbr=er from 10000 to 99999
    """
    return random.randint(10000,99999)

USERS = {
    # this dictionary will hold info of all known system users in format;
    # 'id': username
    #here 'id'is the key in the USERS' dictionary
}

MESSAGES = {
    # this dictionary will hold user messages in format;
    # "id": {
    #       "messages":[ This is a python empty List that is to contain a 
    #            dictionary with
    #           keys 'SENDER','MSG','TIMESTAMP',TIMESTAMP_IN_SECONDS for every message sent or received for every particular id
    #                {
    #               "sender":username, 
    #               "msg":string, 
    #               "timestamp":time-from--time.asctime()),
    #               "timestamp_in_seconds": time-from-time.time()
    #                },
    #           ...
    #       ],
    #
    #       "last_fetch_time": FLOAT (read from time.time())   
    # }
}

#this time storage is not volatile
 
#json_users =json.dumps(USERS)
#fout=open("users.json","w")
#fout.write(json_users)
#fout.close()


#json_messages =json.dumps(MESSAGES)
#fout=open("messages.json","w")
#fout.write(json_messages)
#fout.close()


def login(request):
    #db, cur = databasesql.init()
    #cur.execute("select * from user_details");
    
    #print cur.fetchall();
    
    #json_users =json.dumps(USERS)
    #fout=open("users.json","r")
    #fout.read(json_users)
    #fout.close()
    
    
    #init()
    
   # read_user()
    
    username = request.json["uname"]
    
    user_found = False # initially there is no user in the system
    found_user_id = 0 # as return there is no user_id and default set to 0.
    
    db, cur = sms_data.init()
    users=sms_data.read_user_details(db,cur)
    
    for user in users:
        if user[1]==username:
            user_found = True
            found_user_id = user[0]
            break
    
    return jencode({"status":user_found, "id":found_user_id})

def register(request):
    login_reply = jdecode(login(request)) #this decodes data returned from the login function into json form so that it can be used in this function,in other words
        
    if login_reply["status"]:#status is a "key" from object returned.
        return jencode({"status":False, "id":0})
    
    new_id = generate_ID()
    uname = request.json["uname"]
    
    db, cur = sms_data.init()
    sms_data.write_user_details(db, cur, new_id, uname)
    
    return jencode({"status":True, "id":new_id})

def post_message(request):
    sender_id = request.json["id"]
    
    users =sms_data.read_user_details(*sms_data.init())#datadase details
    
    sender_in_system = False
    for user in users:
        if user[0]==sender_id:
            sender_in_system = True
            sender_username = user[1]
            break
    
    if not sender_in_system:
        return jencode({"status":False, "log":"sender is unknown"})

    #message_time_in_seconds = time.time()
    #human_readable_timestamp = time.asctime() # not needed
    

    
    recepients = request.json["recepients"]
    recepients = [int(recepient) for recepient in recepients]
    print recepients
    
    #sender_username = USERS[sender_id]
    
    message = request.json["msg"]
    
    log = ""
    
    for recepient in recepients:
        db, cur = sms_data.init()
        message_sent = sms_data.save_message(db, cur, recepient, sender_username, message )
        
        
        
       # if not (recepient in message_sent):
        #    log += "(recepient ID %d not in system)..."%recepient
         #   continue
        
     #   if recepient=sender_id:
     #      return jencode({"status":False, "log":"You cannot send yourself a message...!"})
            
        #MESSAGES[recepient]["messages"].append(
         #   {
          #      "sender":sender_username, 
             #   "msg":message, 
              #  "timestamp":human_readable_timestamp,
               # "timestamp_in_seconds": message_time_in_seconds
            #}
        #)
        
        
    
    print message_sent
    return jencode({"status":True, "log":log})

def read_inbox(request):
    uid = request.json["id"]
    print uid
    
    
    messages=sms_data.get_inbox(*sms_data.init()+(uid,))
    
   # if not (client_id in MESSAGES):
    #    return jencode({"status":False, "messages":[], "log":"unknown client ID"})
    
    #timestamp = time.time()
    
    #messages = [msg for msg in MESSAGES[client_id]["messages"] if msg["timestamp_in_seconds"]>MESSAGES[client_id]["last_fetch_time"]]

    #MESSAGES[client_id]["last_fetch_time"] = timestamp
    
    return jencode({"status":True, "messages":messages, "log":""})
    
def users_in_system():
    return jencode(sms_data.read_user_details(*sms_data.init()))
    
    
def fetch_all_messages():
    db, cur = sms_data.init() 
    
    my_id = request.json["id"]
    
    return jencode(sms_data.fetch_all_messages(db,cur,uid));
