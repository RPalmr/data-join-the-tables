# pylint:disable=C0111,C0103

def detailed_orders(db):
    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''
    query = """
    SELECT
        o.orderid,
        c.contactname,
        e.firstname
    FROM
        orders o
    JOIN
        customers c ON  c.CustomerID = o.CustomerID
    JOIN
        employees e ON e.EmployeeID = o.EmployeeID
    ORDER BY
        o.orderid;
    """

    results = db.execute(query)
    results = results.fetchall()

    return results

def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
    amount (to 2 decimal places)
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''
    query = """
      SELECT
        c.ContactName,
        SUM(od.UnitPrice * od.Quantity) AS totalamount
    FROM
        customers c
    JOIN
    	orders o ON o.CustomerID = c.CustomerID
   	JOIN
   		orderdetails od ON od.OrderID = o.OrderID
   	GROUP BY c.CustomerID
   	ORDER BY totalamount
    """

    results = db.execute(query)
    results = results.fetchall()
    spent_per_customer_list = [(row[0], round(row[1], 2)) for row in results]
    return spent_per_customer_list

def best_employee(db):
    '''done - line too long'''
    query = """
    SELECT
        e.firstname,
        e.lastname,
        SUM(od.quantity * od.UnitPrice) as total_quantity
    FROM
        orderdetails od
    JOIN
        orders o ON od.orderid = o.orderid
    JOIN
        employees e ON e.employeeid = o.employeeid
    GROUP BY
        e.employeeid, e.firstname, e.lastname
    ORDER BY
        total_quantity DESC
    LIMIT 1;
    """

    results = db.execute(query)
    results = results.fetchone()

    return results

def orders_per_customer(db):
    '''Return a list of tuples where each tuple contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''
    query= """
    SELECT
        c.contactname,
        COUNT(o.orderid) as number_of_orders
    FROM
        customers c
    LEFT JOIN
        orders o ON c.customerid = o.customerid
    GROUP BY
        c.contactname
    ORDER BY
        number_of_orders ASC;"""

    results = db.execute(query)
    results = results.fetchall()

    return results
