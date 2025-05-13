from abc import ABC, abstractmethod

class AbsClass(ABC):
    def print(self,x):
        self.x=x
        print("Passed value: ", x)
    @abstractmethod
    def task(self):
        print("We are inside AbsClass task")
class sub_class(AbsClass):
    def task(self):
        print("Inside subclass")
ob1=sub_class()
ob1.task()
ob1.print(234)