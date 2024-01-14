from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from rest_framework import status

class FoydalanuvchiView(generics.CreateAPIView):
    permission_classes = []
    queryset = Foydalanunvchi.objects.all()
    serializer_class = UserSerializer

class ProfileView(APIView):
    def get(self, request):
        foydalanuvchi = request.user

        user_serializer = UserSerializer(foydalanuvchi)

        return Response(user_serializer.data, status=status.HTTP_200_OK)

class FoydalanuchiQuizzesView(APIView):
    def get(self, request):
        foydalanuchi = request.user

        user_quizzes = UserQuiz.objects.filter(user=user)
        user_quizzes_serializer = UserQuizSerializer(user_quizzes, many=True)

        return Response(user_quizzes_serializer.data, status=status.HTTP_200_OK)

