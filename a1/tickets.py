"""CSCA08 Fall 2026 Assignment 1.

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2020-2026 Jacqueline Smith and Anya Tafliovich.

"""

from constants import (YR, MON, DAY, DEP, ARR, ROW, SEAT, FFN,
                       WINDOW, AISLE, MIDDLE, SA, SB, SC, SD, SE, SF)


# We provide this function for you to use as a helper.
def is_valid_ticket_format(ticket: str) -> bool:
    """Return True if and only if ticket 'ticket' is in valid format:
    - year is 4 digits
    - month is 2 digits
    - day is 2 digits
    - departure is 3 letters
    - arrival is 3 letters
    - row is 2 digits
    - seat is a characters
    - frequent flyer number is either empty or 4 digits, and
      it is the last record in 'ticket'

    >>> is_valid_ticket_format('20271020YYZYEG12C1236')
    True
    >>> is_valid_ticket_format('20271020YYZYEG12C12361236')
    False
    >>> is_valid_ticket_format('ABC41020YYZYEG12C1236')
    False
    """

    return (FFN == 17
            and (len(ticket) == 17
                 or len(ticket) == 21 and ticket[FFN:FFN + 4].isdigit())
            and ticket[YR:YR + 4].isdigit()
            and ticket[MON:MON + 2].isdigit()
            and ticket[DAY:DAY + 2].isdigit()
            and ticket[DEP:DEP + 3].isalpha()
            and ticket[ARR:ARR + 3].isalpha()
            and ticket[ROW:ROW + 2].isdigit()
            and ticket[SEAT].isalpha())

# We provide this function solution as an example of correct
# documentation, as well as a function that uses constants.


def get_year(ticket: str) -> str:
    """Return the year of ticket 'ticket'.

    Requirement: 'ticket' is in valid format
    
    >>> get_year('20010915YYZYEG12F')
    '2001'
    >>> get_year('20270915YYZYEG12F1236')
    '2027'
    >>> get_year('20301225LAXSEA14C8888')
    '2030'
    """

    return ticket[YR:YR + 4]


def get_day(ticket: str) -> str:
    """Return the date of ticket 'ticket'.

    Requirement: 'ticket' is in valid format

    >>> get_day('20260915YYZYWG12F1234')
    '15'
    >>> get_day('20231221YYZYWG25F4442')
    '21'
    """

    return ticket[DAY:DAY + 2]


# We provide this function solution as an example of correct
# documentation, as well as a function that uses other functions as
# helpers.
# Function to get the date from a string
def get_date(ticket: str) -> str:
    """Return the date of ticket 'ticket' in YYYYMMDD format.

    
    Requirement: 'ticket' is in valid format

    >>> get_date('20260915YYZYEG12F1234')
    '20260915'
    >>> get_date('20270915YYZYEG12F1236')
    '20270915'
    >>> get_date('19990804LAXJFK22B')
    '19990804'
    """

    return get_year(ticket) + get_month(ticket) + get_day(ticket)


# We provide the docstring for this function to help you get started.
def get_month(ticket: str) -> str:
    """Return the month of ticket 'ticket'.

    Requirement: 'ticket' is in valid format

    >>> get_month('20260915YYZYEG12F')
    '09'
    >>> get_month('20271215YYZYEG12F1236')
    '12'
    >>> get_month('20270115YYZYEG12F1236')
    '01'
    """

    return ticket[MON:MON + 2]  # replace this line with your solution


# Returns departure code
def get_departure(ticket: str) -> str:
    """Returns the departure airport code on ticket 'ticket'.

    Requirement: 'ticket' is a valid ticket

    >>> get_departure('20231221YYZYEG25F4442')
    'YYZ'
    >>> get_departure('20260915YWGYEG12F1234')
    'YWG'
    >>> get_departure('20301225LAXSEA14C')
    'LAX'
    """
    return ticket[DEP:DEP + 3]


