from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.authtoken.models import Token
from rest_framework import viewsets, generics, status
from django_todo_app.models import Tasks, AppUser
from django_todo_app.serializers import TasksSerializer, AppUserSerializer
from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication


class TasksView(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = (IsAuthenticated,)
    
    def create(self, request):
        current_user_id = request.user.id
        print(current_user_id, request.data['text'])
        current_user = AppUser.objects.get(id = current_user_id)
        new_task = Tasks.objects.create(completed_date=request.data['completed_date'],
                                        text=request.data['text'], 
                                        is_completed=request.data['is_completed'], 
                                        author=current_user)
        print(TasksSerializer(new_task).data)
        return Response(TasksSerializer(new_task).data)

    def list(self, request):
        tasks = Tasks.objects.filter(author=request.user.id).all()
        task_serialized = TasksSerializer(tasks, many=True, context={'request': request})
        return Response(task_serialized.data)
    
    def retrieve(self, request, pk=None):
        tasks = Tasks.objects.filter(pk=pk, author=request.user.id).all()
        task_serialized = TasksSerializer(tasks, many=True)
        return Response(task_serialized.data)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk=None):
        # print(request.data['id'])
        task = Tasks.objects.get(pk=pk)
        task.is_completed = request.data['is_completed']
        task.save()
        task_serializer = TasksSerializer(task)
        return Response(task_serializer.data)


class AppUserCreate(generics.CreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    permission_classes = (AllowAny, )

