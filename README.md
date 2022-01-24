
# Instalar (Hecho en Django 4.0) #
Para instalar todas las dependencias del proyecto debemos correr: 

    - pip install -r requirements.txt


# URLS #

## Get Prime Numbers ##
    - http://localhost:8000/get-prime-numbers/?number=10

![](readme_imgs/get-prime-numbers.png)


## Convert Height ##

    - http://localhost:8000/convert-height/

    Solicitud de ejemplo:
        {  
            "name": "Pedro", 
            "height": "70 pulgadas" 
        }


![](readme_imgs/convert-height.png)


## Set Data ##

Nota: Para usar esta url, primero se debe preparar la base de datos, es decir, debe crearse con el nombre conectivity y poner la confoguración adecuada en la variable: 
DB_ENGINE = create_engine('postgresql://postgres:emjvp@localhost:5432/conectivity') línea 19,
esto puede modificarse tomando encuenta la estructura: create_engine('postgresql://{user}:{password}@{host}:{port}/conectivity')

Además de esto para generar la el modelo del proyecto debe ejecutarse el archivo manage.py de esta forma:

python3 manage.py; esto por que SqlAlchemy tuvo que adicionarse; es algo similar a las migraciones.

Todo lo anterior dentro del settings ubicado en la ruta conectivity/settings.py


    - http://localhost:8000/set-data/

    Solicitud de ejemplo:
        {  
            "fullname": "sdffdsf",
            "email": "dfszdfsd@example.com",
            "phone": "12334454545"
        }
    
![](readme_imgs/set-data.png)
    
