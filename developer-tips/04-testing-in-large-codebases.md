# Testing your code in a large codebase

In a real project you usually can't "just run main". The program might need
a database, a login, ten minutes to start, and five clicks to reach the
code you changed. So developers don't test changes by running the whole
thing. They run the smallest piece that contains the change.

## Run the piece, not the program

Your change lives in a function or a class. A test can call that function
directly with whatever inputs you choose, in a fraction of a second. This
repo works the same way: you've never run a "main" here, only functions
through their tests.

In a large project you run one test, not all ten thousand:

```bash
pytest tests/test_orders.py::TestDiscounts::test_expired_code
```

That's the path to the file, then the class, then the test. `pytest -k
expired` does the same job by name.

## Why code is written in small functions

Code is easy to test when it takes values in and returns values out, and
hard to test when it reads files, calls the network or asks the clock.
Experienced developers split the two apart:

- a small **outer layer** that reads the file or calls the API
- a **core** of plain functions that take data and return data

The core holds the logic and gets most of the tests. Every exercise in this
repo is "core" code, which is why they're easy to test.

## Standing in for the awkward parts

When code has to touch something slow or external, tests swap in a
stand-in:

| Awkward thing | Stand-in | pytest tool |
|---|---|---|
| Files on disk | A temporary folder, deleted afterwards | `tmp_path` |
| Environment variables, settings | Temporary values for one test | `monkeypatch` |
| A database or web API | A fake object that returns canned answers | `unittest.mock` |
| The same setup in many tests | A reusable piece of setup | fixtures |

You'll use these in the testing topic. For now, know that they exist and
what problem each one solves.

## The usual routine for a bug fix

1. **Reproduce it in a test.** Write a test that fails because of the bug.
   Now you can trigger it in a second, as often as you like.
2. **Fix the code** until that test passes.
3. **Run the tests around it** to check you haven't broken anything nearby.
4. **Leave the new test in.** It stops the bug coming back.

You did this with `initials("   ")`: the test came first, then the fix.

## Other ways to see code run

- **Debug a test.** Set a breakpoint in the code you changed and debug a
  test that reaches it. You get to inspect real values without starting the
  application.
- **Import it in the REPL.** `from orders.discounts import apply_code`, then
  call it by hand.
- **Read the existing tests.** They show how the code is meant to be called,
  and they make good templates for your own test.
- **Find usages** (`Alt+F7`) to see who calls the function you're changing.
- **Logs.** When code only misbehaves in the running system, log messages
  are how you see what it did. That's what the logging topic is for.

Beyond your own machine, teams lean on automated checks that run every test
on each change (called CI), and on a staging environment, which is a copy of
the real system that is safe to break.

## Try it

1. Run a single test in this repo by its full path, class and name.
2. Pick a finished exercise. Without looking at your solution, read only its
   tests and write down what the function must do. How complete is the
   picture?
3. Add a new test for an input the current tests don't cover, then check
   whether your solution handles it.
