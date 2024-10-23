@echo off

python --version

if %errorlevel% == 0 (
	python -m pip install -r requirements.txt
	) else (
		echo Check Python version or command
		)
python -m virtualenv venv
/venv/scripts/activate
git clone https://github.com/deepseagirl/degoogle
python -m pip install --user degoogle/.
echo STARTING BOT
python bot.py
