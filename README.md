# 📝 Django Blog Post Manager

A modern and responsive **Blog Post Management System** built with **Python and Django** using **Class-Based Views (CBVs)**.

This project demonstrates how to build a complete database-driven CRUD application in Django where users can create, view, update, search, and delete blog posts. The application also supports image uploads and provides a clean, responsive interface using **Bootstrap 5**.

---

## 🚀 Project Overview

The **Django Blog Post Manager** is a simple but complete blog management application designed for learning and practicing Django development.

The project focuses on Django's **Class-Based Views** and demonstrates how common web application operations can be implemented using:

* `ListView`
* `DetailView`
* `CreateView`
* `UpdateView`
* `DeleteView`

Users can manage blog posts through an easy-to-use interface.

Each post can contain:

* 📌 Title
* 📝 Content
* 🏷️ Category
* 🖼️ Image

The application also includes a **search feature** that allows users to search posts by title or category.

---

# ✨ Features

## 📋 Post Management

Complete CRUD functionality is implemented.

### Create Post

Users can create a new blog post by providing:

* Post title
* Post content
* Category
* Post image

---

### 👀 View Posts

All available posts are displayed in a responsive post listing.

Each post contains:

* Post number
* Title
* Category
* View Details button

---

### 📄 Post Details

Users can open an individual post and view complete information including:

* Post ID
* Title
* Category
* Full content
* Uploaded image

The detail page also provides options to:

* ✏️ Edit the post
* 🗑️ Delete the post
* ↩️ Return to the post list

---

### ✏️ Update Post

Existing posts can be updated using Django's `UpdateView`.

Users can modify:

* Title
* Content
* Category
* Image

---

### 🗑️ Delete Post

Posts can be deleted using Django's `DeleteView`.

A confirmation page is displayed before deleting a post to prevent accidental deletion.

---

# 🔎 Search Functionality

The project includes a search feature on the post listing page.

Users can search posts using:

* Title
* Category

The search uses Django ORM's `icontains` lookup, making the search **case-insensitive**.

For example:

```text
Programming
python
Django
Web Development
```

A search URL looks like:

```text
/post/post_view/?search=Programming
```

The search logic is implemented inside `PostListView`.

---

# 🖼️ Image Upload

Each post supports an optional image.

Images are uploaded using Django's `ImageField`.

Images are stored inside:

```text
media/post_images/
```

Example:

```python
image = models.ImageField(upload_to="post_images")
```

The application also handles posts without images by displaying a friendly placeholder.

---

# 📱 Responsive Design

The frontend is designed using **Bootstrap 5** and is responsive across different screen sizes.

The UI works on:

* 💻 Desktop
* 💻 Laptop
* 📱 Tablet
* 📱 Mobile

Responsive Bootstrap classes are used throughout the templates.

---

# 🎨 User Interface

The project uses a clean and modern UI design with:

* Bootstrap 5
* Bootstrap Icons
* Responsive cards
* Rounded buttons
* Responsive tables
* Shadow effects
* Mobile-friendly layouts
* Clean form layouts
* Empty states
* Delete confirmation interface

---

# 🛠️ Technologies Used

| Technology               | Purpose               |
| ------------------------ | --------------------- |
| Python                   | Programming Language  |
| Django                   | Backend Web Framework |
| SQLite                   | Database              |
| HTML5                    | Page Structure        |
| CSS3                     | Styling               |
| Bootstrap 5              | Responsive UI         |
| Bootstrap Icons          | Icons                 |
| Django ORM               | Database Operations   |
| Django Class-Based Views | CRUD Architecture     |
| Pillow                   | Image Processing      |

---

# 🧠 Django Concepts Practiced

This project covers several important Django concepts.

### Class-Based Views

The project uses:

```python
ListView
DetailView
CreateView
UpdateView
DeleteView
```

---

### Django Models

The project contains a `Post` model.

```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="post_images")
    content = models.TextField()
    catagory = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
```

---

### Django Forms

The project uses Django's automatic ModelForm generation through:

```python
fields = [
    "title",
    "content",
    "image",
    "catagory"
]
```

---

### Django URL Routing

The application uses named URLs and namespaces:

```python
app_name = "blog_app"
```

Example:

```django
{% url 'blog_app:post_detail_view' post.pk %}
```

