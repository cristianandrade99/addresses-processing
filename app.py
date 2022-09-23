import pandas as pd
import utils
import os

PROJECT_FOLDER = os.getcwd()
ADDRESSES_PATH = os.path.join(PROJECT_FOLDER, 'data', 'addresses_list.json')
CATEGORIES_PATH = os.path.join(PROJECT_FOLDER, 'data', 'categories')
NOT_PROCESSED_PATH = os.path.join(CATEGORIES_PATH, 'not_processed.json')


def get_calle_format(data, calle_keys):
    formated = data
    for key_word in calle_keys:
        formated = formated.replace(key_word, 'Calle')
    # ADD MORE LOGIC
    # ...
    return formated


def main():
    # Save only addresses into json
    # df = pd.read_excel('./Data-Companies.xlsx')
    # addreses_list = df['Direccion_Comercial'].to_list()
    # utils.save_json_file(ADDRESSES_PATH, addreses_list)

    # addreses_list = utils.load_json_file(ADDRESSES_PATH)
    # utils.save_json_file(NOT_PROCESSED_PATH, addreses_list[0:10000])

    addresses_list = utils.load_json_file(ADDRESSES_PATH)

    categories = {
        'calle': [],
        'carrera': [],
        'calle_carrera': [],
        'diagonal': [],
        'not_processed': []
    }

    for i in range(len(addresses_list)):
        address = addresses_list[i]
        address_formated = address.lower().replace('.', '')
        address_words = address_formated.split(' ')

        calle_keys = ['calle', 'cll', 'cl']
        is_calle = any(
            [item in address_words for item in calle_keys])

        carrera_keys = ['carrera', 'cra', 'cr', 'kr']
        is_carrera = any(
            [item in address_words for item in carrera_keys])

        is_diagonal = any(
            [item in address_words for item in ['diagonal', 'diag']])

        key = 'not_processed'
        address_modified = address_formated
        if is_calle and not is_carrera:
            key = 'calle'
            address_modified = get_calle_format(address_modified, calle_keys)

        elif is_carrera and not is_calle:
            key = 'carrera'
            for key_word in carrera_keys:
                address_modified = address_modified.replace(
                    key_word, 'Carrera')

        elif is_carrera and is_calle:
            key = 'calle_carrera'

        elif is_diagonal:
            key = 'diagonal'

        categories[key].append([address_modified, i+2])

    for key in categories:
        category = {'length': len(
            categories[key]), 'addresses': categories[key]}
        utils.save_json_file(os.path.join(
            CATEGORIES_PATH, f'{key}.json'), category)


main()
