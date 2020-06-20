build:
	docker build -t marvel-bot .

reset:
	docker rm marvelbot

start:
	docker run --name marvelbot -d marvel-bot

test:
	poetry run pytest

export:
	git archive master | gzip > latest.tgz