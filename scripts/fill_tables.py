import uvicorn
import psycopg2
import os

from config import config


def fill_tables():

    categories_path = os.path.abspath('categories.csv')
    products_path = os.path.abspath('products.csv')
    products_categories_path = os.path.abspath('products_categories.csv')

    commands = (
        f'''
        COPY categories (category_id, category)
        FROM '{categories_path}'
        DELIMITER ';'
        CSV HEADER;
        ''',
        f'''
        COPY products (product_id, product_name, brand)
        FROM '{products_path}'
        DELIMITER ';'
        CSV HEADER;
        ''',
        f'''
        COPY products_categories (product_id, category_id)
        FROM '{products_categories_path}'
        DELIMITER ';'
        CSV HEADER;
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
    fill_tables()
 