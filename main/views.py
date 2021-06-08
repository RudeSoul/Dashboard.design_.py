from django.shortcuts import render

suppliers = [
    'Amazon',
    'Tinker',
    'eBay',
    'Alibaba'
]

supplier_categories = [
    'Automotive',
    'Electronics',
    'Aeronautical',
]

products = [
    {
        'id': '1',
        'site': '',
        'image': 'https://images.unsplash.com/photo-1560343090-f0409e92791a?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&dl=irene-kredenets-KStSiM1UvPw-unsplash.jpg&w=640',
        'supplier_info': {
            'supplier': 'Amazon',
            'category': 'Automotive',
            'stock_status': 'In Stock',
            'price': '49.99'
        },
        'product_info': {
            'title': '12 PCS Tyre and Wheel Bearings for Kia K5',
            'category': 'Car Parts',
        },
        'status': 'Draft',
        'created_at': '06/01/2021',
        'updated_at': '06/01/2021',
    },
    {
        'id': '2',
        'site': '',
        'image': 'https://images.unsplash.com/photo-1560343090-f0409e92791a?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&dl=irene-kredenets-KStSiM1UvPw-unsplash.jpg&w=640',
        'supplier_info': {
            'supplier': 'Amazon',
            'category': 'Automotive',
            'stock_status': 'In Stock',
            'price': '49.99'
        },
        'product_info': {
            'title': '12 PCS Tyre and Wheel Bearings for Kia K5',
            'category': 'Car Parts',
        },
        'status': 'Staged',
        'created_at': '06/01/2021',
        'updated_at': '06/01/2021',
    },
    {
        'id': '3',
        'site': '',
        'image': 'https://images.unsplash.com/photo-1560343090-f0409e92791a?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&dl=irene-kredenets-KStSiM1UvPw-unsplash.jpg&w=640',
        'supplier_info': {
            'supplier': 'Amazon',
            'category': 'Automotive',
            'stock_status': 'In Stock',
            'price': '49.99'
        },
        'product_info': {
            'title': '12 PCS Tyre and Wheel Bearings for Kia K5',
            'category': 'Car Parts',
        },
        'status': 'Active',
        'created_at': '06/01/2021',
        'updated_at': '06/01/2021',
    },
    {
        'id': '4',
        'site': '',
        'image': 'https://images.unsplash.com/photo-1560343090-f0409e92791a?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&dl=irene-kredenets-KStSiM1UvPw-unsplash.jpg&w=640',
        'supplier_info': {
            'supplier': 'Amazon',
            'category': 'Automotive',
            'stock_status': 'In Stock',
            'price': '49.99'
        },
        'product_info': {
            'title': '12 PCS Tyre and Wheel Bearings for Kia K5',
            'category': 'Car Parts',
        },
        'status': 'Inactive',
        'created_at': '06/01/2021',
        'updated_at': '06/01/2021',
    },
    {
        'id': '5',
        'site': '',
        'image': 'https://images.unsplash.com/photo-1560343090-f0409e92791a?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&dl=irene-kredenets-KStSiM1UvPw-unsplash.jpg&w=640',
        'supplier_info': {
            'supplier': 'Amazon',
            'category': 'Automotive',
            'stock_status': 'In Stock',
            'price': '49.99'
        },
        'product_info': {
            'title': '12 PCS Tyre and Wheel Bearings for Kia K5',
            'category': 'Car Parts',
        },
        'status': 'Draft',
        'created_at': '06/01/2021',
        'updated_at': '06/01/2021',
    },
    {
        'id': '6',
        'site': '',
        'image': 'https://images.unsplash.com/photo-1560343090-f0409e92791a?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&dl=irene-kredenets-KStSiM1UvPw-unsplash.jpg&w=640',
        'supplier_info': {
            'supplier': 'Amazon',
            'category': 'Automotive',
            'stock_status': 'In Stock',
            'price': '49.99'
        },
        'product_info': {
            'title': '12 PCS Tyre and Wheel Bearings for Kia K5',
            'category': 'Car Parts',
        },
        'status': 'Draft',
        'created_at': '06/01/2021',
        'updated_at': '06/01/2021',
    },
]

def homepage(request):
    context = {
        'suppliers': suppliers,
        'supplier_categories': supplier_categories,
        'products': products,
    }

    return render(request=request, template_name="main/home.html", context=context)
