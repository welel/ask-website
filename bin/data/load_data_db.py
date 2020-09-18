import os
import json
from random import randrange
import MySQLdb
from dotenv import load_dotenv


load_dotenv()
USER = os.getenv('USER')
PASSWORD = os.getenv('DATABASE_PASSWORD')

'''Load data from files in valiavles'''
with open('users.csv') as uf:
    users = [tuple(line.split(',')) for line in uf.read().split('\n')]

with open('questions.csv') as qf:
    questions = [tuple(line.split('~^~')[:-1]) for line in qf.read().split('\n')]
questions = [tuple([int(qid), text, int(uid)]) for qid,text,uid in questions]

with open('answers.csv') as af:
    answers = [tuple(line.split('~^~')[:-1]) for line in af.read().split('\n')]
answers = [tuple([text, int(uid), int(qid)]) for text,uid,qid in answers]


db = MySQLdb.connect(host='localhost', user=USER, passwd=PASSWORD, db='ask')
cursor = db.cursor()
'''Set default values for columns'''
cursor.execute('ALTER TABLE auth_user ALTER is_superuser SET DEFAULT 0;')
cursor.execute('ALTER TABLE auth_user ALTER first_name SET DEFAULT \'\';')
cursor.execute('ALTER TABLE auth_user ALTER last_name SET DEFAULT \'\';')
cursor.execute('ALTER TABLE auth_user ALTER email SET DEFAULT \'\';')
cursor.execute('ALTER TABLE auth_user ALTER is_staff SET DEFAULT 0;')
cursor.execute('ALTER TABLE auth_user ALTER is_active SET DEFAULT 1;')
cursor.execute('''ALTER TABLE auth_user MODIFY COLUMN date_joined TIMESTAMP NOT
                  NULL DEFAULT CURRENT_TIMESTAMP;''')
cursor.execute('''ALTER TABLE qa_question MODIFY COLUMN added_at TIMESTAMP NOT
                  NULL DEFAULT CURRENT_TIMESTAMP;''')
cursor.execute('''ALTER TABLE qa_answer MODIFY COLUMN added_at TIMESTAMP NOT
                  NULL DEFAULT CURRENT_TIMESTAMP;''')
db.commit()

'''Insert data in tables'''
cursor.executemany(
                '''INSERT INTO auth_user (username, password)
                   VALUES (%s, %s);''', users
)
db.commit()
cursor.executemany(
                '''INSERT INTO qa_question (id, text, author_id)
                    VALUES (%s, %s, %s);''', questions
)
db.commit()
cursor.executemany(
                '''INSERT INTO qa_answer (text, author_id, question_id)
                    VALUES (%s, %s, %s);''', answers
)
db.commit()
db.close()


