from setuptools import setup, find_packages
#Esta es una de las formas más comunes de configurar un proyecto de Python para su distribución
#E instalación
#setuptools es una biblioteca que extiende las funcionalidades de la biblioteca estándar de Python
#llamada ¿diskutils? el cual se tiene que instalar con el gestor de paquetes pip, proporciona
#herramientas avanzadas para la creacion, distribucion, e instalacion de paquetes de Python y
#se utiliza para definir cómo se va a empaquetar y como se va a distribuir el proyecto incluyendo
#detalles como dependencias, metadatos del paquete y archivos necesarios
#setup es una funcion proporcionada por setuptools que sirve con el nucleo de configuración de
#un paquete se utiliza dentro del archivo setup para poder definir varios aspectos de tu paquete
#por ejemplo, el nombre, la version, el autor, las dependencias y los módulos incluidos. En terminos
#simples setup es lo que le dice a Python como empaquetar y organizar el proyecto para que otros puedan
#instalarlo de manera fácil usando pip
#fin_packages es otra función útil también de setup tools que automáticamente busca y encuentra todos
#los paquetes directorios con archivos __init__.py dentro de tu proyecto, en lugar de especificar
#manualmente todos los paquetes en tu archivo setup puedes usar fin_packages para que los encuentre por ti
setup(
    name="aplicacion_ventas",
    version="0.1.0",
    author="Williams Cantaro",
    author_email="williams.cantaro@gmail.com",
    description="Paquete para gestionar ventas, precios, impuestos y descuentos",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/WCANTARO/APLICACION_DE_VENTAS.git",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    python_requires=">=3.7"
    )