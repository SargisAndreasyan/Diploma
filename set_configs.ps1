Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
py -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
deactivate