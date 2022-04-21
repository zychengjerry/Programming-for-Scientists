# COMP1730/6730 Homework 4
# Submission is due 9:00am, Monday the 18th of April, 2022.

# YOUR ANU ID: u7148404
# YOUR NAME: Zeyuan Cheng

# Implement the function max_increase below.
# (The statement "pass" is just a placeholder that does nothing: you
# should replace it.)
# You can define other functions if it helps you decompose the problem
# and write a better organised and/or more readable solution.

def max_increase(seq):
    """
    This function calculate the max increase value of a sequence.
    And it will return the result of max increase value as a number.

    Parameters
    ----------
    seq : list
        This input is a sequence numbers as a list 

    Returns
    -------
    max_increase_value : int / float
        This output is a number of max increase value of the input sequence. 
        If input is an integer list, the max_increase_value will be an int, 
        and if input is a float list, the max_increase_value will be a float.

    """
    # The index of the elemet in seq
    index = 0
    # initialize max increase value
    max_increase_value = 0
    # For loop
    for i in range(1, len(seq)):
        # Calculate increase value (difference)
        increase_value = seq[i] - seq[index]
        # If the difference is less than / equals to 0, 
        # which means the number in index is larger than / equals to the next number in i, 
        if increase_value <= 0:
            # then change the value of index to i
            index = i
        # If the difference is larger than 0, 
        # which means the number in index is smaller than the next number in i, 
        else:
            # then judging the increase_value and max_increase_value,
            # replace the larger one
            if increase_value > max_increase_value:
                max_increase_value = increase_value
    return max_increase_value


def test_max_increase():
    '''
    This function runs a number of tests of the max_increase function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    '''

    assert max_increase([]) == 0, "empty list has no pair"
    assert max_increase([1]) == 0, "size-1 list has no pair"
    assert max_increase((1,2,3,2)) == 2
    assert max_increase([1.0,3.0,1.0,2.0]) == 2.0
    assert max_increase([3,-1,2,1]) == 3
    assert max_increase([3,2,1,1]) == 0, "no increasing pair"
    assert max_increase([226, 264, 337, 364, 485, 529, 482]) == 303

    btc_data = [ 6729.44, 6690.88, 6526.36, 6359.98, 6475.89, 6258.74,
                 6485.10, 6396.64, 6579.00, 6313.51, 6270.20, 6195.01,
                 6253.67, 6313.90, 6233.10, 6139.99, 6546.45, 6282.50,
                 6718.22, 6941.20, 7030.01, 7017.61, 7414.08, 7533.92,
                 7603.99, 7725.43, 8170.01, 8216.74, 8235.70, 8188.00,
                 7939.00, 8174.06 ]
    btc_data.reverse()
    assert abs(max_increase(tuple(btc_data)) - 589.45) < 1e-6

    print("all tests passed")
