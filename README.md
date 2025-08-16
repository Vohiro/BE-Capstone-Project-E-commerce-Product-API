🛒 E-Commerce Product API

A Django REST Framework (DRF) project providing APIs for managing products and users in an e-commerce application.
This backend is role-based: customers can sign up, browse, and search for products, while admins can manage products (CRUD).

🚀 Features
==> Product Management

Create, Read, Update, and Delete (CRUD) products.

Each product has:

name

description

price

category

stock_quantity

image_url

created_at (auto timestamp).

Search products by name or category.

Pagination on product list/search endpoints.

==> User Management

Custom User model with fields:

username (unique)

email (unique)

password (hashed)

role (customer by default, admin if promoted in Django admin).

==> Roles:

Customer → can only view/browse/purchase products.

Admin → can manage products (create, update, delete).

==> Authentication

Custom Signup API (registers new users as customer).

Custom Login API (returns JWT access + refresh tokens).

Only authenticated users with role = admin can manage products.

==> 🛠 Tech Stack

Python 3.10+

Django 5+

Django REST Framework (DRF)

SimpleJWT for authentication


==> 📌 API Endpoints
Authentication
Method	Endpoint	Description
POST	/api/signup/	Register a new user (role = customer by default).
POST	/api/login/	Log in with username & password, returns JWT tokens.
Products
Method	Endpoint	Description	Auth Required	Role
GET	/api/products/	List all products (paginated).	No	Any
GET	/api/products/<id>/	Retrieve product details.	No	Any
POST	/api/products/	Create a new product.	Yes	Admin
PUT	/api/products/<id>/	Update a product.	Yes	Admin
DELETE	/api/products/<id>/	Delete a product.	Yes	Admin
GET	/api/products/search/?q=<term>	Search products by name/category (paginated).	No	Any


==> 🔒 Roles & Permissions

Customer

Can sign up, log in.

Can view and search products.

Admin

Same as customer + can manage products (CRUD).

Role assigned only by a superuser in the Django Admin Panel.

==> 🛠 Future Enhancements

Order Management (customers place orders, stock auto-reduces).

Password reset with email verification.

Role-based API endpoint for promoting/demoting users (admin-only).

Advanced filtering (price range, stock availability).

==> 📜 License

MIT License © 2025