{
    'name': 'Related Products & Recently Viewed',
    'version': '2.3',
    'category': 'Website',
    'author': 'Real Tech',
    'license': 'LGPL-3',
    'summary': 'Carousel of recently clicked products on website',
    'price': 20,
    'currency': 'USD',
    'depends': ['website'],
    'data': [
        'views/recent_products_carousel.xml',
    ],
    'images': [
        'static/description/main_screenshot.gif',
        'images/main_1.png',
        'images/main_2.png',
        'images/main_3.png'
    ],
    'assets': {
        'web.assets_frontend': [
            'product_carousel/static/src/scss/recent_products_carousel.scss',
            'product_carousel/static/src/js/recent_products_carousel.js',
        ],
    },
    'installable': True,
    'application': False,
}