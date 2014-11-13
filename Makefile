install:
	sudo apt-get update
	sudo apt-get install --yes mplayer python-pip
	sudo pip install Flask Flask-Bootstrap
	sudo cp chooseChanel.sh /usr/local/bin/
	sudo chmod 755 /usr/local/bin/chooseChanel.sh
	sudo cp vol /usr/local/bin/
	sudo chmod 755 /usr/local/bin/vol