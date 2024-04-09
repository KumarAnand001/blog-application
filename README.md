# Django Blog Application

This is a simple blog application built using Django and Django REST Framework.

## Setup Instructions:

1. Clone the repository:
-git clone https://github.com/KumarAnand001/blog-application

2. Navigate to the project directory:
-cd blog_app

3. Install dependencies:
   
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

## Authentication:

Token-based authentication is required to access certain endpoints. Obtain a token by sending a POST request to `api-token-auth/` with valid credentials.

### API Endpoints with example:

**Request:**

#### List Posts:

-GET /api/blog/list-post/

**Response (200 OK):**
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

#### Create Post:
-POST /api/blog/post/

**Request Body**
{
    "title" :"High time to set up India’s AI regulator AIDAI",
    "body" :"The Artificial Intelligence and Data Authority of India (AIDAI) will ensure speedy and equitable development of this sector. The urgency for the speedy development of an artificial intelligence (AI) regulatory framework is growing day",
    "author" : 1
}

**Response Body**
{
    "data": {
        "id": 11,
        "title": "High time to set up India’s AI regulator AIDAI",
        "body": "The Artificial Intelligence and Data Authority of India (AIDAI) will ensure speedy and equitable development of this sector. The urgency for the speedy development of an artificial intelligence (AI) regulatory framework is growing day",
        "likes": 0,
        "author": 1
    },
    "messege": "blog created successfully"
}
