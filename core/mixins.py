from django.contrib.auth.mixins import AccessMixin
from django.http import HttpResponseForbidden


class AddProductMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.has_perm('core.add_product'):
            return super().dispatch(request, *args, **kwargs)

        return HttpResponseForbidden('You do not have permission to add product.')


class UpdateProductMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.has_perm('core.update_product'):
            return super().dispatch(request, *args, **kwargs)

        return HttpResponseForbidden('You do not have permission to edit product.')


class DeleteProductMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.has_perm('core.delete_product'):
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseForbidden('You do not have permission to delete product.')