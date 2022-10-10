
from morse import encode


def test():   # ... --- ...
    """
    test encode
    >>> encode('SOS')
    '... --- ...'
    >>> encode(12)
    Traceback (most recent call last):
    ...
    TypeError: 'int' object is not iterable
    >>> encode('SOS')
    '... --- ..'
    >>> '    ' + encode("SOS")
    ' ... --- ...'
    >>> encode(12)
    Traceback (most recent call last):
    TypeError: 'int' object is not iterable
    >>> encode(['a']) # doctest: +SKIP
    Traceback (most recent call last):
    KeyError: 'a'
    """


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import doctest
    doctest.testmod()
