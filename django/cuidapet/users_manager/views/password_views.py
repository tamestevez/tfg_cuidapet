import logging

from cuidapet.settings import BASE_URL
from django.contrib.auth import authenticate, login
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework import permissions, status, views, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from users_manager.models import BaseUser

from .utils import check_user


class ChangePasswordViewSet(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permissions_classes = [permissions.IsAuthenticated]

    def update(self, request, pk=None):
        result = check_user(request.user)
        if result:
            return result

        user = BaseUser.objects.filter(pk=request.user.pk).first()
        if "old_password" not in request.data and not user.check_password(
            "old_password"
        ):
            logging.error("Contraseña incorrecta.")
            return Response(
                {"detail": "Contraseña incorrecta."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = BaseUser.objects.get(pk=request.user.pk)
        user.set_password(request.data["new_password"])
        user.save()
        user = authenticate(
            emai=request.user.email, password=request.data["new_password"]
        )
        login(request, user)
        return Response(
            {"detail": "Contraseña cambiada."}, status=status.HTTP_200_OK
        )


class ForgotPasswordView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        if not 'email' in request.data:
            logging.error("No existe correo en la petición")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user = BaseUser.objects.filter(email=request.data["email"]).first()
        if not user:
            logging.error("Usuario no encontrado")
            return Response(status=status.HTTP_200_OK)
        user.token_password = PasswordResetTokenGenerator().make_token(user)
        user.save()
        try:
            url = BASE_URL + "/api/reset-password/" + user.token_password
            msg_plain = render_to_string(
                "password/reset_password.txt", {"name": user.name, "url": url}
            )
            msg_html = render_to_string(
                "password/reset_password.html", {"name": user.name, "url": url}
            )
            send_mail(
                subject="Recuperación de contraseña [Cuidapet]",
                message=msg_plain,
                html_message=msg_html,
                from_email=None,
                recipient_list=[user.email],
                fail_silently=False,
            )
        except Exception as e:
            logging.error("Error en ForgotPassword " + str(e))
            return Response(
                {"detail": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        return Response(
            {"detail": "Correo de recuperación de contraseña enviado"},
            status=status.HTTP_200_OK,
        )


class ResetPasswordView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        if not 'token_password' in request.data or not 'new_password' in request.data:
            logging.error("Parametros no encontrados en la petición")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user = BaseUser.objects.filter(
            token_password=request.data["token_password"]
        ).first()
        if not user:
            logging.error("Usuario no encontrado.")
            return Response(
                {"detail": "Usuario no encontrado"},
                status=status.HTTP_404_NOT_FOUND,
            )

        if not PasswordResetTokenGenerator().check_token(
            user, request.data["token_password"]
        ):
            logging.error("Link expirado.")
            return Response(
                {"detail": "Link expirado"}, status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(request.data["new_password"])
        user.token_password = ""
        user.save()
        return Response(
            {"detail": "Contraseña cambiada"}, status=status.HTTP_200_OK
        )
