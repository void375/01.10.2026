def check_access(name, age):
    if age >= 18:  # 1. Добавлено двоеточие
        print("Доступ разрешен")
    else:
        print("Доступ запрещен")
        
    print("Имя пользователя: " + name)  # 2. Исправлена опечатка (print)
    
    # 3. Число преобразовано в строку через str()
    message = "Возраст через год: " + str(age + 1) 
    return message

check_access("Алиса", 20)