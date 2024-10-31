'''
Une tâche contient les attributs suivants :
task_id : uuid
name : string
description : string
status : string
created_at : str
updated_at : str
task_db est un index qui se présente sous la forme suivante :
{
    "uuid1" : {
        "task_id" : "uuid1",
        "name": "Nom",
        "description": "Desc",
        "status": "TODO",
        "created_at" : "date de création",
        "updated_at" : "date de mise à jour"
    }
}
'''
task_db = dict({
  "0316ff74-1711-4774-b6d6-300f3ce9fd57" : {
        "task_id" : "0316ff74-1711-4774-b6d6-300f3ce9fd57",
        "name": "Faire les courses",
        "description": "Acheter du lait, et d'autres items fournis par votre IA générative favorite",
        "status": "TODO",
        "created_at" : "date de création",
        "updated_at" : "date de mise à jour"
    }
})