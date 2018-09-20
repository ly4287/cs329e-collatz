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
        s = "100 200\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  100)
        self.assertEqual(j, 200)


    def test_read_3(self):
        s = "201 210\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  201)
        self.assertEqual(j, 210)


    def test_read_4(self):
        s = "900 1000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 900)
        self.assertEqual(j, 1000)


    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 100000)
        self.assertEqual(v, 351)

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
        v = collatz_eval(1,4)
        self.assertEqual(v, 8)

    def test_eval_6(self):
        v = collatz_eval(300, 400)
        self.assertEqual(v, 144)

    def test_eval_7(self):
        v = collatz_eval(800, 1000)
        self.assertEqual(v, 179)

    def test_eval_8(self):
        v = collatz_eval(100, 50)
        self.assertEqual(v, 119)


    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertEqual(w.getvalue(), "201 210 89\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 300, 400, 144)
        self.assertEqual(w.getvalue(), "300 400 144\n")


    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("201 210\n300 400\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "201 210 89\n300 400 144\n")

    def test_solve_3(self):
        r = StringIO("1 4\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 4 8\n")

    def test_solve_4(self):
        r = StringIO("800 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "800 1000 179\n")

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
