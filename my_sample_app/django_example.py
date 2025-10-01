#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Django REST Framework 예제 - Spring MVC 전체 스타일

Django는 Spring 전체 프레임워크처럼 모든 기능이 포함되어 있습니다:
- ORM (JPA/Hibernate)
- Admin Panel (없음 in Spring)
- Authentication (Spring Security)
- Template Engine (Thymeleaf)
"""

# ============================================
# 1. models.py (JPA Entity와 유사)
# ============================================

"""
from django.db import models

class User(models.Model):
    '''
    Java JPA 비교:
    
    @Entity
    @Table(name = "users")
    public class User {
        @Id
        @GeneratedValue(strategy = GenerationType.IDENTITY)
        private Long id;
        
        @Column(nullable = false, unique = true)
        private String userId;
        ...
    }
    '''
    user_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'users'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} ({self.user_id})"


class Product(models.Model):
    product_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'products'
"""


# ============================================
# 2. serializers.py (DTO + Jackson과 유사)
# ============================================

"""
from rest_framework import serializers
from .models import User, Product

class UserSerializer(serializers.ModelSerializer):
    '''
    Java DTO 비교:
    
    public class UserDto {
        private String userId;
        private String name;
        private String email;
        private Integer age;
        // getters, setters, @JsonProperty 등
    }
    '''
    class Meta:
        model = User
        fields = ['user_id', 'name', 'email', 'age', 'is_active', 'created_at']
        read_only_fields = ['created_at']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
"""


# ============================================
# 3. views.py (Controller와 유사)
# ============================================

"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Product
from .serializers import UserSerializer, ProductSerializer

class UserViewSet(viewsets.ModelViewSet):
    '''
    Java Controller 비교:
    
    @RestController
    @RequestMapping("/api/v1/users")
    public class UserController {
        @Autowired
        private UserService userService;
        ...
    }
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    # GET /api/v1/users/
    def list(self, request):
        users = self.get_queryset()
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)
    
    # POST /api/v1/users/
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # GET /api/v1/users/{id}/
    def retrieve(self, request, pk=None):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)
    
    # PUT /api/v1/users/{id}/
    def update(self, request, pk=None):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE /api/v1/users/{id}/
    def destroy(self, request, pk=None):
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # 커스텀 액션 (Spring의 추가 메서드와 유사)
    @action(detail=False, methods=['get'])
    def active(self, request):
        '''
        GET /api/v1/users/active/
        
        Java 비교:
        @GetMapping("/active")
        public List<User> getActiveUsers()
        '''
        active_users = User.objects.filter(is_active=True)
        serializer = self.get_serializer(active_users, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        '''GET /api/v1/products/by_category/?category=전자제품'''
        category = request.query_params.get('category')
        products = Product.objects.filter(category=category)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
"""


# ============================================
# 4. urls.py (URL 라우팅 - web.xml 또는 @RequestMapping)
# ============================================

"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProductViewSet

# Router 설정 (자동으로 CRUD URL 생성)
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'products', ProductViewSet, basename='product')

# URL 패턴 정의
urlpatterns = [
    path('api/v1/', include(router.urls)),
    # 자동 생성된 URL:
    # GET    /api/v1/users/              -> list
    # POST   /api/v1/users/              -> create
    # GET    /api/v1/users/{id}/         -> retrieve
    # PUT    /api/v1/users/{id}/         -> update
    # DELETE /api/v1/users/{id}/         -> destroy
    # GET    /api/v1/users/active/       -> active (커스텀)
]

'''
Java Spring Boot 비교:

@Configuration
public class WebConfig {
    // 또는 Controller에서 직접
    @RequestMapping("/api/v1/users")
    public class UserController { ... }
}
'''
"""


# ============================================
# 5. settings.py (application.properties/yml)
# ============================================

"""
# Java Spring Boot의 application.yml 비교

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myapp_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Java:
# spring.datasource.url=jdbc:postgresql://localhost:5432/myapp_db
# spring.datasource.username=postgres
# spring.datasource.password=password

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'rest_framework',
    'myapp',
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
"""

print("""
================================
Django vs Spring Framework 비교
================================

구조:
├── models.py          ← @Entity (JPA)
├── serializers.py     ← DTO + Jackson
├── views.py           ← @RestController
├── urls.py            ← @RequestMapping / web.xml
├── settings.py        ← application.yml
└── admin.py           ← (Spring에는 없음)

데이터 흐름:
Frontend → urls.py → views.py → serializers.py → models.py → Database
   ↓         ↓          ↓             ↓              ↓           ↓
  (요청)   (라우팅)  (컨트롤러)      (DTO)        (Entity)     (DB)

Spring Boot:
Frontend → Controller → Service → Repository → Entity → Database

공통점:
- RESTful API 구조 동일
- MVC 패턴
- ORM 사용 (Django ORM ≈ JPA)
- Dependency Injection (Django는 약간 다름)

차이점:
- Django: 모든 기능 포함 (배터리 포함)
- Spring: 필요한 것만 선택 (유연함)
""")

