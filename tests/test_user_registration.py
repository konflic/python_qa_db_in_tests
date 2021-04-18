def test_register_user(new_customer, db_con):
    cursor = db_con.cursor()
    query = "SELECT customer_id FROM oc_customer WHERE email = %s"
    cursor.execute(query, (new_customer,))

    result = cursor.fetchone()
    assert  result, "Data was not added to database"

    customer_id = result[0]
    query = "SELECT ip FROM oc_customer_ip WHERE customer_id = %s"
    cursor.execute(query, (customer_id,))

    result = cursor.fetchone()
    assert  result, "Data for user {} was not added to oc_customer_ip table".format(new_customer)
