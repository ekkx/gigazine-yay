#? help: ヘルプコマンド
help: Makefile
	@echo ""
	@echo "Usage:"
	@echo "  make [target]"
	@echo ""
	@echo "Targets:"
	@sed -n "s/^#?//p" $< | column -t -s ":"
.PHONY: help

#? build: アプリケーションのセットアップ
build:
	docker compose build --no-cache
.PHONY: build

#? up: アプリケーションの起動
up:
	docker compose up -d
.PHONY: up

#? down: アプリケーションの停止
down:
	docker compose down
.PHONY: down
