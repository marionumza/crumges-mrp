{
    'name': 'MRP Potential Stock Visualization',
    'version': '18.0.1.0.2',
    'category': 'Manufacturing',
    'summary': 'Displays potential stock quantity based on BOM components availability',

    'author': 'Crumges',
    'license': 'AGPL-3',
    'depends': ['mrp', 'stock', 'product'],
    'data': [
        'views/product_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
