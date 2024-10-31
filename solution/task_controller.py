from flask import Blueprint, request
from flask_expects_json import expects_json
from task_dto import task_dto, patch_task_dto
import task_service as ts

task_bp = Blueprint('task', __name__)
not_found_error = { "message": "La tache demandée n'existe pas"}, 404

@task_bp.get('/tasks')
def find_many_tasks():
  status = request.args.get('status')
  return ts.find_many(status)

@task_bp.get('/tasks/<uuid:id>')
def find_one(id):
  task = ts.find_one(str(id))
  if task is None:
    return not_found_error

  return task

@task_bp.post('/tasks')
@expects_json(task_dto)
def create_one():
  body = request.get_json()
  return ts.create_one(body)

@task_bp.put('/tasks/<uuid:id>')
@expects_json(task_dto)
def update_one(id):
  body = request.get_json()
  updated_task = ts.update_one(str(id), body)

  if updated_task is None:
    return not_found_error

  return updated_task

@task_bp.patch('/tasks/<uuid:id>')
@expects_json(patch_task_dto)
def patch_one(id):
  body = request.get_json()
  updated_task = ts.patch_one(str(id), body)

  if updated_task is None:
    return not_found_error

  return updated_task

@task_bp.delete('/tasks/<uuid:id>')
def delete_one(id):
  ts.delete_one(str(id))
  return {}, 204