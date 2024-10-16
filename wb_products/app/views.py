from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Product
from .serializers import ProductSerializer
from .tasks import parse_product_and_update_db


class ProductViewSet(viewsets.ViewSet):
    """A viewset for handling product-related operations."""

    @action(detail=False, methods=['post'], url_path='parse-product')
    def parse_product(self, request):
        """Start parsing product data by article number."""
        article_number = request.data.get('article_number')

        if not article_number:
            return Response(
                {"error": "article_number is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Call the Celery task to parse the product data
        parse_product_and_update_db.delay(int(article_number))
        
        return Response(
            {"message": f"Parsing started for product with article number {article_number}."},
            status=status.HTTP_202_ACCEPTED
        )

    @action(detail=False, methods=['get'], url_path='list-products')
    def list_products(self, request):
        """List all products."""
        products = Product.objects.select_related('shop')
        serializer = ProductSerializer(products, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
