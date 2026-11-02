from sqlalchemy.orm import Session

from app.repositories.file import TaskRepository
from app.schemas.file import TaskCreate, TaskRead, TaskUpdate

from app.repositories.file import CategoryRepository
from app.schemas.file import CategoryRead, CategoryCreate, CategoryUpdate

class TaskNotFoundError(Exception):
    pass


class TaskService:

    def __init__(self, db: Session):
        self.db = db
        self.repository = TaskRepository(db)

    def list_tasks(self) -> list[TaskRead]:
        tasks = self.repository.get_all()
        return [TaskRead.model_validate(task) for task in tasks]

    def create_task(self, payload: TaskCreate) -> TaskRead:
        task = self.repository.create(title=payload.title)
        self.db.commit()
        return TaskRead.model_validate(task)

    def update_task(self, task_id: str, payload: TaskUpdate) -> TaskRead:
        task = self.repository.get_by_id(task_id)

        if payload.title is not None:
            task.title = payload.title
        if payload.completed is not None:
            task.completed = payload.completed

        self.db.commit()
        return TaskRead.model_validate(task)

    def delete_task(self, task_id: str) -> None:
        task = self.repository.get_by_id(task_id)

        self.repository.delete(task)
        self.db.commit()








class CategoryNotFoundError(Exception):
    pass


class CategoryService:

    def __init__(self, db: Session):
        self.db = db
        self.repository = CategoryRepository(db)


    def list_categories(self) -> list[CategoryRead]:
        categories = self.repository.get_all()
        return [CategoryRead.model_validate(category) for category in categories]


    def create_category(self, payload: CategoryCreate) -> CategoryRead:
        category = self.repository.create(name=payload.name)
        self.db.commit()
        return CategoryRead.model_validate(category)


    def update_category(self, category_id: str, payload: CategoryUpdate) -> CategoryRead:
        category = self.repository.get_by_id(category_id)

        if payload.name is not None:
            category.name = payload.name
        if payload.completed is not None:
            category.completed = payload.completed

        self.db.commit()
        return CategoryRead.model_validate(category)


    def delete_category(self, category_id: str) -> None:
        category = self.repository.get_by_id(category_id)

        self.repository.delete(category)
        self.db.commit()