from django.conf import settings
from django.utils import timezone
from pymongo import MongoClient


class MongoHandler:

    _conn = None
    _db = None

    def __init__(self, database):

        self._conn = MongoClient(settings.MONGO_HOST, port=settings.MONGO_PORT, username=settings.MONGO_USER, password=settings.MONGO_PASSWORD)
        self._db = self._conn[database]

    def insert(self, collection, document):

        return self._db[collection].insert_one(document).inserted_id


class MongoLogging(MongoHandler):

    def __init__(self, database):

        super().__init__(database)

    def log_debug(self, message):

        log = {
            'type': 'DEBUG',
            'date': timezone.now(),
            'message': message

        }

        self.insert('logs', log)

    def log_error(self, message):

        log = {
            'type': 'ERROR',
            'date': timezone.now(),
            'message': message

        }

        self.insert('logs', log)

    def get_logs(self, type):

        collection = self._db['logs']

        return [x for x in collection.find({'type': type})]
