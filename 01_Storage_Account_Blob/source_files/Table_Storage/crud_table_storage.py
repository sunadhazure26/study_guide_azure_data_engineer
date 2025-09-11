#pip install azure-data-tables run in command prompt


from azure.data.tables import TableClient, TableServiceClient
from azure.core.exceptions import ResourceExistsError

conn_str = "<PUT THE KEY HERE>"

# create/get client
service = TableServiceClient.from_connection_string(conn_str)
table_client = service.get_table_client("customer")

# create table (safe)
try:
    table_client.create_table()
except ResourceExistsError:
    pass

# insert entity
entity = {"PartitionKey":"users", "RowKey":"user1", "Name":"Alice", "Age": 30}
table_client.create_entity(entity)

# get entity
e = table_client.get_entity(partition_key="users", row_key="user1")
print(e)
