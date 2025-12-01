\copy employee from 'seeding/csv/employees.csv' with (format csv, header);
\copy customer from 'seeding/csv/customers.csv' with (format csv, header);
\copy ingredient from 'seeding/csv/ingredients.csv' with (format csv, header);
\copy menu from 'seeding/csv/menu_items.csv' with (format csv, header);
\copy recipe from 'seeding/csv/recipes.csv' with (format csv, header);
\copy "order" from 'seeding/csv/orders.csv' with (format csv, header);
\copy order_content from 'seeding/csv/order_contents.csv' with (format csv, header);


INSERT INTO z_report (timestamp) VALUES (CURRENT_TIMESTAMP - INTERVAL '1 day');