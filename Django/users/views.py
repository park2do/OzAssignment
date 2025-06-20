from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError  
from .serializers import MyInfoSerializer
from django.contrib.auth.password_validation import validate_password

# Create your views here.
class Users(APIView):
    def post(self, request):
        password = request.data.get('password')
        serializer = MyInfoSerializer(data=request.data)
        
        # 비밀번호 유효성 검사
        try: 
            validate_password(password)
        except:
            raise ParseError("Invalid one")

        # 데이터 유효성 검사
        if serializer.is_valid():
            user = serializer.save() #새로운 유저 생성
            user.set_password(password) #비밀번호 해쉬화
            user.save() #  

            serializer = MyInfoSerializer(user)
            return Response(serializer.data)
        else:
            raise ParseError(serializer.errors)

