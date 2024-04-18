from uuid import UUID
from core.category.application.create_category import CreateCategory, CreateCategoryRequest
from core.category.infra.in_memory_category_repository import InMemoryCategoryRepository


class TestCreateCategory:
    def test_create_category_with_valid_data(self):
        repository = InMemoryCategoryRepository() #sQLAlchmny /djangoORMRepository
        use_case = CreateCategory(repository = repository)
        
        request = CreateCategoryRequest(
            name="Filme",
            description="Categoria para filems",
            is_active= True
        )
        
        reesponse = use_case.execute(request)


        assert reesponse.id is not None
        assert isinstance(reesponse.id, UUID)
        assert  len(repository.categories) ==1 
        
        persisted_category = repository.categories[0]
        
        assert persisted_category.id == reesponse.id
        assert persisted_category.name == "Filme"
        assert persisted_category.description == "Categoria para filems"
        assert persisted_category.is_active == True
        