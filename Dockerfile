# steps to create a Docer file

# choose a base OS like below and put the version oof the language you made the application in

FROM python:3.12-slim

# create a work diretory its like a new folder where your application will  live

WORKDIR  /app
# now copy th requirements file into the directory
COPY requirements.txt .
 # then install all the libraries in requirements into the Directory 
RUN pip install --no-cache-dir -r requirements.txt 


# now copy rest of the appliction code into the directory after this the entire app will be inside the directory

COPY . .

# now expose the port where the application runs # as we are currently using the FastAPI application which normaly runs on 8000
EXPOSE 8000  

# now specify the commands that run the application 

CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]


