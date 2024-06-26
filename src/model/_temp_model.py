from peewee import *

database = SqliteDatabase(".\pa.db")


class UnknownField(object):
    def __init__(self, *_, **__):
        pass


class BaseModel(Model):
    class Meta:
        database = database


class Account(BaseModel):
    created = IntegerField()
    description = TextField(null=True)

    class Meta:
        table_name = "account"


class AccountVariable(BaseModel):
    name = TextField()
    value = TextField(null=True)

    class Meta:
        table_name = "account_variable"


class SqliteSequence(BaseModel):
    name = BareField(null=True)
    seq = BareField(null=True)

    class Meta:
        table_name = "sqlite_sequence"
        primary_key = False


class Task(BaseModel):
    account_id = IntegerField(null=True)
    cron = TextField(null=True)
    name = TextField(null=True)
    task_id = IntegerField(null=True)

    class Meta:
        table_name = "task"


class TaskTemplate(BaseModel):
    description = TextField()

    class Meta:
        table_name = "task_template"


class TaskTemplateStep(BaseModel):
    data = TextField(null=True)
    method = TextField()
    parser_pattern = TextField(null=True)
    query = TextField(null=True)
    save_variable = TextField(null=True)
    task_template_id = IntegerField()
    url = TextField()

    class Meta:
        table_name = "task_template_step"
        primary_key = False
