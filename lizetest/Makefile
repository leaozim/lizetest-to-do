NAME 			:= fiscalize_on

up:
	@printf "Launch configuration $(NAME)...\n"
	@docker-compose -f ./docker-compose.yml --env-file .env up -d

build:
	@echo "[WARNING] SEE IF YOU SETUP DE ENV FILE"
	docker-compose -f ./docker-compose.yml build

down:
	@printf "Stopping configuration $(NAME)...\n"
	docker-compose -f ./docker-compose.yml down

clear:
	@printf "Cleaning configuration $(NAME)...\n"
	

ls:
	docker container ls
	docker image ls
	docker volume ls
	docker network ls -f type=custom

.PHONY: down clear build

