# Product Price Calculator

A Python script that calculates tax-included prices for multiple products and displays them in a clean, formatted table. Perfect for beginners and small data projects.

## Features

- Add multiple products interactively.
- Specify individual tax rates for each product (default is 12%).
- Automatically calculates total price including tax.
- Displays a neatly aligned table for easy reading.
- Beginner-friendly, using lists, dictionaries, and f-strings.

## How to Use

1. Clone or download this repository.  
2. Run the script:

```bash
python product_price_calculator.py

3. Follow the prompts:
  - Enter the product name.
  - Enter the product price.
  - Enter the tax rate in percent (press Enter to use the default 12%).
  - Repeat for additional products.

4. When finished, type `no` when asked to add another product.

5. The program will display a table showing:
  - `No.` → Product number
  - `Product` → Name of the product
  - `Tax(%)` → Tax rate applied
  - `Total($)` → Final price including tax
