from uuid import UUID
import uuid

import pytest
from core.category.application.use_cases.get_category  import GetCategory, GetCategoryRequest, GetCategoryResponse
from core.category.domain.category import Category
from core.category.infra.in_memory_category_repository import InMemoryCategoryRepository
from core.category.application.use_cases.execptions import CategoryNotFound

class TestGetCategory:
    def test_get_category_by_id(self):
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
            
            categories= [category_filme,category_serie]) #sQLAlchmny /djangoORMRepository
        use_case = GetCategory(repository = repository)
        
        request = GetCategoryRequest(
            id= category_filme.id,
        )
        
        reesponse = use_case.execute(request)
        
        assert reesponse == GetCategoryResponse(
            id= category_filme.id,
            name= "Filme",
            description = "Categoria para filmes",
            is_active=True
        )
        
        
    def test_when_category_does_not_exist_then_raise_exception(self):
             
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
            
            categories= [category_filme,category_serie]) #sQLAlchmny /djangoORMRepository
        use_case = GetCategory(repository = repository)
        
        not_found_id = uuid.uuid4()
        
        
        request = GetCategoryRequest(
            id = not_found_id,
        )
        
        with pytest.raises(CategoryNotFound) as exec: 
            use_case.execute(request)
       

