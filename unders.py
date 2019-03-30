import os
import json
import urllib3
from datetime import datetime
from math import log, floor
from re import sub

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Underscore:

    def __init__(self):
        # vars
        self.underscore_version = "1.0.0"
        self.his = (1 * 60 * 60)  # hour in seconds
        self.dis = (1 * 60 * 60 * 24)  # day in seconds
        self.mis = (30.5 * 24 * 60 * 60)  # month in seconds
        self.yis = (365 * 24 * 60 * 60)  # year in seconds
        # sub classes
        self.format = FormatClass(self)
        self.grades = GradesClass()
        self.time = TimeClass(self)

    '''
    File functions
    '''

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

    '''
    Other functions
    Formatting mostly
    '''

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

    def get_age(self, date_string):
        date = self.time.parse_date(date_string)
        now = datetime.now()
        date_timestamp = date.timestamp()
        now_timestamp = now.timestamp()
        difference = now_timestamp - date_timestamp
        return floor(difference / self.yis)


class GradesClass:
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
    '''
    Time functions
    '''

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
