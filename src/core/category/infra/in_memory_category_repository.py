from uuid import UUID
from core.category.application.category_repository import CategoryRepository
from core.category.domain.category import Category


class InMemoryCategoryRepository(CategoryRepository): 
    
    def __init__(self, categories= None):
            self.categories = categories or []
            
            
    def save(self, category) -> None:
        self.categories.append(category)
        
        
    def get_by_id(self, id : UUID) -> Category | None: 
        for category in self.categories: 
            if category.id == id : 
                return category
            return None
        
        
    def delete(self, id : UUID) -> None:
        category = self.get_by_id(id)
        self.categories.remove(category)