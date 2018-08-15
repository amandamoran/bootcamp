COPY demo.customer_live( id, customer_name, gender, age, state, home_store, items, year, month, rewards_member) FROM 'customerTest.csv' WITH DELIMITER = '|';
