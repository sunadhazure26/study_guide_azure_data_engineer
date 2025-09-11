import pandas as pd
import numpy as np
import os

# Output folder
output_dir = "sap_extracts"
os.makedirs(output_dir, exist_ok=True)

# Record counts
total_records = 25000
chunk_size = 5000

# Common data
materials = ["WPUR100", "WPUR200", "WPUR300"]   # water purifier product codes
cities = ["Delhi", "Mumbai", "Bangalore", "Hyderabad", "Chennai", "Pune"]
statuses = ["Open", "In Process", "Delivered"]

# Function to generate random orders
def generate_orders(start, end):
    data = {
        "OrderID": [f"OIND{str(i).zfill(6)}" for i in range(start, end)],
        "CustomerID": np.random.randint(1000, 9999, end - start),
        "MaterialCode": np.random.choice(materials, end - start),
        "OrderDate": pd.date_range("2025-01-01", periods=(end - start)).strftime("%Y-%m-%d"),
        "City": np.random.choice(cities, end - start),
        "Quantity": np.random.randint(1, 5, end - start),
        "Status": np.random.choice(statuses, end - start),
    }
    return pd.DataFrame(data)

# Function to generate random deliveries
def generate_deliveries(start, end):
    data = {
        "DeliveryID": [f"DIS{str(i).zfill(6)}" for i in range(start, end)],
        "OrderID": [f"OIND{str(i).zfill(6)}" for i in range(start, end)],  # link to orders
        "DeliveryDate": pd.date_range("2025-02-01", periods=(end - start)).strftime("%Y-%m-%d"),
        "DeliveredQty": np.random.randint(1, 5, end - start),
        "City": np.random.choice(cities, end - start),
        "Status": np.random.choice(["Shipped", "Delivered", "In Transit"], end - start),
    }
    return pd.DataFrame(data)

# Generate files in chunks
for start in range(0, total_records, chunk_size):
    end = start + chunk_size
    
    orders_df = generate_orders(start, end)
    deliveries_df = generate_deliveries(start, end)
    
    orders_file = os.path.join(output_dir, f"OIND_{start+1}_{end}.csv")
    deliveries_file = os.path.join(output_dir, f"DIS_{start+1}_{end}.csv")
    
    orders_df.to_csv(orders_file, index=False)
    deliveries_df.to_csv(deliveries_file, index=False)

    print(f"Generated {orders_file} and {deliveries_file}")
