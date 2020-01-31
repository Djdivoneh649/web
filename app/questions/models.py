from django.db import models

from rest_framework import serializers, viewsets
import django_filters

from economy.models import SuperModel


class Question(SuperModel):

    text = models.TextField(default='', blank=True)
    owner = models.ForeignKey('dashboard.Profile', on_delete=models.SET_NULL,
                              related_name='questions', blank=True, null=True)
    value_in_eth = models.DecimalField(default=1, decimal_places=2,
                                       max_digits=50)


class Answer(SuperModel):

    text = models.TextField(default='', blank=True)
    owner = models.ForeignKey('dashboard.Profile', on_delete=models.SET_NULL,
                              related_name='answers', blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='answers')
    is_accepted = models.BooleanField(default=False)


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('text', 'owner', 'question', 'is_accepted', 'id')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('text', 'owner', 'value_in_eth', 'id', 'answers')