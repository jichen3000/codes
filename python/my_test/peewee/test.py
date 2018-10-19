from peewee import *
# import psycopg2

# conn = psycopg2.connect(dbname="devops_portal_product1", 
#     host='172.30.35.37', user="postgres", password="secret", port=5432)

# Connect to a Postgres database.
# for test
DB = PostgresqlDatabase('devops_portal_product1', user='postgres', password='secret',
                           host='172.30.35.37', port=5432)
# DB = PostgresqlDatabase('devops_portal', user='postgres', password='secret',
#                            host='172.30.35.13', port=5432)


class BaseModel(Model):
    class Meta:
        database = DB

class Project(BaseModel):
    id = IntegerField(column_name="project_id", primary_key=True)
    name = CharField(column_name="project_name")
    email = CharField()
    change_order = IntegerField(column_name="changeorder")
    allow_ga_renumber = BooleanField()
    class Meta:
        table_name = "do_group_email"
        # primary_key = False

class Role(BaseModel):
    id = IntegerField()
    name = CharField(column_name="role")
    class Meta:
        table_name = "do_user_role"

class User(BaseModel):
    id = IntegerField()
    name = CharField()
    role = ForeignKeyField(Role, column_name="role")
    mantis_id = CharField()
    reserved = BooleanField()
    display_name = CharField()
    class Meta:
        table_name = "do_user"

class ProjectPermission(BaseModel):       
    # project = ForeignKeyField(Project, object_id_name="id", column_name="project_id")
    project_id = IntegerField(column_name="project_id")
    project_name = CharField(column_name="proj_name")
    user = ForeignKeyField(User)
    role = ForeignKeyField(Role, column_name="role")
    status = IntegerField()
    incident = CharField(column_name="incident_id")
    class Meta:
        table_name = "do_user_project_associate"
        primary_key = False

def get_field_values(peewee_obj):
    return {field_name:getattr(peewee_obj, field_name) 
        for field_name in peewee_obj._meta.fields}

def one_line_dict(dd):
    return ",".join(["'{}':{}".format(*x) for x in dd.items()])

def print_table(query, count_limit=100):
    count = 0
    for cur_p in query:
        print(count,one_line_dict(get_field_values(cur_p)))
        count += 1
        if count >= count_limit:
            break
# print_table(Project.select())
print_table(User.select().order(User.id))
# print_table(ProjectPermission)

# def test_create():
#     test_project = Project.create(id=999,name="colin/test",email="chengji@fortinet.com")

# def delete():
#     db.execute_sql("delete do_user_project_associate where user_id=23")

# query = User.select().where(User.id == 23)
# for cur_p in query:
#     print(cur_p.name)

# query = ProjectPermission.select()
# for cur_p in query:
#     print(cur_p.project_name, cur_p.user.name, cur_p.role.name)
