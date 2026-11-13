# Comments and docstrings

Code says *what* happens. Comments are for what the code can't say: *why*
it's done this way.

## Comments

A comment that repeats the code adds nothing, and it turns into a lie the
day someone changes the code and forgets the comment.

```python
# Bad: says what the code already says
count += 1  # add one to count

# Good: says why
count += 1  # the header row isn't in the list, so line numbers start at 2
```

Good reasons to write a comment:

- A decision that looks wrong but isn't ("sorted twice on purpose: the
  first sort breaks ties").
- A constraint the reader can't see ("the API rejects more than 100 items
  per call").
- A link to where a rule comes from.

Before writing a comment that explains what a line does, try a better name
instead. `seconds_per_day = 86400` needs no comment. `x = 86400` does.

## Docstrings

A docstring is the string on the first line of a function, class or module.
It describes how to *use* the thing: what goes in, what comes out, and
anything surprising. Comments are for people changing the code. Docstrings
are for people calling it.

Tools read docstrings. `help(function)` prints one, and `Ctrl+Q` in PyCharm
shows it.

```python
def truncate(text: str, max_length: int) -> str:
    """Shorten text to at most max_length characters, ending in "...".

    If text already fits, return it unchanged.
    """
```

The first line is a one-sentence summary. More detail goes after a blank
line. A short, obvious function needs only the first line.

The `>>>` examples in this repo's docstrings are called doctests, and
Python can run them:

```bash
pytest --doctest-modules topics/01-basics/05-strings
```

## Code that's been commented out

Delete it. Old attempts left in comments make readers wonder whether they
still matter. Once the repo is under git, every old version is kept in the
history, so nothing is lost.

## TODO comments

`# TODO: handle negative amounts` is a fine note to yourself while you
work. Clear them before you call the work finished, or they pile up and
nobody trusts them. PyCharm lists them all in its TODO panel.

## Try it

1. Look through your finished exercises for a comment that only repeats the
   code. Delete it, or replace it with a better variable name.
2. Run the doctests for a topic you've finished.
3. Call `help()` on one of your own functions in the REPL.
