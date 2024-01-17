# -*- coding:utf-8 -*-
from odoo import api, fields, models

class ProductTemplateCustom(models.Model):
    _inherit = 'product.template'

    default_code = fields.Integer(string='Referencia interna', unique=True)
    
    
    _sql_constraints = [ ('unique_default_code', 'unique(default_code)', 'Esta referencia interna ya existe en la base de datos!\nPor favor, introduce otra numeración')	]
    