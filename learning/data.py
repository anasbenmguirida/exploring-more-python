import kagglehub

# Download latest version
path = kagglehub.dataset_download("mahoora00135/flights")

print("Path to dataset files:", path)