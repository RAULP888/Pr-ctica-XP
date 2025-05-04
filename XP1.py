import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Datos simulados
tareas = [
    {"nombre": "Mapa Mental", "fecha": "2025-05-02", "estado": "pendiente"},
    {"nombre": "Ecuaciones", "fecha": "2025-05-04", "estado": "pendiente"},
    {"nombre": "Reporte", "fecha": "2025-04-28", "estado": "realizada"},
]

# Función para filtrar tareas
def mostrar_tareas(filtro):
    for widget in contenedor_tareas.winfo_children():
        widget.destroy()

    for tarea in tareas:
        if filtro == "todas" or tarea["estado"] == filtro:
            texto = f'TAREA: {tarea["nombre"]} - Fecha: {tarea["fecha"]}'
            lbl = tk.Label(contenedor_tareas, text=texto, bg="#003366", fg="white", padx=10, pady=5)
            lbl.pack(fill="x", padx=20, pady=5)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calendario de Tareas")
ventana.geometry("500x400")
ventana.configure(bg="white")

# Título
titulo = tk.Label(ventana, text="TAREAS", font=("Helvetica", 16, "bold"), bg="white")
titulo.pack(pady=10)

# Botones de filtro
marco_botones = tk.Frame(ventana, bg="white")
marco_botones.pack(pady=10)

btn_todas = tk.Button(marco_botones, text="TODAS LAS TAREAS", bg="#003366", fg="white", command=lambda: mostrar_tareas("todas"))
btn_todas.pack(side="left", padx=5)

btn_pendientes = tk.Button(marco_botones, text="TAREAS PENDIENTES", bg="#003366", fg="white", command=lambda: mostrar_tareas("pendiente"))
btn_pendientes.pack(side="left", padx=5)

btn_realizadas = tk.Button(marco_botones, text="TAREAS REALIZADAS", bg="#003366", fg="white", command=lambda: mostrar_tareas("realizada"))
btn_realizadas.pack(side="left", padx=5)

# Contenedor para mostrar tareas
contenedor_tareas = tk.Frame(ventana, bg="white")
contenedor_tareas.pack(pady=10, fill="both", expand=True)

# Mostrar tareas al iniciar
mostrar_tareas("pendiente")

ventana.mainloop()