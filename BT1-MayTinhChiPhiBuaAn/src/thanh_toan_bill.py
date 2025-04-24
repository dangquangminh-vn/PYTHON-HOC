def tinh_tien_thue(subtotal, tax_rate=0.08):
    """Tính thuế dựa trên tổng trước thuế."""
    return subtotal * tax_rate

def tinh_tien_tip(subtotal, tip_rate=0.15):
    """Tính tiền típ dựa trên tổng hóa đơn"""
    return subtotal * tip_rate

def tinh_tien_tong_bill(subtotal, tax, tip):
    return subtotal + tax + tip

