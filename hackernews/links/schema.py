from django.contrib.auth import get_user_model
import graphene
from graphene_django import DjangoObjectType

from .models import Link
from users.schema import UserType

class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    def resolve_links(self, info, **kwargs):
        return Link.objects.all()


class CreateLink(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()
    posted_by = graphene.Field(UserType)

    class Arguments:
        url = graphene.String()
        description = graphene.String()

    def mutate(self, info, url, description):
        ## Hack, requires one user to exist
        user = get_user_model().objects.all()[0]

        link = Link(
            url=url, 
            description=description, 
            posted_by=user
        )
        link.save()

        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description,
            posted_by=link.posted_by
        )


class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()