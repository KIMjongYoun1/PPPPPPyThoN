# 🚀 Flask 웹 앱 빠른 시작 가이드

## Java 개발자를 위한 Flask 가이드

이 가이드는 Java Spring Boot 개발자가 Python Flask를 빠르게 이해할 수 있도록 작성되었습니다.

---

## 📋 사전 준비

### 1. Flask 설치
```bash
# 가상환경 활성화
cd /Users/ryankim/Python
source my_python_env/bin/activate

# Flask 설치 (이미 완료됨)
pip install flask
```

### 2. 프로젝트 구조 확인
```bash
cd my_sample_app
tree -I '__pycache__|*.pyc'
```

---

## 🏃 Flask 앱 실행하기

### 방법 1: 직접 실행
```bash
cd /Users/ryankim/Python/my_sample_app
python app_flask.py
```

출력:
```
 * Serving Flask app 'app_flask'
 * Debug mode: on
 * Running on http://0.0.0.0:5000
```

### 방법 2: Flask CLI 사용
```bash
export FLASK_APP=app_flask.py
export FLASK_ENV=development
flask run
```

---

## 🧪 API 테스트하기

Flask 앱이 실행되면 다른 터미널에서 테스트:

### 1. Health Check
```bash
curl http://localhost:5000/health
```

**Java 비교:**
```java
@GetMapping("/health")
public HealthStatus healthCheck() { ... }
```

### 2. 사용자 생성 (POST)
```bash
curl -X POST http://localhost:5000/api/v1/users \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user001",
    "name": "김철수",
    "email": "kim@example.com",
    "age": 25
  }'
```

**Java 비교:**
```java
@PostMapping("/api/v1/users")
public User createUser(@RequestBody UserDto userDto) { ... }
```

**응답:**
```json
{
  "user_id": "user001",
  "name": "김철수",
  "email": "kim@example.com",
  "age": 25,
  "is_active": true
}
```

### 3. 모든 사용자 조회 (GET)
```bash
curl http://localhost:5000/api/v1/users
```

**Java 비교:**
```java
@GetMapping("/api/v1/users")
public List<User> getAllUsers() { ... }
```

### 4. 특정 사용자 조회 (GET)
```bash
curl http://localhost:5000/api/v1/users/user001
```

**Java 비교:**
```java
@GetMapping("/api/v1/users/{id}")
public User getUser(@PathVariable String id) { ... }
```

### 5. 사용자 업데이트 (PUT)
```bash
curl -X PUT http://localhost:5000/api/v1/users/user001 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "김철수(수정)",
    "age": 26
  }'
```

**Java 비교:**
```java
@PutMapping("/api/v1/users/{id}")
public User updateUser(@PathVariable String id, @RequestBody UserDto userDto) { ... }
```

### 6. 사용자 삭제 (DELETE)
```bash
curl -X DELETE http://localhost:5000/api/v1/users/user001
```

**Java 비교:**
```java
@DeleteMapping("/api/v1/users/{id}")
public ResponseEntity<Void> deleteUser(@PathVariable String id) { ... }
```

### 7. 상품 생성
```bash
curl -X POST http://localhost:5000/api/v1/products \
  -H "Content-Type: application/json" \
  -d '{
    "product_id": "prod001",
    "name": "노트북",
    "price": 1200000,
    "category": "전자제품",
    "stock": 10
  }'
```

### 8. 카테고리별 상품 조회 (쿼리 파라미터)
```bash
curl "http://localhost:5000/api/v1/products?category=전자제품"
```

**Java 비교:**
```java
@GetMapping("/api/v1/products")
public List<Product> getProducts(@RequestParam String category) { ... }
```

---

## 📊 요청/응답 흐름

### Java Spring Boot
```
HTTP Request
    ↓
DispatcherServlet
    ↓
@RequestMapping 매칭
    ↓
@RestController 메서드 실행
    ↓
@Service → @Repository → @Entity
    ↓
HTTP Response (Jackson이 자동 JSON 변환)
```

