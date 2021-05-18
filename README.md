**1. Description.**
----
  This project may explain how to work with real API on basic example. It's imaginary social media link-API, where you can try yoursel requests like GET, PUT, POST, PATCH and see what to be. 

**2. Setup. How to install project on local machine.**
----
- Download project on your local machine: `git clone git@github.com:IMegaMaan/api_final_yatube.git` (by SSH using) or see docs: https://git-scm.com/docs/git-clone;
- Create virtial environment: `python3 -m venv /path/to/new/virtual/environment`;
- Activate virtial environment:
    Windows: `C:\> <venv>\Scripts\activate.bat`
    Lunix: `source <venv>/bin/activate`
  officcal docs venv:https://docs.python.org/3/library/venv.html
- Configure dependencies: `pip install -r requirements.txt`
- Launch project by using: `python manage.py runserver`
- Go to the page: /redoc of project. Full url on yout local machine by default: http://127.0.0.1:8000/redoc/
  
**3. Examples. Requests examples to API.**
  ----
  
  **Title**

* **URL**

 http://127.0.0.1:8000/api/v1/posts/

* **Method:**
  
  GET
  
*  **URL Params**

   `group=[integer]` # id number of group

   **Required:**
 
   `group=[integer]`


* **Success Response:**

  * **Code:** 200 <br />
    **Content:** 
 `[
  {
    "id": 0,
    "text": "string",
    "author": "string",
    "pub_date": "2019-08-24T14:15:22Z"
  }
]`
