from counter import Counter
print('олигополия')
counter = Counter()
counter.print()
counter.set_count_of_company(5)
counter.set_capital_of_company([1, 1, 2, 4, 7])

counter.print_count_of_company()
counter.print_of_capital()

counter.calculation()
counter.print_predict()
