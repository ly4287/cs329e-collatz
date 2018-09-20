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

    #-------------
    #my read tests
    #-------------

    def test_read_2(self):
        s = "10 6\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 10)
        self.assertEqual(j, 6)

    def test_read_3(self):
        s = "30 20\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 30)
        self.assertEqual(j, 20)

    def test_read_4(self):
        s = "56 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 56)
        self.assertEqual(j, 10)

        

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

    #---------------
    #My 3 Eval Tests
    #---------------
        
    def test_eval_5(self):
        v = collatz_eval(200, 750)
        self.assertEqual(v, 171)

    def test_eval_6(self):
        v = collatz_eval(350, 250)
        self.assertEqual(v, 144)

    def test_eval_7(self):
        v = collatz_eval(100, 12000)
        self.assertEqual(v, 268)

    def test_eval_8(self):
        v = collatz_eval(5, 5)
        self.assertEqual(v, 6)

    def test_eval_9(self):
        v = collatz_eval(1000, 3500)
        self.assertEqual(v, 217)

    def test_eval_10(self):
        v = collatz_eval(1400, 15000)
        self.assertEqual(v, 276)

    def test_eval_11(self):
        v = collatz_eval(1, 15500)
        self.assertEqual(v, 276)

    def test_eval_12(self):
        v = collatz_eval(1, 105500)
        self.assertEqual(v, 351)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    #---------------
    # My Print Tests
    #---------------

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 10, 30, 112)
        self.assertEqual(w.getvalue(), "10 30 112\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 5, 5, 5)
        self.assertEqual(w.getvalue(), "5 5 5\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 1002, 1000, 143)
        self.assertEqual(w.getvalue(), "1002 1000 143\n")

    # --------------
    # My Solve Tests
    # --------------

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    #---
    # My test_solves
    #---

    def test_solve_2(self):
        r = StringIO("1 10 20\n100 200 125\n201 210 89\n900 1000 174\n200 750 171\n350 250 144\n100 12000 268\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n200 750 171\n350 250 144\n100 12000 268\n")

    def test_solve_3(self):
        r = StringIO("900 1000 174\n200 750 171\n350 250 144\n100 12000 268\n5 5 6\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "900 1000 174\n200 750 171\n350 250 144\n100 12000 268\n5 5 6\n")

    def test_solve_4(self):
        r = StringIO("1002 1000 143\n200 750 171\n350 250 144\n100 12000 268\n5 5 6\n1 1 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1002 1000 143\n200 750 171\n350 250 144\n100 12000 268\n5 5 6\n1 1 1\n")
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
