# Trying out ideas quickly

Experienced developers rarely guess what a piece of code does. They run a
tiny experiment and look. The skill is knowing the quickest place to run it.

## Which tool to use

| You want to... | Use | How |
|---|---|---|
| Check what one expression gives | The REPL | Type `python` in a terminal |
| Poke at functions you've already written | The REPL, with your file loaded | `python -i strings_exercises.py` |
| Try a few lines without touching your project | A scratch file | `Ctrl+Alt+Shift+Insert` in PyCharm |
| Run part of the file you're editing | PyCharm's Python Console | Select the code, press `Alt+Shift+E` |
| Keep the experiment as a permanent check | A test | Add a test to the test file |

## The REPL

REPL stands for read, evaluate, print, loop. You type an expression, Python
prints its value, and you go again. It's the fastest way to answer "what
does this do?"

```python
>>> "a  b".split(" ")
['a', '', 'b']
>>> _            # the last result
['a', '', 'b']
>>> help(str.split)   # read the documentation without leaving the terminal
>>> dir(str)          # list everything a string can do
```

Press `Ctrl+Z` then `Enter` to leave it on Windows.

`python -i your_file.py` runs the file first, then drops you into the REPL
with all its functions loaded. That replaces a temporary
`if __name__ == "__main__":` block: nothing to add, and nothing to remember
to delete.

## Scratch files

A scratch file is a throwaway Python file that PyCharm keeps outside your
project. It can't be committed by accident and it doesn't clutter your
folders. You'll find your scratch files under "Scratches and Consoles" at
the bottom of the Project panel.

Use one when an experiment needs more than a couple of lines, such as
trying three ways of writing a loop and comparing them.

## A test as an experiment

When you find yourself running the same experiment twice, turn it into a
test. A test is an experiment that records the answer you expect and
re-checks it for you every time. You did this when you added the
whitespace-only test for `initials`.

## Try it

1. Open the REPL and find out what `"Hello"[10:]` gives. Does it raise an
   error? Now try `"Hello"[10]`.
2. Run `python -i` on one of your exercise files and call a function you've
   finished with a new input.
3. Create a scratch file in PyCharm. Write a loop that prints `"-" * n` for
   `n` from 1 to 5, then run it.
