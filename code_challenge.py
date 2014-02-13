def calc(nums):
    """calculate sum of numbers
    >>> calc("")
    0
    >>> calc("1")
    1
    >>> calc("1,2")
    3
    """

    if nums == "":
        return 0
    else:
        nums = nums.split(",")
        if len(nums) < 3:
            return sum(int(i) for i in nums)


if __name__ == '__main__':
    import doctest
    doctest.testmod()