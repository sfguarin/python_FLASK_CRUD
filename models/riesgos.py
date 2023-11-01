# from app import db

# class Riesgo(db.Model):
#     # Campos de la entidad Riesgo
#     id = db.Column(db.Integer, primary_key=True)
#     titulo = db.Column(db.String(100), nullable=False)
#     descripcion = db.Column(db.Text)
#     impacto = db.Column(db.String(20))
#     probabilidad = db.Column(db.String(20))
#     proveedor = db.Column(db.String(100))

#     # Relación con la entidad Usuario (cada riesgo está asociado a un usuario)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#     def __init__(self, titulo, descripcion, impacto, probabilidad, proveedor, user_id):
#         self.titulo = titulo
#         self.descripcion = descripcion
#         self.impacto = impacto
#         self.probabilidad = probabilidad
#         self.proveedor = proveedor
#         self.user_id = user_id



from app import db, ma

# Define el modelo de la entidad Riesgo
class Riesgo(db.Model):
    __tablename__ = 'riesgos'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    impacto = db.Column(db.String(20))
    probabilidad = db.Column(db.String(20))
    proveedor = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, titulo, descripcion, impacto, probabilidad, proveedor, user_id):
        self.titulo = titulo
        self.descripcion = descripcion
        self.impacto = impacto
        self.probabilidad = probabilidad
        self.proveedor = proveedor
        self.user_id = user_id

# Define el esquema de serialización para la entidad Riesgo
class RiesgoSchema(ma.Schema):
    class Meta:
        fields = ["id", "titulo", "descripcion", "impacto", "probabilidad", "proveedor", "user_id"]

# Crea instancias de los esquemas
riesgo_schema = RiesgoSchema()
riesgos_schema = RiesgoSchema(many=True)