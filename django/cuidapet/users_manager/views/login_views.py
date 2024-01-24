import logging
import pyotp
from django.contrib.auth import authenticate
from rest_framework import views, permissions, status
from rest_framework.response import Response

from cuidapet.constants import EMAIL_REQUIRED, PASSWORD_REQUIRED, USER_ERROR

class GenerateTwoFactorView(views.APIView):
    permission_classes=(permissions.AllowAny,)

    def post(self, request):
        email=request.data.get('email')
        if not email:
            logging.error("Generate Two Factor View Error: "+EMAIL_REQUIRED)
            return Response({'detail': EMAIL_REQUIRED}, status=status.HTTP_400_BAD_REQUEST)
        password=request.data.get('password')
        if not password:
            logging.error("Generate Two Factor View Error: "+PASSWORD_REQUIRED)
            return Response({'detail': PASSWORD_REQUIRED}, status=status.HTTP_400_BAD_REQUEST)
        user=authenticate(email=email, password=password)
        if not user:
            logging.error("Generate Two Factor View Error: "+USER_ERROR)
            return Response({'detail': USER_ERROR}, status=status.HTTP_401_UNAUTHORIZED)
        if not user.opt_generator_code:
            logging.info("Generate Two Factor View Info: OK")
            return Response({'otpauth_url':pyotp.totp.TOTP(pyotp.random_base32()).provisioning_uri(issuer_name="Cuidapet")}, status=status.HTTP_200_OK)
        logging.info("Generate Two Factor View Info: OK")
        return Response(status=status.HTTP_200_OK)
    

        


