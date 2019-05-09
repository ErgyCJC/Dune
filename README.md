# Dune
[![Build Status](https://travis-ci.org/ErgyCJC/Dune.svg?branch=master)](https://travis-ci.org/ErgyCJC/Dune)

### Описание

Игра происходит на квадратном поле 16x16 между двумя фракциями: Fremen - игрок, House Harkonnen - компьютер. Ходы совершаются поочередно игроком и компьютером. Цель - уничтожить начальную базу противника.
У фракции Fremen база - Village, у House Harkonnen - Harvester.

Изначально каждой стороне даётся по 10 единиц пряности (melange). Её можно тратить на покупку unit'ов.

Стоимости:

|Unit|Стоимость|
|---|---|
|Flyer|9|
|Division|9|
|Village|12|

Подвижность (максимальное манхэттенское расстояние перемещения за 1 ход):

|Unit|Подвижность|
|---|---|
|Flyer|4|
|Division|2|
|Village|Неподвижна|

Здоровье:

|Unit|Здоровье|
|---|---|
|Flyer)|25|
|Division (Fremen)|75|
|Division (Harkonnen)|50|
|Village|400|
|Harvester|250|

Мощность атаки за один ход:

|Unit|Damage|
|---|---|
|Flyer|15|
|Division (Fremen)|35|
|Division (Harkonnen)|25|

За каждый ход unit'ы типа 'база' производят некоторое кол-во пряности, атакованная база в течение 3 ходов не производит пряность:

|Unit|Пряность|
|---|---|
|Village|4|
|Harvester|9|

##### Обозначения

+ `.` - пустое поле
+ `%` - Flyer
+ `*` - Division
+ `@` - Motherbase

##### Команды

+ `create <x> <y> <description>` - создание unit'а, `description` - division, flyer, village
+ `move <x_from> <y_from> <x_to> <y_to>` - переместить свой unit из `(x_from, y_from)` в `(x_to, y_to)`
+ `attack <attacker_x> <attacker_y> <enemy_x> <enemy_y>` - атака unit'ом в `(attacker_x, attacker_y)` unit'а в `(enemy_x, enemy_y)`
+ `pass` - пропустить ход
+ `exit` - выйти из игры

### Из заданий

+ Command* - классы формируемых команд, для исполнения действий в игре (move, attack, create)
+ *Strategy - классы стратегий, получающие состояние доски и формирующие команду для хода в игре (пример - RobotStrategy для игры компьютера)
+ WarriorsUnion и производные от него классы Army, Corps - скомпонованные военные подразделения, имеющие в своей струтуре объекты с таким же поведением
+ AttackedDecorator и ReconstructedDecorator - декораторы для баз для изменения производства пряности после атаки на них

### Установка (подготовка окружения)

`pip3 install -r requirements.txt`

### Запуск
`$ python3 sources/main.py`

### Тестирование
+ `$ pytest sources/` в корневой директории репозитория
+ `$ pytest` в директории `sources`

### CI

Используется сервис Travis-CI. Уведомления о всех build'ах (как удачных, так и неудачных) отправляются на email-адрес `tp.address.ergycjc@gmail.com` Проверка осуществляется под `python3.6` и `python3.7`.

Файл конфигурации - `.travis.yml`.
