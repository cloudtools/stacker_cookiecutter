REGION=us-east-1


POETRY := $(shell command -v poetry 2> /dev/null)

setup:
ifndef POETRY
	$(error "poetry is not available, please install 'pip install poetry'")
endif
	poetry install

test:
	poetry develop
	poetry run python setup.py nosetests

prod: setup
	poetry run stacker build --region ${REGION} ${ARGS} conf/prod.env stacker.yaml

dev: setup
	poetry run stacker build --region ${REGION} ${ARGS} conf/dev.env stacker.yaml

destroy-dev: setup
	poetry run stacker destroy --region ${REGION} ${ARGS} conf/dev.env stacker.yaml

destroy-prod: setup
	poetry run stacker destroy --region ${REGION} ${ARGS} conf/prod.env stacker.yaml
