a = [1, 11, 21, 1211, 111221]

url = "view-source:http://www.pythonchallenge.com/pc/return/bull.html"

def look_and_say_nth_sequence(
    n: int,
):
    if n == 1:
        return 1
    elif n == 2:
        return 11
    prev_no = 11
    for elt in range(3, n+1):
        digits = [int(x) for x in str(prev_no)]
        prev_digit = digits[0]
        counter = 1
        prev_no =  ''
        for index, digit in enumerate(digits[1:]):
            if digit == prev_digit:
                counter += 1
            else:
                prev_no += f'{counter}{prev_digit}'
                counter = 1
                prev_digit = digit
            if index == len(digits)-2:
                prev_no += f'{counter}{prev_digit}'
    return int(prev_no)

def test_bull():
    for i in range(1, 6):
        assert look_and_say_nth_sequence(i) == a[i-1]
    print(look_and_say_nth_sequence(31))
    print(len(str(look_and_say_nth_sequence(31))))

"""
Check answers at http://www.pythonchallenge.com/pcc/def/5808.html
"""