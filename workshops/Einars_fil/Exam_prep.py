def main():
    a = 10
    print(func(func(a)))
def func(x):
    x = x * 2
    return x
main()