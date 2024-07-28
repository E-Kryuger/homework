from functools import wraps


def log(filename=None):
    """Декоратор для логирования результатов функции или возникших ошибок"""

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            try:

                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="windows-1251") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result

            except Exception as exc_info:

                if filename:
                    with open(filename, "a", encoding="windows-1251") as file:
                        file.write(f"{func.__name__} error: {str(exc_info)}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {str(exc_info)}. Inputs: {args}, {kwargs}")

        return wrapper

    return decorator
