import os
import json
import urllib3
from datetime import datetime
from math import log, floor, sqrt
from re import sub, match
from socket import gethostbyname, error
from pprint import pprint

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Underscore:
    """This is the main class for Underscore"""

    def __init__(self):
        # vars
        self.underscore_version = "1.0.2"
        self.his = (1 * 60 * 60)  # hour in seconds
        self.dis = (1 * 60 * 60 * 24)  # day in seconds
        self.mis = (30.5 * 24 * 60 * 60)  # month in seconds
        self.yis = (365 * 24 * 60 * 60)  # year in seconds
        # sub classes
        self.format = FormatClass(self)
        self.grades = GradesClass()
        self.time = TimeClass(self)
        self.convert = ConvertClass()
        self.math = MathClass()
        self.valid = ValidClass()
        self.parse = ParseClass(self)

    # File functions

    # updates the underscore version
    def update(self):
        consent = input("Would you like to download the latest version of underscore? (Y or N)")
        consent = consent.lower()
        if consent == "y" or consent == "yes":
            newest_version = self.rs("https://raw.githubusercontent.com/koon64/underscore/master/unders.py")
            self.sf(newest_version, "unders.py")
            return True
        print("canceling update")
        return False

    def print(self, obj):
        pprint(obj)

    # returns a string from a file's content
    def fs(self, file_path):
        if type(file_path) is str:
            if self.file_exists(file_path):
                with open(file_path, 'r') as file:
                    return file.read()
            else:
                raise Exception('"' + file_path + '" does not exist')
        else:
            raise Exception('the file path must be a string')

    # returns an array from a json file
    def ja(self, file_path):
        json_string = self.fs(file_path)
        try:
            return json.loads(json_string)
        except json.JSONDecodeError as e:
            print(e)

    # writes a string to a file
    def sf(self, string, file):
        try:
            with open(file, "w") as file:
                file.write(string)
                file.close()
                return True
        except Exception as e:
            print(e)
            return False

    # writes an object to a file
    def aj(self, obj, file):
        string = json.dumps(obj)
        return self.sf(string, file)

    # returns a string from the contents of a url
    def rs(self, url):
        http = urllib3.PoolManager()
        response = http.request('GET', url)
        return str(response.data, "utf-8")

    # returns an obj from a rest url
    def ra(self, url):
        response = self.rs(url)
        return json.loads(response)

    # if a file exists or not
    def file_exists(self, file_path):
        return os.path.isfile(file_path)

    # Other functions
    # Formatting mostly    

    # converts a number to a letter, ex: 0 => a, 3 => d
    def assign_letter(self, numb, capital=False):
        letter = chr(numb + 97)
        if capital:
            letter = letter.capitalize()
        return letter

    # removes html tags
    def strip_tags(self, html):
        return sub('<[^<]+?>', '', html)

    # gets the text between
    def between(self, string, beginning, end):
        beginning_position = string.find(beginning)
        end_position = string.find(end)
        if beginning_position == -1 or end_position == -1:
            return string
        return string[(beginning_position+len(beginning)):end_position]

    # deletes all between
    def delete_all_between(self, string, beginning, end):
        text_to_delete = self.between(string, beginning, end)
        return string.replace(text_to_delete, '')

    # calculates the age from a date
    def get_age(self, date_string):
        date = self.time.parse_date(date_string)
        now = datetime.now()
        date_timestamp = date.timestamp()
        now_timestamp = now.timestamp()
        difference = now_timestamp - date_timestamp
        return floor(difference / self.yis)


class GradesClass:
    """Class for converting different grade formats"""

    # converts a letter grade to a gpa
    def grade_to_gpa(self, grade):
        amounts = {
            "A+": 4, "A": 4, "A-": 3.66, "-A": 3.66, "B+": 3.33, "B": 3, "B-": 2.66, "C+": 2.33, "C": 2, "C-": 1.66,
            "D": 1, "F": 0
        }
        if grade in amounts:
            return amounts[grade]
        raise Exception('"' + str(grade) + '" is an invalid grade')

    # converts a 0-100 grade to a letter grade
    def grade_to_letter(self, grade):
        if 0 <= grade <= 100:
            structure = {
                93: 'A', 90: '-A', 89: 'B+', 86: 'B', 82: 'B-', 79: 'C+', 76: 'C', 72: 'C-', 69: 'D+', 66: 'D', 62: 'D-',
                0: 'F'
            }
            for score in structure:
                if grade >= score:
                    return structure[score]
        raise Exception('Grade is not in the range between 0-100')


