from app import app, db

# Ejecuta dentro del contexto de la aplicación Flask
with app.app_context():
    db.create_all()
    print("✔️ Base de datos y tablas creadas correctamente.")
