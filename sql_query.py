drop_token_list = (""" DROP TABLE IF EXISTS token_list """)

# Create table

create_table_token_list = (""" CREATE TABLE token_list
                (name text, address text PRIMARY KEY) """)


# Insert into tables

insert_token_list = (""" INSERT INTO token_list (name,address) VALUES( ?, ? )""")



# Select table

select_token_list = (""" SELECT * FROM token_list """)


# Delete  table
truncate_table_token_list = (""" DELETE FROM token_list """)