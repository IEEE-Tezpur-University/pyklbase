import pickle
import json

def initialise_db(db_name):
    try:
        dbfile = open(db_name+".pickle", 'rb')     
        db = pickle.load(dbfile)
        dbfile.close()
        print("DB Already Initialised")
    except Exception as e:
        # Its important to use binary mode
        dbfile = open(db_name+".pickle", 'wb')
        db = {}
        # source, destination
        pickle.dump(db, dbfile)                     
        dbfile.close()
        print("Initialised DB")

def get_from_db(db_name,property):
    try:
        dbfile = open(db_name+".pickle", 'rb')     
        db = pickle.load(dbfile)
        dbfile.close()
        return db[property]
    except Exception as e:
        print("Empty",property,"in",db_name)
        return None

def add_to_db(db_name,property,value):
    dbfile = open(db_name+".pickle", 'rb')     
    db = pickle.load(dbfile)
    dbfile.close()
    if(not db):
        db = {}
    else:
        db = dict(db)
    
    db[property] = value

    # Its important to use binary mode
    dbfile = open(db_name+".pickle", 'wb')
      
    # source, destination
    pickle.dump(db, dbfile)          
    dbfile.close()

def remove_from_db(db_name,property):
    dbfile = open(db_name+".pickle", 'rb')     
    db = pickle.load(dbfile)
    dbfile.close()
    if(not db):
        db = {}
    else:
        db = dict(db)
    
    db.pop(property)
    
    # Its important to use binary mode
    dbfile = open(db_name+".pickle", 'wb')
      
    # source, destination
    pickle.dump(db, dbfile)                     
    dbfile.close()