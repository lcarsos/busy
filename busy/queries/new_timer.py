import collections

from database import cursor as c

def query(values):
    if isinstance(values, collections.Sequence):
        c.executemany('''
            INSERT INTO times (
                started,
                amount
            ) VALUES (
                ?,
                ?
            );
        ''', values)
    c.execute('''
        INSERT INTO times (
            started,
            amount
        ) VALUES (
            ?,
            ?
        );
    ''')

