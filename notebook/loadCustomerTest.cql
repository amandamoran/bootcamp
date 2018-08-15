COPY demo.customer_test( id, customer_name, gender, age, state, home_store, items, year, month, rewards_member) FROM 'customerTest.csv' WITH DELIMITER = '|';
