# Pythonanny

	Pythonanny is a simple set of scripts that save all your uncaught exceptions (in Python) in a log for reflection and reference.  The intent is that with a few tools for reflecting on this data, the novice hacker can get a sense of where the largest gaps in their knowledge lie, so they can focus on learning those first.  This is a tool made specifically with the beginner in mind, and aims to fill the gap between those beginner and intermediate stages when tailored advice is necessary, but difficult to come by.
	
# Installation

Simply run

```sh
python3 setup.py install --user
```

and pythonanny will install a script in your site-packages that attaches to any python interpreter run in your userspace.  'nanny.log' should show up in your /Documents folder, and will be appended any time you throw an uncaught exception.

# Usage

In it's current form, all that nanny does is save your uncaught exceptions for future reflection.  The next batch of updates will contain some tools that will make that simple and worthwhile for the novice hacker.
