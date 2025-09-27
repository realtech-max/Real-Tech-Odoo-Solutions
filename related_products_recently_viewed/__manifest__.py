{
    'name': 'Related Products & Recently Viewed',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Carousel of recently clicked products on website',
    'depends': ['website'],
    'data': [
        'views/recent_products_carousel.xml',
    ],
    'images': [
        'images/main_screenshot.png',
        'images/main_1.png',
        'images/main_2.png',
        'images/main_3.png',
        'images/main_4.png',
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