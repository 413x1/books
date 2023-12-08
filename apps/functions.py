def get_book_filter(params_dict):
    query = {
        'title': 'title__icontains',
        'description': 'description__icontains',
        'category': 'category',
        'keywords': 'keywords__icontains',
        'price': 'price',
        'author': 'author',
    }

    filter_dict = {}

    for k, v in params_dict.items():
        if query.get(k) and v:
            filter_dict[query[k]] = v
        else:
            continue
    
    return filter_dict
