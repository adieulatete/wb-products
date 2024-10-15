## WB-products

### General information about the project
API for obtaining product data on the Wilberries website by article number

#### Functional

Endpoints:  
• Admin panel - /admin;  
• Endpoint for loading product data - api/products/parse-product/;  
• Endpoint for receiving all products - api/products/list-products/;  

#### Technologies used

`Python`, `PostgreSQL`, `Git`, `Docker`, `Celery`, `Redis`

#### Libraries used

[`Django`](https://github.com/django/django),
[`Django REST framework`](https://github.com/encode/django-rest-framework),
[`Redis`](https://github.com/redis/redis)
[`Celery`](https://github.com/celery/celery)

### Deploy 

```bash
cd ~
git clone https://github.com/adieulatete/wb-products.git
cd ~/wb-products
```

Create environment variables
```bash
cp .env.example .env
vim .env
```

Launching the application
```bash
docker-compose up --build -d
```
