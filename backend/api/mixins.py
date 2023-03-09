from rest_framework import permissions

from .permissions import IsStaffEditorPermission

class StaffEditorPermissionsMixin():
    permission_classes = [IsStaffEditorPermission, permissions.IsAdminUser]
    
    
    
class UserQuerySetMixin():
    user_field = 'user'
    allow_staff_view = False
    def  get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = user
        print(lookup_data)
        qs = super().get_queryset(*args, *kwargs)
        print(qs)
        print(user.is_staff, user)
        if self.allow_staff_view and user.is_staff: #stranely user.is_staff is true for admin :)
            return qs
        #print(qs.filter(**lookup_data)) prints only user related products, using filter method
        return  qs.filter(**lookup_data)