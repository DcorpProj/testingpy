print("========= testingpy session =========")

class TestingPy:
    tested = {}
    @staticmethod
    def __init__():
        TestingPy.tested = {}
    @staticmethod
    def test_function(name, expected=None, except_error=False):
        # Первая функция принимает параметры декоратора
        def decorator(func):
            # Вторая функция - собственно декоратор
            def wrapper(*args, **kwargs):
                print("=====================")
                if expected == None and except_error:
                    print("expect_error overrides excepted")
                print(f" -- testing {name}")
                try:
                    result = func(*args, **kwargs)
                except Exception as e:
                    print(f"----- {name} | exception -----")
                    print(f"  error: {e}")
                    if except_error:
                        TestingPy.tested[name] = "success"
                    else:
                        TestingPy.tested[name] = "failure"
                    return e
                if except_error:
                    print("  error excepted")
                    TestingPy.tested[name] = "failure"
                    return result
                if result != expected:
                    TestingPy.tested[name] = "failure"
                    print(f"----- {name} | failure -----")
                    print(f"  expected {expected}, got {result}")
                else:
                    TestingPy.tested[name] = "success"
                    print(f"----- {name} | success -----")
                return result
            return wrapper
        return decorator
    @staticmethod
    def show_tested():
        all_passed = True
        not_passed = 0
        for n in TestingPy.tested:
            print(f"{n.ljust(20)} {TestingPy.tested[n]}")
            if TestingPy.tested[n] == "failure":
                all_passed = False
                not_passed += 1
        print("All tests passed" if all_passed else f"{not_passed} tests not passed.")
    @staticmethod
    def exit_tested():
        exit(0 if all(TestingPy.tested.get(name) == "success" for name in TestingPy.tested) else 1)
