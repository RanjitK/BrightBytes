import re

def calc(nums):
    """calculate sum of numbers

    >>> calc("")
    0
    >>> calc("1")
    1
    >>> calc("1,2")
    3
    >>> calc("1,2,3")
    6
    >>> calc("1,2,4,5")
    12
    >>> calc("1\\n,2")
    Traceback (most recent call last):
        ...
    Exception: invalid input
    >>> calc("1\\n2,3")
    6
    >>> calc("//;\\n1;2")
    3
    >>> calc("//;\\n1;\\n2")
    Traceback (most recent call last):
        ...
    Exception: invalid input
    >>> calc("//\\n1,2")
    Traceback (most recent call last):
        ...
    Exception: invalid input
    """

    if nums == "":
        return 0
    else:
        delimiter = ','

        if re.match(r"(//)(\W)(\n)", nums) != None:
            delimiter = re.match(r"(//)(\W)(\n)", nums).group(2)
            nums = nums.replace(re.match(r"(//)(\W)(\n)", nums).group(), "")

        #split on delimiter and newline char
        nums = re.split(r"[\n %s]"%delimiter, nums)

        try:
            total = sum(int(i) for i in nums)
        except:
            raise Exception("invalid input")

        return total

if __name__ == '__main__':
    import doctest
    doctest.testmod()
