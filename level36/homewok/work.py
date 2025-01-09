#https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python
def filter_list(l):
    return [item for item in l if not isinstance(item, str)]

#https://www.codewars.com/kata/546e2562b03326a88e000020/train/python
def square_digits(num):
    return int(''.join(str(int(digit) ** 2) for digit in str(num)))

#https://www.codewars.com/kata/56747fd5cb988479af000028/train/python
def get_middle(s):
    length = len(s)
    if length % 2 == 0:
       
        return s[length // 2 - 1: length // 2 + 1]
    else:
       
        return s[length // 2]

#https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python
def find_short(s):
    words = s.split()  
    return len(min(words, key=len))

#https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python
def solution(text, ending):
    return text.endswith(ending)