def get_arrival(ticket: str) -> str:
    """Returns the arrival airport code on ticket 'ticket'.

    Requirement: 'ticket' is a valid ticket

    >>> get_arrival('20260915YYZYEG12F')
    'YEG'
    >>> get_arrival('20260915YYZSTR42F1236')
    'STR'
    >>> get_arrival('20301225LAXSEA14C')
    'SEA'
    """
    return ticket[ARR:ARR + 3]


def get_row(ticket: str) -> int:
    """The parameter represents the ticket. The function should return the 
    row number on the given ticket. You may assume the input ticket is valid.

    Requirement: 'ticket' is a valid ticket.

    >>> get_row('20231221YYZYEG25F4442')
    25
    >>> get_row('20260915YYZSTR42F1236')
    42
    >>> get_row('20301225LAXSEA14C')
    14

    """
    return int(ticket[ROW: ROW + 2])


def get_seat(ticket: str) -> str:
    """Returns the seat value of given ticket 'ticket'

    Requirement: 'ticket' is a valid ticket
    >>> get_seat('20231221YYZYEG25F4442')
    'F'
    >>> get_seat('20260915YYZYEG21Q')
    'Q'
    >>> get_seat('20301225LAXSEA14C8888')
    'C'
    """
    return ticket[SEAT]


def get_ffn(ticket: str) -> str:
    """Returns the frequent flier number of given ticket 'ticket'. 
    Ffn may be empty or an actual value depedning on length of ticket

    Requirement: 'ticket' is a valid ticket

    >>> get_ffn('20231221YYZYEG25F4442')
    '4442'
    >>> get_ffn('20231221YYZYEG25F')
    ''
    >>> get_ffn('20301225LAXSEA14C8888')
    '8888'
    """
    return ticket[FFN:]


# We provide the docstring for this function to help you get started.
def is_valid_seat(ticket: str, first_row: int, last_row: int) -> bool:
    """Return True if and only if ticket 'ticket' has a valid seat. That
    is, if the seat row is between the first row 'first_row' and last
    row 'last_row', inclusive, and the seat is SA, SB, SC, SD, SE, or SF.

    Requirement: 'ticket' is in valid format.

    >>> is_valid_seat('20260915YYZYEG12F1236', 1, 30)
    True
    >>> is_valid_seat('20260915YYZYEG42F1236', 1, 30)
    False
    >>> is_valid_seat('20260915YYZYEG21Q1236', 1, 30)
    False
    """
    # replace this line with your solution
    return first_row <= get_row(ticket) <= last_row and (
        get_seat(ticket) in [SA, SB, SC, SD, SE, SF])


# Determines whether frequent flier number is valid
def is_valid_ffn(ticket: str) -> bool:
    """Returns True if and only if the frequent flier number in ticket
    'ticket' is valid. Frequent flier numbers may be empty or contain a value
    four characters long 

    Requirement: 'ticket' is a valid ticket
    >>> is_valid_ffn('20231221YYZYEG25F4442')
    True
    >>> is_valid_ffn('20231221YYZYEG25F1')
    False
    """
    # Check if ffn is empty
    ffn = get_ffn(ticket)
    if ffn == '':
        return True

    # Make sure any wrong inputs are immediately returned false
    if len(ffn) != 4 or not ffn.isdigit():
        return False

    # If the sum of the first three digits modulus 10 is equal to the last digit
    # And the ffn is four long return true
    sum_modulo = (int(ffn[0]) + int(ffn[1]) + int(ffn[2])) % 10
    return sum_modulo == int(ffn[-1])


