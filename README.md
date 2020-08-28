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

	To connect pythonanny to a project, this pattern must be used:
	
	
	```
	#main.py
	import nanny.py
	try:
		main()
	except Exception as e:
		nanny.nanny_log(e)
		raise
	```
	
	From there, just keep coding!  All errors that are thrown when running your main() method will get stored in pythonanny.log and continue to behave normally.  When you feel like you've hit a wall, or you feel ready to deep-dive into a topic you want a better understanding of, just navigate to the root directory of your project and run python nannytalk.py.
