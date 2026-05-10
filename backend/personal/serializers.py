from rest_framework import serializers

from personal.models import ProjectItemModel, ContactMessageModel


class ProjectItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectItemModel
        fields = '__all__'


class ContactMessageSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = ContactMessageModel
        fields = [
            'id', 'sender_email', 'subject', 'project_theme',
            'body', 'is_from_admin', 'created_at', 'replies'
        ]
        read_only_fields = ['is_from_admin', 'parent']

    def get_replies(self, obj):
        if obj.replies.exists():
            return ContactMessageSerializer(obj.replies.all(), many=True).data
        return []