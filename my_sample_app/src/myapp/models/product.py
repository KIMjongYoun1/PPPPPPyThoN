"""
Product 모델 클래스
"""

class Product:
    """상품 정보를 나타내는 클래스"""
    
    def __init__(self, product_id, name, price, category=None, stock=0):
        """
        상품 객체 초기화
        
        Args:
            product_id (str): 상품 ID
            name (str): 상품명
            price (float): 가격
            category (str, optional): 카테고리
            stock (int): 재고 수량
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock
    
    def __str__(self):
        """문자열 표현"""
        return f"Product(id={self.product_id}, name={self.name}, price={self.price})"
    
    def __repr__(self):
        """개발자용 문자열 표현"""
        return f"Product('{self.product_id}', '{self.name}', {self.price}, '{self.category}', {self.stock})"
    
    def get_info(self):
        """상품 정보 반환"""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'price': self.price,
            'category': self.category,
            'stock': self.stock
        }
    
    def update_stock(self, quantity):
        """재고 수량 업데이트"""
        if self.stock + quantity < 0:
            raise ValueError("재고가 부족합니다.")
        self.stock += quantity
    
    def is_available(self):
        """상품 구매 가능 여부"""
        return self.stock > 0
