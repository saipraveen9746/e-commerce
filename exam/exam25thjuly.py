class Book:
    def __init__(self,title,author,price,genre,topic,style):
        self.title = title
        self.author = author
        self.price = price
        self.genre = genre
        self.topic = topic
        self.style = style
    def getdetails(self):
        return self.title,self.author,self.price
class Fiction(Book):
    def getdetails(self):
        return self.genre



class Nonfiction(Fiction):
    def getdetails(self):
        return self.topic
class story(Nonfiction):
    def getdetails(self):
        return self.style

obj = Book("Ghasakinte ithihasam","o.v vijayan",300,"Mystery","History","sonnet")

print(obj.getdetails())

obj1 = Fiction("Ghasakinte ithihasam","o.v vijayan",300,"Mystery","History","sonnet")
print(obj1.getdetails())
obj2 = Nonfiction("Ghasakinte ithihasam","o.v vijayan",300,"Mystery","History","sonnet")
print(obj2.getdetails())
obj3 = story("Ghasakinte ithihasam","o.v vijayan",300,"Mystery","History","sonnet")
print(obj3.getdetails())
