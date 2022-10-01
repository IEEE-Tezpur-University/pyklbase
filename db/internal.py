from db.imports import *
from db.constants import system_collection, data_directory


def list_collections():
    pass


def create_system_collection():
    create_collection(system_collection)


def db_directory(collection):
    return data_directory+'/'+collection

def path_exists(path):
    return os.path.exists(path)

def create_folder(path):
    os.mkdir(path) if not path_exists(path) else None

def create_collection(collection):
    create_folder(db_directory(collection))

    return True


def drop_collection(collection):
    shutil.rmtree(db_directory(collection))
    return True


def doc_directory(collection, uuid):
    return db_directory(collection)+'/'+uuid


def doc_file(collection, uuid, mode):
    return open(doc_directory(collection, uuid)+'.pickle', mode)


def create_by_uuid(collection, data, uuid):
    doc = doc_file(collection, uuid, 'wb')
    pickle.dump(data, doc)
    doc.close()
    return True


def find_all(collection):
    docs = []
    directory = db_directory(collection)
    return docs


def find_by_uuid(collection, uuid):
    doc = doc_file(collection, uuid, 'rb')
    data = pickle.load(doc)
    doc.close()
    return data


def update_by_uuid(collection, uuid, data={}):
    doc = doc_file(collection, uuid, 'rb')
    doc_data = pickle.load(doc)
    doc.close()

    data = {} if not data else data
    doc_data = {**doc_data, **data}

    doc = doc_file(collection, uuid, 'wb')
    pickle.dump(doc_data, doc)
    doc.close()
    return True


def delete_by_uuid(collection, uuid):
    os.remove(doc_directory(collection, uuid))
    return True
