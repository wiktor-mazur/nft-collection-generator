# NFT collection generator

Simple Python script that allows you to mix arbitrary number of layers into a collection of unique images.

## Installation
1. Make sure you have Python3 installed.
2. Create venv:
    ```bash
    python -m venv env
    ```
3. Activate venv:
    ```bash
    source env/bin/activate
    ```
4. Install requirements:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Configure `config.yaml`.
2. Prepare proper files structure.
3. Run the script:
    ```bash
    python main.py
    ```
4. The result will be generated in `./YOUR_COLLECTION_NAME/result/`.

This repo comes with an example configuration out-of-the-box, so you should be able to run `python main.py` right after
you install all required dependencies.

## Configuration

```yaml
collections:
  - name: example
    layers:
      - background
      - shape
      - text
```
The top-level of the YAML is a list of collections to generate. For each collection you need to specify a name
(which corresponds to a collection's directory that has to be created in the script's root location) and a list of
layers. Each layer is simply a directory name that will need to be created inside the collection's dir. In each layer's
directory you need to put the images that will be used for generation.

## Limitations
- tested image formats: png
- every image in the layers' dirs has to be the exact same dimensions
