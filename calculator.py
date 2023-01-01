print("""Supported signs:+, -, /, *
use 'exit' to exit""")
try:
    str = ''
    while str != 'exit'.upper() and str != 'exit'.capitalize():
        str = input('calculate: ')
        if '+' in str:
            out_put = str.split('+')
            print(f"Ans: {int(out_put[0]) + int(out_put[1])}")
        elif '-' in str:
            out_put = str.split('-')
            print(f"Ans: {int(out_put[0]) - int(out_put[1])}")
        elif '*' in str:
            out_put = str.split('*')
            print(f"Ans: {int(out_put[0]) * int(out_put[1])}")
        elif '/' in str:
            out_put = str.split('/')
            print(f"Ans: {int(out_put[0]) / int(out_put[1])}")
        elif 'exit' in str:
            break
        else:
            print(f"Ans: 0")
except (ValueError) as e:
    print(f'Error: {e}')