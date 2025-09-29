"""
ProductService - 상품 관련 비즈니스 로직
"""

from ..models.product import Product

class ProductService:
    """상품 관련 서비스 클래스"""
    
    def __init__(self):
        """서비스 초기화"""
        self.products = {}  # 메모리에 상품 저장 (실제로는 DB 사용)
    
    def create_product(self, product_id, name, price, category=None, stock=0):
        """
        새 상품 생성
        
        Args:
            product_id (str): 상품 ID
            name (str): 상품명
            price (float): 가격
            category (str, optional): 카테고리
            stock (int): 재고 수량
            
        Returns:
            Product: 생성된 상품 객체
            
        Raises:
            ValueError: 이미 존재하는 상품 ID인 경우
        """
        if product_id in self.products:
            raise ValueError(f"상품 ID '{product_id}'는 이미 존재합니다.")
        
        product = Product(product_id, name, price, category, stock)
        self.products[product_id] = product
        return product
    
    def get_product(self, product_id):
        """
        상품 조회
        
        Args:
            product_id (str): 상품 ID
            
        Returns:
            Product: 상품 객체 (없으면 None)
        """
        return self.products.get(product_id)
    
    def get_all_products(self):
        """
        모든 상품 조회
        
        Returns:
            list: 상품 객체 리스트
        """
        return list(self.products.values())
    
    def get_available_products(self):
        """
        구매 가능한 상품만 조회
        
        Returns:
            list: 구매 가능한 상품 객체 리스트
        """
        return [product for product in self.products.values() if product.is_available()]
    
    def get_products_by_category(self, category):
        """
        카테고리별 상품 조회
        
        Args:
            category (str): 카테고리명
            
        Returns:
            list: 해당 카테고리의 상품 객체 리스트
        """
        return [product for product in self.products.values() if product.category == category]
    
    def update_product(self, product_id, **kwargs):
        """
        상품 정보 업데이트
        
        Args:
            product_id (str): 상품 ID
            **kwargs: 업데이트할 필드들
            
        Returns:
            Product: 업데이트된 상품 객체
            
        Raises:
            ValueError: 상품이 존재하지 않는 경우
        """
        product = self.get_product(product_id)
        if not product:
            raise ValueError(f"상품 ID '{product_id}'를 찾을 수 없습니다.")
        
        for key, value in kwargs.items():
            if hasattr(product, key):
                setattr(product, key, value)
        
        return product
    
    def update_stock(self, product_id, quantity):
        """
        상품 재고 업데이트
        
        Args:
            product_id (str): 상품 ID
            quantity (int): 변경할 수량 (양수: 입고, 음수: 출고)
            
        Returns:
            Product: 업데이트된 상품 객체
            
        Raises:
            ValueError: 상품이 존재하지 않거나 재고가 부족한 경우
        """
        product = self.get_product(product_id)
        if not product:
            raise ValueError(f"상품 ID '{product_id}'를 찾을 수 없습니다.")
        
        product.update_stock(quantity)
        return product
    
    def delete_product(self, product_id):
        """
        상품 삭제
        
        Args:
            product_id (str): 상품 ID
            
        Returns:
            bool: 삭제 성공 여부
        """
        if product_id in self.products:
            del self.products[product_id]
            return True
        return False
    
    def get_product_count(self):
        """
        상품 수 조회
        
        Returns:
            int: 전체 상품 수
        """
        return len(self.products)
    
    def get_total_value(self):
        """
        전체 상품 가치 계산
        
        Returns:
            float: 전체 상품 가치 (가격 × 재고)
        """
        return sum(product.price * product.stock for product in self.products.values())
