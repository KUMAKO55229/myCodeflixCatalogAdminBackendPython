import pytest
from uuid import UUID
from unittest.mock import MagicMock
from core.category.application.category_repository import CategoryRepository
from core.category.application.create_category import CreateCategory, CreateCategoryRequest, CreateCategoryResponse
from core.category.application.execptions import InvalidCategoryData

class TestCreateCategory:
    def test_create_category_with_valid_data(self):
        mock_repository = MagicMock(CategoryRepository)
        use_case = CreateCategory(repository = mock_repository)
        
        request = CreateCategoryRequest(
            name="Filme",
            description="Categoria para filems",
            is_active= True
        )
        
        response = use_case.execute(request)


        assert response.id is not None
        assert isinstance(response, CreateCategoryResponse)
        assert isinstance(response.id, UUID)
        assert mock_repository.save.called is True

    def test_create_category_with_invalid_data(self): 
        use_case = CreateCategory(repository = MagicMock(CategoryRepository))
        with pytest.raises(InvalidCategoryData ,match= "name cannot be empty") as exc_info: 
          
             response = use_case.execute(CreateCategoryRequest(name=""))
    
        assert exc_info.type is InvalidCategoryData
        assert str(exc_info.value) == "name cannot be empty"
       
