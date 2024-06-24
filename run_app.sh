docker-compose --env-file ./.env -f docker-compose.yml up --build -d

docker exec -it asfitness-api-1 python manage.py migrate

echo 'Migrated migration files onto the PostgreSQL Database'

echo 'App is running'