from datetime import datetime

from database import cursor as c

def query(values, columns=('name')):
    if 'created_on' not in columns:
        now = int(datetime.now().timestamp())
        value_stream = ((*row, now) for row in values)
        columns.append('created_on')
    else:
        value_stream = values

    c.executemany('''
        INSERT INTO tasks (
            started,
            amount
        ) VALUES (
            ?,
            ?
        );
    ''', value_stream)

