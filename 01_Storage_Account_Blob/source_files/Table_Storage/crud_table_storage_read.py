from azure.data.tables import TableServiceClient

from azure.data.tables import TableClient, TableServiceClient
from azure.core.exceptions import ResourceExistsError

conn_str = "<PUT THE KEY HERE>"


# Get table client
service = TableServiceClient.from_connection_string(conn_str)
table_client = service.get_table_client("customer")

# Query all entities
for entity in table_client.list_entities():
    print(entity)

# Query with filter (OData)
entities = table_client.query_entities("PartitionKey eq 'users' and Age gt 25")
for e in entities:
    print(e["Name"], e["Age"])
