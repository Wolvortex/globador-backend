from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer
# from django.shortcuts import redirect, render
# from django.contrib.auth import login, authenticate, logout
# from django.views.generic.base import TemplateView
# from django.http import HttpRequest
# from django.shortcuts import redirect
# from django.urls import reverse_lazy



# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         token['username'] = user.username

#         return token

# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer
    
    
    
    
    
# Create your views here.
# def login(request, username, password):
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect('index')
#     else:
#         return render(request, 'login.html', {'error_message': 'Invalid username or password'})

# def login(request):
#     print("A"*50)
#     if request.method == 'GET':
#         print("Y"*50)
#         context = ''
#         return render(request, 'registration/login.html', {'context': context})
    
#     elif request.method == 'POST':
#         print("X"*50)
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')
#         print(username)
#         print("X"*50)
#         username_lowered = username.lower()
#         print(username_lowered)
#         print("X"*50)
        
#         user = authenticate(request, username=username_lowered, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to a success page?
#             return redirect('index')
#             # return HttpResponseRedirect('/')
#         else:
#             context = {'error': 'Wrong credintials'}  # to display error?
#             return render(request, 'registration/login.html', {'context': context})
        
        
##############################################################################################
# class SignedOutView(TemplateView):

#     # template_name = "registration/signout.html"

#     def get(self, request: HttpRequest):
#         logout(request)
#         return redirect(reverse_lazy('login'))
#         # return render(request, self.template_name)
        

# class Register(APIView):
#     permission_classes = [AllowAny]
#     def get(self,request):
#         User.objects.create_superuser(username='admintest1', name='Omar Hatem', user_type='admission', password='admintest1')
#         return JsonResponse({'Message':'DONE!'})
