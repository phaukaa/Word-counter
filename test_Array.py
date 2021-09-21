from Array import *
import pytest

def test_print():
    shape = (3,)
    arr1 = Array(shape, 1, -4, 3)
    arr2 = Array(shape, 2.4, -3.6, 7.0)
    assert str(arr1) == "[1, -4, 3]"
    assert str(arr2) == "[2.4, -3.6, 7.0]"

    shape = (3, 2)
    arr5 = Array(shape, 1, 2, 3, 5, 8, 6)
    assert str(arr5) == "[[1, 2], [3, 5], [8, 6]]"


def test_add():
    shape = (3,)
    arr1 = Array(shape, 1, -4, 3)
    arr2 = Array(shape, 2, 3, -1)
    res1 = arr1 + arr2
    arr3 = Array(shape, 2.4, -3.6, 7.0)
    arr4 = Array(shape, 2.0, 3.2, -4.4)
    res2 = arr3 + arr4
    res3 = arr1 + 10
    assert res1[1] == -1
    assert res2[2] == pytest.approx(2.6)
    assert res3[2] == 13

    #2D array test
    shape = (3, 2)
    arr5 = Array(shape, 1, 2, 3, 4, 5, 6)
    arr6 = Array(shape, 2, 3, 4, 5, 6, 7)
    res4 = arr5 + arr6
    assert res4[0] == 3
    assert res4[4] == 11


def test_radd():
    shape = (3,)
    arr = Array(shape, 2, 4, 6)
    res = 10 + arr
    assert res[0] == 12
    assert res[1] == 14
    assert res[2] == 16

def test_sub():
    shape = (3,)
    arr1 = Array(shape, 1, -4, 3)
    arr2 = Array(shape, 2, 3, -1)
    res1 = arr1 - arr2
    arr3 = Array(shape, 2.4, -3.6, 7.0)
    arr4 = Array(shape, 2.0, 3.2, -4.4)
    res2 = arr3 - arr4
    res3 = arr1 - 10
    assert res1[1] == -7
    assert res2[2] == 11.4
    assert res3[2] == -7

    #2D array test
    shape = (3, 2)
    arr5 = Array(shape, 1, 2, 3, 5, 8, 6)
    arr6 = Array(shape, 2, 3, 4, 4, 4, 7)
    res4 = arr5 - arr6
    assert res4[0] == -1
    assert res4[4] == 4


def test_rsub():
    shape = (3,)
    arr = Array(shape, 2, 4, 6)
    res = 10 - arr
    assert res[0] == 8
    assert res[1] == 6
    assert res[2] == 4

    res2 = -5 - arr
    assert res2[0] == -7

def test_mul():
    shape = (3,)
    arr1 = Array(shape, 2, 4, 6)
    arr2 = Array(shape, 2, 3, 4)
    res1 = arr1 * 3
    res2 = arr1 * arr2
    assert res1[0] == 6
    assert res1[1] == 12
    assert res1[2] == 18
    assert res2[0] == 4
    assert res2[1] == 12
    assert res2[2] == 24

def test_rmul():
    shape = (3,)
    arr = Array(shape, 2, 4, 6)
    res = 3 * arr
    assert res[0] == 6
    assert res[1] == 12
    assert res[2] == 18


def test_comp():
    shape = (3,)
    arr1 = Array(shape, 2, 3, 4)
    arr2 = Array(shape, 2, 3, 4)
    assert arr1 == arr2
    arr3 = Array(shape, 2.2, 3.3, 4.4)
    arr4 = Array(shape, 2.2, 3.3, 4.4)
    assert arr3 == arr4
    assert not arr1 == arr3

    #2D array test
    shape = (3, 2)
    arr5 = Array(shape, 1, 2, 3, 4, 5, 6)
    arr6 = Array(shape, 1, 2, 3, 4, 5, 6)
    assert arr5 == arr6

def test_is_equal():
    shape = (3,)
    arr1 = Array(shape, 2, 3, 4)
    arr2 = Array(shape, 2, 3, 4)
    res1 = arr1.is_equal(arr2)
    assert res1[0] == True
    assert res1[1] == True
    assert res1[2] == True
    arr3 = Array(shape, 2.2, 3.3, 4.4)
    arr4 = Array(shape, 2.2, 9.9, 8.8)
    res2 = arr3.is_equal(arr4)
    assert res2[0] == True
    assert res2[1] == False
    assert res2[2] == False

def test_mean():
    shape = (3,)
    arr1 = Array(shape, 2, 3, 7)
    arr2 = Array(shape, 3.3, 5.2, 3.5)
    assert arr1.mean() == 4
    assert arr2.mean() == 4

    #2D array test
    shape = (3, 2)
    arr5 = Array(shape, 1, 2, 3, 4, 5, 6)
    assert arr5.mean() == 3.5

def test_variance():
    shape = (3,)
    arr1 = Array(shape, 2, 3, 7)
    arr2 = Array(shape, 3, 4, 5)
    variance1 = arr1.variance()
    variance2 = arr2.variance()
    assert variance1 == pytest.approx(4.67, 0.1)
    assert variance2 == pytest.approx(0.67, 0.1)

def test_min():
    shape = (3,)
    arr1 = Array(shape, 2, 3, 7)
    arr2 = Array(shape, 3, -4, 5)
    assert arr1.min_element() == 2
    assert arr2.min_element() == -4

    #2D array test
    shape = (3, 2)
    arr5 = Array(shape, 1, 2, 3, 4, 5, 6)
    arr6 = Array(shape, 2, 3, 4, -5, 6, 7)
    assert arr5.min_element() == 1
    assert arr6.min_element() == -5
