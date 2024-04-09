# Django Blog Application

This is a simple blog application built using Django and Django REST Framework.

## Setup Instructions:

1. Clone the repository:
-git clone https://github.com/KumarAnand001/blog-application

2. Navigate to the project directory:
-cd blog_app

3. Install dependencies:
-pip install djangorestframework
-pip install djangorestframework-simplejwt

   
4. Apply migrations:    
-py manage.py makemigrations
-python manage.py migrate
   
5. Create a superuser (for accessing the Django admin panel):
-python manage.py createsuperuser

6. Run the development server:
-python manage.py runserver

7. Access the application at http://localhost:8000/

## API Endpoints:

- **User Registration:** `POST /api/account/register/`
- **User Login:** `POST /api/account/login/`
- **List Posts:** `GET /api/blog/list-post/`
- **Create Post:** `POST /api/blog/post/`
- **Retrieve Post:** `GET /api/blog/post/<post_id>/`
- **Update Post:** `PATCH /api//blog/post/<post_id>/`
- **Delete Post:** `DELETE /api/blog/post/<post_id>/`
- **List Comments for a Post:** `GET /api/comment/cmts/posts/<post_id>/`
- **Create Comment for a Post:** `POST /api/comment/cmts/<post_id>/`
- **Like Post:** `POST /api/blog/like/`
- **Like Count:** `GET /api/blog/likes/`

## Authentication

This application uses token-based authentication to secure certain endpoints. Users need to register or log in to obtain an access token, which they can then use to access protected endpoints.

### Endpoints:

- **User Registration:**
  - **URL:** `/api/account/register/`
  - **Method:** `POST`
  - **Description:** Register a new user.
  - **Request Body Example:**
    ```json
    {
       "first_name": "Anand",
       "last_name": "Kumar",
       "username": "ansh123",
       "password": "Adfd565#"
    }
    ```
  - **Response Example:**
    ```json
    {
        "message": "Your account has been created"
    }
    ```

- **User Login:**
  - **URL:** `/api/account/login/`
  - **Method:** `POST`
  - **Description:** Log in a user and obtain a token for authentication.
  - **Request Body Example:**
    ```json
    {
       "username": "ansh123",
       "password": "Adfd565#"
    }
    ```
  - **Response Example:**
    ```json
   {
       "messege": "login successful",
       "data": {
           "token": {
               "refresh": "eyJhbGciOiJIUzcCI6IkpXVCJ9.eyJ0b2tlbl90eXBlI5MTgxLCJqdGkiOiIxZWY4ODI0ODk4NGINyIsInVzZXJfaWQiOjl9.N0fBT0ZHVL4mODQ_LYQrFm9zYDvPDqfeaRjDfrIbdbs",
               "access": "eyJhbGciOiJIUzIR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXByNjg5NDgxLCJpYXQiOjE3MTI2ODjAyZWFmZDg5MzFiMjQ3NmYIiwidXNlcl9pZCI6OX0.JeX6QVAXXf3OeRJ3UWF5asApRTB_6-39sV6mG1mCoGU"
           }
       }
   }
    ```

### Authentication Process:

To access protected endpoints, include the obtained access token in the `Authorization` header of your requests. Tokens have an expiration time, so if your token expires, obtain a new one using the refresh token provided during registration or login.


### API Endpoints with example:

#### List Posts:

- **Method:** `GET`
- **URL:** `/api/blog/list-post/`
- **Description:** Retrieve a list of all posts.
- **Response (200 OK):**
  ```json
  {
      "data": [
          {
              "id": 9,
              "title": "Dialogue",
              "body": "In addition to the frequency of updates, the thing that distinguishes most blogs from ordinary Web pages is the inclusion of forums for readers to post comments to which the blogger might respond.",
              "likes": 0,
              "author": 1
          },
          {
              "id": 10,
              "title": "Political blogs",
              "body": "The U.S. presidential election of 2004 brought blogs to a newfound prominence as bloggers for both parties used the Internet as another arena of debate and conversation—as well as fund-raising. Democratic presidential primary candidate Howard Dean was the most prominent user of the Internet and the blogosphere.",
              "likes": 0,
              "author": 1
          }
      ],
      "message": "post fetch successfully"
  }
  ```
  
Create Post:
-Method: POST
-URL: /api/blog/post/
-Description: Create a new post.
-Request Body:
   ```json
   {
       "title": "High time to set up India’s AI regulator AIDAI",
       "body": "The Artificial Intelligence and Data Authority of India (AIDAI) will ensure speedy and equitable development of this sector. The urgency for the speedy development of an artificial intelligence (AI) regulatory framework is growing day",
       "author": 1
   }
   ```
-Response (201 Created):
   ```json
   {
       "data": {
           "id": 11,
           "title": "High time to set up India’s AI regulator AIDAI",
           "body": "The Artificial Intelligence and Data Authority of India (AIDAI) will ensure speedy and equitable development of this sector. The urgency for the speedy development of an artificial intelligence (AI) regulatory framework is growing day",
           "likes": 0,
           "author": 1
       },
       "message": "blog created successfully"
   }
   ```

