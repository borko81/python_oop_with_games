n: int = 3
numbers = [2, 3, 7, 4, 8]
result = None

# while n > 0:
#     exec(input(f"{n} --> "))
#     n -= 1

if 0 <= n <= 10:
    print(f'{n} is between 0 and 10')

exec("result=sum(num for num in numbers if num % 2 == 0)")
print(result)

# name = input("Your name :"); print(f'Hello {name}')

code = """
random_numbers = [2, 1, 6, 5]

def check_is_odd(n):
    return n & 1
 
print('Only odd number')   
print([r for r in filter(lambda x: check_is_odd(x), random_numbers)])
"""
compiled_code = compile(code, "<string>", "exec")
exec(compiled_code)
exec(compiled_code)

sum_two_numbers = """z=x+y"""
x: int = 2
y: int = 5
exec(sum_two_numbers)
print(z)




