# NATAS_6 WriteUp
:computer: Host: http://natas6.natas.labs.overthewire.org/  
:bust_in_silhouette: Usename: natas6  
:key: Password: fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR

:triangular_flag_on_post: Flag: jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr

- [NATAS\_6 WriteUp](#natas_6-writeup)
  - [Обзор веб-приложения](#обзор-веб-приложения)
  - [Решение](#решение)

## Обзор веб-приложения
<a name="Обзор_веб-приложения"></a> 
Веб-приложение выглядит следующим образом
![Скриншот веб-приложения](./img/natas6/natas6_0.png)

Форма ввода секретного слова в самом деле работает. Ввод слова ``test`` привёл к вот такой реакции  
![Скриншот веб-приложения](./img/natas6/natas6_1.png)

Кнопка <kbd>**View sourcecode**</kbd> позволяет просмотреть исходный код страницы
```php
// HTML Code ...
<?
include "includes/secret.inc";
    if(array_key_exists("submit", $_POST)) {
        if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
    } else {
        print "Wrong secret";
    }
    }
?>
// HTML Code ...
```


## Решение
<a name="Решение"></a>
В исходном коде мы видим директиву ``include``, которая подключает какой-то ``secret.inc``
```php
include "includes/secret.inc";
```

Проверим этот файл и получим в ответ секретное слово - ``FOEIUWGHFEEUHOFUOIU``
![Секретное слово](img/natas6/natas6_4.png)  

Введём этот секрет на главной странице и получим в ответ флаг
![Получение флага](img/natas6/natas6_5.png)  


Полученный флаг: jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr
