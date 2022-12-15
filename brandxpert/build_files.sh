# build_files.sh
python -m venv bxenv
source bxenv/bin/activate
pip install -r requirements.txt
python manage.py collectstatic
