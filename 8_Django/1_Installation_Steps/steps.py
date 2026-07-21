
"""

Step 1

- Create a virtual environment
"""

# python -m venv venv






'-----------------------------------------------------------------------'

"""






Step 2

- Activate the virtual environment
"""

# venv\Scripts\activate



"""

venv\Scripts\activate
│      │        │
│      │        └── The activation script
│      └────────── Scripts folder inside the virtual environment
└───────────────── Name of the virtual environment folder

"""









'-----------------------------------------------------------------------'
""" 









Step 3

- Chack a Django version
"""

# python -m django --version


"""  If Django is not installed   """

# pip install django









'-----------------------------------------------------------------------'
"""





Step 4

- Create a Django project
"""


# django-admin startproject myproject




'''
Move into the project folder:
'''

# cd myproject







'---------------------------------------------------------------------------------'
"""




Step 5

- Run the development server
"""

# python manage.py runserver












'----------------------------------------------------------------------------------'

'''



                                    Create environment
                                            │
                                            ▼
                                    python -m venv venv
                                            │
                                            ▼
                                    venv/
                                     ├── Scripts/
                                     ├── Lib/
                                     └── Include/
                                            │
                                            ▼
                                    Activate it
                                    venv\Scripts\activate
                                            │
                                            ▼
                                    (venv) C:\MyProject>
                                            │
                                            ▼
                                    Install Django
                                    pip install django
                                            │
                                            ▼
                                    Run your project
                                    python manage.py runserver









'''