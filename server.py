#!/usr/bin/env python
from flask import Flask
from util import response
import sqlite3

app = Flask('packer-test')

db = sqlite3.connect(':memory:', isolation_level=None)
db.row_factory = sqlite3.Row

c = db.cursor()
c.execute('CREATE TABLE counters (visits int)')
c.execute('INSERT INTO counters (visits) VALUES (0)')

@app.route('/')
def status():
  c.execute('UPDATE counters SET visits = visits + 1')
  c.execute('SELECT visits FROM counters')
  row = c.fetchone()
  return response.send({
    'name'  : 'packer-test',
    'count' : row[0],
  })


if __name__ == '__main__':
  app.run(host='0.0.0.0')
