# 🔥 Java Spring Boot vs Python Web Frameworks

## 📊 전체 비교표

| 구분 | Java Spring Boot | Python Flask | Python Django |
|------|------------------|--------------|---------------|
| **스타일** | 중간 (필요한 것 선택) | 경량 (미니멀) | 무거움 (All-in-one) |
| **학습곡선** | 중간 | 쉬움 | 어려움 |
| **ORM** | JPA/Hibernate | SQLAlchemy (선택) | Django ORM (내장) |
| **라우팅** | `@RequestMapping` | `@app.route()` | `urls.py` 파일 |
| **DI** | `@Autowired` | 직접 인스턴스 생성 | 직접 인스턴스 생성 |
| **설정 파일** | `application.yml` | 코드 내 설정 | `settings.py` |
| **관리자 페널** | ❌ | ❌ | ✅ (자동 생성) |

---

## 🔄 데이터 흐름 비교

### Java Spring Boot
```
Frontend (React/Vue)
    ↓
🌐 HTTP Request
    ↓
@RestController           ← @RequestMapping("/api/v1/users")
    ↓
@Service                  ← @Autowired
    ↓
@Repository               ← JPA Repository
    ↓
@Entity                   ← User.java
    ↓
💾 Database (PostgreSQL/MySQL)
```

### Python Flask
```
Frontend (React/Vue)
    ↓
🌐 HTTP Request
    ↓
@app.route('/api/v1/users', methods=['GET'])  ← 라우팅
    ↓
UserService 인스턴스     ← 직접 생성
    ↓
SQLAlchemy Model         ← (선택사항)
    ↓
💾 Database
```

### Python Django
```
Frontend (React/Vue)
    ↓
🌐 HTTP Request
    ↓
urls.py                   ← URL 패턴 매칭
    ↓
views.py (ViewSet)        ← 컨트롤러 역할
    ↓
serializers.py            ← DTO 역할
    ↓
models.py                 ← Entity 역할
    ↓
💾 Database
```

---

## 📝 코드 비교: CRUD API

### 1️⃣ 사용자 생성 (POST)

#### Java Spring Boot
```java
@RestController
@RequestMapping("/api/v1/users")
public class UserController {
    
    @Autowired
    private UserService userService;
    
    @PostMapping
    public ResponseEntity<User> createUser(@RequestBody UserDto userDto) {
        User user = userService.createUser(userDto);
        return ResponseEntity.status(HttpStatus.CREATED).body(user);
    }
}
```

#### Python Flask
```python
@app.route('/api/v1/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    user = user_service.create_user(
        user_id=data['user_id'],
        name=data['name'],
        email=data['email']
    )
    
    return jsonify({
        'user_id': user.user_id,
        'name': user.name,
        'email': user.email
    }), 201
```

#### Python Django REST Framework
```python
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    # create() 메서드는 자동 제공됨!
    # POST /api/v1/users/
```

---

### 2️⃣ 사용자 조회 (GET)

#### Java Spring Boot
```java
@GetMapping("/{id}")
public ResponseEntity<User> getUser(@PathVariable String id) {
    User user = userService.getUser(id);
    if (user == null) {
        return ResponseEntity.notFound().build();
    }
    return ResponseEntity.ok(user);
}
```

#### Python Flask
```python
@app.route('/api/v1/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify({
        'user_id': user.user_id,
        'name': user.name,
        'email': user.email
    }), 200
```

#### Python Django
```python
# GET /api/v1/users/{id}/
# retrieve() 메서드 자동 제공됨!
```

---

### 3️⃣ 쿼리 파라미터 처리

#### Java Spring Boot
```java
@GetMapping
public List<Product> getProducts(@RequestParam(required = false) String category) {
    if (category != null) {
        return productService.getProductsByCategory(category);
    }
    return productService.getAllProducts();
}
```

#### Python Flask
```python
@app.route('/api/v1/products', methods=['GET'])
def get_products():
    category = request.args.get('category')  # ?category=전자제품
    
    if category:
        products = product_service.get_products_by_category(category)
    else:
        products = product_service.get_all_products()
    
    return jsonify([...]), 200
```

---

## 🎯 주요 개념 매핑

### 어노테이션/데코레이터

