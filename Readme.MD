[![Pylint](https://github.com/iwizard7/redis-random-data-generator/actions/workflows/pylint.yml/badge.svg)](https://github.com/iwizard7/redis-random-data-generator/actions/workflows/pylint.yml) [![CodeQL](https://github.com/iwizard7/redis-random-data-generator/actions/workflows/codeql.yml/badge.svg)](https://github.com/iwizard7/redis-random-data-generator/actions/workflows/codeql.yml)![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/iwizard7/redis-random-data-generator) ![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/iwizard7/redis-random-data-generator)
# Redis Random Data Generator ⚙️

## Описание

Этот скрипт на Python предназначен для генерации и загрузки случайных данных различных типов в Redis. Он использует библиотеки `redis`, `Faker` и `argparse` для создания данных и управления параметрами командной строки.

## Возможности

- Генерация случайных данных для различных типов Redis: строки, списки, множества, упорядоченные множества и хэши.
- Конфигурация параметров подключения и количества записей через аргументы командной строки.
- Обработка ошибок подключения к Redis и выполнения операций.

## Установка

1. Убедитесь, что у вас установлен Python 3.6 или новее.
2. Установите необходимые библиотеки с помощью pip:

   ```bash
   pip install redis faker
   ```

## Использование

Запустите скрипт, передав необходимые параметры:

```bash
python random_gen.py --host <REDIS_HOST> --port <REDIS_PORT> --db <REDIS_DB> --num <NUM_ENTRIES>
```

Где:
- `<REDIS_HOST>` — хост Redis сервера (по умолчанию `localhost`).
- `<REDIS_PORT>` — порт Redis сервера (по умолчанию `6379`).
- `<REDIS_DB>` — номер базы данных Redis (по умолчанию `0`).
- `<NUM_ENTRIES>` — количество записей для вставки (по умолчанию `100`).

### Пример

```bash
python random_gen.py --host 127.0.0.1 --port 6379 --db 0 --num 100
```

Этот пример создаст 100 случайных записей и загрузит их в базу данных Redis на локальном сервере.

## Примечания

- Убедитесь, что Redis сервер запущен и доступен по указанному хосту и порту.
- Скрипт обрабатывает ошибки подключения и выполнения операций, чтобы помочь вам выявить возможные проблемы.

## Вклад

Если вы хотите внести вклад в проект, пожалуйста, создайте запрос на изменение (pull request) с описанием внесенных изменений. Мы будем рады вашим предложениям и улучшениям!

## Лицензия

Этот проект лицензируется под [MIT License](LICENSE).
