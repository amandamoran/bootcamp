COPY demo.customer_transactions( id, customer_name, gender, age, state, home_store, items, year, month, rewards_member) FROM 'customer.csv' WITH DELIMITER = '|';
