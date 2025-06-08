import os
import shutil
from flask_frozen import Freezer
from app import app

def build_static():
    # Create docs directory if it doesn't exist
    if not os.path.exists('docs'):
        os.makedirs('docs')

    # Initialize freezer
    freezer = Freezer(app)

    # Build static files
    freezer.freeze()

    # Move static files to docs directory
    if os.path.exists('build'):
        for item in os.listdir('build'):
            src = os.path.join('build', item)
            dst = os.path.join('docs', item)
            if os.path.exists(dst):
                if os.path.isdir(dst):
                    shutil.rmtree(dst)
                else:
                    os.remove(dst)
            shutil.move(src, dst)
        shutil.rmtree('build')

if __name__ == '__main__':
    build_static() 