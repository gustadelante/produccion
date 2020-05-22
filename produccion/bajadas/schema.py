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
        user = info.context.user

        if user.is_anonymous:
            raise Exception('Log in para agregar bajada.')
        
        bajada1 = bajada(ancho=ancho, diametro=diametro, gramaje=gramaje, peso=peso, 
        bobinanro=bobinanro, ofnro=ofnro, turno=turno, calidad=calidad, usuariocreacion=user)
        bajada1.save()
        return CreateBajada(bajada=bajada1)

class UpdateBajada(graphene.Mutation):
    bajada = graphene.Field(BajadaType)

    class Arguments:
        bajada_id = graphene.Int(required=True)
        ancho = graphene.Int()
        diametro = graphene.Int()
        gramaje = graphene.Int()
        peso = graphene.Int()
        bobinanro = graphene.Int()
        ofnro = graphene.Int()
        turno = graphene.String()
        calidad = graphene.Int()

    def mutate(self, info, bajada_id, ancho, diametro, gramaje, peso, bobinanro, ofnro, turno,
     calidad):

        user = info.context.user
        bajada2 = bajada.objects.get(id=bajada_id)

        #if bajada.usuariocreacion != user:
        #    raise Exception('No permitido usuario diferente.')
        #if user.is_anonymous:
        #    raise Exception('Log in para agregar bajada.')

        bajada2.ancho = ancho
        bajada2.diametro = diametro
        bajada2.gramaje = gramaje
        bajada2.peso = peso
        bajada2.bobinanro = bobinanro
        bajada2.ofnro = ofnro
        bajada2.turno = turno
        bajada2.calidad = calidad

        bajada2.save()

        return UpdateBajada(bajada=bajada2)

class DeleteBajada(graphene.Mutation):
    bajada_id = graphene.Int()

    class Arguments:
        bajada_id = graphene.Int(required=True)

    def mutate(self, info, bajada_id):
        user = info.context.user
        bajada3 = bajada.objects.get(id=bajada_id)

        #if user.is_anonymous:
        #    raise Exception('Log in para agregar bajada.')

        bajada3.delete()

        return DeleteBajada(bajada_id=bajada_id)


class Mutation(graphene.ObjectType):
    create_bajada = CreateBajada.Field()
    update_bajada = UpdateBajada.Field()
    delete_bajada = DeleteBajada.Field()


        





