# import pytest
import scripts.extract as e


"""

"""
# def test_currency_list():
#     actual = type(e.currency)
#     expected = type([])
#     message = f'e.currency returned {actual} instead of {expected}'
#     assert actual == expected, message

# def test_dollars_list():
#     actual = type(e.dollars)
#     expected = type([])
#     message = f'e.dollars returned {actual} instead of {expected}'
#     assert actual == expected, message

# def test_cents_list():
#     actual = type(e.cents)
#     expected = type([])
#     message = f'e.cents returned {actual} instead of {expected}'
#     assert actual == expected, message

# def test_prices_list():
#     actual = type(e.prices)
#     expected = type([])
#     message = f'e.prices returned {actual} instead of {expected}'
#     assert actual == expected, message


"""
"""
# def test_currency_list_index():
#     for i in e.currency:
#         actual = type(i)
#         expected = type('')
#         message = f'e.currency[{i}] returned {actual} instead of {expected}'
#         assert actual == expected, message

# def test_currency_list_index():
#     for i in e.currency:
#         actual = type(i)
#         expected = type('')
#         message = f'e.currency[{i}] returned {actual} instead of {expected}'
#         assert actual == expected, message

# def test_dollars_list_index():
#     for i in e.dollars:
#         actual = type(i)
#         expected = type('')
#         message = f'e.dollars[{i}] returned {actual} instead of {expected}'
#         assert actual == expected, message

# def test_prices_list_index():
#     for i in e.prices:
#         actual = type(i)
#         expected = type('')
#         message = f'e.prices[{i}] returned {actual} instead of {expected}'
#         assert actual == expected, message


"""
"""
# def test_len_currency_dollars():
#     actual = len(e.currency)
#     expected = len(e.dollars)
#     message = f"e.currency's length returned {actual} instead of {expected}"
#     assert actual == expected, message

# def test_len_currency_cents():
#     actual = len(e.currency)
#     expected = len(e.cents)
#     message = f"e.currency's length returned {actual} instead of {expected}"
#     assert actual == expected, message

# def test_len_dollars_cents():
#     actual = len(e.dollars)
#     expected = len(e.cents)
#     message = f"e.dollars' length returned {actual} instead of {expected}"
#     assert actual == expected, message

# def test_len_prices_cents():
#     actual = len(e.prices)
#     expected = len(e.cents)
#     message = f"e.prices' length returned {actual} instead of {expected}"
#     assert actual == expected, message



def test_getPr():
    actual = len(e.prices)
    expected = len(e.currency)
    message = f"e.prices' length returned {actual} instead of {expected}"
    assert actual == expected, message