FILES :=                              \
    Collatz.html                      \
    Collatz.log                       \
    Collatz.py                        \
    RunCollatz.in                     \
    RunCollatz.out                    \
    RunCollatz.py                     \
    TestCollatz.out                   \
    TestCollatz.py

#    collatz-tests/YourGitLabID-RunCollatz.in   \
#    collatz-tests/YourGitLabID-RunCollatz.out  \
#    collatz-tests/YourGitLabID-TestCollatz.out \
#    collatz-tests/YourGitLabID-TestCollatz.py  \
#

ifeq ($(shell uname), Darwin)          # Apple
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else ifeq ($(CI), true)                # Travis CI
    PYTHON   := python
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage
    PYDOC    := pydoc
    AUTOPEP8 := autopep8
else ifeq ($(shell uname -p), unknown) # Docker
    PYTHON   := python                # on my machine it's python
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := python -m pydoc        # on my machine it's pydoc 
    AUTOPEP8 := autopep8
else                                   # UTCS
    PYTHON   := python3.5
    PIP      := pip3
    PYLINT   := pylint3
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
endif


collatz-tests:
	git clone https://gitlab.com/fareszf/cs329e-collatz-tests.git

Collatz.html: Collatz.py
	$(PYDOC) -w Collatz

Collatz.log:
	git log > Collatz.log

RunCollatz.tmp: RunCollatz.in RunCollatz.out RunCollatz.py
	$(PYTHON) RunCollatz.py < RunCollatz.in > RunCollatz.tmp
	diff RunCollatz.tmp RunCollatz.out

TestCollatz.tmp: TestCollatz.py
	$(COVERAGE) run    --branch TestCollatz.py >  TestCollatz.tmp 2>&1
	$(COVERAGE) report -m                      >> TestCollatz.tmp
	cat TestCollatz.tmp

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -f  RunCollatz.tmp
	rm -f  TestCollatz.tmp
	rm -rf __pycache__
	rm -rf cs329e-collatz-tests

config:
	git config -l

format:
	$(AUTOPEP8) -i Collatz.py
	$(AUTOPEP8) -i RunCollatz.py
	$(AUTOPEP8) -i TestCollatz.py

scrub:
	make clean
	rm -f  Collatz.html
	rm -f  Collatz.log
	rm -rf collatz-tests

status:
	make clean
	@echo
	git branch
	git remote -v
	git status
	
versions:
	which     $(AUTOPEP8)
	autopep8 --version
	@echo
	which    $(COVERAGE)
	coverage --version
	@echo
	which    git
	git      --version
	@echo
	which    make
	make     --version
	@echo
	which    $(PIP)
	pip      --version
	@echo
#	which    $(PYDOC)
#	pydoc    --version
#	@echo
	which    $(PYLINT)
	pylint   --version
	@echo
	which    $(PYTHON)
	python   --version

test: Collatz.html Collatz.log RunCollatz.tmp TestCollatz.tmp collatz-tests check
