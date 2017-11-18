from __future__ import division
from __future__ import print_function

import mxklabs as mxk

def find_divisor(logger, n):

    constraints = []

    # We're looking for ANY non-trivial divisor of n (with non-trivial we mean
    # that it can't be 1 or n). A divisor is an integer d such that there's no
    # remainder in the division n/d.
    #
    # Note that if d is a divisor of n then n/d is also a divisor of n because
    # n = d * n/d. From this it follows that either divisor d or n/d is an
    # integers in the interval [2,sqrt(n)]. This is because it can't be the case
    # that both d and n/d are strictly greater than sqrt(n) because this would
    # imply d * n/d is strictly greater than n (and hence not n).
    #
    # Suppose n is a number representable with N bits. The question we want to
    # answer next is: how many bits do we need to use to represent a divisor of
    # n such that if there is a divisor one of those divisors is representable
    # with this number of bits. It turns out CEIL(N/2) bits is sufficient.
    #
    # To see this number of bits is sufficient, recall that we only need to be
    # able to represent up to the largest integer that is smaller or equal to
    # sqrt(n). Also, clearly, with i bits, we can represent numbers up to 2^i-1.
    # Hence it must be that n <= 2^N-1. Now consider that:
    #
    #   sqrt(n) <= sqrt(2^N-1)
    #           <  sqrt(2^N)
    #           <= sqrt((2^(N/2))^2)
    #           <= 2^(N/2) .
    #
    # Assume for the moment that N is even (and hence CEIL(N/2)=N/2).Recall that
    # if a divisor of n exists then one exists that is smaller or equal to
    # sqrt(n) and, because of the inequality above, it is *strictly* smaller
    # 2^(N/2). As 2^(N/2) is an integer and a divisor is guaranteed to be
    # strictly less than this integer, it must be at most 2^(N/2)-1 and hence
    # can be represented with CEIL(N/2)=N/2 bits.
    #
    # For odd N we can't use N/2 bits as N is not divisible by 2. However,
    # CEIL(N/2) for odd N is (N+1)/2 and the following holds
    #
    #   sqrt(n) <  2^(N/2)                   (see above)
    #           <= 2^(N/2) * 2^(1/2) - 1     (only for N>=3)
    #           <= 2^(N/2 + 1/2)-1
    #           <= 2^((N+1)/2)-1 .
    #
    # Again, if a divisor of n exists then one exists that is smaller or equal
    # to sqrt(n) and, hence, strictly smaller than 2^((N+1)/2)-1). As a result,
    # it can be represented with CEIL(N/2)=(N+1)/2 bits.
    #
    # As a side note, note that one of the inequalities above only holds for
    # N>=3. However, we've checked CEIL(N/2) is sufficient for N<3 manually.

    # Work out bit length for n.
    N = n.bit_length()
    logger("N={}".format(N))

    # Work out bit length for divisor.
    DIVISOR_BIT_LENGTH = (N // 2) if (N % 2) == 0 else (N // 2) + 1
    logger("CEIL(N/2)={}".format(DIVISOR_BIT_LENGTH))

    n_ = mxk.Constant('uint%d' % N, n)
    divisor_ = mxk.Variable('uint%d' % DIVISOR_BIT_LENGTH, n)



    # We're done! We got all the constraints. Let's use a constraint solver
    # to find an assignment to variables under which all constraints hold.
    solver = mxk.TseitinConstraintSolver(logger=None)
    result = solver.solve(constraints)

    # See if the solver was able to find a satisfying assignment.
    if result == mxk.ConstraintSolver.RESULT_SAT:

        # Get the assignment of values to variables.
        assignment = solver.get_satisfying_assignment()


    elif result == mxk.ConstraintSolver.RESULT_UNSAT:
        logger("Unable to find a solution, sorry.")
    elif result == mxk.ConstraintSolver.RESULT_ERROR:
        logger("Something went wrong, sorry.")
    else:
        raise Exception("Unable to interpret result from solver")


def run_example(logger):
    """
    This example demonstrates how to factorise a 2048 bit number
    """
    #n = 22580116242535058188623517908541842633310092715854343846499796528769924223671807456607207419106621519588054730245966134358662000861657234814981687546213715297116993744190702405123601421779826894111197445944603613969124042229902202605182127458854328092374858429249966182880779471051954712334390750518196900438794893396809490213228123823764463452353363582030091984618564441824624833291389753934147982215735585974663924374055872463956337167613961791649759852314679564700205664568046040625039008367966025154382490947923562947778613745893443444809542921142924788398447884047063914104247152421812331793595144009461596199479
    n = 1234

    find_divisor(logger, n)

if __name__ == '__main__':
    run_example(logger=print)

import unittest


class Test_EinsteinsRiddle(unittest.TestCase):
    def test_example_solve_einsteins_riddle(self):
        logs = []
        logger = lambda msg: logs.append(msg)

        run_example(logger=logger)

        self.assertEqual(['Solution: Norwegian drinks the water, Japanese owns '
                          'the zebra!'], logs)