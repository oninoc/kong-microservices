up: run

build:
	docker compose -f "docker-compose.kong.yml" -f "docker-compose.local.yml" build
run:
	docker compose -f "docker-compose.kong.yml" -f "docker-compose.local.yml" up
logs:
	docker compose -f "docker-compose.kong.yml" -f "docker-compose.local.yml" logs -f
run:
	docker compose -f "docker-compose.kong.yml" -f "docker-compose.local.yml" down