def check_access(name: str, age: int) -> str:
    
    # Валидация входных данных
    if not name.strip():
        raise ValueError("Имя не может быть пустым")
    if age < 0 or age > 120:
        raise ValueError("Некорректный возраст")

    if age >= 18:
        print(f"[{name}] Доступ разрешен")
    else:
        print(f"[{name}] Доступ запрещен")
        
    return f"Возраст через год: {age + 1}"

# Тестовые данные (последний пользователь с пустым именем вызовет ошибку)
users = [
    {"name": "Алиса", "age": 20},
    {"name": "Боб", "age": 15},
    {"name": " ", "age": 30}
]

for user in users:
    try:
        result = check_access(user["name"], user["age"])
        print(f"  -> {result}")
    except ValueError as e:
        print(f"  -> Ошибка: {e}")
