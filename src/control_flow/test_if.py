"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'

    assert conclusion == 'Number bigger than or equal to one'


def test_if_elif_chain():
    """Multiple ELIF branches

    Only the first condition that is True runs; the rest are skipped.
    """

    score = 83
    grade = ''

    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    assert grade == 'B'



def test_nested_if_statement():
    """Nested IF statements

    An inner condition is only checked when the outer condition is True.
    """

    age = 20
    has_ticket = True
    message = ''

    if age >= 18:
        if has_ticket:
            message = 'Entry allowed'
        else:
            message = 'Adult without a ticket'
    else:
        message = 'Too young to enter'

    assert message == 'Entry allowed'