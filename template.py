import os

# Define the folders to be created
folders = [
    "data/raw",
    "data/processed",
    "models",
    "notebooks",
    "src",
    "src/data",
    "src/models",
    "src/visualization",
    "logs",
    "tests",
    "streamlit_app"
]

# Define the files to be created
files = [
    "README.md",
    "requirements.txt",
    ".gitignore",
    "config.yaml",
    "main.py",
    "setup.py",
    "src/__init__.py",
    "src/data/__init__.py",
    "src/data/data_loader.py",
    "src/data/preprocessing.py",
    "src/models/__init__.py",
    "src/models/sentiment_model.py",
    "src/visualization/__init__.py",
    "src/visualization/visualize.py",
    "notebooks/eda.ipynb",
    "streamlit_app/app.py",
    "tests/test_data_loader.py",
    "tests/test_sentiment_model.py",
    "logs/.gitkeep"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file in files:
    with open(file, "w") as f:
        if file.endswith(".py"):
            f.write("# This is a placeholder file\n")
        elif file.endswith(".md"):
            f.write("# Reddit Sentiment Analysis Project\n")
        elif file.endswith(".gitignore"):
            f.write("data/raw/\ndata/processed/\nmodels/\nlogs/\n")
        elif file.endswith("requirements.txt"):
            f.write("praw\ntransformers\nnltk\nstreamlit\nmatplotlib\npandas\nscikit-learn\n")
        else:
            f.write("")

print("Project structure created successfully in the current directory!")

