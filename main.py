

get_ipython().system('git clone https://github.com/Ashwin-S-Nair/document-layout-analysis.git')

get_ipython().system('git config --global user.name "Ashwin-S-Nair"')
get_ipython().system('git config --global user.email "ashwinesnair@gmail.com"')

get_ipython().run_line_magic('cd', '/content/document-layout-analyzer')

get_ipython().system('ls /content')

get_ipython().run_line_magic('cd', '/content/document-layout-analysis')

# Add dataset processing scripts
get_ipython().system('git add preprocess.py prepare_dataset.py')

get_ipython().system('ls -la /content/document-layout-analysis')

get_ipython().system('mv /content/yolov8_config.yaml /content/document-layout-analysis/')
get_ipython().system('mv /content/datasets /content/document-layout-analysis/')
# Add more `mv` commands if needed for other files

get_ipython().run_line_magic('cd..', '')

get_ipython().run_line_magic('cd..', '')

get_ipython().run_line_magic('cd', '/content')

get_ipython().system('ls')

get_ipython().run_line_magic('cd', '/sample_data')

get_ipython().run_line_magic('cd', '/content/sample_data')

get_ipython().system('ls')

get_ipython().system('ls')

get_ipython().run_line_magic('cd', '/content')

get_ipython().system('ls')

with open("/content/document-layout-analysis/main.py", "w") as f:
    for cell in get_ipython().user_ns['In']:  # Get all Colab input cells
        f.write(cell + "\n\n")  # Write each cell as Python code

