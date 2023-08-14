install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py

format:
	black ./

test:
	python -m pytest -vv --cov=hello test_hello.py

docker-build:
	docker build -t mlops .

docker-run:
	docker run -p 5000:5000 mlops

docker-debug:
	#to debug inside the container
	docker run -d -p 5000:5000 --name mlops-container mlops
	docker exec -it mlops-container bash

docker-clean:
	#remove all images locally
	if [ -n "$$(docker images -aq)" ]; then \
		docker rmi -f $$(docker images -aq); \
	fi

all:
	install lint test
