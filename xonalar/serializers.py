from rest_framework import serializers
from .models import Savol, Soha, Variant

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'

class SavolSerializer(serializers.ModelSerializer):
    javoblar = SavolSerializer(many=True)

    class Meta:
        model = Savol
        fields = '__all__'

class SohaSerializer(serializers.ModelSerializer):
    savollar = QuestionSerializer(many=True)

    class Meta:
        model = Soha
        fields = '__all__'

class YuborishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yuborish
        fields = ('id', 'user_quiz', 'question', 'choice')