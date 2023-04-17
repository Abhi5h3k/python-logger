# 🔥 Python Logging Utility 🔥  

[![Abhishek LinkedIn](https://img.shields.io/badge/Abhishek-LinkedIn-blue.svg?style=for-the-badge)](https://www.linkedin.com/in/abhi5h3k/) [![Abhishek StackOverflow](https://img.shields.io/badge/Abhishek-StackOverflow-orange.svg?style=for-the-badge)](https://stackoverflow.com/users/6870223/abhi?tab=profile)

This is a Python logging utility that logs Error, Info, and Debug logs to a file, and automatically deletes log files older than 7 days. It also logs unhandled exceptions.

## Usage
To use this logging utility, follow these steps:
1. Clone this repository or download the logger.py file.
2. Import the log object into your Python file using ```from logger import log```
3. Start logging messages using any of the following methods:
```
log.debug('Debug message')
log.info('Info message')
log.error('Error message')
```
## Example
Here's an example usage of this logging utility in a file called example.py:

```
from logger import log

def some_function():
    # some code
    log.info("This is an info message.")
    # some more code

if __name__ == '__main__':
    some_function()

```

When you run this file, it will create a log file in the **logs** directory with a name like **2023-04-18.log**. It will log any info messages to this file, and automatically delete any log files older than 7 days.

## Contributions
Contributions to this logging utility are welcome! If you find a bug or want to suggest a feature, please open an issue or submit a pull request.

## Authors

* **Abhishek Bhardwaj** - *Stackoverflow profile* - [Stackoverflow profile](https://stackoverflow.com/users/6870223/abhi?tab=profile)
			  *Linkedin profile* - [Linkedin profile](https://www.linkedin.com/in/abhishek-bhardwaj-b16764166)

## License

This project is opensource, Kindly maintain the proper credits for author and contributers.
