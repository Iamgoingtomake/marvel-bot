build:
	docker build -t marvel-bot .

start:
	docker run --name marvelbot -d marvel-bot

test:
	docker exec marvelbot python -m pytest