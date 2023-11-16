from openpyxl import Workbook
import random

# Create a workbook and select the active sheet
wb = Workbook()
sheet = wb.active

# Add headers
headers = ['Product ID', 'Product Name', 'Price', 'Quantity']
sheet.append(headers)

# Generate sample data for 100 electronic products
for i in range(1, 101):
    product_id = f'P{i:03}'  # Generate product ID
    product_name = f'Product{i}'  # Generate product name
    price = round(random.uniform(10.0, 1000.0), 2)  # Generate random price
    quantity = random.randint(1, 50)  # Generate random quantity

    # Add data to the sheet
    data_row = [product_id, product_name, price, quantity]
    sheet.append(data_row)

# Save the workbook
wb.save("sales.xlsx")
