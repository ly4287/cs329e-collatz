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

    def test_read(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)


    def test_read_negative(self):
        s = "-1 -10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  -1)
        self.assertEqual(j, -10)

    def test_read_intparser(self):
        with self.assertRaises(ValueError):
            s = "1.0 5.8\n"
            i, j = collatz_read(s)

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

    def test_eval_negative(self):
        with self.assertRaises(AssertionError):
            collatz_eval(-10, -30)
        
    def test_eval_large_number(self):
        v = collatz_eval(1000, 10000)
        self.assertEqual(v, 262)

    def test_eval_single(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_i_over_j(self):
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_neg(self):
        w = StringIO()
        collatz_print(w, -1, -10, 0)
        self.assertEqual(w.getvalue(), "-1 -10 0\n")  

    def test_print_float(self):
        w = StringIO()
        collatz_print(w, 1.1, 5.5, 7.5)   
        self.assertEqual(w.getvalue(), "1 5 7\n")          

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_large(self):
        r = StringIO("837798 837800\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "837798 837800 525\n")

    def test_solve_largest(self):
        r = StringIO("8400510 8400512\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "8400510 8400512 686\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage-3.5 run --branch TestCollatz.py >  TestCollatz.out 2>&1


% cat TestCollatz.out
.................
----------------------------------------------------------------------
Ran 17 tests in 0.961s
OK


% coverage-3.5 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.................
----------------------------------------------------------------------
Ran 17 tests in 0.961s

OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          39      0     12      0   100%
TestCollatz.py      71      0      0      0   100%
------------------------------------------------------------
TOTAL              110      0     12      0   100%
"""
