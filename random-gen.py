import redis
from faker import Faker
import random
import argparse

# Создайте объект Faker для генерации случайных данных
fake = Faker()


# Функция для генерации случайных данных для различных типов Redis
def populate_redis(host, port, db, num_entries):
    # Создайте объект Redis-клиента с заданными параметрами
    try:
        r = redis.Redis(host=host, port=port, db=db)
        print(f'Connected to Redis at {host}:{port}, database {db}')
    except Exception as e:
        print(f'Error connecting to Redis: {e}')
        return

    for _ in range(num_entries):
        # Генерация случайного типа данных
        data_type = random.choice(['string', 'list', 'set', 'zset', 'hash'])
        key = fake.uuid4()

        try:
            if data_type == 'string':
                value = fake.sentence()
                r.set(key, value)
                print(f'Set string key: {key}, value: {value}')

            elif data_type == 'list':
                values = [fake.word() for _ in range(random.randint(1, 10))]
                r.rpush(key, *values)
                print(f'Set list key: {key}, values: {values}')

            elif data_type == 'set':
                values = {fake.word() for _ in range(random.randint(1, 10))}
                r.sadd(key, *values)
                print(f'Set set key: {key}, values: {values}')

            elif data_type == 'zset':
                values = {fake.word(): random.uniform(1, 100) for _ in range(random.randint(1, 10))}
                r.zadd(key, {member: score for member, score in values.items()})
                print(f'Set zset key: {key}, values: {values}')

            elif data_type == 'hash':
                fields = {fake.word(): fake.sentence() for _ in range(random.randint(1, 10))}
                r.hset(key, mapping=fields)
                print(f'Set hash key: {key}, fields: {fields}')

        except Exception as e:
            print(f'Error setting key {key}: {e}')


# Основная функция для парсинга аргументов и запуска скрипта
def main():
    parser = argparse.ArgumentParser(description='Populate Redis with random data.')
    parser.add_argument('--host', type=str, default='localhost', help='Redis server host')
    parser.add_argument('--port', type=int, default=6379, help='Redis server port')
    parser.add_argument('--db', type=int, default=0, help='Redis database number')
    parser.add_argument('--num', type=int, default=100, help='Number of records to insert')

    args = parser.parse_args()

    populate_redis(args.host, args.port, args.db, args.num)


if __name__ == '__main__':
    main()