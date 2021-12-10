from PIL import Image
from os import listdir, makedirs, path as os_path
from shutil import rmtree
from itertools import product
from hashlib import md5
from yaml import safe_load as yaml_safe_load, YAMLError


def get_layer_path(collection_name, layer_name):
    return './' + collection_name + '/' + layer_name + '/'


def prepare_clean_directory(path):
    if os_path.exists(path):
        rmtree(path)
    makedirs(path)


def get_layers_images(collection):
    """Returns a two-dimensional array.
    First-level is an array of layers
    Second-level is an array of images in the particular array
    """
    layers_images = []
    for layer in collection['layers']:
        layers_images.append(listdir(get_layer_path(collection['name'], layer)))

    return layers_images


def get_config():
    with open('config.yaml', "r") as stream:
        try:
            return yaml_safe_load(stream)
        except YAMLError:
            print('Could not read config.yaml - make sure it exists and is valid.')
            exit()


def main():
    config = get_config()

    for collection in config['collections']:
        layers_images = get_layers_images(collection)
        layers_cartesian_product = list(product(*layers_images))
        result_dir = './' + collection['name'] + '/result/'
        prepare_clean_directory(result_dir)

        number_of_unique_sets = len(layers_cartesian_product)

        decision = input('You are about to generate ' + str(number_of_unique_sets) + ' unique images in the "'
                         + collection['name'] + '" collection. Do you want to continue? (Y/n) ')

        if decision != 'y' and decision != 'Y':
            exit()
        else:
            print('Processing the "' + collection['name'] + '" collection...\n')

        for unique_set in layers_cartesian_product:
            background_layer_img = None
            for index, image_name in enumerate(unique_set):
                image_path = get_layer_path(collection['name'], collection['layers'][index]) + image_name

                if index == 0:
                    background_layer_img = Image.open(image_path).convert('RGBA')
                else:
                    current_layer_img = Image.open(image_path).convert('RGBA')
                    background_layer_img.paste(current_layer_img, (0, 0), current_layer_img)

            result_name = md5(bytes('-'.join(unique_set), 'utf-8')).hexdigest()
            background_layer_img.save(result_dir + result_name + '.png', format='png')


if __name__ == '__main__':
    main()