class FormatClass:
    """Class for formating a various amount of information"""

    def __init__(self, underscore):
        self._ = underscore

    # formats a phone number
    def phone(self, phone, international_number=1):
        if type(phone) is int:
            phone = str(phone)
        if len(phone) != 11:
            phone = str(international_number) + phone
        return '+{} ({}) {}-{}'.format(phone[:-10], phone[-10:4], phone[-7:7], phone[-4:])

    # formats bytes
    def bytes(self, size, precision=2):
        units = ["B", "KB", "MB", "GB", "TB", "YB"]
        exponent = floor(log(size, 1024)) | 0
        return str(round(size / (pow(1024, exponent)), precision)) + units[exponent]

    # formats a number with commas
    def number(self, number):
        return "{:,}".format(number)

    # returns a string with the appropriate plural
    def plural(self, number, text):
        exceptions = {
            "person": "people",
            "cactus": "cacti",
            "mouse": "mice"
        }
        if number == 1:
            return str(number) + " " + text
        if text in exceptions:
            text = exceptions[text]
        else:
            text = text + "s"
        return str(number) + " " + text

    # returns a string of a formated time from int seconds 
    def time(self, seconds, full_text=False):
        if seconds / self._.yis >= 1:
            return str(floor(seconds / self._.yis)) + "y" \
                if not full_text else self.plural(floor(seconds / self._.yis), "year")
        elif seconds / self._.mis >= 1:
            return str(floor(seconds / self._.mis)) + "mo" \
                if not full_text else self.plural(floor(seconds / self._.mis), "month")
        elif seconds / self._.dis >= 1:
            return str(floor(seconds / self._.dis)) + "d" \
                if not full_text else self.plural(floor(seconds / self._.dis), "day")
        elif seconds / self._.his >= 1:
            return str(floor(seconds / self._.his)) + "h" \
                if not full_text else self.plural(floor(seconds / self._.his), "hour")
        elif seconds / 60 >= 1:
            return str(floor(seconds / 60)) + "m" \
                if not full_text else self.plural(floor(seconds / 60), "minute")
        else:
            return str(seconds) + "s" if not full_text else self.plural(seconds, "second")

    # returns a string of a number and it's ordinal indicator ("1st", "25th")
    def ordinal(self, number):
        number_string = str(number)
        last_number = int(number_string[-1])
        last_two_numbers = int(number_string[-2:])
        if 11 <= last_two_numbers <= 13:
            return number_string + "th"
        elif last_number == 1:
            return number_string + "st"
        elif last_number == 2:
            return number_string + "nd"
        elif last_number == 3:
            return number_string + "rd"
        return number_string + "th"

    def possession(self, string):
        if string[-1] == "s":
            return string + "'"
        else:
            return string + "'s"


class TimeClass:
    """
    Time functions
    """

    def __init__(self, underscore):
        self._ = underscore

    def parse_date(self, string):
        return datetime.strptime(string, "%m/%d/%Y")

    def same_day(self, time1, time2):
        return self.same_date(time1, time2) and time1.year == time2.year

    def same_date(self, time1, time2):
        return time1.day == time2.day and time1.month == time2.month

    def is_today(self, date):
        now = datetime.now()
        return self.same_day(now, date)

    def natural_day(self, date):
        if type(date) is str:
            date = self.parse_date(date)
        if self.is_today(date):
            return "today"
        today = datetime.now()
        date_seconds = date.timestamp()
        today_seconds = today.timestamp()
        difference = today_seconds - date_seconds
        days_difference = floor(difference / self._.dis)
        if abs(days_difference) == 1:
            if days_difference == -1:
                return "tomorrow"
            return "yesterday"
        return None


class ConvertClass:
    def __init__(self):
        self.decimal = ConvertDecimal()
        self.hex = ConvertHex(self.decimal)
        self.binary = ConvertBinary(self.decimal)
        self.ascii = ConvertAscii(self.decimal)


class ConvertDecimal:
    def binary(self, x):
        return bin(x)[2:]

    def hex(self, x):
        return hex(x)[2:]


