import os
import subprocess
import asyncio

async def open_server():
    os.chdir('./core_API')
    
    subprocess.run(['python', 'manage.py', 'runserver'], check=True)
    
async def main():
    # Abrir el server
    await open_server()

if __name__ == "__main__":
    asyncio.run(main())
