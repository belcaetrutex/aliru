def print_pyramid(n, current_row=1):
    for i in range(1, current_row + 1):
        print(' ' * (n - i) + '*' * i)
