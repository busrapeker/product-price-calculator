products = []

# Loop to add products
while True:
    name = input("Product name: ")
    price = float(input("Product price: "))
    
    tax_input = input("Tax rate (%) [press enter for 12%]: ")
    if tax_input.strip() == "":
        tax = 0.12
    else:
        tax = float(tax_input) / 100
    
    products.append({"name": name, "price": price, "tax": tax})
    
    more = input("Add another product? (yes/no): ").lower()
    if more != "yes":
        break

# Print table header
print("\n--- Products with Tax-Included Price ---")
print(f"{'No.':<4} {'Product':<15} {'Tax(%)':<8} {'Total($)':>10}")
print("-" * 40)

# Print each product with total price
for i, product in enumerate(products, start=1):
    total = product["price"] * (1 + product["tax"])
    print(f"{i:<4} {product['name']:<15} {product['tax']*100:<8.0f} {total:>10.2f}")
