

from dataclasses import dataclass
from uuid import UUID

from core.category.application.category_repository import CategoryRepository
from core.category.application.use_cases.execptions import CategoryNotFound
from core.category.domain.category import Category



@dataclass
class DeleteCategoryRequest: 
    id: UUID
    
    



class DeleteCategory:
    def __init__(self , repository : CategoryRepository):
        self.repository = repository
        
    def execute(self, request : DeleteCategoryRequest)-> None: 
       category = self.repository.get_by_id(id = request.id)
        
       if category is None: 
            raise CategoryNotFound("Category with {request.id} not found")
        
       self.repository.delete(category.id)
        
     
