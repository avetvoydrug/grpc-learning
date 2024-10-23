from database import Base
from sqlalchemy.orm import mapped_column, Mapped

class Todo(Base):
    __tablename__ = "todo"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)
    day: Mapped[int] = mapped_column(default=0)