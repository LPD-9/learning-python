# Debugging

Debugging is finding the first place where what the code does differs from
what you believe it does. Every technique here is a way of comparing those
two things.

## Read the error from the bottom

A Python traceback lists the calls that led to the error, oldest first.
Start at the bottom:

1. **The last line** names the error and says what went wrong.
2. **The lines just above it** show where it happened.
3. Work upwards until you reach a line of *your* code. That's usually the
   place to look, even when the error was raised inside Python itself.

pytest adds one more clue. On a failed `assert` it prints the value you
returned next to the value the test expected. Read that before anything
else.

## Predict, then look

Before you run anything, say what you expect to see. If you're right, the
bug is somewhere else. If you're wrong, you've found the misunderstanding.
Working out by hand why `"  ada lovelace ".split(" ")` gave three empty
strings was exactly this.

## Printing, done well

Printing is a perfectly good tool. Two things make it better:

```python
print(f"{words=}")   # prints  words=['ada', 'lovelace']
```

The `=` inside the braces prints the variable's name along with its value,
and shows strings with their quotes, so stray spaces become visible. Run
`pytest -s` to see print output from tests.

Remove the prints when you're done.

## The debugger

A debugger pauses your program on a line you choose and lets you look at
every variable, then run one line at a time. Reach for it when you'd
otherwise need more than two or three prints.

In PyCharm: click in the left margin to set a breakpoint, then click the
green arrow next to a test and choose Debug.

| Key | What it does |
|---|---|
| `F8` | Run this line and stop on the next one |
| `F7` | Step into the function this line calls |
| `Shift+F8` | Run to the end of this function and step back out |
| `F9` | Carry on to the next breakpoint |
| `Alt+F8` | Evaluate any expression using the current variables |

Outside an IDE, put `breakpoint()` on a line and run the program. Python
stops there and gives you a prompt.

## Useful pytest options

| Option | What it does |
|---|---|
| `-k initials` | Run only tests whose names contain "initials" |
| `-x` | Stop at the first failure |
| `--lf` | Run only the tests that failed last time |
| `-s` | Show print output |
| `-vv` | Show the full difference between two values |
| `--pdb` | Open the debugger at the point where a test fails |

## When you're stuck

- **Make the problem smaller.** Find the shortest input that still fails.
- **Change one thing at a time**, and re-run after each change.
- **Explain the code out loud**, line by line, to anyone or to nobody. Many
  bugs give themselves up halfway through the explanation.
- **Check your assumptions.** The bug is often in the line you're sure is
  fine.
- **Set a time limit.** After 20 to 30 minutes with no progress, ask for a
  hint and say what you've tried.

## Try it

1. Add `print(f"{text=}")` to a finished exercise and run its tests with
   `pytest -s`.
2. Set a breakpoint inside a loop in one of your solutions, debug a test,
   and press `F8` to watch the variables change on each pass.
3. Break a finished solution on purpose, then run `pytest -x --lf` twice
   and see which tests run each time.
