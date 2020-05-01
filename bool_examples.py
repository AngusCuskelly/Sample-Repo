def is_even(num):
    ''' (int) -> bool
    
    Return True if int num is an even number, 
    or return False if number num is an odd number.
    
    Pre-condition: num != 0.
    
    >>> is_even(4)
    True
    >>> is_even(77)
    False
    '''
    return num % 2 == 0
