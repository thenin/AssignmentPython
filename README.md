# AssignmentPython

Write a simple test framework that corresponds the following requirements:

1. There is a test runner that finds test modules located under ./test folder. Runner is placed to a repository with tests to root folder. Test folder should be also placed to root of the project. (advanced level)

2. Implement handlers that will identify before and after methods in test modules to be executed before test run. (advanced level)

3. Implement a verifiers.py module that will provide the following assertions for tests:

   - verify_equals(actual, expected) - compares 2 values and expects them to be equal. If they are not equal, throw an exception.

   - verify_type(value, expected_type) - checks the type of given value and throws an exception when type is incorrect. 

   - verify_not_equals(actual, expected) - compares 2 values and expects them to not be equal. If they are equal, throw an exception.

   - verify_returns - should take verified method object, verified method parameters (if any) as and expected return value as parameters and check whether given method returns expected value. If not, throw an exception.

   

   usage example: 

   

       def test_one:

           verify_type(1, "int") //will not throw

           verify_equals(1, 0) // will throw an exception

     

4. Write a simple test that shows the above requirements are satisfied.