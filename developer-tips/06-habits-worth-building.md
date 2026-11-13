# Habits worth building

None of these are about Python. They're what experienced engineers do
without thinking, and what makes the biggest difference early on.

## Before you write code

**Read the requirement twice, then restate it.** Most wasted effort comes
from solving a slightly different problem from the one that was asked. In
this repo the docstring and the test names are the requirement.

**Work one example by hand.** If you can't get from the input to the output
on paper, you can't write the code yet. Working `format_row` through as a
table before writing anything is this habit.

**Ask what could be empty.** Before you call something finished, run
through this list in your head:

- nothing at all: `""`, `[]`, `{}`, `None`, `0`
- exactly one item
- duplicates
- negative numbers
- input that's already the answer (text that already fits, a list that's
  already sorted)
- whitespace that only looks empty: `"   "`

## While you write code

**Take small steps.** Write a little, run the tests, repeat. When something
breaks, the cause is in the last few lines you wrote. Fifty lines written
without running them could hide the bug anywhere.

**Make it work, then make it right.** Get the tests passing with the
plainest code you can. Then tidy it up while the tests stay green. Trying
to write the elegant version first is slower.

**Name things for what they are.** `word`, not `x`. `width`, not
`padding_size` when it holds a width. A misleading name is worse than a
vague one.

**Check each branch can be reached.** For every `if`, ask whether any input
actually gets there.

**Clean up after a change of plan.** When you switch approach, remove what
the old one left behind: unused imports, old variables, commented-out
attempts, debugging prints.

## Finding things out

**Don't guess. Run it.** A ten-second experiment in the REPL beats a
ten-minute argument with yourself.

**Read the error message.** All of it, slowly. It usually says what's
wrong, and where.

**Read the documentation for the thing you're using.** Finding `maxsplit`
came from reading about `split`. The official docs for a function take two
minutes and often show an option that removes half your code.

**Read other people's code.** Press `Ctrl+B` on a library function now and
then. You'll pick up idioms faster than from any tutorial.

## Working with others, and with your future self

**Commit small and often.** Each commit is a point you can go back to. A
good moment is every time the tests go green.

**Write for the reader.** Code is read far more often than it's written,
and the reader is usually you in three months, with no memory of today.

**Ask good questions.** Say what you were trying to do, what you expected,
what happened instead, and what you've already tried. Writing that down
solves the problem surprisingly often.

**Keep notes on your own mistakes.** The "Things I keep getting wrong" list
in `CLAUDE.md` is this habit. Senior engineers aren't people who never make
mistakes. They've made each one often enough to check for it first.

## Try it

1. Take the next exercise and write down, before coding, the inputs from
   the "could be empty" list that apply to it. Check which ones the tests
   cover.
2. On your next exercise, run the tests after every two or three lines you
   write, and notice how it changes where you look when one fails.
