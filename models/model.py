from mongoengine import Document, StringField, ReferenceField, CASCADE
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask import current_app

class School(Document):
    schoolName = StringField(required=True)
    conventionName = StringField()
    emailId = StringField()
    contact = StringField()

class User(Document):
    fullName = StringField(required=True)
    emailID = StringField(required=True, unique=True)
    password = StringField(required=True)
    
    school = ReferenceField(School, required=True, reverse_delete_rule=CASCADE)
    
    course_opted1 = StringField()
    course_opted2 = StringField()
    course_opted3 = StringField()
    course_teaching = StringField()