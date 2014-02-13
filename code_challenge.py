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
    """

    if nums == "":
        return 0
    else:
        nums = re.split(r"[\n,]", nums)

        if "" in nums:
            raise Exception("invalid input")

        return sum(int(i) for i in nums)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
