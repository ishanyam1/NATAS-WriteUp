# NATAS_3 WriteUp
:computer: Host: http://natas3.natas.labs.overthewire.org/  
:bust_in_silhouette: Usename: natas3  
:lock: Password: G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q

:triangular_flag_on_post: Flag: tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm

## Обзор веб-приложения
Веб-приложение выглядит следующим образом
![Скриншот веб-приложения](./img/natas3/natas3_0.png)

Функционал не представлен никакой

## Решение
В HTML коде страницы видим комментарий с намёком на то, что стоит проверить ``/robots.txt``
![Код страницы](img/natas3/natas3_1.png)

В файле ``robots.txt`` находим указание на секретный ресурс
![Файл /robots.txt](img/natas3/natas3_2.png)

На секретном ресурсе видим файл ``users.txt``
![Содержимое секретного ресурса](img/natas3/natas3_3.png)

А в файле ``users.txt`` видим флаг
![Файл users.txt](img/natas3/natas3_4.png)

Полученный флаг: tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm