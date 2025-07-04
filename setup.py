import setuptools

setuptools.setup(
    name="jupyter-notes-proxy",
    version='0.0.40',
    url="https://gitlab.mpcdf.mpg.de/khr/jupyter-streamlit-proxy",
    author="Klaus Reuter",
    description="klaus.reuter@mpcdf.mpg.de",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'notes = jupyter_notes_proxy:setup_notes_proxy',
        ]
    },
    package_data={
        'jupyter_notes_proxy': ['icons/*'],
    },
)
