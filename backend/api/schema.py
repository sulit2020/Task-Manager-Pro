import graphene
from graphene_django import DjangoObjectType
from .models import Task

class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = ("id", "title", "completed")

class Query(graphene.ObjectType):
    all_tasks = graphene.List(TaskType)
    task = graphene.Field(TaskType, id=graphene.Int())

    def resolve_all_tasks(root,info):
        return Task.objects.all()
    
    def resolve_task(root,info,id):
        return Task.objects.get(pk=id)
    
class CreateTask(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)

    task = graphene.Field(TaskType)

    def mutate(self,info,title):
        task = Task(title=title)
        task.save()
        return CreateTask(task=task)

class UpdateTask(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        completed = graphene.Boolean(required=True)

    task = graphene.Field(TaskType)

    def mutate(self,info,id, completed):
        task = Task.objects.get(pk=id)
        task.completed =completed
        task.save()
        return UpdateTask(task=task)

class Mutation(graphene.ObjectType):
    create_task = CreateTask.Field()
    update_task = UpdateTask.Field()