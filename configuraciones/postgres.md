Para instalar postgres en su pc linux:
sudo apt-get install postgresql

Crear usuario: CREATE USER bigdata WITH PASSWORD 'password';

Crar bd: CREATE DATABASE repoejemplo ENCODING 'UTF8' LC_COLLATE='C' LC_CTYPE='C' template=template0 OWNER bigdata;

Dar privilegios sobre una sola bd: GRANT ALL PRIVILEGES ON DATABASE repoejemplo to bigdata;

Para ingresar a la bd con el usuario previamente creado:
psql -d repoejemplo -U bigdataq