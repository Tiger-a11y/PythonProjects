#
# class First_ten:
#     def __init__(self):
#         self.num1 = 1
#         self.num2 = 11
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.num1 < self.num2:
#             value = self.num1
#             self.num1 += 1
#
#             return value
#         else:
#            raise StopIteration
#
# values = First_ten()
#
# for i in values:
#     print(i)


# Here is an example of a python inbuilt iterator
# value can be anything which can be iterate
iterable_value = 'Geeks'
iterable_obj = iter(iterable_value)

while True:
    try:
        # Iterate by calling next
        item = next(iterable_obj)
        print(item)
    except StopIteration:

        # exception will happen when iteration will over
        break

# for i in iterable_value:
#     print(i)