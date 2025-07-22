# Kyle Segrist
# Chapter 6 Lab 1
# Restaraunt sales tracker

DAY = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

def main():

    index = 0
    sale_list = []
    while index < len(DAY):
        for day in range(len(DAY)):
            try:
                sales = float(input(f'Enter the sales for {DAY[day]} $ ')or"0")
                sale_list.append(sales)
                index += 1
            except ValueError:
                float(input(f'Error please enter a value for the sales for {DAY[day]} $ ' or "0"))
                sale_list.append(sales)
                index += 1

    total = sum(sale_list)
    print()
    print(f'The total sales for the week are: $ {total:,.2f}')
    print()
    average = total / len(DAY)
    print(f'The average sales for the week are: $ {average:,.2f}')
    print()
    high_sales = max(sale_list)
    low_sales = min(sale_list)
    print(f"The lowest sales for the week are: $ {low_sales:,.2f} on {DAY[sale_list.index(low_sales)]}.")
    print(f"The highest sales for the week are: $ {high_sales:,.2f} on {DAY[sale_list.index(high_sales)]}.")



main()