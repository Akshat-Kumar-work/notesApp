# Create a virtual environment
```
python -m venv venv
```

# Activate the virtual environment in PowerShell
```
.\venv\Scripts\activate
```

# Or in CMD
```
venv\Scripts\activate.bat
```


# Install required packages
```
pip install fastapi
```
```
pip install uvicorn[standard]
```

# To start the server using uvicorn
```
uvicorn main:app --reload
```

# To connect with mongodb install pymongo
```
pip install pymongo
```
