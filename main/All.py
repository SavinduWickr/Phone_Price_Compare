import subprocess

# Define the paths to the Python scripts you want to run
script_paths = [
    # 'web_to_html/Celtronic.py',
    #'web_to_html/Emboile.py',
    #'web_to_html/Genuis_Mobile.py',
    # 'web_to_html/idea_beam_all.py',
    # 'web_to_html/Life_Mobile.py',
    # 'instock_checker/+link/Celltronic.py',
    # 'instock_checker/+link/Emobile.py',
    # 'instock_checker/+link/Genuis_Mobile.py',
    # 'instock_checker/idea_beam.py',
    # 'instock_checker/+link/Life_Mobile.py',
    # 'Instock_to_ram_rom/conversion.py',
    # 'Instock_to_ram_rom/genuis_conversion.py',
    # 'combining_data/combine_all.py',
    'excel_sql/excel_sql.py',
]

# Loop through the script paths and execute them one by one
for script_path in script_paths:
    print(f"Running script: {script_path}")

    # Start the script as a subprocess and capture its output in real-time
    process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                               bufsize=1, universal_newlines=True)

    # Read and print the output line by line
    for line in process.stdout:
        print(line, end='')

    # Wait for the subprocess to finish
    process.wait()

    # Check if there was an error
    if process.returncode != 0:
        print(f'Error executing {script_path}. Exit code: {process.returncode}')
        print(f'Stdout: {process.stdout.read()}')
        print(f'Stderr: {process.stderr.read()}')

    print(f"Finished running script: {script_path}\n")
