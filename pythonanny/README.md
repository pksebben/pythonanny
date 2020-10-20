# Pythonanny

	Like hootenanny, but with snakes.
	
	Pythonanny is here to guide a leet-hacker-in-training with a gentle hand, and suggest reading material that might help their creations sparkle more and crash less.  Pythonanny will watch your error reports, and periodically (or when called upon) offer resources or recommendations for what to learn next.
	
	Pythonanny is _not_:
	
		- A static analysis tool
		- An effective solution for error logging
		- Built for production
		- Turing complete
		- Your mother (have you called her lately?)
		
# Usage

	To get started with Pythonanny, simply run:
	
	```bash
	python3 setup.py --user
	```
	
	the ``` --user ``` ensures that pythonanny gets into your user-specific site-packages directory, which is where it needs to be to attach to your coding environment.
	
	That's it! Pythonanny is now saving all uncaught exceptions for later review, in a file called nanny.log.  Located by default in your Documents folder.
