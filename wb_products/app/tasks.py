from celery import shared_task
from .models import Product, Shop
from .parsers import parse_product_data


@shared_task
def parse_product_and_update_db(article_number: int):
    """Parses product data from a website and updates the database."""
    try:
        # Get parsed data from the parser
        parsed_data = parse_product_data(article_number)

        # Get or create the shop using the name and rating from parsed data
        shop, _ = Shop.objects.get_or_create(
            name=parsed_data['shop_name'],
            defaults={'rating': parsed_data['shop_rating']}
        )

        # Get or create the product using the article number
        product, created = Product.objects.get_or_create(
            article_number=article_number,
            defaults={
                'name': parsed_data['product_name'],
                'color': parsed_data['color'],
                'price_before_discounts': parsed_data.get('price_before_discounts', 0),
                'price_after_discounts': parsed_data.get('price_after_discounts', 0),
                'remainder': parsed_data.get('remainder', 0),
                'number_of_reviews': parsed_data.get('number_of_reviews', 0),
                'rating': parsed_data.get('rating', 0),
                'shop': shop
            }
        )

        # If the product already exists, update its data
        if not created:
            for key, value in parsed_data.items():
                setattr(product, key, value)
            product.save()
            print(f"Product with Article Number {article_number} updated.")
        else:
            print(f"Product with Article Number {article_number} created.")

    except Exception as e:
        print(f"Error while parsing or updating data: {e}")
