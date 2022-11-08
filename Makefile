start:
	git checkout main
	git pull
	cd tui && make setup
	cd tui && poetry run python src/main.py
ca:
	git add .
	git commit -m "commit all"
	git push origin head