---

### Django ORM

Database operations are performed using Django ORM.

Examples include:

```python
Post.objects.all()
```

and:

```python
Post.objects.filter(...)
```

---

### Search Queries

Search is implemented using:

```python
title__icontains
```

and:

```python
catagory__icontains
```

---

### Reverse URL Resolution

The `Post` model contains:

```python
def get_absolute_url(self):
    return reverse(
        "blog_app:post_detail_view",
        kwargs={"pk": self.pk}
    )
```

This allows Django's `CreateView` and `UpdateView` to redirect automatically to the post detail page.

---

# 📂 Project Structure

```text
Django-Blog-Post-Manager/
│
├── blog/
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── ...
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── post_list.html
│   │   ├── post_detail.html
│   │   ├── post_create_form.html
│   │   └── post_confrim_delet.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── CBV/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── media/
│   └── post_images/
│
├── static/
│   └── ...
│
├── db.sqlite3
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

> **Note:** Your actual folder structure may differ slightly depending on how your Django project is organized.

---

# 🗃️ Database Model

The main model is `Post`.

```python
class Post(models.Model):

    title = models.CharField(max_length=200)

    image = models.ImageField(
        upload_to="post_images"
    )

    content = models.TextField()

    catagory = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "blog_app:post_detail_view",
            kwargs={"pk": self.pk}
        )
```

---

# 🔗 URL Configuration

The application uses the following URL patterns:

```python
from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

app_name = "blog_app"

urlpatterns = [

    path(
        "post/post_view/",
        PostListView.as_view(),
        name="post_list_view"
    ),

    path(
        "post/<int:pk>/",
        PostDetailView.as_view(),
        name="post_detail_view"
    ),

    path(
        "post/create_view/",
        PostCreateView.as_view(),
        name="post_create_view"
    ),

    path(
        "post/<int:pk>/post_update_view/",
        PostUpdateView.as_view(),
        name="post_update_view"
    ),

    path(
        "post/<int:pk>/post_delete_view/",
        PostDeleteView.as_view(),
        name="post_delete_view"
    ),
]
```

---

# 👨‍💻 Views Architecture

## PostListView

Displays all posts and provides search functionality.

```python
class PostListView(ListView):

    model = Post

    template_name = "post_list.html"

    context_object_name = "posts"

    def get_queryset(self):

        queryset = Post.objects.all()

        search_query = self.request.GET.get(
            "search",
            ""
        )

        if search_query:

            queryset = (
                queryset.filter(
                    title__icontains=search_query
                )
                |
                queryset.filter(
                    catagory__icontains=search_query
                )
            )

        return queryset
```

---

## PostDetailView

Displays complete information about a specific post.

```python
class PostDetailView(DetailView):

    model = Post

    template_name = "post_detail.html"

    context_object_name = "post"
```

---

## PostCreateView

Creates a new post.

```python
class PostCreateView(CreateView):

    model = Post

    template_name = "post_create_form.html"

    fields = [
        "title",
        "content",
        "image",
        "catagory"
    ]
```

---

## PostUpdateView

Updates an existing post.

```python
class PostUpdateView(UpdateView):

    model = Post

    template_name = "post_create_form.html"

    fields = [
        "title",
        "content",
        "image",
        "catagory"
    ]
```

---

## PostDeleteView

Deletes a post after confirmation.

```python
class PostDeleteView(DeleteView):

    model = Post

    template_name = "post_confrim_delet.html"

    success_url = reverse_lazy(
        "blog_app:post_list_view"
    )
```

---

# ⚙️ Installation & Setup

Follow these steps to run the project locally.

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/szofficiall/Django-Blog-Post-Manager.git
```

---

## 2️⃣ Navigate to the Project

```bash
cd Django-Blog-Post-Manager
```

---

## 3️⃣ Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

---

## 4️⃣ Activate Virtual Environment

Windows CMD:

```bash
venv\Scripts\activate
```

PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` does not exist, install Django and Pillow:

```bash
pip install django pillow
```

---

# 🗄️ Database Setup

Run migrations:

```bash
python manage.py makemigrations
```

Then:

```bash
python manage.py migrate
```

---

# 👤 Create Superuser

To access Django Admin:

```bash
python manage.py createsuperuser
```

Enter:

```text
Username
Email
Password
```

---

# ▶️ Run Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

---

# 🔐 Django Admin

You can access the Django admin panel at:

```text
http://127.0.0.1:8000/admin/
```

Login using the superuser credentials created earlier.

---

# 📸 Media Configuration

Because the project supports image uploads, make sure media configuration exists in `settings.py`.

Example:

```python
MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"
```

During development, media URLs can be served from the project's main `urls.py`.

Example:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # project URLs
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
```

---

# 🔍 How Search Works

The search form sends a GET request:

```text
/post/post_view/?search=Programming
```

Django receives the query through:

```python
self.request.GET.get("search", "")
```

Then the posts are filtered using:

```python
title__icontains
```

or:

```python
catagory__icontains
```

Because `icontains` is case-insensitive:

```text
Programming
programming
PROGRAMMING
```

can match the same category.

---

# 🔄 CRUD Flow

The application follows this basic flow:

```text
             ┌─────────────────┐
             │   Post List     │
             └────────┬────────┘
                      │
          ┌───────────┼────────────┐
          │           │            │
          ▼           ▼            ▼
      Create        View         Search
          │           │
          ▼           ▼
      Database      Detail
                      │
                ┌─────┴─────┐
                │           │
                ▼           ▼
              Update      Delete
```

---

# 📚 What I Learned From This Project

This project helped me practice:

* Django project structure
* Django apps
* Models
* Database migrations
* Django ORM
* Class-Based Views
* CRUD operations
* ListView
* DetailView
* CreateView
* UpdateView
* DeleteView
* ModelForm handling
* URL namespaces
* Dynamic URLs
* URL reversing
* `get_absolute_url()`
* GET request handling
* Search functionality
* Case-insensitive searching
* ImageField
* Media files
* Django templates
* Template inheritance
* CSRF protection
* Bootstrap 5
* Responsive design
* Git & GitHub workflow

---

# 🚧 Future Improvements

The project can be extended with more advanced functionality.

### 🔐 Authentication

Add:

* User registration
* Login
* Logout
* Password reset

---

### 👤 User-Based Posts

Allow users to create and manage only their own posts.

---

### 💬 Comments

Add a comment system so users can comment on blog posts.

---

### ❤️ Likes

Allow users to like and unlike posts.

---

### 🏷️ Category Filtering

Add dedicated category filters such as:

```text
Programming
Django
Python
Web Development
Technology
Tutorials
```

---

### 📄 Pagination

Add pagination when the number of posts becomes large.

---

### 🔎 Advanced Search

Search across:

* Title
* Content
* Category

using Django `Q` objects.

---

### 🖼️ Image Preview

Add image preview before uploading a post image.

---

### 🌙 Dark Mode

Add a dark/light theme switcher.

---

# 🧪 Testing

Run Django's test suite using:

```bash
python manage.py test
```

Testing can be extended to cover:

* Post creation
* Post update
* Post deletion
* Post detail
* Search functionality
* URL resolution
* Model methods

---

# 📦 Requirements

Typical dependencies include:

```text
Django
Pillow
```

You can generate the current environment's dependency file using:

```bash
pip freeze > requirements.txt
```

---

# 🛡️ Security Notes

Before deploying the project to production:

* Set `DEBUG = False`
* Use a secure `SECRET_KEY`
* Configure `ALLOWED_HOSTS`
* Configure static files
* Configure media storage
* Use environment variables for secrets
* Use a production-ready database
* Configure HTTPS

Never commit sensitive credentials to GitHub.

---

# 🌐 GitHub

The project repository:

**Django Blog Post Manager**

Built as a Django practice project to demonstrate practical backend development and Class-Based View architecture.

---

# 👨‍💻 Author

## Sultan Zaib

Software Engineer | Django & Python Developer

This project was created as part of my journey in learning and practicing **Python, Django, backend development, database-driven applications, and responsive web development**.

---

# ⭐ Support

If you find this project useful for learning Django, consider giving the repository a ⭐ on GitHub.

---

# 📄 License

This project is available for educational and personal learning purposes.

You are free to study, modify, and improve the project for your own learning.

---

## 💙 Built With

```text
Python
Django
SQLite
HTML5
CSS3
Bootstrap 5
Bootstrap Icons
Pillow
```

### Built with ❤️ by Sultan Zaib
