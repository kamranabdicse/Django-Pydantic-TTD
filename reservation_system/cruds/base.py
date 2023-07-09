from typing import TypeVar, List
from django.db import models

from reservation_system.utils.crud import get_object


ModelType = TypeVar("ModelType", bound=models.Model)


class BaseCRUD:
    """
    Base CRUD functionality for DRY principle
    """

    def __init__(self, model) -> None:
        self.model = model

    def create(self, obj_in) -> ModelType:
        """
        Create new instance
        """
        return self.model.objects.create(**obj_in.dict())

    def update(self, obj, obj_in=None):
        if obj_in is not None:
            obj_data = obj_in.dict()
            update_data = obj_in.dict(exclude_unset=True)
            for field in obj_data:
                if field in update_data:
                    setattr(obj, field, update_data[field])
        obj.save()
        return obj

    def get(self, pk):
        return get_object(self.model, pk=pk)

    def delete(self, pk: int) -> None:
        """
        Delete requested instance
        """
        instance = get_object(self.model, pk=pk)
        instance.delete() if instance else None
        return None





    # def read(*, model: ModelType, pk: int) -> ModelType:
    #     """
    #     Return detail of requested instance
    #     """
    #     return get_object(model, pk=pk)

    # def list(*, model: ModelType) -> List[ModelType]:
    #     """
    #     Return list of all instance for requested model
    #     """
    #     return model.objects.all()