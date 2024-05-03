import setuptools

DESCRIPTION = 'Generate random files of given size'
  
setuptools.setup( 
    name="generate_random_files", 
    version="0.0.1", 
    author="NishithRaveeshKashyap", 
    author_email="nishithkp175@gmail.com", 
    packages=["generate_random_files"],
    description=DESCRIPTION, 
    long_description=DESCRIPTION, 
    long_description_content_type="text/markdown", 
    url="https://github.com/gituser/test-tackage", 
    license='MIT', 
    python_requires='>=3.8',
    install_requires=[] 
)
