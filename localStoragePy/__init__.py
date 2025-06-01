__author__ = 'Suraj Mandal'
__copyright__ = 'Copyright (C) 2021-present Suraj Mandal'
__license__ = 'MIT License'
__version__ = '0.3.0'

from .storage_backends import BasicStorageBackend, TextStorageBackend, SQLiteStorageBackend, JSONStorageBackend

class localStoragePy:
    def __init__(self, app_namespace: str, storage_backend: str = "sqlite") -> None:
        self.storage_backend_instance = BasicStorageBackend(app_namespace)
        if storage_backend == "text":
            self.storage_backend_instance = TextStorageBackend(app_namespace)
        elif storage_backend == "sqlite":
            self.storage_backend_instance = SQLiteStorageBackend(app_namespace)
        elif storage_backend == "json":
            self.storage_backend_instance = JSONStorageBackend(app_namespace)
        else:
            self.storage_backend_instance = SQLiteStorageBackend(app_namespace)

    def getItem(self, item: str) -> any:
        return self.storage_backend_instance.get_item(item)

    def setItem(self, item: str, value: any) -> None:
        self.storage_backend_instance.set_item(item, value)

    def removeItem(self, item: str) -> None:
        self.storage_backend_instance.remove_item(item)

    def getAll(self) -> dict:
        return self.storage_backend_instance.get_all()

    def getMany(self, items: list) -> dict:
        return self.storage_backend_instance.get_many(items)

    def removeAll(self) -> None:
        self.storage_backend_instance.remove_all()

    def clear(self):
        self.storage_backend_instance.clear()

