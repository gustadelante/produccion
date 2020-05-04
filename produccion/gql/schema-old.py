import graphene
from items.models import Movie
from bajadas.models import bajada
from graphene_django.types import DjangoObjectType

# api-bajada-model
class BajadaType(DjangoObjectType):
    id = graphene.Int()
    ancho = graphene.Int()
    diametro = graphene.Int()
    gramaje = graphene.Int()
    peso = graphene.Int()
    bobinanro = graphene.Int()
    ofnro = graphene.Int()
    fecha = graphene.types.datetime.Date()
    turno = graphene.String()
    calidad = graphene.Int()
    fechacreacion = graphene.types.datetime.Date()

    class Meta:
        model = bajada

    def resolve_id(self, info):
        return self.id
    
    def resolve_ancho(self, info):
        return self.ancho

    def resolve_turno(self, info):
        return self.turno

    #def resolve_summary(self, info):
    #    return self.summary

    #def resolve_poster_url(self, info):
        # Note: in client side app snake_case fields
        # will be resolved as camelCase
        # Eg: poster_url ==> posterUrl
    #    return self.poster_url

    #def resolve_slug(self, info):
    #    return self.slug

# api-movie-model
class MovieType(DjangoObjectType):
    id = graphene.Int()
    name = graphene.String()
    year = graphene.Int()
    summary = graphene.String()
    poster_url = graphene.String()
    slug = graphene.String()

    class Meta:
        model = Movie

    def resolve_id(self, info):
        return self.id
    
    def resolve_name(self, info):
        return self.name

    def resolve_year(self, info):
        return self.year

    def resolve_summary(self, info):
        return self.summary

    def resolve_poster_url(self, info):
        # Note: in client side app snake_case fields
        # will be resolved as camelCase
        # Eg: poster_url ==> posterUrl
        return self.poster_url

    def resolve_slug(self, info):
        return self.slug


class Query(graphene.ObjectType):
    movie_list = graphene.List(MovieType)
    movie = graphene.Field(MovieType, slug=graphene.String())
    bajada_list = graphene.List(BajadaType)
    bajada = graphene.List(BajadaType)


    def resolve_movie_list(self, info, *_):
        # for large lists only query what you need
        return Movie.objects.all().only("name", "poster_url", "slug")
    
    def resolve_movie(self, info, slug):
        movie_queryset = Movie.objects.filter(slug=slug)
        if movie_queryset.exists():
            return movie_queryset.first()

    def resolve_bajada_list(self, info, *_):
        # for large lists only query what you need
        return bajada.objects.all().only("id", "ancho", "turno")
    
    def resolve_bajada(self, info, id):
        bajada_queryset = Bajada.objects.filter(id=id)
        if bajada_queryset.exists():
            return bajada_queryset.first()

schema = graphene.Schema(query=Query)