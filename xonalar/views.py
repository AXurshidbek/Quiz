# quiz/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Quiz, Question, Choice, UserQuiz, UserChoice
from .serializers import (
    SohaSerializer,YuborishSerializer,VariantSerializer,
    SavolSerializer
)

class SohalarView(generics.ListAPIView):
    queryset = Savol.objects.all()
    serializer_class = SohaSerializer

class SavollarListView(generics.ListAPIView):
    serializer_class = SavolSerializer

    def get_queryset(self):
        soha_id = self.kwargs['soha_id']
        return Question.objects.filter(quiz_id=soha_id)



class YuborishView(APIView):
    def post(self, request):
        serializer = YuborishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Javonigiz qabul qilindi'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

