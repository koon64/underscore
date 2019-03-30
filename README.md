# Underscore Python Library
###### By Max Koon

The goal of this project is to decress the amount of code that you need to type and increase the speed at which the code is typed

_Similar to Jquery_

## Setup

```python
from unders import Underscore
_ = Underscore()
```
That was pretty easy, so now lets look at the
## Functionality
### Variables
```python
# Number of seconds in an hour
_.his                 # 3600
# Number of seconds in a day
_.dis                 # 86400
# Number of seconds in a month
_.mis                 # 2635200
# Number of seconds in a year
_.yis                 # 31536000
```
### File functions

```python
string = "Some text"
file_path = "file.txt"

# If file exists from a path string
print(_.file_exists(file_path))  # False

# writes a string to a file
_.sf(string, file_path)

# Gets the content of a file
content = _.fs(file_path)
print(content)  #  "Some text"

obj = {
    "foo": "bar",
    "arr": [
        "ay"
    ]
}
new_file_path = "file.json"

# writes the object to a json file
_.aj(obj, new_file_path)

# gets the contents of a json file and converts it into an obj
json = _.ja(new_file_path)
print(json)  # { 'foo': 'bar', 'arr': [ 'ay' ] }

```

### Rest Functions
These are some simple functions for interacting with RESTful APIs
```python
json = _.ra('http://history.muffinlabs.com/date')
print(json)  # the response in an obj {...}
```
You can also get content as a raw string with...
```python
string = _.rs('https://www.google.com')
print(string)  # the html of google
```

### Miscellaneous Functions

```python
# Returns a letter from the alphabet from its place
# 2nd Param makes it capital
_.assign_letter(0)  # "a"
_.assign_letter(26, True)  # "Z"

string = "<h1>Hello, here is some text</h1>"
# Removes html tags
_.strip_tags(string)  # Hello, here is some text

# Gets text between two strings
_.between(string, "here", "text")  # " is some "

# Removes the text between two string
_.remove_all_between(string, "here", "text")  # "<h1>Hello, heretext</h1>"

# Gets an age from a string 
_.get_age("3/29/2003")  # 15

```

### Formatting Functions

```python
# Formats a phone number
_.format.phone(8001234567)  # "+1 (800) 123-4567"

# Formats Bytes
_.format.bytes(12288)  # "12 KB"

# Adds commas to a number
_.format.number(12345678)  # "12,345,678"

# Returns a string with a number and the plural word after the amount
_.format.plural(5, "dog")  # "5 dogs"
_.format.plural(1, "tree")  # "1 tree"
# Some special cases built in
_.format.plural(6, "person")  # "6 people"

# Formats seconds into time units
_.format.time(3600)  # "1h"
_.format.time(360000)  # "4d"
_.format.time(3600000)  # "1mo"
# Full text
_.format.time(3600, True)  # "1 hour"

# Formats the ending text of a number (ordinal)
_.format.ordinal(1)  # "1st"
_.format.ordinal(203)  # "203rd"

# Returns a possession string based on the items name
_.format.possession("Max")  # "Max's"
_.format.possession("Alexis")  # "Alexis'"
```

