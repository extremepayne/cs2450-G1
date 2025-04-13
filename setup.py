from setuptools import setup, find_packages

setup(
    name="task-manager",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "tkinter",
        "tkcalendar",
    ],
    package_data={
        "gui": ["assets/*"],
    },
    entry_points={
        "console_scripts": [
            "taskmanager=src.run_gui:main",
        ],
    },
    python_requires=">=3.12",
)
