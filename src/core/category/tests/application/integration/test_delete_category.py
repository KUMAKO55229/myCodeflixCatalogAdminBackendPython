
from unittest.mock import create_autospec

from core.category.application.use_cases.delete_category import DeleteCategory, DeleteCategoryRequest

from core.category.domain.category import Category
from core.category.infra.in_memory_category_repository import InMemoryCategoryRepository


class TestDeleteCategory: 
        category_filme = Category(
            name = "Filme",
            description="Categoria para filmes",
            is_active=True
        )
        category_serie = Category(
            name="Serie",
            description="Categoria para séries",
            is_active= True
        )
        repository = InMemoryCategoryRepository(
            
            categories= [category_filme,category_serie]) 
        use_case = DeleteCategory(repository = repository)
        
        request = DeleteCategoryRequest(
            id= category_filme.id,
        )
        
        assert repository.get_by_id(category_filme.id) is not None
        reesponse = use_case.execute(request)
        
        assert repository.get_by_id(category_filme.id) is not None
        assert reesponse is None
        
   