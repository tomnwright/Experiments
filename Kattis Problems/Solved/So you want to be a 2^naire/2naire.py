# import random
#
#
# def random_float(minimum, maximum, decimal_places):
#     res = 10 ** decimal_places
#
#     lower = int(minimum * res)
#     upper = int(maximum * res)
#
#     return random.randint(lower, upper) / res
#
#
# t = 0.3
# n = 24
#
#
# def prob_t():
#     global t
#     return random_float(t, 1, 10)
#
#
# def prob_01():
#     return random_float(0, 1, 10)
#
#
# def do_test(n):
#     for k in range(n):
#
#         p = prob_t()
#
#         if p < 0.5:
#             return pow(2, k)
#         else:
#             event = prob_01()
#
#             if event > p:
#                 return 0
#     return pow(2, n)
#
#
# total = 0.2
# tests = 24
#
# for i in range(tests):
#     total += do_test(n)
#
# print(total / tests)

# def expectedold(n, t):
#     a = clamp01(0.5 / (1 - t))
#     q = 1 - a
#     r = (max(0.5, t) + 1) / 2
#
#     print(r)
#
#     prev_expectation = pow(2, n)
#
#     for i in range(n):
#         k = n - i  # kth question
#
#         prev_expectation = a * r * prev_expectation + q * pow(2, k - 1)
#
#     return prev_expectation


def clamp01(x):
    if x < 0:
        return 0
    if x > 1:
        return 1
    return x


def expected_prize(n, t):
    """
    https://open.kattis.com/problems/2naire
    -Player starts with $1; asked questions.
    -Before answering each, the player is told
    the probability, p, of them answering correctly
    -p is random uniform random variable between t and 1
    -The player can either quit and keep the money
    or answer the question
    -If they answer correct, they double their money
    and continue
    -If they answer incorrectly, they lose everything
    -After n questions, the game ends and the player
    keeps the money

    Calculates the maximum expected prize assuming the
    player employs the best possible strategy
    :param n: Total number of questions
    :param t: Lower bound for p (t<=p<=1)
    :return: Maximum expected prize
    """

    # Strategy: for each question, answer or quit
    #   based on which has the higher expected prize
    # Function tracks back from nth question
    # End prize is only known correct expected prize (2^n)

    # expected prize of following (k+1)th question
    e_next = pow(2, n)  # starts at max prize, 2^n

    for i in range(n):
        # kth question
        k = n - i

        e_q = pow(2, k - 1)  # expected quit prize (prize from prev question, k-1)
        m = e_q / e_next  # lower bound for p (p > m) such that e_a > e_q

        e_p = (1 + max(m, t)) / 2  # expected value for success prob p (over many similar games)
        e_a = e_next * e_p  # expected prize for answering, give expected probability

        a = clamp01((1 - m) / (1 - t))  # probability that answering is favourable
        q = 1 - a  # probability that quitting is favourable

        e_k = a * e_a + q * e_q  # overall max expected prize for kth question
        e_next = e_k  # set e_next for next question (moving backwards, to k-1)

    # finally, e_next becomes expected prize for Question 1, ie. overall expected prize
    return e_next


def format_expected(n, t):
    """
    Wrapper for expected_prize(n, t).
    Executes expected_prize and formats to 3 decimal places.
    """
    result = round(expected_prize(n, t), 3)
    return "{:.3f}".format(result)



if __name__ == '__main__':

    import sys

    for line in sys.stdin:
        stripped = line.strip()

        if stripped == "0 0":
            break

        split = stripped.split(" ")
        _n = int(split[0])
        _t = float(split[1])

        print(format_expected(_n, _t))
