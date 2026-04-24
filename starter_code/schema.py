from pydantic import BaseModel, Field

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================

class UnifiedDocument(BaseModel):
    """
    Hệ thống cần 6 trường thông tin chuẩn (document_id, source_type, author, category, content, timestamp). 
    TODO: Khai báo các trường với kiểu dữ liệu str ở dưới.
    """
    document_id: str = Field(..., description="ID của tài liệu")
    source_type: str = Field(..., description="Loại nguồn")
    author: str = Field(..., description="Tác giả")
    category: str = Field(..., description="Thể loại")
    content: str = Field(..., description="Nội dung")
    timestamp: str = Field(..., description="Thời gian")
    
