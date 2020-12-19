start:
	@echo "Starting FastAPI app"
	@echo "--------------------"
	python app/main.py

hash:
	python tools/hash.py

help:
	@echo "start - Start FastAPI app"
	@echo "stop - To stop FastAPI app [CTRL + c]"