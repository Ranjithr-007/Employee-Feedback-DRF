# Employee-Feedback-DRF

# # Create virtual environment to isolate python dependencies
python -m venv ./venv

# # Activate virtual environment

source ./venv/bin/activate #(linux/mac users)

venv\Scripts\activate #(windows users)

# # Install dependencies
pip install -r requirements.txt

#  Prepare and run the app
# # Run migrations
python manage.py makemigrations
python manage.py migrate


# # Create superuser
python manage.py createsuperuser


# # Run the app
python manage.py runserver


Design
------


Admins and Users from Django's built-in authentication system are used to manage the app. Authenticated users may use the /api/admin endpoints. These endpoints are:

    Add, edit, delete and view employees (/api/admin/employees)
    Add, edit and view reviews. Reviews cannot be deleted. (/api/admin/reviews)
    Assign employees to give feedbacks to reviews. This is done by creating a feedback entry. Feedbacks cannot be deleted or edited via /api/admin admin routes. (/api/admin/feedbacks)

Unauthenticated users may use all other endpoints under /api/ endpoints. These endpoints are:

    View employees (/api/employees). It is possible to access all pending feedbacks for an employee by accessing /api/employees/{id}/pending-feedbacks
    View reviews (/api/reviews)
    Give feedback to reviews. This is done by consulting and patching existent feedback entries. (/api/feedbacks)
