{
    'name': 'Product Margin Report',
    'version': '1.0',
    'summary': 'Product-wise margin report with filter & group by',
    'description': 'Shows unit price, cost, and margin per product from invoices.',
    'author': 'Concept',
    'depends': ['account', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_margin_report_view.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'OPL-1',
    'price': 50.00,
    'currency': 'USD',
}
