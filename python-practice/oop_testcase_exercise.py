"""
Python OOP practice exercise: classes, objects, attributes, methods.
Two small classes modeling QA concepts (bug reports and test cases),
used to practice __init__, instance attributes, and methods that
read/mutate object state.
"""

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


if __name__ == "__main__":
    bug1 = BugReport("Login button broken", "High")
    bug1.describe()
    bug1.close()
    bug1.describe()

    tc1 = TestCase("Login test", "Success")
    tc1.run("Success")
    print(tc1.passed())

    tc2 = TestCase("Login test 2", "Success")
    tc2.run("Failure")
    print(tc2.passed())
