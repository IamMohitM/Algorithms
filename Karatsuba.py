import math


def karatsuba_multiplication(X, Y):
    print(X, Y)
    len_x = len(X)
    len_y = len(Y)
    if len_x <= 1 or len_y <= 1:
        return int(X) * int(Y)
    else:
        n_by_2 = math.floor(len_x / 2)
        print(f'n/2 --> {n_by_2}')
        if len_x % 2 == 1:
            power = len_x - 1
            a = X[:n_by_2 + 1]
            b = X[n_by_2 + 1:]
            c = Y[:n_by_2 + 1]
            d = Y[n_by_2 + 1:]
        else:
            power = len_x
            a = X[:n_by_2]
            b = X[n_by_2:]
            c = Y[:n_by_2]
            d = Y[n_by_2:]
        print(a, b, c, d)
        # input()
        return ((10 ** power) * karatsuba_multiplication(a, c)) + ((10 ** n_by_2) * (
                karatsuba_multiplication(a, d) + karatsuba_multiplication(b, c))) + (karatsuba_multiplication(b, d))


if __name__ == '__main__':
    # X = '3141592653589793238462643383279502884197169399375105820974944592'
    # Y = '2718281828459045235360287471352662497757247093699959574966967627'
    X = '1531'
    Y = '631'
    print(int(karatsuba_multiplication(X, Y)))
    print(int(X) * int(Y))
