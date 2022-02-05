import math


def get_pi_to_the_nth_digit(n):
    return str(math.pi)[0:2+n]


# Print the value of pi
print(get_pi_to_the_nth_digit(2))
print(get_pi_to_the_nth_digit(4))
print(get_pi_to_the_nth_digit(6))
print(get_pi_to_the_nth_digit(8))
