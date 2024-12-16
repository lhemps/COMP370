'''
initial code given:
# get all the sales data by product type
book_sales_2022 = load("data/book_sales_2022.csv")
book_sales_2023 = load("data/book_sales_2023.csv")
book_sales_2024 = load("data/book_sales_2024.csv")

game_sales_2022 = load("data/game_sales_2022.csv")
game_sales_2023 = load("data/game_sales_2023.csv")
game_sales_2024 = load("data/game_sales_2024.csv")

# calculate the total sales for each year
total_sales_2022 = sum_sales(book_sales_2022, game_sales_2022)
total_sales_2023 = sum_sales(book_sales_2023, game_sales_2023)
total_sales_2024 = sum_sales(book_sales_2024, game_sales_2024)

'''
# i'm assuming this is the right load function
from json import load

total_sales = {}
for i in range(2022,2025):
    book_sales = load('data/book_sales_'+i+'.csv')
    game_sales = load('data/game_sales_'+i+'.csv')
    # don't know what sum_sales function is so this code won't actually run lol
    total_sales[i] = sum_sales(book_sales, game_sales)

# for each variable total_sales_YYYY, you just have to do total_sales['YYYY']