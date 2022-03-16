import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hyperx_keyboard_rgb",
    version="1.4",
    author="K4CZP3R",
    author_email="contact@k4czp3r.xyz",
    description="Control your keyboard rgb lights using hidapi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/K4CZP3R/hyperx-keyboard-rgb",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
    install_requires=[
        'hidapi @ git+https://github.com/K4CZP3R/cython-hidapi@master#egg=hidapi&subdirectory=../../cython-hidapi'
    ],
    dependency_links=[
        'git+https://github.com/K4CZP3R/cython-hidapi@master#egg=hidapi&subdirectory=../../cython-hidapi']
)
