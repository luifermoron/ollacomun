echo "### Pulling changes ###"
git pull origin master

echo "### Stop old version ###"
docker-compose down
rm -rf /home/ubuntu/ollacomun/static

echo "### Start Server ###"
docker-compose up --build -d

echo "### Run Migration ###"
docker-compose run backend python manage.py migrate

echo "### Collect Static ###"
docker-compose run backend python manage.py collectstatic

echo "### Move Statics ###"
sudo rm -rf /var/www/static
sudo cp -R /home/ubuntu/ollacomun/static /var/www/static
sudo chgrp -R www-data /var/www/static