# Функции 

## Содержание  

[Базовые требования](#Базовые-требования)  
[Не забыть](#Не-забыть)    


----
## Базовые требования    
**Именование**    
Описательные имена    

**Чистота**  
Не зависит от глобальных объектов  
Нет побочных эффектов (ничего не меняет в глобальной области видимости)    
Возвращает один и тот же результат при одних и тех же входных данных  

**Документация**  
PEP 257  

**Аннотации типов**  
PEP 484  

**Минимизация аргументов**  
Если функция принимает слишком много параметров, следует:    
- Использовать *args, **kwargs   
- Упаковать в какую-нибудь стркутуру данных  

**Обработка ошибок**  
Понятные сообщения об ошибках  


----
## Не забыть  
1. *args, **kwargs   
2. Распаковка * и **  
