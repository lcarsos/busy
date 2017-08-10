from datetime import datetime

from database import cursor as c

def query(values, columns=('name',)):
    """
    values MUST be a row tuple
    columns should be a tuple of the columns that are being inserted
    """
    if 'created_on' not in columns:
        now = int(datetime.now().timestamp())
        value_stream, columns = ((*row, now) for row in values), (*columns, 'created_on')
    else:
        value_stream = values

    val_qs = (['?'] * len(columns)).join(',')
    c.executemany(
        '''
        INSERT INTO tasks (
            {columns}
        ) VALUES (
            {val_qs}
        );
        '''.format(columns=columns,
                   val_qs=val_qs),
        value_stream)

