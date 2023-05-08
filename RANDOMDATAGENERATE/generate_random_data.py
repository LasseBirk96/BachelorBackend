from psycopg2 import connect
import csv
import random
from nanoid import generate
from dataclasses import astuple
from RANDOMDATAGENERATE.Muleapplication import MuleApplication
def establish_connection():
    return connect(dbname="postgres",user="postgres", password="123",port=5432, host="127.0.0.1")



#THIS IS PURELY USED FOR GENERATING RANDOM DATA THAT WAS NEEDED DURING DEVELOPMENT - DELETE FOLDER IF UNWANTED

list_of_first_names = []
with open("./names.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    list_of_first_names.append(row[0])

list_of_last_names = []
with open("./lastnames.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    name = row[0]
    list_of_last_names.append(name.capitalize())



list_of_project_names = []
with open("./projects.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    list_of_project_names.append(row[0])

list_of_costcenters = ["RS", "AD", "CS", "LD", "ZD"]


list_of_muleapp_names = []
with open("./muleappNames.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    list_of_muleapp_names.append(row[0])



list_of_status = ["DEPLOYED", "FAILED", "PENDING"]
list_of_cateory = ["KNOWN", "UNKNOWN"]

onboard = generate(size=10)

def create_initials(first_name, last_name):
    i = first_name[0:2]
    b = last_name[0:2]
    initials = i.upper() + b.upper()
    return initials
    

def create_onboard_id():
    onboard = generate(size=10)
    return onboard


def create_id():
    id = generate(size=10)
    return id


def get_entry(thing):
    max_index = len(thing) - 1
    min_index = 0
    
    entry = random.randint(min_index, max_index)
    return thing[entry]


def get_app(_list, index):
    return _list[index]



def create_mule_app(amount_of_apps):
    _list = []
    max_index = amount_of_apps
    for i in range(amount_of_apps):
        
        id = create_id()
        muleAppName = get_app(list_of_muleapp_names, max_index)
        max_index = max_index - 1
        first_name = get_entry(list_of_first_names)
        last_name = get_entry(list_of_last_names)
        contact_person = first_name +" "+ last_name
        initials = create_initials(first_name, last_name)
        projectname = get_entry(list_of_project_names)
        onboard = create_onboard_id()
        status = get_entry(list_of_status)
        category = get_entry(list_of_cateory)
        costcenter = get_entry(list_of_costcenters)
        dude = MuleApplication(id, muleAppName, contact_person , initials, projectname, onboard, status, category, costcenter)
        _list.append(dude)
    return _list

lenht = len(list_of_muleapp_names) -1
muleApps = create_mule_app(lenht)



def return_muleapplication_table():
    return str("""
            CREATE TABLE IF NOT EXISTS MuleApplication (
                Id VARCHAR(100) primary KEY,
                Name VARCHAR(100) UNIQUE,
                ContactPerson VARCHAR(100),
                ContactPersonInitials VARCHAR(100),
                ProjectName VARCHAR(100),
                OnboardingAgreementID VARCHAR(50),
                Status VARCHAR(50),
                Category VARCHAR(50),
                CostCenterLabel VARCHAR(50))
        """,)

connection = establish_connection()
cursor = connection.cursor()
cursor.execute(return_muleapplication_table())
query = "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
try:
    for element in muleApps:
        cursor.execute(query, astuple(element),)
    
    connection.commit()
except Exception:
        raise
