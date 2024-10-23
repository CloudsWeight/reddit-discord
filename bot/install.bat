@echo off

python --version

if %errorlevel% == 0 (
	python -m pip install -r requirements.txt
	) else {
		echo Check Python version or command
		)

git clone https://github.com/deepseagirl/degoogle
cd degoogle
python -m pip install . 

venv/bin/activate
echo STARTING BOT
python bot.py