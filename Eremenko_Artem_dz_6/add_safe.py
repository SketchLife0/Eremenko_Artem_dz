import sys
sales_amount = sys.argv[1]
with open('bakery.csv', 'a', encoding='utf-8') as fa:
    if ',' in sales_amount:
        sales_amount = sales_amount.replace(',', '.')
    sales_amount = float(sales_amount)
    print(sales_amount, file=fa)