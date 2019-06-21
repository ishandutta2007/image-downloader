#coding=utf-8

import MySQLdb


sql = "select product_id from oc_product where oc_product.product_id not in ( select oc_product_description.product_id from oc_product  join oc_product_description where oc_product.product_id = oc_product_description.product_id"
del_sql = "delete from oc_product where product_id = %d"

def get_ids():
    conn = MySQLdb.connect(host="localhost", user="opencart", passwd="password", db="replica")
    cur.execute(sql)
    results = cur.fetch()
    cur.close()
    conn.close()
    print (results)
    for result in results:
        conn = MySQLdb.connect(host="localhost", user="opencart", passwd="password", db="replica")
        conn.escape_string(del_sql % result[0])
        cur = conn.cursor()
        cur.execute(del_sql)
        conn.commit()
        cur.close()
        conn.close()


if __name__ == "__main__":
    get_ids()