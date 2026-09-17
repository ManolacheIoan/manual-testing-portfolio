class BugReport:
    def __init__(self, title, severity):
        self.title = title
        self.severity = severity
        self.status = "Open"

    def close(self):
        self.status = "Closed"

    def describe(self):
        print(f"{self.title} - Severity: {self.severity} - Status: {self.status}")


class TestCase:
    def __init__(self, name, expected_result):
        self.name = name
        self.expected_result = expected_result
        self.actual_result = None

    def run(self, actual):
        self.actual_result = actual

    def passed(self):
        return self.actual_result == self.expected_result


class TestSuite:
    def __init__(self, name):
        self.name = name
        self.test_cases = []

    def add_test(self, test_case):
        self.test_cases.append(test_case)

    def report(self):
        print(f"--- Suite: {self.name} ---")
        for tc in self.test_cases:
            result = "PASS" if tc.passed() else "FAIL"
            print(f"{tc.name}: {result}")


class APITestCase(TestCase):
    def __init__(self, name, expected_result, expected_status_code):
        super().__init__(name, expected_result)
        self.expected_status_code = expected_status_code
        self.actual_status_code = None

    def run(self, actual, status_code):
        super().run(actual)
        self.actual_status_code = status_code

    def passed(self):
        return super().passed() and self.actual_status_code == self.expected_status_code


if __name__ == "__main__":
    bug1 = BugReport("Login button broken", "High")
    bug1.describe()
    bug1.close()
    bug1.describe()

    tc1 = TestCase("Login test", "Success")
    tc1.run("Success")

    tc2 = TestCase("Login test 2", "Success")
    tc2.run("Failure")

    tc3 = TestCase("Signup test", "Account created")
    tc3.run("Account created")

    suite = TestSuite("Regression Suite")
    suite.add_test(tc1)
    suite.add_test(tc2)
    suite.add_test(tc3)
    suite.report()

    api1 = APITestCase("Get user profile", "Success", 200)
    api1.run("Success", 200)
    print(api1.passed())

    api2 = APITestCase("Get order details", "Success", 200)
    api2.run("Success", 404)
    print(api2.passed())