def is_valid_date(ticket: str) -> bool:
    """Returns True if and only if ticket 'ticket' has a valid date. 
    Dates include a year, a month, a a day. A valid year must be
    positive and contain digits. A valid month must be between 1 and 12 
    inclusive. A valid day must be between 1 and the max 
    number of days for a given month.

    Requirement: 'ticket' is a valid ticket
    >>> is_valid_date('20230915YYZYEG12F1236')
    True
    >>> is_valid_date('20230229YYZYEG12F1236')
    False
    >>> is_valid_date('20231315YYZYEG12F1236')
    False
    >>> is_valid_date('20230431YYZYEG12F1236')
    False
    """
    # Keep track of month, day and year in their owm variables
    month = int(get_month(ticket))
    day = int(get_day(ticket))
    year = int(get_year(ticket))
    # Check if year and month is valid
    if year <= 0 or not 1 <= month <= 12:
        return False

    # Evaluates if year is leap year
    is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    # Regular months
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    max_day = days_in_month[month - 1]

    # February has 29 days in a leap year
    if month == 2 and is_leap:
        max_day = 29
    return 1 <= day <= max_day


# Checks if ticket is valid
def is_valid_ticket(ticket: str, first_row: int, last_row: int) -> bool:
    """Returns True if and only if ticket 'ticket' is a valid ticket. A ticket
    is valid when it's departure and arrival airposts are letters, the flight 
    doesn't depart and arrive at the same airport, 
    the row, seats, are real numbers, 
    the frequent flier number is valid, 
    and ticket format is also valid. 
    It's seat is also between first row 'first_row' and last row 'last_row'

    Requirements: 'ticket' is a valid ticket and 'first_row' and 
    'last_row' are valid row constraints
    >>> is_valid_ticket('20230915YYZYEG12F1236', 1, 30)
    True
    >>> is_valid_ticket('20230431YYZYEG12F1236', 1, 30)
    False
    >>> is_valid_ticket('20230915YYZYEG32F1236', 1, 30)
    False
    >>> is_valid_ticket('20230915YYZYEG12H1236', 1, 30)
    False
    >>> is_valid_ticket('20230915YYZYEG12F12A6', 1, 30)
    False
    """
    return (is_valid_ticket_format(ticket)
            and not get_departure(ticket) == get_arrival(ticket)
            and get_row(ticket)
            and is_valid_ffn(ticket)
            and is_valid_date(ticket)
            and is_valid_seat(ticket, first_row, last_row))


# We provide the docstring for this function to help you get started.
def visits_airport(ticket: str, airport: str) -> bool:
    """Return True if and only if either departure or arrival airport on
    ticket 'ticket' is the same as 'airport'.

    Requirement: 'ticket' is a valid ticket.

    >>> visits_airport('20260915YYZYEG12F1236', 'YEG')
    True
    >>> visits_airport('20260915YEGYYZ12F1236', 'YEG')
    True
    >>> visits_airport('20260915YYZYEG12F1236', 'YVR')
    False
    """
    return (get_departure(ticket) == airport) or (
        get_arrival(ticket) == airport)


# We provide the docstring for this function to help you get started.
def adjacent(ticket1: str, ticket2: str) -> bool:
    """Return True if and only if the seats in tickets 'ticket1' and
    'ticket2' are adjacent (next to each other). Seats across an aisle
    are not considered to be adjacent.

    Requirement: 'ticket1' and 'ticket2' are valid tickets.

    >>> adjacent('20260915YYZYEG12D1236', '20260915YYZYEG12E1236')
    True
    >>> adjacent('20260915YYZYEG12B1236', '20260915YYZYEG12A1236')
    True
    >>> adjacent('20260915YYZYEG12C1236', '20260915YYZYEG12D1236')
    False
    >>> adjacent('20260915YYZYEG12A1236', '20260915YYZYEG11B1236')
    False
    """
    if get_row(ticket1) != get_row(ticket2):
        return False

    seat1 = get_seat(ticket1)
    seat2 = get_seat(ticket2)

    return (seat1, seat2) in {
        ('A', 'B'), ('B', 'A'),
        ('B', 'C'), ('C', 'B'),
        ('D', 'E'), ('E', 'D'),
        ('E', 'F'), ('F', 'E'),
    }


