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

    def test_read_1(self):
        t = "5 20\n"
        k, l = collatz_read(t)
        self.assertEqual(k, 5)
        self.assertEqual(l, 20)

    def test_read_2(self):
        u = "8 25\n"
        m, n = collatz_read(u)
        self.assertEqual(m, 8)
        self.assertEqual(n, 25)

    def test_read_3(self):
        w = "18 500\n"
        o, p = collatz_read(w)
        self.assertEqual(o, 18)
        self.assertEqual(p, 500)

    def test_read_4(self):
        x = "45 15\n"
        p, q = collatz_read(x)
        self.assertEqual(p, 45)
        self.assertEqual(q, 15)

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
        v = collatz_eval(45, 15)
        self.assertEqual(v, 112)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_1(self):
        x = StringIO()
        collatz_print(x, 900, 1000, 174)
        self.assertEqual(x.getvalue(), "900 1000 174\n")

    def test_print_2(self):
        y = StringIO()
        collatz_print(y, 50, 500, 144)
        self.assertEqual(y.getvalue(), "50 500 144\n")

    def test_print_3(self):
        z = StringIO()
        collatz_print(z, 3, 8000, 262)
        self.assertEqual(z.getvalue(), "3 8000 262\n")

    def test_print_4(self):
        a = StringIO()
        collatz_print(a, 45, 15, 112)
        self.assertEqual(a.getvalue(), "45 15 112\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1(self):
        c = StringIO("8 50\n500 600\n1000 3001\n100000 150000")
        d = StringIO()
        collatz_solve(c, d)
        self.assertEqual(d.getvalue(), "8 50 112\n500 600 137\n1000 3001 217\n100000 150000 375\n")

    def test_solve_2(self):
        e = StringIO("7 29\n15 9000\n2 3\n57 92")
        f = StringIO()
        collatz_solve(e, f)
        self.assertEqual(f.getvalue(), "7 29 112\n15 9000 262\n2 3 8\n57 92 116\n")

    def test_solve_3(self):
        g = StringIO("1 2\n18 24\n17 76\n9000000 9000001")
        h = StringIO()
        collatz_solve(g, h)
        self.assertEqual(h.getvalue(), "1 2 2\n18 24 21\n17 76 116\n9000000 9000001 257\n")

    def test_solve_4(self):
        i = StringIO("45 15\n")
        j = StringIO()
        collatz_solve(i, j)
        self.assertEqual(j.getvalue(), "45 15 112\n")

    def test_solve_5(self):
        k = StringIO("\n")
        l = StringIO()
        collatz_solve(k, l)
        self.assertEqual(l.getvalue(), "")

# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage-3.5 run --branch TestCollatz.py >  TestCollatz.out 2>&1


% cat TestCollatz.out
.....................
----------------------------------------------------------------------
Ran 21 tests in 0.261s

OK


% coverage-3.5 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.....................
----------------------------------------------------------------------
Ran 21 tests in 0.261s

OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          28      0     12      0   100%
TestCollatz.py      96      0      0      0   100%
------------------------------------------------------------
TOTAL              124      0     12      0   100%

"""
