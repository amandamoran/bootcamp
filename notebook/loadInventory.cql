COPY demo.inventory( sku, item_name, item_type, stock_loc, num_items, backorder) FROM 'inventory.csv' WITH DELIMITER = '|';
