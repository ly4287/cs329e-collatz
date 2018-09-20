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
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "1 10\n"
        t = type(collatz_read(s))
        self.assertEqual(t, type([]))

    def test_read_3(self):
        s = "100 \n"
        try:
            i, j = collatz_read(s)
        except IndexError:
            self.assertEqual(True, True)
            return()
        self.assertEqual("error", "not caught")

    def test_read_4(self):
        s = "1 2 3"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 2)

    def test_read_5(self):
        s = "an error\n"
        try:
            i, j = collatz_read(s)
        except ValueError:
            self.assertEqual(True, True)
            return()
        self.assertEqual("error", "not caught")

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
        v = collatz_eval(1000, 1000)
        self.assertEqual(v, 112)

    def test_eval_6(self):
        v = collatz_eval(1000, 900)
        self.assertEqual(v, 174)

    def test_eval_7(self):
        try:
            v = collatz_eval(0, 10)
        except AssertionError:
            self.assertEqual(True, True)
            return()
        self.assertEqual("Error", "not caught")

    def test_eval_8(self):
        try:
            v = collatz_eval(1,1000000)
        except AssertionError:
            self.assertEqual(True, True)
            return()
        self.assertEqual("Error", "not caught")

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 1, 10, collatz_eval(1, 10))
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_5(self):
        w = None
        try:
            collatz_print(w, 1, 10, collatz_eval(1, 10))
        except AttributeError:
            self.assertEqual(True, True)
            return()
        self.assertEqual("Error", "not caught")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("1 10")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_solve_3(self):
        r = StringIO("")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "")

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
