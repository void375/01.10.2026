def check_access(name: str, age: int) -> str:
    if age >= 18:
        print("Доступ разрешен")
    else:
        print("Доступ запрещен")
        
    print(f"Имя пользователя: {name}")
    
    message = f"Возраст через год: {age + 1}"
    return message

check_access("Алиса", 20)
