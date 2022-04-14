import cx_Freeze

executables = [cx_Freeze.Executable('snake.py')]

cx_Freeze.setup(
    name="Snake Game",
    options={'build_exe': {'packages':['pygame'],
                           'include_files':['record.txt']}},

    executables = executables
    
)