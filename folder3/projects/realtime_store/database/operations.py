from database.db import get_connection

# search
def search_products(keyword):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT title, price, rating
    FROM products
    WHERE LOWER(title) LIKE %s
    """

    cursor.execute(query, (f"%{keyword.lower()}%",))
    results = cursor.fetchall()

    cursor.close()
    conn.close()
    return results

# filter by price
def filter_by_price(max_price):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)

    query="""Select title, price from products where price<=%s"""
    cursor.execute(query,(max_price,))
    results= cursor.fetchall()
    cursor.close()
    conn.close()
    return results

# filter by rating
def filter_by_rating(min_rating):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)

    query="""Select title, rating from products where rating>=%s"""
    cursor.execute(query,(min_rating,))
    results= cursor.fetchall()
    cursor.close()
    conn.close()
    return results

# statistics:
def get_stats():
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    query="""select count(*) as Total_products,
            avg(price) as Avg_price,
            max(price) as Max_price,
            min(price) as Min_price
            from products
        """
    cursor.execute(query)
    result=cursor.fetchone()
    cursor.close()
    conn.close()
    return result

# categories
def get_categories():
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    query="""select distinct category from products 
        """
    cursor.execute(query)
    result=cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# sort by price
def sort_by_price(order):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)

    if order.lower() =="asc":
        query="select title,price from products order by price"
    else:
        query="select title, price from products order by price DESC "
    
    cursor.execute(query)
    result=cursor.fetchall()
    cursor.close()
    conn.close()
    return result
