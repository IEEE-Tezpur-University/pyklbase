from db.imports import *
from db.internal import *
from db.utils import generate_uuid
from db.constants import data_directory


class PyklBase:
    def __init__(self, collection):
        self.collection = collection
        create_folder(data_directory)
        create_collection(collection)

    def drop(self):
        return drop_collection(self.collection)

    def create_by_uuid(self, data={}, uuid=generate_uuid()):
        created = create_by_uuid(
            collection=self.collection,
            data=data,
            uuid=uuid
        )
        return uuid if created else None

    def find_by_uuid(self, uuid):
        return find_by_uuid(
            collection=self.collection,
            uuid=uuid
        )
