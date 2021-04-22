def to_vtkjs(self, folder='.', name=None) -> str:
    """Write a vtkjs file.

    Write your honeybee-vtk model to a vtkjs file that you can open in
    Paraview-Glance.

    Args:
        folder: A valid text string representing the location of folder where
            you'd want to write the vtkjs file. Defaults to current working
            directory.
        name : Name for the vtkjs file. File name will be Model.vtkjs if not
            provided.

    Returns:
        A text string representing the file path to the vtkjs file.
    """

    # name of the vtkjs file
    file_name = name or 'model'
    # create a temp folder
    temp_folder = tempfile.mkdtemp()
    # The folder set by the user is the target folder
    target_folder = os.path.abspath(folder)
    # Set a file path to move the .zip file to the target folder
    target_vtkjs_file = os.path.join(target_folder, file_name + '.vtkjs')

    # write every dataset
    scene = []
    for data_set in DATA_SETS.values():
        data = getattr(self, data_set)
        path = data.to_folder(temp_folder)
        if not path:
            # empty dataset
            continue
        scene.append(data.as_data_set())

    # add sensor grids
    # it is separate from other DATA_SETS mainly for data visualization
    data = self.sensor_grids
    path = data.to_folder(temp_folder)
    if path:
        scene.append(data.as_data_set())

    # write index.json
    index_json = IndexJSON()
    index_json.scene = scene
    index_json.to_json(temp_folder)

    # zip as vtkjs
    temp_vtkjs_file = convert_directory_to_zip_file(temp_folder, extension='vtkjs',
                                                    move=False)

    # Move the generated vtkjs to target folder
    shutil.move(temp_vtkjs_file, target_vtkjs_file)

    return target_vtkjs_file

def to_html(self, folder='.', name=None, show=False):
    """Write an HTML file.

    Write your honeybee-vtk model to an HTML file.

    Args:
        folder: A valid text string representing the location of folder where
            you'd want to write the HTML file. Defaults to current working directory.
        name : Name for the HTML file. File name will be Model.html if not provided.
        show: A boolean value. If set to True, the HTML file will be opened in the
            default browser. Defaults to False

    Returns:
        A text string representing the file path to the HTML file.
    """
    # Name of the html file
    file_name = name or 'model'
    # Set the target folder
    target_folder = os.path.abspath(folder)
    # Set a file path to move the .zip file to the target folder
    html_file = os.path.join(target_folder, file_name + '.html')
    # Set temp folder to do the operation
    temp_folder = tempfile.mkdtemp()
    vtkjs_file = self.to_vtkjs(temp_folder)
    temp_html_file = add_data_to_viewer(vtkjs_file)
    shutil.copy(temp_html_file, html_file)
    try:
        shutil.rmtree(temp_folder)
    except Exception:
        pass
    if show:
        webbrowser.open(html_file)
    return html_file