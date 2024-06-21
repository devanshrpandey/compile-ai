An AI-first compiler for Python code, written in Python.

This compiler directly translates your Python code into C code, by:

- taking the code
- asking Claude to turn it to C
- compiling and running the code
- asking Claude nicely to fix any mistakes!

Claude is Turing-complete (citation needed), so there should be no issue whatsoever compiling Python to C for any input perfectly and flawlessly. We of course bear no responsibility if Claude decides to run the equivalent of `rm -rf /`.

Usage:
Set Anthropic API key as an environment variable:

- `ANTHROPIC_API_KEY`

Then run the compiler with the path to the file you want to compile:
```
python main.py <path_to_file>
```
Optional flags:
- `-O{x} (0 < x < 3)`: Default O0. Specify the number of optimization levels to use. By "optimization level" we mean "the number of times we ask Claude to make the code faster."
- `--model`: Defaults to Sonnet-3.5. Specify any valid Anthropic model tag, or "opus", "sonnet", "haiku". We strongly recommend using Sonnet 3.5 at this time.
- `--debug`: Defaults to False. Prints the C code and text of error messages if any come up.
- `--use-cache`: Defaults to True. If True, the compiler will check if there's a cached version of the runfile and use that if it exists. If False, it will always run Claude to generate the C code and compile / run it.


Usage:
```
git clone compile-ai
cd compile-ai
sudo mv compile-ai /usr/local/bin/ 
pip install anthropic
speedpy <options> <path_to_file>
```

To test:
```
speedpy sieve_of_erathosenes.py
speedpy two_sum.py
```