from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserPublicSerializer


class GetUser(APIView):
    def get(self, request):
        users_objects = User.objects.all()
        serializer = UserPublicSerializer(users_objects, many=True)
        return Response({"status": 200, "payload": serializer.data})


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserPublicSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"status": 403, "errors": serializer.errors, "message": "Some problems"}
            )
        serializer.save()

        user = User.objects.get(username=serializer.data["username"])
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"status": 200, "payload": serializer.data, "message": "Ok"})
