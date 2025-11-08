#!/usr/bin/env python
"""
Proto BFO - Basic Formal Ontology in Protocol Buffers

A comprehensive implementation of BFO using Protocol Buffers for
efficient serialization and cross-language support.
"""

import os
import subprocess
from setuptools import setup, find_packages, Command


class CompileProtoCommand(Command):
    """Custom command to compile proto files."""

    description = 'Compile .proto files to Python'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Compile all proto files."""
        proto_root = 'proto'
        proto_files = []

        # Find all .proto files
        for root, dirs, files in os.walk(proto_root):
            for file in files:
                if file.endswith('.proto'):
                    proto_files.append(os.path.join(root, file))

        # Compile each proto file
        for proto_file in proto_files:
            print(f"Compiling {proto_file}...")
            try:
                subprocess.check_call([
                    'protoc',
                    f'--python_out=.',
                    f'-I{proto_root}',
                    '-I.',
                    proto_file
                ])
                print(f"✓ Compiled {proto_file}")
            except subprocess.CalledProcessError as e:
                print(f"✗ Failed to compile {proto_file}: {e}")
            except FileNotFoundError:
                print("Error: protoc not found. Please install protobuf compiler.")
                print("  Ubuntu/Debian: sudo apt-get install protobuf-compiler")
                print("  macOS: brew install protobuf")
                raise


# Read long description from README
with open('readme.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Read requirements
with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='proto_bfo',
    version='2.0.0',
    description='Basic Formal Ontology implemented in Protocol Buffers',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Olle Nordesjo',
    author_email='olle@nordesjo.net',
    url='https://github.com/Rasinj/proto_bfo',
    packages=find_packages(exclude=['tests', 'tests.*', 'examples', 'examples.*']),
    install_requires=requirements,
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
            'black>=22.0.0',
            'isort>=5.0.0',
            'flake8>=5.0.0',
        ],
        'docs': [
            'sphinx>=5.0.0',
            'sphinx-rtd-theme>=1.0.0',
        ],
    },
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='ontology bfo protobuf formal-ontology knowledge-representation',
    cmdclass={
        'build': CompileProtoCommand,
    },
    project_urls={
        'Documentation': 'https://github.com/Rasinj/proto_bfo/tree/main/docs',
        'Source': 'https://github.com/Rasinj/proto_bfo',
        'Bug Reports': 'https://github.com/Rasinj/proto_bfo/issues',
    },
)
