import functools

def get_image_path(image_name):
    return f"../images/{image_name}"

@functools.lru_cache(maxsize=None)
def fibonacci(n):
    if(n <= 1):
        return 1
    return fibonacci(n-1) + fibonacci(n-2) 

def fibonacci_no_cache(n):
    if(n <= 1):
        return 1
    return fibonacci_no_cache(n-1) + fibonacci_no_cache(n-2) 