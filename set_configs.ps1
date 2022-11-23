Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
python -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
deactivate