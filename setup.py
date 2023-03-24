import cx_Freeze
import sys

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [cx_Freeze.Executable("JuegoSerpiente.py", base=base, icon="icono.ico")]

cx_Freeze.setup(
	name="Serpiente",
	version="1.0",
	options={"build_exe": {"packages": ["pygame", "random"], "include_files":["manzana.png", "logo.jpg", "icono.ico", "comer.wav", "botones.wav", "letrasjuego.ttf"]}},
	description="Serpiente XD",
	executables = executables

	)
