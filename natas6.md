# NATAS_6 WriteUp
:computer: Host: http://natas6.natas.labs.overthewire.org/  
:bust_in_silhouette: Usename: natas6  
:lock: Password: fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR

:triangular_flag_on_post: Flag: jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr

## Обзор веб-приложения
Веб-приложение выглядит следующим образом
![Скриншот веб-приложения](./img/natas6/natas6_0.png)

Форма ввода секретного слова в самом деле работает. Ввод слова ``test`` привёл к вот такой реакции  
![Скриншот веб-приложения](./img/natas6/natas6_1.png)

Кнопка <kbd>**View sourcecode**</kbd> позволяет просмотреть исходный код страницы
![Скриншот исходного кода](./img/natas6/natas6_2.png)


## Решение
В исходном коде мы видим директиву ``include``, которая подключает какой-то ``secret.inc``
![Директива include](img/natas6/natas6_3.png)

Проверим этот файл и получим в ответ секретное слово - ``FOEIUWGHFEEUHOFUOIU``
![Секретное слово](img/natas6/natas6_4.png)  

Введём этот секрет на главной странице и получим в ответ флаг
![Получение флага](img/natas6/natas6_5.png)  


Полученный флаг: jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr
