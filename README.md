# Underscore Python Library
###### By Max Koon

The goal of this project is to decress the amount of code that you need to type and increase the speed at which the code is typed

_Similar to Jquery_

## Table of Contents
1. [Setup](#setup)
2. [Variables](#variables)
3. [File Functions](#file-functions)
4. [Rest Functions](#rest-functions)
5. [Other Functions](#miscellaneous-functions)
6. [Formatting Functions](#formatting-functions)
7. [Grade Functions](#grade-functions)
8. [Time Functions](#time-functions)
9. [Converting Functions](#convert-class)
10. [Math Functions](#math-functions)
11. [Parsing Functions](#parse-functions)
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
# Matches a grade number with text
_.grade_match[12]  # "Senior"
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

# Deletes the text between two string
_.delete_all_between(string, "here", "text")  # "<h1>Hello, heretext</h1>"

# Gets an age from a string 
_.get_age("3/29/2003")  # 15

# Returns the zodiac sign from a birthdate, can also return the emoji
_.get_zodiac("3/29/2004", return_emoji=False)  # "aries"
_.get_zodiac("3/29/2004", return_emoji=True)  # "♈"

# Returns grade level from a HS year of graduation
_.get_grade(2019, school_start_month=8, school_end_month=6)  # 12
# You can use this with the _.grade_match variable to get the text version of the grade
_.grade_match[_.get_grade(2019)]  # "Senior"

# Returns all the common characters from two strings
_.common(string, "Hello World")  # "Helloor"


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

### Grade Functions

```python
# Converts a letter grade to a gpa
_.grades.grade_to_gpa("A")  # 4

# Converts a grade (%) to a letter
_.grades.grade_to_letter(95)  # "A"
```

### Time Functions
```python
# Returns the current datetime obj
_.time.now()

# Turns a date string "mm/dd/YYYY" to a datetime obj
time1 = _.time.parse_date("06/26/2019")
time2 = _.time.parse_date("6/26/2016")

# Tests if two datetime objs are the same DAY, not year (good for birthdays)
_.time.same_day(time1, time2)  # True

# Tests if two datetime objs are the same date
_.time.same_date(time1, time2)  # False

# Tests if a datetime obj is the same DAY as today
_.time.is_today(time1)  # True

# Returns a natural day from a datetime obj
_.time.natural_day(time1)  # "today"
```

### Convert Class
#### Decimal
```python
# Converts decimal to binary
_.convert.decimal.binary(69) # '1000101'

# Converts decimal to hex
_.convert.decimal.hex(420)  # '1a4'

```
#### Hex
```python
# Converts hex to decimal
_.convert.hex.decimal(45)  # 69

# Converts hex to binary
_.convert.hex.binary('1a4')  # '110100100'
```

#### Binary
```python
# Converts binary to decimal
_.convert.binary.decinal('1000000')  # 64

# Converts binary to hex
_.convert.binary.hex('1000000')  # 40
```

### Math Functions
#### Point Functions
A point will be a tuple `(1,2)` 
```python
# Get the distance between two points
_.math.distance((1,2), (4,2))  # 3.0

# Get the slope of two points
_.math.slope((0,0), (1,2))  # 2.0

# Get the midpoint of two points
_.math.midpoint((1,2), (4,2))  # (2.5, 2.0)
```
#### Other Functions
```python
# Get a list factors of a number
_.math.factors(64)
# Gets the greatest common factor
_.math.gcf(64, 364)  # 4
```

### Parse Functions
#### Email
```python
email = _.parse.email("john@gmail.com")
print(email)  # "john@gmail.com"

email.username  # "john"
email.domain  # "gmail.com"
```
#### Address
This is US addresses only for the moment
```python
address = _.parse.address("15 Main Street, Millburn, NJ 07041")
print(address)  # "15 Main Street, Millburn, NJ 07041, USA"

address.number    # 15
address.street    # "Main Street"
address.locality  # "Millburn"
address.zip       # "07041"
address.sid       # "NJ"
address.state     # "New Jersey"
address.cid       # "USA"
address.country   # "United States of America"

# You can print the street format of the address with:
address.street_format  # "15 Main Street"

# This also works with PO boxes
address = _.parse.address("p.o. box 55 15 Main Street, Millburn, NJ 07041")
print(address)  # "P.O. Box 55 15 Main Street, Millburn, NJ 07041, USA"
address.po_box_number  # 55
```

### Validate Functions
#### Domain
```python
_.valid.domain("google.com")  # True
_.valid.domain("sdfsdhgfdcvbrt.com")  # False
```
#### Email
```python
_.valid.email("john@gmail.com", check_domain=False)  # True
_.valid.email("john@sdfsdhgfdcvbrt.com", check_domain=False)  # True
# If you set check_domain to true, it will see if the domain is valid
_.valid.email("john@sdfsdhgfdcvbrt.com", check_domain=True)  # False
```