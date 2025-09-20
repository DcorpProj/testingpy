# TestingPy
Small framework for testing Python functions<br>
Example:
```python
import testingpy as tpy

test = tpy.TestingPy()
def sum(a, b):
    return a + b

@test.test_function(name="sum valid", expected=10)
def test_sum():
    return sum(5, 5)

test_sum()
```

What done:
 - basic testing
 - basic reports
Plans:
 - Add fixtures
 - Add CI/CD integration
 - Make report more informative