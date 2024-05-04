import os
import platform
import subprocess
import asyncio

async def create_virtual_env():
    # Obtener el nombre del sistema operativo
    operating_system = platform.system()

    if operating_system == 'Windows':
        # Comandos específicos para Windows
        subprocess.run(['python', '-m', 'venv', 'env'], check=True)
        subprocess.run(['env\\Scripts\\activate.bat'], check=True, shell=True)
    elif operating_system in ('Linux', 'Darwin'):
        # Comandos específicos para Linux y MacOS
        subprocess.run(['python3', '-m', 'venv', 'env'], check=True)
        subprocess.run(['source', 'env/bin/activate'], check=True, shell=True)
    else:
        print("Sistema operativo no compatible.")

    # Crear el archivo .gitignore dentro de la carpeta env si no existe
    gitignore_path = os.path.join('env', '.gitignore')
    if not os.path.exists(gitignore_path):
        with open(gitignore_path, 'w') as f:
            # Ignorar todos los archivos y carpetas dentro de env
            f.write('# Generado automáticamente por el script de configuración\n')
            f.write('*\n')  

async def install_requirements(requirements_file):
    # Obtener la ruta completa del archivo de dependencias
    requirements_path = os.path.abspath(requirements_file)
    
    # Instalar las dependencias desde el archivo requirements.txt
    subprocess.run(['pip', 'install', '-r', requirements_path], check=True)

async def run_migrations():
    # Cambiar al directorio del proyecto
    os.chdir('./core_API')
    
    # Ejecutar las migraciones de Django
    subprocess.run(['python', 'manage.py', 'makemigrations'], check=True)
    subprocess.run(['python', 'manage.py', 'migrate'], check=True)

async def seed_database():
    # Sembrar la base de datos
    subprocess.run(['python', 'manage.py', 'seed_db'], check=True)
    
async def main():
    # Crear el entorno virtual y activarlo
    await create_virtual_env()

    # Instalar las dependencias
    await install_requirements('requirements.txt')

    # Migraciones
    await run_migrations()

    # Sembrar la base de datos
    await seed_database()

if __name__ == "__main__":
    asyncio.run(main())
