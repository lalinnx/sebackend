import json
import requests
import keyring
import sys

TOKEN = "21123~Ci16eEjIuU2RnkZW4iPgSMq5cSOWgIiLUqFNdtUUCMaHhNFjSjMOb6IYRkHC62ZP"
HEADER = {'Authorization': 'Bearer ' + TOKEN}
URL = 'https://mango-cmu.instructure.com/api/v1'

course_id = 1306
quiz_title = "[New Quizzes]ทดสอบเพิ่มquiz จาก api"

quiz = {}
quiz['quiz[title]'] = '%s' %(quiz_title)

END = '/courses/%s/quizzes' %(course_id)
print(URL+END)
x = requests.post(URL + END, headers=HEADER, data=quiz )

x = x.json()
y = {x.get('id'),x.get('title')}
print(y)