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
    '''Implement the best_employee method to determine who’s the best employee! By “best employee”, we mean the one who sells the most.
    We expect the function to return a tuple like: ('FirstName', 'LastName', 6000 (the sum of all purchase)). The order of the information is irrelevant'''
    pass  # YOUR CODE HERE

def orders_per_customer(db):
    '''Return a list of tuples where each tuple contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''
    pass  # YOUR CODE HERE
