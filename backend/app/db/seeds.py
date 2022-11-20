from app.api.dependencies.database import get_repository
from app.api.routes.items.items_resource import create_new_item
from app.db.repositories.items import ItemsRepository
from app.models.domain.users import User
from app.models.schemas.items import ItemInCreate

for i in range(100):
    item_create = ItemInCreate(title="title_{i}", description="desc_{i}", body="body_{i}")
    user = User(username="user_{i}", email="user_{i}@email.com")
    item_repo = get_repository(ItemsRepository)
    create_new_item(item_create, user, item_repo)
