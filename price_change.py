#coding=utf-8

import MySQLdb


sql = "select price from oc_product"
del_sql = "update from oc_product where product_id = %d"

def get_ids():
    conn = MySQLdb.connect(host="104.237.140.40", user="opencart", passwd="password", db="replica")
    cur.execute(sql)
    results = cur.fetch()
    cur.close()
    conn.close()
    print (results)
    # for result in results:
    #     conn = MySQLdb.connect(host="104.237.140.40", user="opencart", passwd="password", db="replica")
    #     conn.escape_string(del_sql % result[0])
    #     cur = conn.cursor()
    #     cur.execute(del_sql)
    #     conn.commit()
    #     cur.close()
    #     conn.close()


if __name__ == "__main__":
    get_ids()