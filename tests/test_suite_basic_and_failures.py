# test_suite.py

import pytest

def test_one():
    assert 2 + 2 == 4  # Passing test
    

def test_two():
    assert 3 * 3 == 9  # Passing test
    

def test_three():
    assert 5 - 2 == 3  # Passing test


def test_four():
    assert 10 / 2 == 5  # Passing test


def test_five():
    assert "hello".upper() == "HELLO"  # Passing test


def test_six():
    assert isinstance(100, int)  # Passing test


def test_seven():
    assert "pytest" in "pytest framework"  # Passing test


def test_eight():
    assert 2 + 2 == 5  # Failing test


def test_nine():
    assert False  # Failing test


def test_ten():
    assert "error" in "success"  # Failing test
