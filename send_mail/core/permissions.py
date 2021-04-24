import logging

from rest_framework.permissions import BasePermission

from apps.users.models import FxResPartner

_logger = logging.getLogger(__name__)


class UserPermissions(BasePermission):
    def has_permission(self, request, view):
        try:
            if not request.user:
                return False
            if isinstance(request.user, FxResPartner):
                return True
            return False
        except Exception as e:
            _logger.info(e)
            return False
