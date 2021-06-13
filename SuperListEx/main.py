class SuperList(list, dict):
    def __len__(self):
        return 1000

    pass


super_list1 = SuperList()
print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(list, object))  # is list subclass of object??
