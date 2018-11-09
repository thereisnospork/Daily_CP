# # cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
# #
# # Given this implementation of cons:
#
def cons(a, b):
    return lambda f: f(a, b)


#
# print(cons(1,2))
#
# a = cons(1,2)
# # print(a.__globals__)
# def car(func):
#     return lambda f : a * f(a,b)
#
# def cdr(func):
#     None
#
# print(car(a))


# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair

def car(f):
    def left(a, b):
        return a

    return f(left)


def cdr(f):
    def right(a, b):
        return b

    return f(right)


print(car(cons(3, 4)))
print(cdr(cons(3, 4)))

# looked up answer.  f in question definition is just the function defined as car
# - which when fed cons self-reference in cons definition
