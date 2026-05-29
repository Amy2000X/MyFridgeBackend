from fastapi import APIRouter, Depends, Header

from app.dependencies.auth_dependency import (
    get_current_user
)

from app.schemas.fridge_schema import (
    CreateFridgeItem,
    UpdateFridgeItem
)

from app.services.fridge_service import (
    create_item,
    get_items,
    update_item,
    delete_item
)

router = APIRouter(
    prefix="/fridge",
    tags=["Fridge"]
)


@router.post("/")
def create_fridge_item(
    data: CreateFridgeItem,
    auth=Depends(get_current_user)
):
    return create_item(
        auth["token"],
        auth["user"].id,
        data
    )

@router.get("/items")
def get_fridge_items(
    auth=Depends(get_current_user)
):
    return get_items(
        auth["token"]
    )

@router.put("/{item_id}")
def update_fridge_item(
    item_id: str,
    data: UpdateFridgeItem,
    auth=Depends(get_current_user)
):
    return update_item(
        auth["token"],
        item_id,
        data
    )

@router.delete("/{item_id}")
def delete_fridge_item(
    item_id: str,
    auth=Depends(get_current_user)
):
    return delete_item(
        auth["token"],
        item_id
    )
