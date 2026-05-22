from rest_framework import serializers

from personal.models import ProjectItemModel, InboundMessageModel


class ProjectItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectItemModel
        fields = '__all__'


class InboundMessageSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = InboundMessageModel
        fields = [
            'id', 'subject_email', 'subject_name', 'project_theme',
            'mail_body', 'is_from_admin', 'is_read', 'is_replied',
            'is_spam', 'is_archived', 'is_deleted', 'created_at', 'replies'
        ]
        read_only_fields = ['is_from_admin', 'parent']

    def get_replies(self, obj):
        if obj.replies.exists():
            return InboundMessageSerializer(obj.replies.all(), many=True).data
        return []