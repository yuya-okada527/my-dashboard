setup:
	pyenv install -s 3.10.6
ca:
	git add .
	git commit -m "commit all"
	git push origin head
