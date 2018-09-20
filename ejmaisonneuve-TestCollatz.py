#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "1234 10444\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1234)
        self.assertEqual(j, 10444)
 
    def test_read_3(self):
        s = "987 4356\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  987)
        self.assertEqual(j, 4356)

    def test_read_4(self):
        s = "1 999999\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 999999)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5(self):
        v = collatz_eval(1, 999999)
        self.assertEqual(v, 525)

    def test_eval_6(self):
        v = collatz_eval(1200, 800000)
        self.assertEqual(v, 509)

    def test_eval_7(self):
        v = collatz_eval(79867, 98765)
        self.assertEqual(v, 333)

    def test_eval_8(self):
        v = collatz_eval(123456, 345678)
        self.assertEqual(v, 443)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 123456, 345678, 443)
        self.assertEqual(w.getvalue(), "123456 345678 443\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 1, 2, 3)
        self.assertEqual(w.getvalue(), "1 2 3\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 6, 999999, 525)
        self.assertEqual(w.getvalue(), "6 999999 525\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("456 999\n1000 2000\n2001 2100\n900566 999999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "456 999 179\n1000 2000 182\n2001 2100 157\n900566 999999 507\n")

    def test_solve_3(self):
        r = StringIO("123 1023\n10230 22300\n2081 4100\n900 100000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "123 1023 179\n10230 22300 279\n2081 4100 238\n900 100000 351\n")

    def test_solve_4(self):
        r = StringIO("1 500000\n100000 300000\n209851 567834\n98765 298765\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 500000 449\n100000 300000 443\n209851 567834 470\n98765 298765 443\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage-3.5 run --branch TestCollatz.py >  TestCollatz.out 2>&1


% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK


% coverage-3.5 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          12      0      2      0   100%
TestCollatz.py      32      0      0      0   100%
------------------------------------------------------------
TOTAL               44      0      2      0   100%
"""
