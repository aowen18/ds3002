#1. Write a query to get Product name and quantity/unit.  
Select northwind.products.product_name, northwind.products.quantity_per_unit FROM northwind.products;
# 2. Write a query to get current Product list (Product ID and name).  
Select northwind.products.product_name, northwind.products.id FROM northwind.products WHERE northwind.products.discontinued ='0';
# 3. Write a query to get discontinued Product list (Product ID and name). discontinued
Select northwind.products.product_name, northwind.products.id FROM northwind.products WHERE northwind.products.discontinued ='1';
# 4. Write a query to get most expense and least expensive Product list (name and unit price).
Select northwind.products.product_name, northwind.order_details.unit_price FROM northwind.products JOIN northwind.order_details ON northwind.products.id = northwind.order_details.product_id WHERE unit_price= (select MAX(unit_price) FROM northwind.order_details) OR unit_price= (select MIN(unit_price) from northwind.order_details);
# 5. Write a query to get Product list (id, name, unit price) where current products cost less than $20.
Select northwind.order_details.product_id, northwind.products.product_name, northwind.order_details.unit_price FROM northwind.products JOIN northwind.order_details ON northwind.products.id = order_details.product_id WHERE unit_price<20;
# 6. Write a query to get Product list (id, name, unit price) where products cost between $15 and $25
Select northwind.order_details.product_id, northwind.products.product_name, northwind.order_details.unit_price FROM northwind.products JOIN northwind.order_details ON northwind.products.id = order_details.product_id WHERE unit_price between 15 and 25;
# 7. Write a query to get Product list (name, unit price) of above average price.
Select northwind.products.product_name, northwind.order_details.unit_price FROM northwind.products JOIN northwind.order_details ON northwind.products.id = northwind.order_details.product_id WHERE unit_price> (select AVG(unit_price) FROM northwind.order_details);
# 8. Write a query to get Product list (name, unit price) of ten most expensive products. 
Select northwind.products.product_name, northwind.order_details.unit_price FROM northwind.order_details JOIN northwind.products ON northwind.products.id = order_details.product_id order by unit_price desc LIMIT 10;
# 9. Write a query to count current and discontinued products. 
Select northwind.products.discontinued, COUNT(*) AS 'current' from northwind.products group by discontinued;
# 10. Write a query to get Product list (name, units on order, units in stock) of stock is less than the quantity on order.
Select northwind.products.product_name, northwind.order_details.quantity, northwind.inventory_transactions.quantity FROM northwind.products JOIN northwind.order_details JOIN northwind.inventory_transactions ON northwind.products.id=northwind.order_details.product_id AND northwind.order_details.product_id=inventory_transactions.product_id WHERE inventory_transactions.quantity < northwind.order_details.quantity;