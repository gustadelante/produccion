import graphene
from items.models import Movie
from bajadas.models import bajada
from graphene_django.types import DjangoObjectType

class BajadaType(DjangoObjectType):
    class Meta:
        model = bajada

class Query(graphene.ObjectType):
    bajada_list = graphene.List(BajadaType)
    bajada = graphene.List(BajadaType)

    def resolve_bajada_list(self, info, *_):
            # for large lists only query what you need
            #return bajada.objects.all().only("id", "ancho", "turno")
            return bajada.objects.all()
            
    def resolve_bajada(self, info, id):
        bajada_queryset = Bajada.objects.filter(id=id)
        if bajada_queryset.exists():
            return bajada_queryset.first()

class CreateBajada(graphene.Mutation):
    bajada = graphene.Field(BajadaType)

    class Arguments:
        #id = graphene.Int()
        ancho = graphene.Int()
        diametro = graphene.Int()
        gramaje = graphene.Int()
        peso = graphene.Int()
        bobinanro = graphene.Int()
        ofnro = graphene.Int()
        turno = graphene.String()
        calidad = graphene.Int()

    def mutate(self, info, ancho, diametro, gramaje, peso, bobinanro, ofnro, turno, calidad):
        bajada1 = bajada(ancho=ancho, diametro=diametro, gramaje=gramaje, peso=peso, 
        bobinanro=bobinanro, ofnro=ofnro, turno=turno, calidad=calidad)
        bajada1.save()
        return CreateBajada(bajada=bajada1)

class Mutation(graphene.ObjectType):
    create_bajada = CreateBajada.Field()


        





