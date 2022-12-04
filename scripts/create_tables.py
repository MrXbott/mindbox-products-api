import uvicorn
import psycopg2

from config import config


def create_tables():
    '''This function creates tables in the PostgreSQL database'''

    commands = (
        '''
        CREATE TABLE IF NOT EXISTS categories (
            category_id SERIAL,
            category VARCHAR(255) NOT NULL UNIQUE,
            PRIMARY KEY (category_id)
        )
        ''',
        '''
        CREATE TABLE IF NOT EXISTS products (
            product_id SERIAL,
            product_name VARCHAR(300) NOT NULL,
            brand VARCHAR(100) NOT NULL,
            PRIMARY KEY (product_id)
        )
        ''',
        '''
        CREATE TABLE IF NOT EXISTS products_categories (
            product_id int REFERENCES products (product_id) ON UPDATE CASCADE,
            category_id int REFERENCES categories (category_id) ON UPDATE CASCADE,
            CONSTRAINT products_categories_pkey PRIMARY KEY (product_id, category_id)
        )
        ''',
    )

    connection = None
    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()
        for command in commands:
            cursor.execute(command)
        cursor.close()
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as e:
        print('error: ', e)
    finally:
        if connection is not None:
            connection.close()


if __name__ == '__main__':
    create_tables()