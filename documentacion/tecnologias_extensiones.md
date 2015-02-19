#Extensiones
##Flask-Bcrypt
Uso de http://flask-bcrypt.readthedocs.org/en/latest/ para generar el hash de las contraseñas, en vez de 
```
from werkzeug.security import generate_password_hash, check_password_hash
```
ya que puede estar roto en alguna versión de python 2.7.X, además de ser mas seguro al usar funciones lentas de hassings. En caso de usar werkzeug tampoco son muchos los cambios a realizar. Basicamente en la class User.

##itsdangerous
http://pythonhosted.org/itsdangerous/ Usado para los tokens de autentificación, para comprobar que nadie ha modificado el tiempo de caducidad, se firma este.