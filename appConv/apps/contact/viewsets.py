from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializer import MessageSerializer, MobileTokenSerializer


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = MessageSerializer.Meta.model.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Provider guardado con exito... "},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MobileTokenViewSet(ModelViewSet):
    serializer_class = MobileTokenSerializer
    queryset = MobileTokenSerializer.Meta.model.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Provider guardado con exito... "},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        message = self.queryset.get(pk=pk)
        if message:
            message.delete()
            response = {"message": "Mobile-Token eliminado correctamente."}
            return Response(response, status=status.HTTP_200_OK)
        return Response(
            {"error": "No existe el Mobile-Token en los datos..."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def list(self, request):
        response = {"message": "Delete function is not offered in this path."}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, pk=None):
        response = {"message": "Delete function is not offered in this path."}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, pk=None):
        response = {"message": "Delete function is not offered in this path."}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None):
        response = {"message": "Delete function is not offered in this path."}
        return Response(response, status=status.HTTP_403_FORBIDDEN)
