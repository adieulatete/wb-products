from collections.abc import Mapping

import requests
import pandas as pd


def parse_product_data(article_number: int) -> Mapping[str, str]:
    """
    Parses product data from a website based on the provided article number.
    """
    url = f'https://card.wb.ru/cards/v2/detail?appType=1&curr=rub&dest=-1257786&spp=30&ab_testing=false&nm={article_number}'
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data for article number {article_number}. Status code: {response.status_code}")
    
    json_data = response.json()
    df = pd.DataFrame(json_data['data']['products'])
    result = df[df['id'] == article_number].to_dict(orient='records')[0]

    product_data = {
        'product_name': result['name'],
        'color': result.get('colors')[0]['name'] if result.get('colors') else None,
        'price_before_discounts': result['sizes'][0].get('price')['basic'] / 100 if result['sizes'][0].get('price') else 0,
        'price_after_discounts': result['sizes'][0].get('price')['product'] / 100 if result['sizes'][0].get('price') else 0,
        'remainder': result['totalQuantity'],
        'number_of_reviews': result['feedbacks'],
        'rating': result['reviewRating'],
        'shop_name': result['supplier'],
        'shop_rating': result['supplierRating'],
    }

    return product_data
