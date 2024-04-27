

from dataclasses import dataclass
from uuid import UUID

from core.category.application.category_repository import CategoryRepository
from core.category.application.use_cases.execptions import CategoryNotFound
from core.category.domain.category import Category



@dataclass
class GetCategoryRequest: 
    id: UUID
    
    
@dataclass
class GetCategoryResponse: 
    id: UUID
    name : str
    description :str
    is_active : bool


class GetCategory:
    def __init__(self , repository : CategoryRepository):
        self.repository = repository
        
    def execute(self, request : GetCategoryRequest)-> GetCategoryResponse: 
       category = self.repository.get_by_id(id = request.id)
        
       if category is None: 
            raise CategoryNotFound("Category with {request.id} not found")
        
       return GetCategoryResponse(
           id= category.id,
           name = category.name,
           description= category.description,
           is_active= category.is_active
       )
        
