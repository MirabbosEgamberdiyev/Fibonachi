# while True:
#     a=int(input("Iltimos bironta son kiriting => "))
#     fibonacci_numbers=[0,1]
#     def fibonacci(a):
#         if a>=0:
            
#                 if a==0:
#                     return 0
#                 elif a==1:
#                     return [0,1]
#                 else:
#                     fibonacci(a-1)
#                     return fibonacci_numbers.append(fibonacci_numbers[-1]+fibonacci_numbers[-2])
#         else:
#             print("Iltimos musbat son kiriting ")        
#     fibonacci(a)
#     print(fibonacci_numbers)

# a = int(input("Iltimos bironta son kiriting => "))
# b = int(input("Iltimos bironta son kiriting => "))

# fibonacci_numbers = [0, 1]
# fibonacci_numbers1 = [0, 1]

# def fibonacci(a, b):
#     if a >= 0 and b >= 0:
#         if a > b:
#             if a == 0:
#                 return [0]
#             elif a == 1:
#                 return fibonacci_numbers
#             else:
#                 fibonacci(a - 1, b)
#                 fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
#                 return fibonacci_numbers
#         elif b == 0:
#             return [0]
#         elif b == 1:
#             return fibonacci_numbers1
#         else:
#             fibonacci(b - 1)
#             fibonacci_numbers1.append(fibonacci_numbers1[-1] + fibonacci_numbers1[-2])
#             return fibonacci_numbers1
#     else:
#         raise ValueError("Bu sonlar orasida fibonacci sonlari mavjud emas")

# result = fibonacci(a, b)
# print(result)
