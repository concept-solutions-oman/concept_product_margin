from odoo import models, fields, api

class ProductMarginReport(models.Model):
    _name = 'product.margin.report'
    _description = 'Product Margin Report'
    _auto = False  # SQL view

    product_id = fields.Many2one('product.product', string='Product', readonly=True)
    company_id = fields.Many2one('res.company', string="Company")
    invoice_id = fields.Many2one('account.move', string="Invoice", readonly=True)
    invoice_date = fields.Date(string="Invoice Date")
    invoice_number = fields.Char(string="Invoice Number")
    
    price_unit = fields.Float(string='Unit Price', readonly=True)
    cost = fields.Float(string='Cost', readonly=True)
    margin = fields.Float(string='Margin', readonly=True)
    quantity = fields.Float(string="Quantity", readonly=True)

    move_type = fields.Selection(
        [
            ('out_invoice', 'Customer Invoice'),
            ('out_refund', 'Customer Credit Note'),
            ('in_invoice', 'Vendor Bill'),
            ('in_refund', 'Vendor Credit Note')
        ],
        string="Invoice Type",
        readonly=True
    )
   
    @api.model
    def init(self):
        self._cr.execute("DROP VIEW IF EXISTS product_margin_report")
        self._cr.execute("""
            CREATE VIEW product_margin_report AS
            SELECT
                aml.id AS id,
                aml.product_id AS product_id,
                aml.company_id AS company_id,
                aml.move_id AS invoice_id,
                am.invoice_date AS invoice_date,
                am.name AS invoice_number,
                aml.price_unit AS price_unit,
                aml.cost AS cost,
                aml.margin AS margin,
                am.move_type AS move_type,
                aml.quantity AS quantity
            FROM account_move_line aml
            JOIN account_move am ON aml.move_id = am.id
            WHERE am.move_type IN ('out_invoice', 'out_refund', 'in_invoice', 'in_refund')
            AND am.state = 'posted'
            AND aml.product_id IS NOT NULL
        """)



