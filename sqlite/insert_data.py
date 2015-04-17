import os
import csv
import glob
import time
import sqlite3
from datetime import datetime

DATABASE_NAME = 'phila_traffic2.db'
DATE_FORMAT = '%m/%d/%Y'
DATETIME_FORMAT = '%m/%d/%Y %I:%M%p'

def convert_date(date_str):
    try:
        result = datetime.strptime(date_str, DATE_FORMAT)
        return result
    except:
        return None

# I believe that this will save the times according to your machine's
# timezone, so if you aren't in EST you'll have to adjust
def convert_datetime(datetime_str):
    try:
        result = datetime.strptime(datetime_str, DATETIME_FORMAT)
        return result
    except:
        return None

files = glob.glob('../citations*.tsv')

for file in files:
    filename = os.path.basename(file)
    if filename != 'citationsHeaders.tsv':
        with open(file, 'rb') as in_file:
            print 'Inserting {}...'.format(filename)
            conn = sqlite3.connect(DATABASE_NAME)
            conn.text_factory = str
            cur = conn.cursor()
            violations = csv.reader(in_file, delimiter='\t')
            next(violations, None) # skip the header

            i = 0

            for v in violations:
                filed_date = convert_date(v[1])
                issue_date = convert_date(v[2])
                defendent_dob = convert_date(v[12])
                disposition_date = convert_date(v[17])
                h_dt = ''
                if len(v[25].strip()) == 0:
                    h_dt = convert_date(v[24])
                else:
                    h_t = v[25].strip()
                    h_t = h_t.replace('P', 'PM')
                    h_t = h_t.replace('A', 'AM')
                    h_dt = v[24] + ' ' + h_t
                    h_dt = convert_datetime(h_dt)
                try:
                    cur.execute('INSERT INTO violations values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', \
                                (v[0], filed_date, issue_date, v[3], v[4], v[5], \
                                v[6], v[7], v[8], v[9], v[10], v[11], defendent_dob, \
                                v[13], v[14], v[15], v[16], disposition_date, v[18], \
                                v[19], v[20], v[21], v[22], v[23], h_dt))
                except sqlite3.IntegrityError as err:
                    print err
                    pass

                i = i + 1
                if i % 25000 == 0:
                    print '{} records inserted so far...'.format(i)
            conn.commit()
            conn.close()
            print 'Done inserting {}'.format(filename)