class ConvertHex:
    def __init__(self, decimal_class):
        self.base = decimal_class

    def binary(self, x):
        return self.base.binary(self.decimal(x))

    def decimal(self, x):
        return int(x, 16)


class ConvertBinary:
    def __init__(self, decimal_class):
        self.base = decimal_class

    def decimal(self, binary):
        return int(binary, 2)

    def hex(self, binary):
        return self.base.hex(self.decimal(binary))


class ConvertAscii:
    def __init__(self, decimal_class):
        self.base = decimal_class

    def decimal(self, text):
        chars = list(text)
        return [ord(char) for char in chars]

    def hex(self, text):
        decimals = self.decimal(text)
        return [self.base.hex(num) for num in decimals]


class MathClass:
    def get_points(self, point_a, point_b):
        if type(point_a[0]) is int or type(point_a[0]) is float:
            if type(point_a[1]) is int or type(point_a[1]) is float:
                if type(point_b[0]) is int or type(point_b[0]) is float:
                    if type(point_b[1]) is int or type(point_b[1]) is float:
                        return point_a[0], point_b[0], point_a[1], point_b[1]
                    raise Exception("the 2nd part in the 2nd tuple must be in int or float")
                raise Exception("the 1st part in the 2nd tuple must be in int or float")
            raise Exception("the 2nd part in the 1st tuple must be in int or float")
        raise Exception("the 1st part in the 1st tuple must be in int or float")

    def distance(self, point_a, point_b):
        if type(point_a) is tuple and type(point_b) is tuple:
            x1, x2, y1, y2 = self.get_points(point_a, point_b)
            return sqrt((x2 - x1)**2 + (y2 - y1)**2)
        raise Exception('Point A and or B must be tuples')

    def slope(self, point_a, point_b):
        if type(point_a) is tuple and type(point_b) is tuple:
            x1, x2, y1, y2 = self.get_points(point_a, point_b)
            rise = y2 - y1
            run = x2 - x1
            if run != 0:
                return rise / run
            else:
                return "undefined"
        raise Exception('Point A and or B must be tuples')

    # returns the midpoint of two cordinates
    def midpoint(self, point_a, point_b):
        if type(point_a) is tuple and type(point_b) is tuple:
            x1, x2, y1, y2 = self.get_points(point_a, point_b)
            return ((x1 + x2) / 2), ((y1 + y2) / 2)
        raise Exception('Point A and or B must be tuples')

    # returns all the factors of a number
    def factors(self, number):
        if type(number) is int:
            factor = 1
            factors = []
            while True:
                if factor >= number:
                    factors.append(number)
                    break
                if number % factor == 0:
                    factors.append(factor)
                factor += 1
            return factors
        raise Exception("The number must be an int")
    
    # returns the GCF of two or more number
    def gcf(self, number1, number2):
        if type(number1) is int and type(number2) is int:
            factors1 = self.factors(number1)
            factors2 = self.factors(number2)  
            main_factors = factors1 if len(factors1) > len(factors2) else factors2
            sub_factors = factors1 if len(factors1) < len(factors2) else factors2
            factors = []
            for number in main_factors:
                if number in sub_factors:
                    factors.append(number)
            return factors[len(factors) - 1]
        raise Exception("numbers 1 and 2 must be type int")

class ParseClass:
    def __init__(self, underscore):
        self._ = underscore

    # parses an email address
    def email(self, email_address):
        if self._.valid.email(email_address):
            parts = email_address.split("@")
            return EmailAddress(parts[0], parts[1]) 

class ValidClass:
    # tests if a domain exists
    def domain(self, domain_name):
        try:
            gethostbyname(domain_name)
            return True
        except error:
            return False

    # tests if an email is valid
    def email(self, email_address, check_domain=False):
        if type(email_address) is str:
            if bool(match("[^@]+@[^@]+\.[^@]+", email_address)):
                if not check_domain:
                    return True
                domain = email_address.rsplit('@', 1)[-1]
                return self.domain(domain)
        raise Exception("Email address much be a str")


class EmailAddress:
    def __init__(self, username, domain):
        self.username = username
        self.domain = domain

    def __str__(self):
        return "{}@{}".format(self.username, self.domain)

    def __tuple__(self):
        return (self.username, self.domain)
