# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError

class HrWorkEntry(models.Model):
    _inherit = 'hr.work.entry'

    subarea_id = fields.Many2one('agricola.catalogos.subareas', 'Sub Area')
    area_id = fields.Many2one('agricola.catalogos.areas', related='subarea_id.area_id',store=True,string='Area')
    finca_id = fields.Many2one('agricola.catalogos.fincas',related="area_id.finca_id",store=True,string="Finca")
    produccion = fields.Float('Producción', digits=(16,2))
    udm_produccion = fields.Many2one('uom.uom', string='Unidad de Producción')

    @api.model_create_multi
    def create(self, vals):
        for v in vals:
            create_desde_app = v.pop('create_desde_app', False)
            if create_desde_app:
                v['contract_id'] = self.env['hr.employee'].browse(v['employee_id']).contract_id.id

        result = super().create(vals)
        return result
