.PHONY: test build stage prod dev

REGION=us-east-1

build:
	docker build -t remind101/stacks .

test:
	python setup.py nosetests

{{cookiecutter.repo_name}}:
	stacker build --region ${REGION} ${ARGS} conf/{{cookiecutter.repo_name}}/${ENV_NAME}.env {{cookiecutter.repo_name}}.yaml
