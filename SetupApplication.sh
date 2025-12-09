#!/bin/bash

echo "Updating and upgrading system packages..."
sudo apt update -y
sudo apt upgrade -y

echo "Installing GPIO Zero library..."
sudo apt install -y python3-gpiozero

echo "Downloading application repository..."
cd ~
if [ ! -d "6919_komodo_ole-runners-club" ]; then
    git clone https://github.com/Grafico-Las-Vegas/6919_komodo_ole-runners-club.git
else
    echo "Repository already exists. Pulling latest changes..."
    cd 6919_komodo_ole-runners-club
    git pull
    cd ..
fi

echo "Setting up Python virtual environment..."
cd ~/6919_komodo_ole-runners-club
python3 -m venv .venv6919Komodo
source .venv6919Komodo/bin/activate

echo "Installing required Python packages..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Launching Ole Runners Club application..."
python3 OleRunnersClub.py
