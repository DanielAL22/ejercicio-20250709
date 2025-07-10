from app.coupons import apply_coupon, get_final_price

def test_discount_sale10():
    assert apply_coupon(100, "SALE10") == 90.0
    
def test_discount_super20():
    assert apply_coupon(200, "SUPER20") == 160.0
    
def test_discount_welcome():
    assert apply_coupon(100, "WELCOME") == 85.0
    
def test_final_price_with_taxexs():
    assert get_final_price(100, "SALE10") == 107.1