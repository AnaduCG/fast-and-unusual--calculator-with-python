print("""Supported signs:+, -, /, *
use 'end' OR to exit""")
try:
    str = ''
    while str != 'end'.upper() and str != 'end'.capitalize():
        str = input('calculate: ')
        if '+' in str:
            out_put = str.split('+')
            print(int(out_put[0]) + int(out_put[1]))
        elif '-' in str:
            out_put = str.split('-')
            print(int(out_put[0]) - int(out_put[1]))
        elif '*' in str:
            out_put = str.split('*')
            print(int(out_put[0]) * int(out_put[1]))
        elif '/' in str:
            out_put = str.split('/')
            print(int(out_put[0]) / int(out_put[1]))
        elif 'end' in str:
            break
        else:
            print(f"ans: 0")
except (ValueError) as e:
    print(f'Error: {e}')