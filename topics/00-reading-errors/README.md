# 00 Reading errors

Fix-it exercises written like tickets from work. Each folder holds a small
program that somebody says is broken, a short ticket describing the symptom,
and unit tests that describe how it should behave. You find the mistake and
fix it in the script.

The skill being practised is working out *where* a problem is, not
understanding every line. You use three tools together:

- **Error messages.** Some of the scripts crash, and the traceback is your
  first clue.
- **Unit tests.** Some of the scripts crash and some quietly give the wrong
  answer. The tests describe the right behaviour, so they fail now. Which ones
  pass and which fail narrows down where to look.
- **Debugging.** Printing a value or setting a breakpoint settles an argument
  between you and the code.

| Exercise | Ticket |
|---|---|
| [01-sales-export](01-sales-export/README.md) | Monthly sales export is crashing |
| [02-month-end-report](02-month-end-report/README.md) | October total is lower than Finance's figure |
| [03-settings-loader](03-settings-loader/README.md) | Service won't start after the settings change |
| [04-config-overrides](04-config-overrides/README.md) | Debug mode is on in production |
| [05-log-summary](05-log-summary/README.md) | Daily log summary crashes |

## How to use an exercise

1. Read the ticket in the exercise's `README.md`.
2. Run the script. It may crash, or it may run and print something wrong.
3. Before you change anything, write one sentence saying what you think is
   wrong.
4. Run the tests, for example `pytest topics/00-reading-errors/01-sales-export`.
   Note which tests pass and which fail. The passing ones show what isn't
   broken.
5. Fix the mistake in the script, then run the tests again. Keep going until
   they all pass.

Don't edit the test files. They're the specification, so changing them to pass
would hide the mistake. Fixing one problem sometimes reveals another, so run
the real script once more at the end.

## The routine for reading an error

1. **Read the last line first.** The type (`NameError`, `KeyError`) says what
   kind of problem it is. The message gives the detail.
2. **Find the lowest line in the traceback that is in your file.** That's
   where Python stopped.
3. **Look at the values in the message.** Quoted names, and numbers such as
   `line 6 column 25`, are clues.
4. **If the message says one error caused another**, the first one listed is
   usually the real cause.
5. **Ask where the bad value came from.** Read upwards through the traceback
   to find the call that passed it in.
6. **Form a theory, then change one thing to test it.**

## When nothing crashes

If a script runs but prints the wrong answer, there's no traceback to read.
Work from the tests instead:

1. Find the smallest failing test.
2. Work out by hand what the right answer should be.
3. Find the first place where the code's value differs from yours, by printing
   it or stepping through with the debugger.
