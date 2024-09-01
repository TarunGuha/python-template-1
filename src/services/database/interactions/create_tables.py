import logging


class CreateTables:

    def __init__(self, db, request):
        self.db = db
        self.request = request

    def execute(self):
        return {"status": "ok"}


def create_tables(db, request):
    return CreateTables(db=db, request=request).execute()
