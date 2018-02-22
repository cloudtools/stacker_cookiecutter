REGION=us-east-1

build:
	docker build -t remind101/stacks .

test:
	python setup.py nosetests

prod:
	stacker build --region ${REGION} ${ARGS} conf/prod.env stacker.yaml

dev:
	stacker build --region ${REGION} ${ARGS} conf/dev.env stacker.yaml
