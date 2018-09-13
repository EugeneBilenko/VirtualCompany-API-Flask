import datetime
import config

DATABASE = config.getDB()


class VirtualCo(Model):
    name = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect(reuse_if_open=True)
    DATABASE.create_tables([VirtualCo], safe=True)
    DATABASE.close()
