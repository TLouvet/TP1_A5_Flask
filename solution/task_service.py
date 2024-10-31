from uuid import uuid4
from datetime import datetime
from task_db import task_db

def find_many(status: str):
  if status is None:
    return list(task_db.values())

  return [task for task in task_db.values() if task['status'] == status]

def find_one(id: str):
   task = task_db.get(str(id))
   return task if task else None

def create_one(new_task):
  new_id = str(uuid4())
  now = datetime.now()

  new_task['task_id'] = new_id
  new_task['created_at'] = now
  new_task['updated_at'] = now

  task_db[new_id] = new_task

  return new_task

def update_one(id:str, task):
  task_in_db = task_db.get(id)

  if task_in_db is None:
    return None

  task['task_id'] = id
  task['created_at'] = task_in_db['created_at']
  task['updated_at'] = datetime.now()

  task_db[id] = task

  return task

def patch_one(id:str, task):
  task_in_db = task_db.get(id)

  if task_in_db is None:
    return None

  fields = ['name', 'description', 'status']

  for field in fields:
    if field in task:
      task_in_db[field] = task[field]

  task_in_db['updated_at'] = datetime.now()

  return task_in_db
  

def delete_one(id:str):
  task = task_db.get(id)
  if task is None:
    return

  task_db.pop(id)