### Python Flask
```
HTTP Request
    ↓
Werkzeug (WSGI 서버)
    ↓
@app.route() 매칭
    ↓
함수 실행
    ↓
Service → Model
    ↓
jsonify()로 JSON 변환
    ↓
HTTP Response
```

---

## 🔍 코드 상세 분석

### 라우팅 비교

#### Java
```java
@RestController
@RequestMapping("/api/v1/users")
public class UserController {
    
    @GetMapping  // GET /api/v1/users
    public List<User> getAllUsers() { ... }
    
    @PostMapping  // POST /api/v1/users
    public User createUser(@RequestBody UserDto dto) { ... }
    
    @GetMapping("/{id}")  // GET /api/v1/users/{id}
    public User getUser(@PathVariable String id) { ... }
}
```

#### Python Flask
```python
# GET /api/v1/users
@app.route('/api/v1/users', methods=['GET'])
def get_all_users():
    users = user_service.get_all_users()
    return jsonify([...]), 200

# POST /api/v1/users
@app.route('/api/v1/users', methods=['POST'])
def create_user():
    data = request.get_json()  # @RequestBody
    user = user_service.create_user(...)
    return jsonify({...}), 201

# GET /api/v1/users/<user_id>
@app.route('/api/v1/users/<user_id>', methods=['GET'])
def get_user(user_id):  # @PathVariable
    user = user_service.get_user(user_id)
    return jsonify({...}), 200
```

---

## 🎯 핵심 차이점

### 1. 의존성 주입

**Java:**
```java
@Autowired
private UserService userService;
```

**Python:**
```python
# 직접 인스턴스 생성
user_service = UserService()
```

### 2. JSON 변환

**Java:**
```java
// Jackson이 자동으로 변환
return user;  // → JSON
```

**Python:**
```python
# 명시적으로 변환
return jsonify({
    'user_id': user.user_id,
    'name': user.name
}), 200
```

### 3. 예외 처리

**Java:**
```java
@ControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(UserNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleUserNotFound(UserNotFoundException e) { ... }
}
```

**Python:**
```python
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404
```

### 4. HTTP 메서드 지정

**Java:**
```java
@GetMapping
@PostMapping
@PutMapping
@DeleteMapping
```

**Python:**
```python
@app.route('/path', methods=['GET'])
@app.route('/path', methods=['POST'])
@app.route('/path', methods=['PUT'])
@app.route('/path', methods=['DELETE'])
```

---

## 💾 데이터베이스 연동 (선택)

### Java JPA
```java
@Entity
public class User {
    @Id
    @GeneratedValue
    private Long id;
    
    @Column(nullable = false)
    private String name;
}

public interface UserRepository extends JpaRepository<User, Long> {
    User findByUserId(String userId);
}
```

### Python SQLAlchemy (Flask)
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<User {self.name}>'

# 사용
user = User.query.filter_by(user_id='user001').first()
all_users = User.query.all()
```

---

## 📝 실습 과제

1. **새로운 엔드포인트 추가**
   - `GET /api/v1/users/active` - 활성 사용자만 조회
   - Java의 커스텀 메서드와 동일한 개념

2. **검증 추가**
   - 이메일 형식 검증
   - 나이 범위 검증 (0-120)
   - Java의 `@Valid` + Bean Validation과 유사

3. **페이지네이션 구현**
   - `?page=1&size=10`
   - Spring Data JPA의 `Pageable`과 유사

---

## 🎓 참고 자료

- [Flask 공식 문서](https://flask.palletsprojects.com/)
- [Flask RESTful API](https://flask-restful.readthedocs.io/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Postman](https://www.postman.com/) - API 테스트 도구

---

## 🚀 다음 단계

1. **Flask-RESTful** - REST API 전용 확장
2. **Flask-SQLAlchemy** - ORM 통합
3. **Flask-JWT-Extended** - JWT 인증
4. **Flask-CORS** - CORS 처리
5. **Flask-Migrate** - DB 마이그레이션

모두 Java Spring Boot의 대응 기능이 있습니다!

