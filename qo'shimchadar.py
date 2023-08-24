# print(dir(tuple))
# print(dir(list))
# print(dir(set))
# print(dir(dict))
# list1=[]
# def range_my(son):
#     if son==0:
#         return 0
#     range_my(son-1)
#     list1.append(son)
# range_my(10)
# print(list1)
# class Range:
#     def __init__(self, stop) -> None:
#         self.start=-1
#         self.stop=stop
#     def __iter__(self):
#         print("Iter ishladi ")
#         return self
#     def __next__(self):
#         if self.start==self.stop:
#             raise StopAsyncIteration
#         self.start+=1
#         return self.start
    
# a = Range (23)
# for i in a:
#     print(i)    
        
            
 
# class My_range:
#     def __init__(self, stop, start, stap) -> None:
#         self.start=start
#         self.stop=stop
#         self.stap=stap
#     def __iter__(self):
#         print("Iter ishladi ")
#         return self
#     def __next__(self):
#         if self.stop==self.start:
#             raise StopAsyncIteration
#         self.start+=  self.stap
#         return self.start
# a= My_range(10, 1,3)
# for i in a:
#     print(i)    



def sana():
    yield 12
    yield 120
    yield 120
    yield 120
    yield 120
    yield 120
    yield 120
    yield 120
    yield 120
    yield 120
    yield 120
    yield 120
    yield 120
    yield 120
a = sana()
for i in a:
    print(i)