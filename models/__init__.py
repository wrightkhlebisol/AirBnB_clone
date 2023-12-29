"""Read file and deserialize it back to object."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
