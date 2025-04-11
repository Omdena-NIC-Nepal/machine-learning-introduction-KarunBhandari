import io
import sys
import pytest 
# Assumes the student's solution is in assignment.py

import nbconvert
import io

def notebook_to_python(notebook_path):
    exporter = nbconvert.PythonExporter()
    python_code, _ = exporter.from_filename(notebook_path)
    
    # Remove IPython magic and get_ipython references
    lines = python_code.splitlines()
    cleaned_lines = [
        line for line in lines 
        if not line.strip().startswith('%') and 'get_ipython()' not in line
    ]
    cleaned_code = '\n'.join(cleaned_lines)
    
    return cleaned_code

import importlib.util
import sys
def import_notebook_module(notebook_path):
    module_name = 'assignment'
    spec = importlib.util.spec_from_loader(module_name, loader=None)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module

    cleaned_code = notebook_to_python(notebook_path)
    exec(cleaned_code, module.__dict__)
    
    return module


assignment = import_notebook_module('../notebooks/Model_Training.ipynb')

def test_notebook():
    assignment.load_dataset()
    assignment.select_features()
    assignment.train_linear_regression()
   