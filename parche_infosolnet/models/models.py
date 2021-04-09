# -*- coding: utf-8 -*-

from odoo import models, fields

class ServidorSQL(models.Model):
    _inherit = 'res.partner'

    servidor_sql = fields.Char(string="Conexión Admin")
    licencia_saint = fields.Char(string="Identificador")
    serial_saint = fields.Char(string="Serial")
    conexion_contab = fields.Char(string="Conexión Contab")
    nros_contratos = fields.One2many(
        'isn.contratos', 'identificador', string="Contratos")


class ProductosLicenciados(models.Model):
    _name = 'isn.productos'

    codprod = fields.Char(string="Codigo", required="True")
    name = fields.Char(string="Descripcion", required="True")
    duracion = fields.Integer(string="Duracion", required="True")
    unitario = fields.Selection(string="Unitario", selection=[("1", "Moviles"), ("0", "Cloud"), ("2", "Apps")])
    nros_contratos = fields.One2many(
        'isn.contratos', 'cod_serv', string="Contratos")

    class ContratosLicencias(models.Model):
        _name = 'isn.contratos'

        nro_contrato = fields.Char(string="Nro contrato", required=True)
        # identificador = fields.Char(string="Identificador", required="True")
        # cod_serv = fields.Char(string="Codigo producto", required="True")
        cantidad = fields.Integer(string="Cantidad", required=True)
        fecha_exp = fields.Date(string="Fecha expiración", required=True)
        activo = fields.Selection(selection=[("0", "Inactivo"), ("1", "Activo")], required=True)
        tipo_contrato = fields.Selection(selection=[("VM", "Local"), ("CL", "Cloud"), ("WM", "Windows")], required=True)
        name = fields.Char(string="Contrato", required="True")
        cod_serv = fields.Many2one('isn.productos', ondelete='cascade', string="Producto", required=True)
        identificador = fields.Many2one('res.partner', ondelete='cascade', string="Cliente", required=True)
        instancia_sql = fields.Char(string="Sql Server")
        data_base = fields.Char(string="Base Datos")
        user_sql = fields.Char(string="Usuario Sql")
        pass_sql = fields.Char(string="Password Sql")

