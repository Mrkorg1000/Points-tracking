# Test Case

### Points Tracking


### Задание:

- Сделать сервер по сбору и выдаче параметров.

- Таблица 1  "Point"
  Содержит данные объектов, альясы

  poind_id: Int
  
  name: String
  
  alias: String


- Таблица 2 "GPS"
  Содержится данные геоположения
 
  gps_id - счетчик общий по все таблице
  
  Point_id  - id поинта (таблица 1)
  
  Point_gps_id - счетчик поинта, порядковый номер записи для каждого поинта
  
  lat: Float
  
  lon: Float
  
  speed: Float
  
  time - время записи



### Стэк:

- fast api
- Postgresql 
- SqlAlchemy

## Инструкция

Для поднятия проекта в Docker:

Замените ".env.example" на ".env"

Запускаем команду  -  `docker compose build`

Запускаем проект  -  `docker compose up -d`
