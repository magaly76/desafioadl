from .models import Tarea, Subtarea

def recuperar_tarea(tarea_id):
     return Tarea.objects.get(tarea_id=tarea_id)
    

def recuperar_subtarea(subtarea_id):
    return Subtarea.objects.get(subtarea_id=subtarea_id)

def crear_nueva_tarea(descripcion, eliminada=False):
    tarea = Tarea(
    descripcion=descripcion,
    eliminada=eliminada
)
    tarea.save()

def crear_nueva_subtarea(descripcion, eliminada, tarea_id):
    tarea=Tarea.objects.get(tarea_id=tarea_id)
    subtarea = Subtarea(
    descripcion=descripcion,
    eliminada=eliminada,
    tarea=tarea
)
    subtarea.save()

def eliminar_tarea(tarea_id):
    tarea=Tarea.objects.get(tarea_id=tarea_id)
    tarea.delete()

def eliminar_subtarea(subtarea_id):
    subtarea=Subtarea.objects.get(subtarea_id=subtarea_id)
    subtarea.delete()

def imprimir_en_pantalla():
    tareas=Tarea.objects.all()
    subtareas=Subtarea.objects.all()

    tareas_listado={}
    for tarea in tareas:
        tareas_listado[tarea.tarea_id] = {
            'descripcion': tarea.descripcion,
            'subtareas' : []
        }
    
    for subtarea in subtareas:
        tarea_id = subtarea.tarea_id
        if tarea_id is not None and tarea_id in tareas_listado:
            tareas_listado[tarea_id] ['subtareas'].append({
                'id':subtarea.subtarea_id,
                'descripcion':subtarea.descripcion
            })
    
    resultado = []
    for tarea_id, info in tareas_listado.items():
        resultado.append(f"[{tarea_id}] {info['descripcion']}")
        for subtarea in info['subtareas']:
            resultado.append(f"   ... [{subtarea['id']}] {subtarea['descripcion']}")

    return "\n".join(resultado)

def editar_tarea(tarea_id, descripcion=None, eliminada=None):
    tarea=Tarea.objects.get(tarea_id=tarea_id)
    if descripcion is not None:
        tarea.descripcion=descripcion
    if eliminada is not None:
        tarea.eliminada=eliminada
    tarea.save()
    return tarea

def editar_subtarea(subtarea_id, descripcion=None, eliminada=None, tarea_id=None):
    subtarea=Subtarea.objects.get(subtarea_id=subtarea_id)
    if descripcion is not None:
        subtarea.descripcion=descripcion
    if eliminada is not None:
        subtarea.eliminada=eliminada
    if tarea_id is not None:
        subtarea.tarea=Tarea.objects.get(tarea_id=tarea_id)
    
    subtarea.save()
    return subtarea
    