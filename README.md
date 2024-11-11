# 📜 CommentBeGone

Do you have too many comments? Can’t see the forest for the comments? Or maybe your code is as chatty as that one friend who *always* leaves voice notes? Introducing **CommentBeGone** – the revolutionary Python package that puts your comments in their place: nowhere.

## Why CommentBeGone?

Let’s face it – comments are great, *until* they aren’t:
- **Too many “I’ll explain this later”** notes? Later is *now*.
- **Confusing inline comments**? Your `if` statements deserve a little peace and quiet.
- **Random comments in YAML files** that aren’t helping anyone? Say goodbye.

With CommentBeGone, your code can finally look as mysterious as you always wanted it to be!

## What It Does

CommentBeGone purges comments from your Python and YAML files so you can send cleaner code to your coworkers, or impress hiring managers with a mysterious sense of minimalism.

## Install

    pip install commentbegone

_Requires Python 3.8+. Will probably not work on ancient computers or quantum systems._

## Usage

Want to rid your file of those pesky comments? Just call CommentBeGone from the command line.

    commentbegone your_code.py no_more_comments.py

Or for YAML files:

    commentbegone configs.yaml clean_configs.yaml

*Poof!* Your comments are gone, and your file is ready for a quieter tomorrow.

## Advanced Example

Let’s say you have a file, `chatty_code.py`, with this noisy mess:

    # This function adds two numbers
    def add(a, b):
        return a + b  # Returns the sum of two numbers, obviously

Just run:

    commentbegone chatty_code.py silent_code.py

And in `silent_code.py` you’ll find:

    def add(a, b):
        return a + b

Pure, mysterious code – just like nature intended.

## How It Works

> "How does it know the difference between escaped and unescaped hashes?" –You

Good question! `CommentBeGone` uses regex sorcery to differentiate real comments from innocent hashes. We make sure those escaped `#` symbols in strings stay untouched. It’s a magical balance of regex and Python wizardry.

## Contributing

Found a way to silence even more comments? Or maybe you’ve written some code that needs **more** comments removed? Either way, submit a PR, open an issue, or shout into the void – we might hear you.

## License

MIT – use responsibly. (No, it won’t work on your boss’s emails.)

---

Enjoy a quieter codebase with **CommentBeGone** – because code is meant to be read... by the very brave.
