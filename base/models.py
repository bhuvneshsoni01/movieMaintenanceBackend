from django.db import models
import uuid

# Create your models here.

class Movie(models.Model):
    # id                  = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    title               = models.CharField(max_length=100)
    description         = models.TextField(max_length=200)
    release_D           = models.DateField()
    no_of_votes         = models.IntegerField(default=10)
    # number_of_actors    = models.IntegerField(default=0)

    @property
    def upvote(self):
        self.no_of_votes += 1

    @property
    def downvote(self):
        self.no_of_votes -= 1

    # @property
    # def title(self):
    #     return self.title


class Actor(models.Model):
    # id                  = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name                = models.CharField(max_length=100)
    dob                 = models.DateField()
    # number_of_movies    = models.IntegerField(default=0)



class Relationship(models.Model):
    # movie_name = models.CharField(max_length=100, default="")
    # actor_name = models.CharField(max_length=100, default="")
    movie               = models.ForeignKey("Movie", on_delete=models.CASCADE, default="")
    actor               = models.ForeignKey("Actor", on_delete=models.CASCADE, default="")

    @property
    def title(self):
        return self.movie.title

    @property
    def name(self):
        return self.actor.name
