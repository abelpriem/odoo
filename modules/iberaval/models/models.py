from odoo import models, fields

class IberavalEntity(models.Model):
    _name = "iberaval.entity"
    _description = "Entidad Financiera"
    _rec_name="descri_entidad"
    
    cod_entidad = fields.Char(string="COD_ENTIDAD")
    descri_entidad = fields.Char(string="DESCRI_ENTIDAD", required=True)
    nif = fields.Char(string="NIF")
    claset4 = fields.Char(string="CLASET4", required=True)
    domicilio = fields.Char(string="DOMICILIO")
    id_poblacion = fields.Integer(string="IDPOBLACION", required=True, default=0)
    contacto =fields.Char(string="CONTACTO")
    telefono1 = fields.Char(string="TELEFONO1")
    telefono2 = fields.Char(string="TELEFONO2")
    extension = fields.Char(string="EXTENSION")
    fax = fields.Char(string="FAX")
    cod_fichero = fields.Char(string="COD_FICHERO")
    nombre_fichero = fields.Char(string="NOMBRE_FICHERO")
    g3_bloqueo = fields.Char(string="G3_BLOQUEO", required=True, default="X")
    g3_control = fields.Char(string="G3_CONTROL")
    email = fields.Char(string="EMAIL")
    f_convenio = fields.Char(string="F_CONVENIO")
    aval_fase_dias = fields.Integer(string="AVAL_FASE_DIAS", required=True, default=0)
    g3_baja = fields.Char(string="G3_BAJA")
    bic = fields.Char(string="BIC")
    abreviatura = fields.Char(string="ABREVIATURA")
    cod_pais = fields.Char(string="COD_PAIS")
    g3_identidad = fields.Integer(string="G3_IDENTIDAD", default=0)
    
class IberavalAgency(models.Model):
    _name="iberaval.agency"
    _description="Agencia Financiera"
    _rec_name="descri_agencia"
    
    # FK de Entidad
    entity_id = fields.Many2one('iberaval.entity', string="Entidad Financiera", required=True, ondelete="cascade")
    
    cod_entidad = fields.Char(string="COD_ENTIDAD (Ref)", required=True)
    cod_agencia = fields.Char(string="COD_AGENCIA")
    descri_agencia = fields.Char(string="DESCRI_AGENCIA")
    grupo = fields.Char(string="GRUPO")
    nif = fields.Char(string="NIF")
    domicilio = fields.Char(string="DOMICILIO")
    id_poblacion = fields.Integer(string="IDPOBLACION", required=True, default=0)
    g3_bloqueo = fields.Char(string="G3_BLOQUEO", required=True, default="X")
    g3_control = fields.Char(string="G3_CONTROL")
    g3_baja = fields.Char(string="G3_BAJA")
    cod_pais = fields.Char(string="COD_PAIS")
    web_identidad = fields.Integer(string="WEB_IDENTIDAD")