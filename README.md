# Best Practices in Software Development

## General

- Tests
- Linters
- CI

> Code quality - <https://realpython.com/python-code-quality/>

## Tests

### Why test?

- **reduce bugs** in existing code
- **ensure bugs** that are fixed stay fixed
- **ensure new features** don't break old ones
- **ensure refactoring** doesn't introduce new bugs
- **ensure clean code** (e.g. no unused imports)
- **ensure code** is **readable** (e.g. no long functions)
- **ensure code** is **flexible** and **scalable** (e.g. no hard-coded values)
- **ensure code** is **extensible** (e.g. no tight coupling)
- **ensure code** is **performant** (e.g. no unnecessary loops)
- **ensure code** is **secure** (e.g. no SQL injections)
- **ensure code** is **accessible** (e.g. no missing alt text)
- **ensure code** is **usable** (e.g. no broken links)
- **ensure code** is **robust** and **monitored** (e.g. no unhandled exceptions)
- **ensure code** is **reliable** (e.g. no unhandled errors)
- **ensure code** is **portable** (e.g. no hard-coded paths)
- **ensure code** is **stable** (e.g. no memory leaks)
- **ensure code** is **consistent** (e.g. no inconsistent naming conventions)
- **ensure code** is **maintainable** (e.g. no duplicate code)
- **ensure code** is **testable** (e.g. no untestable code)
- **ensure code** is **documented** (e.g. no missing docstrings)
- **ensure code** is **deployable** (e.g. no missing requirements)
- **ensure code** is **version controlled** (e.g. no uncommitted changes)
- **ensure code** is **backed up** (e.g. no single point of failure)
- **ensure code** is **backwards compatible** (e.g. no breaking changes)
- **ensure code** is **forward compatible** (e.g. no deprecated functions)
- **ensure code** is **internationalized** (e.g. no hard-coded strings)

etc.

### What to test?

- **unit tests** - test individual units of code (e.g. functions)
- **integration tests** - test how multiple units work together
- **end-to-end tests** - test the entire application
- **regression tests** - test that new changes don't break old ones
- **smoke tests** - test the most important functionality of an application
- **sanity tests** - test that the application is sane
- **load tests** - test how the application behaves under load
- **stress tests** - test how the application behaves under stress
- **performance tests** - test the performance of the application
- **security tests** - test the security of the application
- **fuzz tests** - test the application with random data
- **mutation tests** - test the application with mutated data
- **usability tests** - test the usability of the application
- **accessibility tests** - test the accessibility of the application
- **compatibility tests** - test the compatibility of the application
- **reliability tests** - test the reliability of the application
- **robustness tests** - test the robustness of the application
- **edge case tests** - test the application with edge case data
- **negative tests** - test the application with negative data
- **positive tests** - test the application with positive data
- **manual tests** - test the application manually
- **automated tests** - test the application automatically
- **exploratory tests** - test the application without a plan
- **acceptance tests** - test the acceptance criteria of the application
- **system tests** - test the entire system
- **system integration tests** - test how multiple systems work together
- **user acceptance tests** - test the application with real users
- **user interface tests** - test the user interface of the application
- **user experience tests** - test the user experience of the application
- **visual regression tests** - test the visual appearance of the application

### Test plan

A test plan is a document describing the scope, approach, resources, and schedule of intended test activities. It identifies:

- parts of your application you want to test
- the order in which you want to test them
- the expected responses from your application

## Tests in Python

### Code coverage VS Test coverage

> <https://www.honeybadger.io/blog/code-test-coverage-python/>
>
> File(s): [tests.py](/tests.py), [main.py](/main.py), [.coverage](/.coverage)

For transition from code coverage to test coverage, see [this code diff](https://github.com/NdagiStanley/code-quality/commit/55a99f932b5be6c8d2ce1ec6553f2435fba460cd).

```bash
coverage run -m unittest discover
```

### Unit tests VS Integration tests

> <https://realpython.com/python-testing/>
>
> File(s): [test_sum.py](/test_sum.py)

- **integration testing** - Testing multiple components

  An integration test helps you to find bugs in the interaction between different components.

- **unit test** - Tests one component

  A unit test helps you to isolate what is broken in your application and fix it faster

### Further

[test_sum.py](/test_sum.py) has:

- **test case**
- **assertion**
- **entry point** (the command line)

```py
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")
```

> sum() accepts any iterable as its first argument, and an optional start parameter that defaults to 0.
>
> iterables - lists, tuples, sets, dictionaries, strings, and generators

An **AssertionError** is raised when a test fails. This is a subclass of **Exception**.

Such an assertion works best singly. To run more tests, enter **test runners**.

### Test runners

The **test runner** is a special application designed for running tests, checking the output, and giving you tools for debugging and diagnosing tests and applications.

- unittest - [test_sum_unittest.py](/test_sum_unittest.py)
- nose (now nose2)
  - extends unittest to make testing nicer and easier to understand
  - supports execution of `unittest` test cases
  - install `pip install nose2`
  - run `python -m nose2`
- pytest - [test_sum_pytest.py](/test_sum_pytest.py)
  - most popular
  - supports execution of `unittest` test cases
  - `pytest` test cases: functions in a Python file starting with the name test_
    - TestCase, any use of classes, dropped
    - command-line entry point, dropped

### Side effects

Tests should be **independent** from each other, maintain **state**, and only do one thing test (single responsibility).

Enter mocking.

#### Mocking

Fixtures

### Testing in Multiple Environments

`tox` - <https://tox.readthedocs.io/en/latest/>

## Linters

[ruff](https://astral.sh/ruff) is an all-in-one linter.

> See [pyproject.toml](pyproject.toml) for the configuration.

### Static Analysis

> <https://www.infoworld.com/article/3705568/a-gentle-introduction-to-static-code-analysis.html>
>
> <https://www.geeksforgeeks.org/types-of-static-analysis-methods/>

### *Flake8* Passive Linting

flake8 is a passive linter: it recommends changes, but you have to go and change the code

### *Black* Autoformatting

Black is an unforgiving formatter

- No configuration options
- Very specific style

### *Isort* Import Sorting

### *Bandit* Security Linting

### *Pydocstyle* Docstring Linting

### *Mypy* Static Type Checking

## Continuous Integration

- CircleCI
- GitHub actions
