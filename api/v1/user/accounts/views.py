from django.db.models import F
from rest_framework import views, permissions, response, status, exceptions
from drf_spectacular.utils import extend_schema
from django.db import connection, IntegrityError
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _

from account_app.models import User, ContentDevice
from . import serializers
from .permissions import NotAuthenticated
from .token import get_tokens_for_user


class UserLoginApiView(views.APIView):
    serializer_class = serializers.UserLoginSerializer
    permission_classes = (NotAuthenticated,)

    @extend_schema(responses={200: serializers.TokenResponseSerializer})
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        device_model = serializer.validated_data['device_model']
        device_os = serializer.validated_data['device_os']
        device_number = serializer.validated_data['device_number']
        ip_address = serializer.validated_data['ip_address']
        fcm_token = serializer.validated_data.get("fcm_token", None)

        user = User.objects.filter(username=username).only("username", "password", "is_active", "number_of_max_device")
        user_first = user.first()

        if user_first and user_first.check_password(password):
            token = get_tokens_for_user(user_first)
            user.update(number_of_login=F("number_of_login") + 1, fcm_token=fcm_token)

            device = ContentDevice.objects.filter(device_number=device_number, user=user_first).only(
                "id", "is_blocked"
            ).first()

            if device:
                if device.is_blocked:
                    return JsonResponse(
                        data={"detail": "Your device is blocked"},
                        status=status.HTTP_403_FORBIDDEN,
                        safe=False
                    )
                # اگر دستگاه وجود دارد و بلاک نیست، توکن را برگردان
                return JsonResponse(
                    data={'token': token},
                    status=status.HTTP_200_OK,
                    safe=False
                )
            else:
                # بررسی تعداد دستگاه‌های کاربر قبل از ایجاد دستگاه جدید
                device_count = ContentDevice.objects.filter(user=user_first).only("id").count()
                if device_count >= user_first.number_of_max_device:
                    return JsonResponse(
                        data={"detail": "Maximum number of devices reached"},
                        status=status.HTTP_403_FORBIDDEN,
                        safe=False
                    )

                try:
                    ContentDevice.objects.create(
                        user=user_first,
                        device_model=device_model,
                        device_os=device_os,
                        device_number=device_number,
                        ip_address=ip_address
                    )
                except IntegrityError:
                    return JsonResponse(
                        data={"detail": "Device with this number already exists"},
                        status=status.HTTP_400_BAD_REQUEST,
                        safe=False
                    )
                return JsonResponse(
                    data={'token': token},
                    status=status.HTTP_200_OK,
                    safe=False
                )

        else:
            raise exceptions.ValidationError(
                detail={"message": _("invalid username and password")},
                code=status.HTTP_400_BAD_REQUEST
            )


class UserProfileApiView(views.APIView):
    serializer_class = serializers.UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return response.Response(data=serializer.data)
