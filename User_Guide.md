# User Guide

Here I will list all guidlines to make the for you, to train the model, and makes eveything works probarly, and get our results, feel free to add more feature and contribute to this repo:

- Create a new virtual environment, by chaning your directory to the directory you specify and then run this command:

  ```
  python -m venv <virtual environment name>
  ```

- To activate the virtual environment, run this command inside the specified folder:

  ```
  .\<virtual environment name>\Scripts\activate

  ```

- Run those commands:

  ```
  pip install ipykernel
  python -m ipykernel install --user --name=deepmatrix
  pip install jupyterlab
  ```

- Install all listed libraries

  ```
  pip install ipykernel
  pip install opencv-python
  pip install --upgrade pyqt5 lxml
  pip install wget
  pip install tensorflow
  pip install gin-config==0.1.1
  pip install protobuf matplotlib
  pip install Pillow
  pip install protobuf
  pip install PyYAML
  pip install tensorflow-addons
  pip install pyttsx3
  pip install tk-tools

  ```

- Use Jupyter lab, to access this file, `Install_Lib_folders.ipynb` then run all it`s commands, this will ensure that you installed all the required libraries and created all the folders tree.

- Use Jupyter lab, to access this file, `Take_photos.ipynb`.

- After taking pictures of the sign movements, Now you are ready to train the model, for this accrss this file `train_the_model.ipynb`, if the training is so slow, you need to use GPU or google COLAB.

- To test your model, access this file `detection.ipynb`, and run all cells.

- You can use our ready trained model, by downloading it from here:
  - Annotatiots
    `https://drive.google.com/drive/folders/1-1hERXJQ68yiK3U2NknFWWQJdHIejr7D?usp=sharing`
  - Model
    `https://drive.google.com/drive/folders/1-1hERXJQ68yiK3U2NknFWWQJdHIejr7D?usp=sharing`

But make sure the to put them in the write place

- For the Annotatiots
  `Tensorflow\workspace\annotations`

- for the Model
  `Tensorflow\workspace\models`
