# load_balance_nginx

Start:

    docker-compose build
    docker-compose up --scale app=2 -d
    docker-compose logs -t -f

Access: http://localhost/

Stop:

    docker-compose down
