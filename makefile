SRC=aoc2022
PROMPT=${SRC}

## List of makefile targets
## - help    : show this help documentation
.PHONY: help
help: makefile
	@sed -n 's/^.*##[ ]//p' $<

## - lint    : Run flake8 and mypy on the source code
.PHONY: lint
lint: env
	. env/bin/activate && python3 -m flake8 ${SRC}/
	. env/bin/activate && python3 -m mypy ${SRC}/

## - black   : Run black on the source code
.PHONY: black
black: env
	. env/bin/activate && python3 -m black ${SRC}/

## - env     : Set up the virtual environment
env: env/bin/activate

env/bin/activate: requirements.txt
	test -d env || python3 -m venv --prompt ${PROMPT} env/
	. env/bin/activate && python3 -m pip install -r requirements.txt
	touch env/bin/activate
