# learning-python

Learning Python by solving problems. Every topic is a set of small
functions to write, with tests already in place that say what each one
must do.

## How a topic works

1. Open the topic's `*_exercises.py` file and read the first docstring.
2. Read that function's tests in the `test_*_exercises.py` file beside it.
   The tests are the full requirement.
3. Replace `raise NotImplementedError` with your code.
4. Run the tests. Repeat until they pass, then move to the next function.
5. When the file is finished, ask Claude for a review.
6. Write a `notes.md` in the topic folder, in your own words.

Exercises run from easy to hard. The first one or two are warm-ups, and the
last is marked **(Stretch)**.

## Commands

| What | Command |
|---|---|
| Run one topic | `pytest topics/01-basics/05-strings` |
| Run one function's tests | `pytest topics/01-basics/05-strings -k truncate` |
| Run everything | `pytest` |
| See progress across all topics | `python progress.py` |
| Check style | `ruff check` |

## Layout

```
learning-python/
├── README.md            this file: the roadmap
├── CLAUDE.md            how Claude should behave here (tutor, not solver)
├── progress.py          shows tests passing per topic
├── topics/              the exercises, in learning order
│   ├── 01-basics/
│   ├── 02-fundamentals/
│   └── ...
├── developer-tips/      short guides on how engineers work day to day
└── challenges/          katas and projects that combine topics
```

## Roadmap

Sections are meant to be done in order, and so are the topics inside them.
Every topic below is **Ready**, with exercises waiting. A topic added later
starts as **Planned** until its exercises are written.

### 00. Reading errors (`topics/00-reading-errors/`)

Five fix-it exercises written like tickets from work. Each is a small, realistic
script with a mistake in it and tests that fail until you fix it. Some crash
with an error to read, and some quietly give the wrong answer. The goal is
working out where the problem is, using error messages, tests and the
debugger. [Start here](topics/00-reading-errors/README.md).

Three topics work a little differently from the rest. Their own files explain
how:

- **modules**: for the last two exercises you create a new file yourself.
- **testing-with-pytest**: the code is already written and you write the
  tests. A checker plants bugs in the code to see whether your tests notice.
- **type-annotations** (section 2): the stubs have no annotations, and adding
  them is the exercise.

### 1. Basics (`topics/01-basics/`)

The building blocks: values, and the statements that act on them.

| # | Topic | What it covers | Status |
|---|---|---|---|
| 01 | variables-and-syntax | assignment, expressions, return values, f-strings | Ready |
| 02 | operators | arithmetic, comparison, logic, `in`, `is` | Ready |
| 03 | conditionals | `if`/`elif`/`else`, guard clauses, `match` | Ready |
| 04 | loops | `for`, `while`, `range`, `break`, nested loops | Ready |
| 05 | strings | methods, slicing, formatting | Ready |
| 06 | integers | `//`, `%`, `divmod`, number bases | Ready |
| 07 | floats | rounding error, `Decimal`, NaN | Ready |
| 08 | booleans-and-none | truthiness, `is None`, `and`/`or` | Ready |

### 2. Fundamentals (`topics/02-fundamentals/`)

Collections, functions, and the tools you'll use in almost every program.

| # | Topic | What it covers | Status |
|---|---|---|---|
| 01 | lists | indexing, slicing, in-place changes | Ready |
| 02 | tuples | unpacking, `NamedTuple`, tuples as keys | Ready |
| 03 | sets | membership, set operations | Ready |
| 04 | dictionaries | counting, grouping, nested lookups | Ready |
| 05 | mutability | aliasing, copies, changing data safely | Ready |
| 06 | type-casting | converting between types, and when it fails | Ready |
| 07 | functions | defaults, `*args`, `**kwargs`, closures | Ready |
| 08 | builtin-functions | `sum`, `min`, `max`, `sorted`, `any`, `all`, `zip` | Ready |
| 09 | comprehensions-and-iteration | comprehensions, `enumerate`, `zip` | Ready |
| 10 | exceptions | `try`/`except`, raising, custom errors | Ready |
| 11 | type-annotations | annotating functions, `TypedDict`, generics | Ready |

### 3. Intermediate Python (`topics/03-intermediate/`)

Language features that make larger programs manageable.

| # | Topic | What it covers | Status |
|---|---|---|---|
| 01 | variable-scope | local, global, `nonlocal`, the LEGB rule | Ready |
| 02 | lambdas | small functions as arguments, `key=` | Ready |
| 03 | modules | imports, packages, `__name__` | Ready |
| 04 | error-handling | `finally`, context managers, retrying, error design | Ready |
| 05 | iterators-and-generators | the iterator protocol, `yield`, laziness | Ready |
| 06 | decorators | wrapping functions, `functools.wraps` | Ready |
| 07 | regular-expressions | the `re` module, groups, common patterns | Ready |
| 08 | files-and-pathlib | reading and writing files, CSV, JSON | Ready |
| 09 | testing-with-pytest | writing your own tests, fixtures, parametrize | Ready |
| 10 | logging | levels, handlers, logging instead of printing | Ready |

### 4. Object-oriented programming (`topics/04-oop/`)

| # | Topic | What it covers | Status |
|---|---|---|---|
| 01 | classes | `__init__`, attributes, instances | Ready |
| 02 | methods | instance, class and static methods, `__repr__`, `__eq__` | Ready |
| 03 | encapsulation | properties, private names, protecting state | Ready |
| 04 | inheritance | subclasses, `super()`, composition instead | Ready |

### 5. Data structures and algorithms (`topics/05-data-structures-and-algorithms/`)

Building the classic structures yourself, and learning what each costs.

| # | Topic | What it covers | Status |
|---|---|---|---|
| 01 | recursion | base cases, the call stack, when a loop is better | Ready |
| 02 | arrays-and-linked-lists | how lists store data, building a linked list | Ready |
| 03 | stacks-and-queues | LIFO and FIFO, `deque` | Ready |
| 04 | hash-maps | how dictionaries work, building one | Ready |
| 05 | heaps | priority queues, `heapq` | Ready |
| 06 | binary-search-trees | insert, search, traversal | Ready |
| 07 | sorting-algorithms | bubble, insertion, merge and quick sort, Big-O | Ready |

### Developer tips (`developer-tips/`)

Guides to read at any point. Each ends with things to try.

| # | Guide |
|---|---|
| 01 | [Trying out ideas quickly](developer-tips/01-trying-out-ideas.md): the REPL, scratch files, quick experiments |
| 02 | [PyCharm essentials](developer-tips/02-pycharm-essentials.md): the shortcuts worth learning first |
| 03 | [Debugging](developer-tips/03-debugging.md): tracebacks, printing well, the debugger |
| 04 | [Testing your code in a large codebase](developer-tips/04-testing-in-large-codebases.md): what to do when you can't just run main |
| 05 | [Comments and docstrings](developer-tips/05-comments-and-docstrings.md) |
| 06 | [Habits worth building](developer-tips/06-habits-worth-building.md): what senior engineers do without thinking |

### Challenges (`challenges/`)

Katas (short problems) and projects (multi-day builds where you decide the
design). Ask Claude for one whenever you want to put several topics
together. A good time is at the end of each section.

## Where the original topic list went

A few items moved from where they were first listed:

- **Data Structures & Algorithms** was split in two. Modules, lambdas,
  decorators, iterators, regular expressions, variable scope and error
  handling are Python language features, so they became section 3. The
  actual data structures and algorithms are section 5.
- **OOP comes before data structures.** Linked lists, stacks and trees are
  built from classes, so classes need to come first.
- **Strings, integers, floats and booleans** are in Basics, as the "data
  types" half of "Variables and Data Types".
- **Exceptions and Error Handling** overlap. Exceptions (section 2) covers
  catching and raising. Error handling (section 3) covers designing how a
  program deals with failure.
- **Comments** can't be tested with code, so it became a developer-tips
  guide.
- **Files, testing and logging** weren't on the list. They were added to
  section 3 because real programs need all three.