# Checks if two flights are connecting
def connecting(ticket1: str, ticket2: str) -> bool:
    """Returns True if and only if the flights in tickets 'ticket1' and 
    'ticket2' are connecting. Connecting flights 
    mean the first ticket arrives in the 
    same airport as the departure of the second ticket, 
    and the flights are on the same date.

    Requirement: 'ticket1' and 'ticket2' are valid tickets

    >>> connecting('20260915YYZYEG12D1236', '20260915YYZYEG12E1236')
    False
    >>> connecting('20231201LAXYWG22B9981', '20231201YWGSTR14C5555')
    True
    >>> connecting('20231201LAXYWG22B9981', '20231201YVRTOR14C5555')
    False
    """
    return get_date(ticket1) == get_date(ticket2) and (
        get_arrival(ticket1) == get_departure(ticket2))


# Checks if one seat is behind another
def behind(ticket1: str, ticket2: str) -> bool:
    """Return True if and only if the seats in tickets 'ticket1' and
    'ticket2' are immediately behind each other. Seats across an aisle
    are not considered to be adjacent.
    
    Requirement: 'ticket1' and 'ticket2' are valid tickets.
    >>> behind('20260915YYZYWG12A', '20260915YYZYWG13A')
    True
    >>> behind('20260915YYZYWG12A1236', '20260915YYZYWG14A1236')
    False
    >>> behind('20260915YYZYWG12A1236', '20260915YYZYWG12A1236')
    False
    """

    return (get_seat(ticket1) == get_seat(ticket2)
            and abs(get_row(ticket1) - get_row(ticket2)) == 1)


# We provide the docstring for this function to help you get started.
def get_seat_type(ticket: str) -> str:
    """Return WINDOW, AISLE, or MIDDLE depending on the type of seat in
    ticket 'ticket'.

    Requirement: 'ticket' is a valid ticket.

    >>> get_seat_type('20260915YYZYEG12F1236')
    'window'
    >>> get_seat_type('20260915YYZYEG08B')
    'middle'
    >>> get_seat_type('20260915YYZYEG12C1236')
    'aisle'

    """
    seat = get_seat(ticket)

    # if their in seat SA or SF says its a window
    if seat == SA or seat == SF:
        return WINDOW

    # If the seat is SB or SE, it's an middle
    if seat == SB or seat == SE:
        return MIDDLE

    # Everything else is a aisle seat
    return AISLE


# COMPLETE BONUS FUNCS IF YOU HAVE TIME
def change_seat(ticket: str, row_num: str, seat: str) -> str:
    """Returns a new ticket 'ticket' that is in the 
    same format as the input ticket
    with new seat information in the given row 'row_num' and seat 'seat'

    Requirement: 'ticket' is a valid ticket, 'row_num' is a valid
    row number, and 'seat' is a valid seat
    >>> change_seat('20260915YYZYEG12F1236', '14', 'C')
    '20260915YYZYEG14C1236'
    >>> change_seat('20231201LAXJFK22B9981', '05', 'A')
    '20231201LAXJFK05A9981'
    >>> change_seat('19990704YVRYUL03A5555', '03', 'F')
    '19990704YVRYUL03F5555'
    """

    return ticket[0:ROW] + row_num + seat + ticket[SEAT + 1:]


def change_date(ticket: str, day: str, month: str, year: str) -> str:
    """Returns a new ticket 'ticket' with the date updated to day 'day', month
    updated to month 'month', and year updated to year 'year'

    Requirement: 'ticket' is a valid ticket
    >>> change_date('20260915YYZYEG12F1236', '01', '12', '2027')
    '20271201YYZYEG12F1236'
    >>> change_date('19990704YVRYUL03A5555', '25', '12', '2000')
    '20001225YVRYUL03A5555'
    >>> change_date('20231201LAXJFK22B9981', '15', '01', '2024')
    '20240115LAXJFK22B9981'
    """

    return year + month + day + ticket[DEP:]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
