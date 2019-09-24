from django.db import models

from django.contrib.auth.models import User

class Fields(models.Model):
    damage = models.CharField(max_length = 128)
    #creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'creator_id', null=True, blank = True)
    
    objects = models.Manager()

    def get_fields_by_user(self, user):
        fields = Fields.objects.filter(owner=user)
        return fields

    def get_fields_by_status(self, status):
        fields = Fields.objects.filter(status=status)
        return fields

    def get_fiields_by_creator_id(self, owner_id):
        fields = Fields.objects.filter(owner_id=owner_id)
        return fields