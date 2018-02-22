REGION=us-east-1

setup:
	pipenv install

test:
	pipenv install --dev
	pipenv run python setup.py nosetests

prod: setup
	pipenv run stacker build --region ${REGION} ${ARGS} conf/prod.env stacker.yaml

dev: setup
	pipenv run stacker build --region ${REGION} ${ARGS} conf/dev.env stacker.yaml

destroy-dev: setup
	pipenv run stacker destroy --region ${REGION} ${ARGS} conf/dev.env stacker.yaml

destroy-prod: setup
	pipenv run stacker destroy --region ${REGION} ${ARGS} conf/prod.env stacker.yaml
