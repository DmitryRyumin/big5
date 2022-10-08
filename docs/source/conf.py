# -*- coding: utf-8 -*-

"""
Конфигурационный файл для процесса генерации документации с помощью Sphinx

Официальная документация:
    https://www.sphinx-doc.org/en/master/usage/configuration.html
Сборка:
    sphinx-build -a -b html ./doc/source ./doc/build
"""

# ######################################################################################################################
# Импорт необходимых инструментов
# ######################################################################################################################

import os  # Взаимодействие с файловой системой
import sys # Доступ к некоторым переменным и функциям Python

from unittest.mock import MagicMock

# ######################################################################################################################
# Информации о пути проекта
# ######################################################################################################################

PATH_TO_SOURCE = os.path.abspath(os.path.dirname(__file__))
PATH_TO_ROOT = os.path.join(PATH_TO_SOURCE, '..', '..')

sys.path.insert(0, os.path.abspath(PATH_TO_ROOT))

# ######################################################################################################################
# Фиктивное использование библиотек
# ######################################################################################################################

class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name): return MagicMock()

MOCK_MODULES = [
    'librosa', 'librosa.display', 'audioread', 'soundfile'
]
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

# ######################################################################################################################
# Импорт проекта
# ######################################################################################################################

import big5

# ######################################################################################################################
# Информация о проекте (Project information)
# ######################################################################################################################

# Название задокументированного проекта
project = big5.__title__

# Автор(ы) проекта
author = big5.__author__en__

# Авторские права
copyright = big5.__copyright__

# Версия проекта
version = big5.__version__
release = big5.__release__

# ######################################################################################################################
# Основные настройки (General configuration)
# ######################################################################################################################

# Расширения: https://www.sphinx-doc.org/en/master/usage/extensions
extensions = [
    'sphinx.ext.mathjax',             # Отображение формул (JavaScript)
    'sphinx.ext.napoleon',            # Документация в стиле NumPy или Google
    'sphinx.ext.viewcode',            # Добавление ссылки на исходный код
    'sphinx.ext.inheritance_diagram', # Добавление диаграммы классов
    'sphinx.ext.autodoc.typehints',   # Поддержка подсказок типа (PEP 484)
    'sphinx.ext.autodoc',             # Документация из строк кода в полуавтоматическом режиме
    'sphinx.ext.autosummary',
    'sphinx_toolbox.code',            # https://sphinx-toolbox.readthedocs.io/en/latest/index.html
    'sphinx_toolbox.collapse',
    # 'autodocsumm',
]

# Локализация (язык): https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language
language = 'ru'

# Директории и файлы, которые следуют исключить при сборке
exclude_patterns = ['../build']

# Директории и файлы, содержащие дополнительные стили темы
templates_path = ['_templates']

# Минимальная версия Sphinx
needs_sphinx = '5.1.1'

# Способ представления подсказок
autodoc_typehints = 'both'
autoclass_content = 'both'

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': True,
    'inherited-members': False,
    'show-inheritance': True,
    # 'autosummary': True,
}

autodoc_mock_imports = []

# ######################################################################################################################
# Настройки для генерации документации в формат HTML (Options for HTML output)
# ######################################################################################################################

# HTML-тема документации: https://sphinx-themes.org/
#     pydata_sphinx_theme
#     sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'

# Путь к пользовательским статическим файлам (изображения, стили (*.css) и тд.)
html_static_path = ['_static']

# Favicon документации
html_favicon = '_static/favicon.ico'

# Логотип документации
html_logo = "_static/logo.svg"

# Отображение надписи "Собрано при помощи Sphinx ..."
html_show_sphinx = True

# Отображение авторских прав
html_show_copyright = True

# ######################################################################################################################
# Настройки для генерации документации в формат LaTeX->PDF (Options for LaTeX output)
# ######################################################################################################################

latex_elements = {
    'preamble': '\\usepackage[utf8]{inputenc}',
    'babel': '\\usepackage[russian]{babel}',
    'cmappkg': '\\usepackage{cmap}',
    'fontenc': '\\usepackage[T1,T2A]{fontenc}',
    'utf8extra':'\\DeclareUnicodeCharacter{00A0}{\\nobreakspace}',
}

latex_documents = [
  ('index', 'PDF.tex', u'PDF', u'big5', 'manual'),
]
