"""
Team project for discrette math
"The analogue of itertools"
"""
from typing import Iterable, Iterator


def count(start: int, step=1) -> Iterator | str:
    """
    Function that replace itertool's count method.
    The given one returns an endless iterator with given start and step, if needed(step is optional)

    :param start: the number, which is a start of the iteration
    :type start: int
    :param step: the step through which the iteration will occur
    :type step: int
    :return: infinite loop iterator
    """
    assert isinstance(start, int), 'Type valid type of parametr(int).'
    default_step = 0
    while True:
        if step:
            yield start + default_step * step
        else:
            yield start + default_step
        default_step += 1


def cycle(iterable: Iterable) -> Iterator:
    """
    Function that replace itertool's cycle method
    Returns an endless iterator by looping through the values of the iterator "iterable"

    :param iterable: the iterated object on which the iteration will take place
    :type iterable: Iterable
    :return: infinite loop iterator
    """
    assert isinstance(iterable, Iterable), 'Type valid type of parametr(iterable).'
    while True:
        for i in iterable:
            yield i


def repeat(value):
    """
    Function that replace itertool's repeat method
    Returns an infinite iterator of repeated value values

    :param value: value which will be iterate
    :type value: any
    :return: infinite loop operator
    """
    while True:
        yield value
