SHELL := /bin/bash
COMPOSE := docker compose
IMAGE ?= devops-practice-lab:local
SCENARIO ?= dependency

.PHONY: doctor test build up down smoke observe incident recover verify privacy \
	aws-init aws-plan aws-apply aws-destroy aws-destroy-check k8s-load k8s-up k8s-down

doctor:
	@python3 scripts/doctor.py

test:
	@python3 -m unittest discover -s app/tests -v

build:
	docker build -t $(IMAGE) app

up:
	$(COMPOSE) up -d --build

down:
	$(COMPOSE) down --remove-orphans

smoke:
	@python3 scripts/smoke_test.py

observe:
	@echo "API:        http://localhost:$${APP_PORT:-8080}"
	@echo "Prometheus: http://localhost:9090"
	@echo "Grafana:    http://localhost:3000 (anonymous local access)"
	@echo "Loki:       http://localhost:3100/ready"

incident:
	@python3 scripts/incident.py "$(SCENARIO)"

recover:
	@python3 scripts/incident.py recover

privacy:
	@python3 scripts/privacy_check.py

verify: test privacy
	@python3 scripts/repo_check.py

aws-init:
	terraform -chdir=infra/terraform init

aws-plan:
	terraform -chdir=infra/terraform plan

aws-apply:
	@python3 scripts/cloud_guard.py
	terraform -chdir=infra/terraform apply

aws-destroy:
	terraform -chdir=infra/terraform destroy

aws-destroy-check:
	@python3 scripts/destroy_check.py

k8s-load: build
	kind load docker-image $(IMAGE) --name devops-lab

k8s-up:
	kubectl apply -k platform/kubernetes

k8s-down:
	kubectl delete -k platform/kubernetes --ignore-not-found
