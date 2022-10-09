# python-ITE-306-flask-Hospital-Website
Creating a Hospital Website using Flask Framework

### Step 1: Run Flask .venv

  * Open Terminal and type this commands:<br>
    
      `py -3 -m venv .venv 
      .venv\scripts\activate`
    
    
 ### Step 2: Run `function.py` in terminal and make sure you are in the folder using this command:
 
    python function.py
    
    
    
  code:
  
  
      from flask import Flask, render_template, url_for, request, redirect


      app = Flask(__name__)


      @app.route("/home")
      def home():
          return render_template("index.html")


      @app.route("/about")
      def about():
          return render_template("about.html")


      @app.route("/contact")
      def contact():
          return render_template("contact.html")


      @app.route("/treatment")
      def treatment():
          return render_template("treatment.html")


      @app.route("/partner")
      def partner():
          return render_template("partner.html")


      @app.route("/service")
      def service():
          return render_template("service.html")


      if __name__ == "__main__":
            app.run(debug=True)
    
    
   ####   the output will be:
   
   
      (.venv) C:\Users\jesre\OneDrive\Desktop\flask\flask_website>python function.py
      * Serving Flask app 'function'
      * Debug mode: on
      WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
      * Running on http://127.0.0.1:5000
      Press CTRL+C to quit
      * Restarting with stat
      * Debugger is active!
      * Debugger PIN: 836-352-937
      
      
      
      
   #### Try to open the url:
   
        http://127.0.0.1:5000/home
        http://127.0.0.1:5000/about
        http://127.0.0.1:5000/contact
        http://127.0.0.1:5000/service
        http://127.0.0.1:5000/partner
        http://127.0.0.1:5000/treatment
   
     



## Documentation:


![Screenshot (87)](https://user-images.githubusercontent.com/113341443/194739474-3f42ca2e-53ef-4087-a4d0-481bd7c05f79.png)
![Screenshot (88)](https://user-images.githubusercontent.com/113341443/194739476-f7b42d59-370d-40fb-aa27-2a74bdf84d58.png)
![Screenshot (89)](https://user-images.githubusercontent.com/113341443/194739478-30f08552-c1cd-42bd-b997-d0b7fc469963.png)
![Screenshot (90)](https://user-images.githubusercontent.com/113341443/194739479-4ea2da7d-e2cf-40ff-9b6a-dba82dd3519e.png)
![Screenshot (91)](https://user-images.githubusercontent.com/113341443/194739480-9a3e821c-4a11-46c6-8e90-23fc8341de91.png)
![Screenshot (92)](https://user-images.githubusercontent.com/113341443/194739483-7b55086d-5c3d-493d-81b9-7599382836a9.png)
![Screenshot (93)](https://user-images.githubusercontent.com/113341443/194739484-fd6af4a6-6800-42ba-b05f-af37c0a697d7.png)
![Screenshot (80)](https://user-images.githubusercontent.com/113341443/194739485-811d96f9-3da9-423d-aa28-821a8f3a5a57.png)
![Screenshot (81)](https://user-images.githubusercontent.com/113341443/194739489-a266cd6a-b0d9-419a-867f-fd6dd93e3239.png)
![Screenshot (82)](https://user-images.githubusercontent.com/113341443/194739490-d2c21bb0-4f6a-44d2-931d-2efb6805f43a.png)
![Screenshot (83)](https://user-images.githubusercontent.com/113341443/194739492-9b4a94b2-d918-4f98-ab7e-c0518e925ec4.png)
![Screenshot (84)](https://user-images.githubusercontent.com/113341443/194739494-d0e2d0b2-9212-4936-82b9-10dffd9086f4.png)
![Screenshot (85)](https://user-images.githubusercontent.com/113341443/194739496-f686fdd9-3af8-4196-80de-3df17672cb9a.png)
![Screenshot (86)](https://user-images.githubusercontent.com/113341443/194739500-78cd9cb1-7a96-416a-a417-59864ea4fcc3.png)
