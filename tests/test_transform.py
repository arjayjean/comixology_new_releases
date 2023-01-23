# import pytest
import scripts.etl as etl


"""

"""
# def test_currency_list():
#     actual = type(etl.currency)
#     expected = type([])
#     message = f'etl.currency returned {actual} instead of {expected}'
#     assert actual == expected, message

# def test_dollars_list():
#     actual = type(etl.dollars)
#     expected = type([])
#     message = f'etl.dollars returned {actual} instead of {expected}'
#     assert actual == expected, message

# def test_cents_list():
#     actual = type(etl.cents)
#     expected = type([])
#     message = f'etl.cents returned {actual} instead of {expected}'
#     assert actual == expected, message

# def test_prices_list():
#     actual = type(etl.prices)
#     expected = type([])
#     message = f'etl.prices returned {actual} instead of {expected}'
#     assert actual == expected, message


"""
"""
# def test_currency_list_index():
#     for i in etl.currency:
#         actual = type(i)
#         expected = type('')
#         message = f'etl.currency[{i}] returned {actual} instead of {expected}'
#         assert actual == expected, message

# def test_currency_list_index():
#     for i in etl.currency:
#         actual = type(i)
#         expected = type('')
#         message = f'etl.currency[{i}] returned {actual} instead of {expected}'
#         assert actual == expected, message

# def test_dollars_list_index():
#     for i in etl.dollars:
#         actual = type(i)
#         expected = type('')
#         message = f'etl.dollars[{i}] returned {actual} instead of {expected}'
#         assert actual == expected, message

# def test_prices_list_index():
#     for i in etl.prices:
#         actual = type(i)
#         expected = type('')
#         message = f'etl.prices[{i}] returned {actual} instead of {expected}'
#         assert actual == expected, message


"""
"""
# def test_len_currency_dollars():
#     actual = len(etl.currency)
#     expected = len(etl.dollars)
#     message = f"etl.currency's length returned {actual} instead of {expected}"
#     assert actual == expected, message

# def test_len_currency_cents():
#     actual = len(etl.currency)
#     expected = len(etl.cents)
#     message = f"etl.currency's length returned {actual} instead of {expected}"
#     assert actual == expected, message

# def test_len_dollars_cents():
#     actual = len(etl.dollars)
#     expected = len(etl.cents)
#     message = f"etl.dollars' length returned {actual} instead of {expected}"
#     assert actual == expected, message

# def test_len_prices_cents():
#     actual = len(etl.prices)
#     expected = len(etl.cents)
#     message = f"etl.prices' length returned {actual} instead of {expected}"
#     assert actual == expected, message



def test_getPr():
    actual = len(etl.prices)
    expected = len(etl.currency)
    message = f"etl.prices' length returned {actual} instead of {expected}"
    assert actual == expected, message