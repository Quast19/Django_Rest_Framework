from rest_framework import permissions

from .permissions import IsStaffEditorPermission

class StaffEditorPermissionsMixin():
    permission_classes = [IsStaffEditorPermission, permissions.IsAdminUser]
    
    
    
class UserQuerySetMixin():
    user_field = 'user'
    def  get_queryset(self, *args, **kwargs):
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user
        print(lookup_data)
        qs = super().get_queryset(*args, *kwargs)
        print(qs)
        return  qs.filter(**lookup_data)