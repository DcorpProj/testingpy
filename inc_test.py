import testingpy as tpy

def inc(n):
    return n + 1

test = tpy.TestingPy()
@test.test_function(except_error=True, name="inc error")
def inc_error():
    return inc("bob")

@test.test_function(expected=5, name="inc valid")
def inc_valid():
    return inc(4)

inc_error()
inc_valid()
test.show_tested()
test.exit_tested()
