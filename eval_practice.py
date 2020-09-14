def get_total():
    x = 4
    y = 5
    z = 4 + 5
    return z

code = '=get_total()'
res = "res1"
exec(res+code)
print(eval(res))
