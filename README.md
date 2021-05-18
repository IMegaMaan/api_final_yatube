**1. Description.**
----
  This project may explain how to work with real API on basic example. It's imaginary social media link-API, where you can try yoursel requests like GET, PUT, POST, PATCH and see what to be. 

**2. Setup. How to install project on local machine.**
----
- Download project on your local machine: git clone git@github.com:IMegaMaan/api_final_yatube.git (by SSH using) or see docs: https://git-scm.com/docs/git-clone;
- Create virtial environment: python3 -m venv /path/to/new/virtual/environment;
- Activate virtial environment:
    Windows: C:\> <venv>\Scripts\activate.bat
    Lunix: source <venv>/bin/activate
  officcal docs venv:https://docs.python.org/3/library/venv.html
- Configure dependencies: pip install -r requirements.txt
- Launch project by using: python manage.py runserver
- Go to the page: /redoc of project. Full url on yout local machine by default: http://127.0.0.1:8000/redoc/
  
**3. Examples. Requests examples to API.**
  ----
  
  **Title**
----
  <_Additional information about your API call. Try to use verbs that match both request type (fetching vs modifying) and plurality (one vs multiple)._>

* **URL**

  <_The URL Structure (path only, no root url)_>

* **Method:**
  
  <_The request type_>

  `GET` | `POST` | `DELETE` | `PUT`
  
*  **URL Params**

   <_If URL params exist, specify them in accordance with name mentioned in URL section. Separate into optional and required. Document data constraints._> 

   **Required:**
 
   `id=[integer]`

   **Optional:**
 
   `photo_id=[alphanumeric]`

* **Data Params**

  <_If making a post request, what should the body payload look like? URL Params rules apply here too._>

* **Success Response:**
  
  <_What should the status code be on success and is there any returned data? This is useful when people need to to know what their callbacks should expect!_>

  * **Code:** 200 <br />
    **Content:** `{ id : 12 }`
 
* **Error Response:**

  <_Most endpoints will have many ways they can fail. From unauthorized access, to wrongful parameters etc. All of those should be liste d here. It might seem repetitive, but it helps prevent assumptions from being made where they should be._>

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "Log in" }`

  OR

  * **Code:** 422 UNPROCESSABLE ENTRY <br />
    **Content:** `{ error : "Email Invalid" }`

* **Sample Call:**

  <_Just a sample call to your endpoint in a runnable format ($.ajax call or a curl request) - this makes life easier and more predictable._> 

* **Notes:**

  <_This is where all uncertainties, commentary, discussion etc. can go. I recommend timestamping and identifying oneself when leaving comments here._> 
