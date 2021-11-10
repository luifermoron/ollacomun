echo "### Stop old version ###"
docker-compose down
rm -rf /root/apps/backend/static

echo "### Start Server ###"
docker-compose up --build -d

echo "### Run Migration ###"
docker-compose run backend python manage.py migrate

echo "### Collect Static ###"
docker-compose run backend python manage.py collectstatic

echo "### Move Statics ###"
rm -rf /var/www/static
cp -R /root/apps/backend/static /var/www/static
chgrp -R www-data /var/www/static