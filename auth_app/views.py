from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from .token import account_activation_token


class UserAPI(APIView):
    def get(self, request):
        obj = User.objects.all()
        form = UserSerializer(obj, many=True)
        return Response(data=form.data)

    def post(self, request):
        pm = "poojasandhale1095@gmail.com"
        form = UserSerializer(data=request.data)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            subject = "Activate Your Account"
            c_mail = user.email
            token = account_activation_token.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            send_mail(subject, f"http://127.0.0.1:8000/activate/{uid}/{token}", pm, [c_mail], fail_silently=False)
            return Response(data={"message":"mail send success"})
        return Response(data=form.errors)



class Activate(APIView):

    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User._default_manager.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return Response(data={"message": "user register successfully"})