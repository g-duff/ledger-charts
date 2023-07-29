SHELL = /bin/sh

environment := ./.venv
environment_bin := ${environment}/bin

.PHONY: clean format

# Default Goal
dev_dependencies: .venv
	${environment_bin}/pip3 install --upgrade pip
	${environment_bin}/pip3 install -r ./requirements.txt

clean:
	rm -rf ${environment}

format:
	${environment_bin}/black --include ./ledger_charts/*py

.venv:
	python3 -m venv ${environment}
