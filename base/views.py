from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.shortcuts import redirect

from .models import Movie,Actor,Relationship
from .serializers import MovieSerializers,ActorSerializers,RelationshipSerializers
from collections import defaultdict
# Create your views here.


def defalut_return_val():
    return 0

@csrf_exempt
def movieAPI(request):
    if request.method == 'GET':
        print('in movies requests: ',request)
        movies_data = MovieSerializers(Movie.objects.all(),many=True)
        actor_count = defaultdict(defalut_return_val)

        for i in Relationship.objects.all():
            # print(i.title)
            actor_count[i.title] = actor_count[i.title]+1

        for i in movies_data.data:
            i.update({'numberOfActors' : actor_count[i['title']]})

        print()
        for i in movies_data.data:
            print(i)
        return JsonResponse(movies_data.data , safe=False)

@csrf_exempt
def movieVoteAPI(request):
    if request.method == 'PUT':
        print('in put request in movies')
        datatatata = JSONParser().parse(request)
        [movie_title , flag]  = [datatatata['title'] , datatatata['flag']]
        movies = Movie.objects.all()
        for i in movies:
            if i.title == movie_title:
                if flag == 'True':
                    i.upvote
                else:
                    i.downvote
                print("After upvoting movie votes = ",i.no_of_votes)


        for i in movies:
            movie = Movie.objects.get(pk=i.pk)
            movie.no_of_votes = i.no_of_votes
            movie.save()

        return JsonResponse("Upvoted successfully",safe =False)
        # movies_data = MovieSerializers(Movie.objects.all(),many=True)
        # actor_count = defaultdict(defalut_return_val)

        # for i in Relationship.objects.all():
        #     actor_count[i.title] = actor_count[i.title]+1

        # for i in movies_data.data:
        #     i.update({'numberOfActors' : actor_count[i['title']]})

        # return JsonResponse(movies_data.data , safe=False)

def actorAPI(request):
    if request.method == 'GET':
        relationship_data = RelationshipSerializers(Relationship.objects.all(),many=True)
        actors_data = ActorSerializers(Actor.objects.all(),many=True)
        # print(Actor.objects.all())
        # for i in Actor.objects.all():
        #     print(i)
        # # for ind,i in enumerate(actors_data.data):
        # #     print(i)
        # #     # name_of_this = i['name']
        # #     # i.update({'numberOfActors':Relationship.objects.raw('SELECT COUNT(*) FROM Relatoinship where movie=%s}',name_of_this)})
        # #     i.update({'numberOfMovies':count_dict[i['id']]})
        # # actorSerializers = ActorSerializers(actor , many=True)  ## mant=True repersent list or many items
        # # print(actorSerializers.data)
        # # RelationshipS = RelationshipSerializers(Relationship.objects.all(),many=True).data
        # # for i in RelationshipS:
        # #     print(i)
        # # print(relationship_data.data)

        
        movie_count = defaultdict(defalut_return_val)

        for i in Relationship.objects.all():
            # print(i.name)
            movie_count[i.name] = movie_count[i.name]+1

        # print()
        for i in actors_data.data:
            # print(i['name'])
            i.update({'numberOfMovies' : movie_count[i['name']]})

        print()
        for i in actors_data.data:
            print(i)
        return JsonResponse(actors_data.data , safe=False)


# def upvote_trigger(request):
#         print('Inside upvote trigger........................................')
#         movies_data = MovieSerializers(Movie.objects.all(),many=True)
#         for i in movies_data.data:
#             if i['title'] == 'request_title':
#                 i['no_of_votes'] += 1

# def downvote_trigger(request):
#         print('Inside downvote trigger........................................')
#         movies_data = MovieSerializers(Movie.objects.all(),many=True)
#         for i in movies_data.data:
#             if i['title'] == 'request_title':
#                 i['no_of_votes'] -= 1