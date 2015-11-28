from rest_framework import viewsets
from custom_api_permissions.mixins.custom_permission_create_model_mixin import CustomPermissionCreateModelMixin
from custom_api_permissions.mixins.custom_permission_destroy_model_mixin import CustomPermissionDestroyModelMixin
from custom_api_permissions.mixins.custom_permission_list_model_mixin import CustomPermissionListModelMixin
from custom_api_permissions.mixins.custom_permission_retrieve_model_mixin import CustomPermissionRetriveModelMixin
from custom_api_permissions.mixins.custom_permission_update_model_mixin import CustomPermissionUpdateModelMixin


class CustomPermissionModelViewSet(viewsets.GenericViewSet, CustomPermissionCreateModelMixin,
                                   CustomPermissionDestroyModelMixin, CustomPermissionUpdateModelMixin,
                                   CustomPermissionListModelMixin, CustomPermissionRetriveModelMixin):
    pass
