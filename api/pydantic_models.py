from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime

class ModelName(str, Enum):
    GEMINI_1_5_PRO_LATEST = "models/gemini-1.5-pro-latest"
    GEMINI_1_5_FLASH = "models/gemini-1.5-flash"
    CHAT_BISON_001 = "models/chat-bison-001"  

class QueryInput(BaseModel):
    question: str
    session_id: str = Field(default=None)
    model: ModelName = Field(default=ModelName.GEMINI_1_5_PRO_LATEST)
    
class QueryResponse(BaseModel):
    answer: str
    session_id: str
    model: ModelName

class DocumentInfo(BaseModel):
    id: int
    filename: str
    upload_timestamp: datetime

class DeleteFileRequest(BaseModel):
    file_id: int