| Java | Python Flask | Python Django | 역할 |
|------|--------------|---------------|------|
| `@RestController` | `@app.route()` | `class ViewSet` | 컨트롤러 정의 |
| `@RequestMapping` | `@app.route('/path')` | `path()` in urls.py | URL 매핑 |
| `@GetMapping` | `methods=['GET']` | `def list()` | GET 요청 |
| `@PostMapping` | `methods=['POST']` | `def create()` | POST 요청 |
| `@PathVariable` | `<variable>` | `pk` 파라미터 | URL 변수 |
| `@RequestParam` | `request.args.get()` | `request.query_params` | 쿼리 파라미터 |
| `@RequestBody` | `request.get_json()` | `request.data` | 요청 본문 |
| `@Autowired` | 직접 인스턴스 생성 | 직접 인스턴스 생성 | 의존성 주입 |
| `@Entity` | SQLAlchemy Model | `models.Model` | 엔티티 |
| `@Service` | 일반 클래스 | 일반 클래스 | 서비스 레이어 |
| `@Repository` | 직접 구현 | `objects` 매니저 | 데이터 접근 |
| `@Valid` | 커스텀 검증 | `serializer.is_valid()` | 유효성 검증 |

### HTTP 상태 코드

| Java | Python |
|------|--------|
| `HttpStatus.OK` | `200` |
| `HttpStatus.CREATED` | `201` |
| `HttpStatus.NO_CONTENT` | `204` |
| `HttpStatus.BAD_REQUEST` | `400` |
| `HttpStatus.NOT_FOUND` | `404` |
| `HttpStatus.INTERNAL_SERVER_ERROR` | `500` |

---

## 🗂️ 프로젝트 구조 비교

### Java Spring Boot
```
src/
└── main/
    ├── java/
    │   └── com.mycompany.myapp/
    │       ├── MyAppApplication.java      ← main()
    │       ├── controller/                ← @RestController
    │       │   └── UserController.java
    │       ├── service/                   ← @Service
    │       │   └── UserService.java
    │       ├── repository/                ← @Repository
    │       │   └── UserRepository.java
    │       ├── model/                     ← @Entity
    │       │   └── User.java
    │       └── dto/                       ← DTO
    │           └── UserDto.java
    └── resources/
        └── application.yml                ← 설정 파일
```

### Python Flask
```
my_sample_app/
├── app_flask.py                          ← Flask 앱 + 라우팅
├── src/
│   └── myapp/
│       ├── models/                       ← Model
│       │   └── user.py
│       ├── services/                     ← Service
│       │   └── user_service.py
│       └── utils/                        ← Utils
│           └── helpers.py
└── requirements.txt                      ← 의존성 (pom.xml)
```

### Python Django
```
myproject/
├── manage.py                             ← 관리 스크립트
├── myproject/
│   ├── settings.py                       ← application.yml
│   ├── urls.py                           ← 전역 URL 설정
│   └── wsgi.py
└── myapp/
    ├── models.py                         ← @Entity
    ├── views.py                          ← @RestController
    ├── serializers.py                    ← DTO
    ├── urls.py                           ← @RequestMapping
    └── admin.py                          ← 관리자 페이지
```

---

## 🚀 실행 방법

### Java Spring Boot
```bash
# Maven
mvn spring-boot:run

# Gradle
./gradlew bootRun

# JAR
java -jar target/myapp-0.0.1-SNAPSHOT.jar
```

### Python Flask
```bash
# 직접 실행
python app_flask.py

# 또는 Flask CLI
export FLASK_APP=app_flask.py
flask run

# 프로덕션
gunicorn app_flask:app
```

### Python Django
```bash
# 개발 서버
python manage.py runserver

# 마이그레이션
python manage.py makemigrations
python manage.py migrate

# 프로덕션
gunicorn myproject.wsgi:application
```

---

## 💡 언제 어떤 프레임워크를 사용할까?

### Flask를 선택하는 경우
- ✅ 작은 마이크로서비스
- ✅ API 서버만 필요
- ✅ 빠른 프로토타이핑
- ✅ 최소한의 학습 곡선
- ✅ Spring Boot와 가장 유사한 느낌

### Django를 선택하는 경우
- ✅ 전체 웹 애플리케이션
- ✅ 관리자 페이지 필요
- ✅ ORM 필수
- ✅ 인증/권한 시스템 내장
- ✅ "배터리 포함" 원칙

### Spring Boot를 선택하는 경우
- ✅ 대규모 엔터프라이즈
- ✅ 강력한 타입 시스템
- ✅ 성능이 중요
- ✅ Java 생태계 활용
- ✅ 복잡한 비즈니스 로직

---

## 🎓 결론

**Java 개발자가 Python으로 넘어온다면:**

1. **Flask** - Spring Boot와 가장 유사, 쉽게 시작
2. **FastAPI** - 최신 트렌드, 타입 힌트 활용
3. **Django** - 전체 프레임워크 필요 시

**핵심 차이:**
- Java: 컴파일 언어, 강타입, 명시적
- Python: 인터프리터 언어, 동적 타입, 간결함

**공통점:**
- MVC 패턴
- RESTful API 구조
- 의존성 관리
- 테스트 프레임워크

