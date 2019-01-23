"""
calculator
"""

def add(*args):
    """ calculator """
    answer = 0
    for value in args:
        answer += value
    return answer
