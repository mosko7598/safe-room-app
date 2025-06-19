from .database import engine
from .models import Base

# יוצר את כל הטבלאות במסד הנתונים
Base.metadata.create_all(bind=engine)
