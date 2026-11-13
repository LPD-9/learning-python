"""Your tests for testing_exercises.py. In this topic, you write this file.

Read each function's docstring in testing_exercises.py and treat it as the
requirement. Then write tests below, one exercise at a time.

1. add_vat: write your first tests with plain `assert`. Include a price
   where the rounding matters.
2. is_adult: test the boundary. Which ages sit right on the edge?
3. withdraw: test that errors are raised. Look up `pytest.raises`.
4. slugify: test many inputs with one test function. Look up
   `@pytest.mark.parametrize`.
5. Basket: several tests need a basket that already has items in it.
   Build it once in a fixture. Look up `@pytest.fixture`.
6. save_high_score: it needs a real file. pytest's built-in `tmp_path`
   fixture gives each test its own empty folder.
7. greeting (Stretch): the result depends on the clock, so a plain test
   would pass in the morning and fail at night. Replace current_hour
   with a fake for the length of one test. Look up pytest's
   `monkeypatch` fixture.

Run this folder's tests often. test_my_tests_catch_bugs.py tells you
which functions still have bugs your tests wouldn't notice.
"""
