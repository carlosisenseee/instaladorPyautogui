winget install --id Python.Python.3 --source winget --accept-package-agreements --accept-source-agreements

Start-Sleep -Seconds 60

$env:Path += ";$env:LocalAppData\Programs\Python\Python311\Scripts;$env:LocalAppData\Programs\Python\Python311"

python --version
pip --version

python -m pip install --upgrade pip

pip install pyautogui opencv-python

Start-Sleep -Seconds 60

python "C:\MeusScripts\app.py" # Colocar o caminho correto