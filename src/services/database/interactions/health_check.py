import logging


class HealthCheck:

    def __init__(self, db, request):
        self.db = db
        self.request = request

    def execute(self):
        return {"status": "ok"}


def health_check(db, request):
    return HealthCheck(db=db, request=request).execute()
