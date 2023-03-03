import logging
from rest_framework import permissions, viewsets
from apps.models import Todo
from apps.permissions import IsOwnerOrReadOnly
from apps.serializers import TodoSerializer

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class TodoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        try:
            serializer.save(owner=self.request.user)
            logger.info(f"Todo created by {self.request.user.username}")
        except Exception as e:
            logger.exception(str(e))
            raise
