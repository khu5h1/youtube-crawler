# youtube-crawler


## To run the project inside a container using docker
1. Create a .env file and add your google API key there with the name of variable being `GOOGLE_API_KEY`.
2. Run the `docker-compose up` command.

## To run the project locally use the below mentioned commands
1. Run `pip install -r requirements.txt`
2. Create a .env file and add your google API key there with the name of variable being `GOOGLE_API_KEY`.
3. Run `python manage.py migrate`.
4. Run `python manage.py crontab add` to initate the cron job to pull youtube videos.
5. Run the server using `python manage.py runserver`.
