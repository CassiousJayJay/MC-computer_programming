def main():
  fun_of_dict()
  fun_of_list()
  fun_of_tuple()

def fun_of_list():
  my_List = ["apple", "banana", "cherry", "date", "elderberry"]
  
  my_List = len(my_List)
  print("The length of my_List is: ", my_List)

  y = my_List.pop()
  print(y)

  my_List.insert(0, fig)
  print("The updated list is: ", + str(my_List))


def fun_of_tuple():
  my_tuple = (10, 20, 30, 40, 50)
  print("The length of my tuple is: ", len(my_tuple))

  i = my_tuple[4]
  print("The 4th element is: ", i)


def fun_of_dict():
  my_dict = {'name': 'John', 'age': 25, 'country': 'USA'}
  print(my_dict.get('name'))

  my_dict.update({'age': 26})
  print(my_dict.get('age'))


if __name__ == "__main__":
  main()