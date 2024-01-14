from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=20,null=True)
    email = models.EmailField(unique=True,null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True,default="studybud/static/images/avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []





# the room will the child of a topic 

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# # a topic can have multiple rooms 
# # topic : Room --- 1:M  pk of topic to room 
# # Room:  host 1:1 but but host :Rooom 1:M
# # Room:host
# # 1:1
# # M:1
# # Finall 1:M 

class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null = True)

    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null = True);
    name = models.CharField(max_length=200)
    description = models.TextField(null = True , blank=True)
    # description can be null , when we submit a form that can be empty
    participants =  models.ManyToManyField(User,related_name='participants',blank=True)
#     # currently active in  room
#     updated = models.DateTimeField(auto_now=True)
#     # take a snapshot to know hwen its updated
#     created = models.DateTimeField(auto_now_add = True)
#     # only take a snapshot when we create a instance 
#     # will never change 

#     class Meta:
#         ordering = ['updated','created']


#     def __str__(self):
#         return self.name
    


#     # django builds in a defualt user model (class )
# # when a room is deleted  all Message deleted
#     # a user can have many messages 1:M 
#     # in order to create a one to many relations
# # in 1 :M rel pk of 1 goes to the M 
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.body[0:50]




