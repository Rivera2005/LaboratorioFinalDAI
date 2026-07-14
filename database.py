"""
Acceso a datos.

Responsabilidad: toda interacción con Supabase debe permanecer en este archivo.
No colocar llamadas a Supabase directamente en app.py.
"""
from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def obtener_libros():
    """Devuelve todos los libros ordenados por id."""
    respuesta = supabase.table("libros").select("*").order("id").execute()
    return respuesta.data

def obtener_libro_por_id(libro_id: int):
    respuesta = (
        supabase
        .table("libros")
        .select("*")
        .eq("id", libro_id)
        .execute()
    )
    if respuesta.data:
        return respuesta.data[0]
    
    return None

def insertar_libro(libro):
    response = (
        supabase
        .table("libros")
        .insert(libro)
        .execute()
    )
    return response.data

def actualizar_libro(id, libro):
    response = (
        supabase
        .table("libros")
        .update(libro)
        .eq("id", id)
        .execute()
    )
    return response.data

def eliminar_libro(id):
    response = (
        supabase
        .table("libros")
        .delete()
        .eq("id", id)
        .execute()
    )
    return response.data