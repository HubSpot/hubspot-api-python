VENV_NAME?=.venv

venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: setup.py
	@test -d $(VENV_NAME) || python3 -m venv $(VENV_NAME)
	@${VENV_NAME}/bin/python -m pip install --upgrade pip
	@${VENV_NAME}/bin/python -m pip install -e .[dev]
	@touch $(VENV_NAME)/bin/activate

test: venv
	@${VENV_NAME}/bin/python -m pytest ./tests/spec

integration_test: venv
	@${VENV_NAME}/bin/python -m pytest ./tests/integration

fmt: venv
	@${VENV_NAME}/bin/python -m black ./

clean:
	@rm -rf $(VENV_NAME) build/ dist/

.PHONY: venv test clean
