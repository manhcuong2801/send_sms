from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from send_mail import schema, utils
from send_mail.core.responses import ResponseObject
from send_mail.core.schema import validate_data


class SendingMailAPI(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        _respone = ResponseObject()

        valid_data = validate_data(schema.MailResponse, request.data)
        name = valid_data.get('name')
        mobile = valid_data.get('mobile')
        code = valid_data.get('code')
        email = valid_data.get('email')

        utils.send_mail(email, name, mobile, code)
        utils.send_sms(mobile, name, code)
        return Response(status=status.HTTP_200_OK)

