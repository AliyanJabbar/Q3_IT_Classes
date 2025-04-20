# 1.
# def buckets():
#     items :list= ["iphone"]
#     return items

# 2.
from dataclasses import dataclass
@dataclass()  # this is decorator # we are using it so that the Buckets class can take bucket_name as an argument in test_buckets. So here dataclass is an extra layer on Buckets class. 
class Buckets(): #class is not taking any argument but we will give an argument in class in test_buckets
    bucket_name: str  # variable in a class is called an attribute
    items = []

    def add_item(self, item: str):  # function in a class is called method
        self.items.append(
            item
        )  # will use self to access attribute present in the class
