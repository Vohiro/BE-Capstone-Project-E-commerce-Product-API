# 🛒 E-Commerce Product API

A **Django REST Framework (DRF)** project providing APIs for managing **products** and **users** in an e-commerce application.  
This backend is **role-based**:  

- **Customers** → can sign up, browse, and search for products.  
- **Admins** → can manage products (**CRUD** operations).  

---

## 🚀 Features

### ✅ Product Management
- Create, Read, Update, and Delete (CRUD) products.
- Each product includes:
  - `name`
  - `description`
  - `price`
  - `category`
  - `stock_quantity`
  - `image_url`
  - `created_at` (auto timestamp).
- Search products by **name** or **category**.
- Pagination on product list/search endpoints.

### 👤 User Management
- Custom **User model** with fields:
  - `username` (unique)
  - `email` (unique)
  - `password` (hashed)
  - `role` (`customer` by default, `admin` if promoted in Django Admin).
  
### 🔑 Roles
- **Customer**
  - Can view & search products.
  - Can sign up & log in.
- **Admin**
  - Can perform **all customer actions**.
  - Can manage products (**CRUD**).
  - Role assigned **only by a superuser** in Django Admin.

### 🔒 Authentication
- Custom **Signup API** (registers new users as customer).
- Custom **Login API** (returns **JWT access + refresh tokens**).
- Only authenticated users with **role = admin** can manage products.

---

## 🛠 Tech Stack
- Python **3.10+**
- Django **5+**
- Django REST Framework (**DRF**)
- **SimpleJWT** for authentication

---

## 📌 API Endpoints

### 🔐 Authentication
| Method | Endpoint                                 | Description                                    |
|--------|------------------------------------------|------------------------------------------------|
| POST   | `/api/accounts/registe/`                 | Register a new user (role = customer).         |
| POST   | `/api/accounts/login/`                   | Log in with username & password, returns JWT   |
| PATCH  | `api/accounts/users/{pk}/update_role`    | Update a user to role either customer or admin |


---

### 📦 Products
| Method | Endpoint                              | Description                      | Auth Required |     Role    |
|--------|---------------------------------------|----------------------------------|---------------|-------------|
| GET    | `/api/v1/products/`                   | List all products (paginated).   | No            |     Any     |
| GET    | `/api/v1/products/{pk}/`              | Retrieve product details.        | No            |     Any     |
| POST   | `/api/v1/products/`                   | Create a new product.            | Yes           |     Admin   |
| PUT    | `/api/v1/products/{pk}/`              | Update a product.                | Yes           |     Admin   |
| PATCH  | `/api/v1/products/{pk}/`              | Update a product.                | Yes           |     Admin   |
| DELETE | `/api/v1/products/{pk}/`              | Delete a product.                | Yes           |     Admin   |
| GET    | `/api/v1/products/search/?q=...`      | Search by name/category.         | No            |     Any     |
| GET    | `/api/v1/products/?category=...`      | filter by category id            | No            |     Any     |
| GET    | `/api/v1/products/?category__name=...`| filter by category name          | No            |     Any     |
| GET    | `/api/v1/products/?available=...`     | filter by product availabilty    | No            |     Any     |
| GET    | `/api/v1/products/?min_price=...`     | filter by minimum price          | No            |     Any     |
| GET    | `/api/v1/products/?max_price=...`     | filter by maximum price          | No            |     Any     |
| GET    | `/api/v1/products/?in_stock=...`      | filter by product in stock       | No            |     Any     |

---

###  Categories
| Method | Endpoint                         | Description                         | Auth Required |     Role    |
|--------|----------------------------------|-------------------------------------|---------------|-------------|
| GET    | `api/v1/categories/`             | List all categories (paginated).    | No            |     Any     |
| GET    | `api/v1/categories/{pk}/`        | Retrieve a category details.        | No            |     Any     |
| POST   | `api/v1/categories/`             | Create a new category.              | Yes           |     Admin   |
| PUT    | `api/v1/categories/{pk}/`        | Update a category.                  | Yes           |     Admin   |
| PATCH  | `api/v1/categories/{pk}/`        | Update a category.                  | Yes           |     Admin   |
| DELETE | `api/v1/categories/{pk}/`        | Delete a category.                  | Yes           |     Admin   |


---

###  Reviews
| Method | Endpoint                                    | Description                        | Auth Required |     Role             |
|--------|---------------------------------------------|------------------------------------|---------------|----------------------|
| GET    | `api/v1/products/{pk}/reviews/`             | List all reviews for a product.    | No            |     Any              |
| GET    | `api/v1/products/{pk}/reviews/{pk}/`        | Retrieve a review for a product.   | No            |     Any              |
| POST   | `api/v1/products/{pk}/reviews/{pk}/`        | Create a new review.               | Yes           |     customer/Admin   |
| PUT    | `api/v1/products/{pk}/reviews/{pk}/`        | Update a review.                   | Yes           |     customer/Admin   |
| PATCH  | `api/v1/products/{pk}/reviews/{pk}/`        | Update a review.                   | Yes           |     customer/Admin   |
| DELETE | `api/v1/products/{pk}/reviews/{pk}/`        | Delete a review.                   | Yes           |     customer/Admin   |


---

###  Product Images
| Method | Endpoint                                   | Description                        | Auth Required |     Role    |
|--------|--------------------------------------------|------------------------------------|-------------- |-------------|
| GET    | `api/v1/products/{pk}/images/`             | List all images for a product.     | No            |     Any     |
| GET    | `api/v1/products/{pk}/images/{pk}/`        | Retrieve a image for a product.    | No            |     Any     |
| POST   | `api/v1/products/{pk}/images/{pk}/`        | Add an new image to a product.     | Yes           |     Admin   |
| DELETE | `api/v1/products/{pk}/images/{pk}/`        | Delete an new image for a product. | Yes           |     Admin   |


---

### 📦 wishlists
| Method | Endpoint                               | Description                                        | Auth Required |     Role             |
|--------|----------------------------------------|----------------------------------------------------|---------------|----------------------|
| GET    | `/api/v1/wishlists/`                   | List all products in a user wishlists              | No            |     Any              |
| GET    | `/api/v1/wishlists/{pk}/`              | Retrieve a product detail in a user wishlists.     | No            |     Any              |
| POST   | `/api/v1/wishlists/`                   | Add a new product to a user wishlists.             | Yes           |     customer/Admin   |
| DELETE | `/api/v1/wishlists/{pk}/`              | Delete a product from a user wishlist.             | Yes           |     customer/Admin   |

---

## 🔒 Roles & Permissions

### 👤 Customer
- Can **sign up & log in**.
- Can **view & search** products.

### 🛠 Admin
- Same as customer **+ product CRUD management**.
- Role assigned **via Django Admin Panel and update-role endpoint**.

---

## 🛠 Future Enhancements
- 🛍 Order Management (customers place orders, stock auto-reduces).
- 📧 Password reset with email verification.
- 🔑 Role-based API endpoint for promoting/demoting users (admin-only).
- 🎯 Advanced filtering (price range, stock availability).

---

## 📜 License
MIT License © 2025

