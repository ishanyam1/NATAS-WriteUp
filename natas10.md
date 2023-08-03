# NATAS_10 WriteUp
:computer: Host: http://natas10.natas.labs.overthewire.org/  
:bust_in_silhouette: Usename: natas10  
:key: Password: D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE

:triangular_flag_on_post: Flag: 1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg

## Обзор веб-приложения
Веб-приложение выглядит следующим образом
![Скриншот веб-приложения](./img/natas10/natas10_0.png)

Ввод слова ``test`` привёл к вот такой реакции 
![Скриншот веб-приложения](./img/natas10/natas10_1.png)

Кнопка <kbd>**View sourcecode**</kbd> позволяет просмотреть исходный код страницы
![Скриншот исходного кода](./img/natas10/natas10_2.png)

## Решение
В исходном коде веб-приложения видим фильтр символов `` [ ; | & ] ``, что не позволяет нам встроить свою команду на исполнение  
![Фильтр ввода](img/natas10/natas10_3.png)

В данном случае мы вынуждены нарушить логику работы команды ``grep`` таким образом, чтобы она вывела нам флаг  

:space_invader: Payload: ``-r .* /etc/natas_webpass/ # ``  

![Получение флага](img/natas10/natas10_4.png)

Полученный флаг: 1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg
