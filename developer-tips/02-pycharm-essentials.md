# PyCharm essentials

An IDE earns its keep by answering questions about code faster than you
could by reading. These are the features worth learning first. The
shortcuts are PyCharm's Windows defaults. Menus move a little between
versions, so if a shortcut does nothing, press `Shift` twice and type the
action's name.

## Finding your way around

| Shortcut | What it does | When to use it |
|---|---|---|
| `Shift` twice | Search everywhere | Open any file, function or setting by name |
| `Ctrl+B` (or `Ctrl`+click) | Go to definition | "What does this function actually do?" |
| `Alt+F7` | Find usages | "Who calls this? What breaks if I change it?" |
| `Ctrl+E` | Recent files | Jump back to where you just were |
| `Ctrl+Shift+F` | Find in files | Search the whole project for some text |
| `Ctrl+Q` | Quick documentation | Read a function's docstring where you stand |
| `Ctrl+P` | Parameter info | See which arguments a function takes |

`Ctrl+B` works on Python's own functions too. Reading how the standard
library does something is a good way to learn.

## Changing code safely

| Shortcut | What it does |
|---|---|
| `Shift+F6` | Rename a variable or function everywhere it's used |
| `Ctrl+Alt+V` | Pull the selected expression out into a named variable |
| `Ctrl+Alt+M` | Pull the selected lines out into a new function |
| `Alt+Enter` | Show quick fixes for the warning under the cursor |
| `Ctrl+Alt+L` | Reformat the file |

Use rename instead of find-and-replace. It understands the code, so
renaming `x` won't also change the `x` inside `text`.

**Local History** is your safety net when you haven't committed. Right-click
a file, choose Local History, then Show History. PyCharm keeps every saved
version, so you can get back code you deleted an hour ago.

## Running and debugging

| Shortcut | What it does |
|---|---|
| Green arrow in the left margin | Run that one test or test class |
| `Ctrl+Shift+F10` | Run whatever the cursor is in |
| `Shift+F9` | Debug the last thing you ran |
| `Ctrl+F8` | Add or remove a breakpoint on this line |

If the green arrows don't appear next to your tests, go to Settings, then
Tools, then Python Integrated Tools, and set the default test runner to
pytest.

The debugger has its own guide: see [03-debugging.md](03-debugging.md).

## Try it

1. Put the cursor on `split` in one of your solutions and press `Ctrl+Q`.
   Then press `Ctrl+B` to see where it's defined.
2. Use `Shift+F6` to rename a loop variable in a finished exercise, then
   run its tests.
3. Delete a line from a file, save, and bring it back with Local History.
