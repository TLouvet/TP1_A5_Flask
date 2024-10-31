task_dto = {
  "type": "object",
  "properties": {
    "name": { "type": "string", "minLength": 1},
    "description": {"type": "string", "minLength": 1},
    "status": {"type": "string", "enum": ['TODO', "DONE", "IN PROGRESS"]}
  },
  "required": ['name', 'description', "status"],
  "additionalProperties": False
}

patch_task_dto = dict({**task_dto, "required": []})
