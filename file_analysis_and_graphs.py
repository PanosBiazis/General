import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Define a function to detect the programming language or file type
def detect_language(file_name):
    # List of file extensions for each language
    extensions = {
        'Python': ['.py'],
        'C++': ['.cpp', '.h', '.hpp'],
        'C': ['.c', '.h'],
        'HTML': ['.html', '.htm'],
        'PHP': ['.php'],
        'Java': ['.java'],
        'Fortran': ['.f', '.f90'],
        'Pascal': ['.pas'],
        'Go': ['.go', '.mod'],  # Go modules (.mod) extension
        'Ruby': ['.rb'],
        'Perl': ['.pl'],
        'Lua': ['.lua'],
        'Rust': ['.rs'],
        'Text File': ['.txt', '.log', '.md', '.ini', '.json', '.csv', '.xml', '.yaml', '.rtf', '.bib', '.cfg'],
        'Image File': ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.svg', '.webp', '.ico', '.heif', '.raw'],
        'Audio File': ['.mp3', '.wav', '.flac', '.ogg', '.aac', '.m4a', '.wma', '.opus', '.alac', '.aiff'],
        'Video File': ['.mp4', '.mkv', '.avi', '.mov', '.webm', '.flv', '.wmv', '.mpg', '.mpeg', '.mov', '.3gp'],
        'Web File': ['.css', '.js', '.json', '.ts', '.scss', '.sass', '.html', '.woff', '.woff2'],
        'Database File': ['.sql', '.sqlite', '.db', '.mdb', '.dbd', '.h2', '.sqlite3'],
        'Office File': ['.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Ebook File': ['.epub', '.mobi', '.azw3', '.pdf'],
        'Compressed': ['.zip', '.tar', '.tar.gz', '.rar', '.7z', '.gzip', '.xz', '.tar.bz2', '.bz2'],
        'Executable': ['.exe', '.bat', '.sh', '.msi', '.apk', '.app', '.bin', '.run'],
        'Package File': ['.deb', '.rpm', '.apk', '.tar.bz2', '.tar.gz', '.tar.xz'],
        'Programming Language File': ['.scala', '.kotlin', '.swift', '.dart', '.ts', '.r', '.haskell', '.clj', '.lisp', '.clj', '.erl'],
        'Document File': ['.pdf', '.odt', '.txt', '.rtf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.tex', '.latex'],
        'System File': ['.sys', '.dll', '.drv', '.inf', '.bin', '.img', '.vxd'],
        'Miscellaneous': ['.log', '.bak', '.swp', '.dat', '.tmp', '.pid', '.torrent', '.lock'],
        'Font Files': ['.ttf', '.otf', '.woff', '.woff2', '.eot', '.fnt', '.fon'],
        'Archive': ['.tar', '.tar.gz', '.tgz', '.zip', '.rar', '.7z', '.xz', '.lzma'],
        'Virtual Disk Image': ['.vmdk', '.vdi', '.vhd', '.img'],
        '3D Models': ['.stl', '.obj', '.3ds', '.fbx', '.blend'],
        'Android File': ['.apk', '.obb'],
        'iOS File': ['.ipa'],
        'Assembly': ['.asm', '.s', '.inc', '.mac', '.lst'],
        'Batch File': ['.bat', '.cmd'],
        'CSV File': ['.csv'],
        'Markdown': ['.md'],
        'LaTeX': ['.tex'],
        'JSON': ['.json'],
        'YAML': ['.yaml', '.yml'],
        'Log File': ['.log'],
        'Backup File': ['.bak'],
        'WebAssembly': ['.wasm'],
        'Other': [],
            # New extensions added
        '.classpath': 'Unknown',
        '.project': 'Unknown',
        '.ai': 'Unknown',
        '.app': 'Unknown',
        '.asm': 'Assembly',
        '.app2': 'Unknown',
        '.db': 'Database File',
        '.exefile': 'Executable',
        '.cbl': 'COBOL',
        '.lsp': 'Lisp',
        '.f': 'Fortran',
        '.f90': 'Fortran',
        '.pas': 'Pascal',
        '.vbs': 'Visual Basic Script',
        '.bat': 'Batch Script',
        '.pdb': 'Program Database',
        '.qs': 'Quantum Script',
        '.lst': 'Listing File',
        '.tfc': 'TFC',
        '.tsv': 'Tab Separated Value',
        '.xlsx': 'Excel',
    }
    
    # Check the file extension
    for language, exts in extensions.items():
        if any(file_name.endswith(ext) for ext in exts):
            return language
    return 'Unknown'

# Define the function to generate 2D and 3D graphs
def generate_graphs(file_types):
    languages = list(file_types.values())
    
    # Unique programming languages
    unique_languages = list(set(languages))
    num_languages = len(unique_languages)
    
    # Get a colormap for the number of unique languages
    colors = plt.get_cmap('tab20', num_languages)  # Use the tab20 colormap

    # Create a 2D bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    language_counts = [languages.count(lang) for lang in unique_languages]
    
    # Set colors for each language in the bar chart
    ax.bar(unique_languages, language_counts, color=colors(range(num_languages)))
    ax.set_xlabel('File Types')
    ax.set_ylabel('Count')
    ax.set_title('File Types Distribution')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Display the 2D bar chart
    plt.show()

    # Create a 2D Pie Chart
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Get the data for the pie chart
    sizes = language_counts
    labels = unique_languages
    colors_2d = [colors(i) for i in range(num_languages)]
    
    # Create a 2D pie chart
    ax.pie(sizes, labels=labels, colors=colors_2d, autopct='%1.1f%%', startangle=90)
    ax.set_title('File Types Distribution (2D)')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    # Display the 2D pie chart
    plt.show()

    # Create a 3D "Circular" Bar Chart
    fig = plt.figure(figsize=(10, 6))
    ax3d = fig.add_subplot(111, projection='3d')

    # Create a circular arrangement for 3D bars
    theta = np.linspace(0, 2 * np.pi, num_languages, endpoint=False)
    xpos = np.cos(theta)  # X positions based on a circle
    ypos = np.sin(theta)  # Y positions based on a circle
    zpos = np.zeros(num_languages)  # Z positions for the bars, all starting from 0

    dx = np.ones(num_languages)  # Bar width
    dy = np.ones(num_languages)  # Bar depth
    dz = language_counts  # Bar height

    # Apply color based on the count of the languages
    ax3d.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors(range(num_languages)))

    # Set labels for the 3D graph
    ax3d.set_xlabel('File Types')
    ax3d.set_ylabel('Count')
    ax3d.set_zlabel('File Count')
    ax3d.set_title('3D Circular Bar Chart of File Types')

    # Display labels next to the bars
    for i in range(num_languages):
        ax3d.text(xpos[i], ypos[i], dz[i] + 0.1, unique_languages[i], color='black', ha='center')

    # Display the 3D bar chart
    plt.show()

# Specify the folder path you want to scan
folder_path = input("Give the folder path to analyze: ") #'F:\\panag\\Documents\\ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ'  # Replace with your folder path

# List all files in the directory
file_names = os.listdir(folder_path)

# Detect the language for each file
file_types = {file_name: detect_language(file_name) for file_name in file_names}

# Generate graphs based on the detected file types
generate_graphs(file_types)
