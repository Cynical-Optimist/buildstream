# Makefile for updating BuildStream's requirements files.
#

REQUIREMENTS_IN := $(wildcard *.in)
REQUIREMENTS_TXT := $(REQUIREMENTS_IN:.in=.txt)
PYTHON := python3
VENV := $(PYTHON) -m venv

VENV_PIP = $(VENVDIR)/bin/pip


.PHONY: all

all: $(REQUIREMENTS_TXT)

%.txt: %.in
	$(eval VENVDIR := $(shell mktemp -d $(CURDIR)/.bst-venv.XXXXXX))
	$(VENV) $(VENVDIR)
	$(VENV_PIP) install -r $^
	$(VENV_PIP) freeze -r $^ > $@
	rm -rf $(VENVDIR)
