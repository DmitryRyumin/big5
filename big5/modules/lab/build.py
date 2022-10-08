#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Сборка
"""

# ######################################################################################################################
# Импорт необходимых инструментов
# ######################################################################################################################
# Подавление Warning
import warnings
for warn in [UserWarning, FutureWarning]: warnings.filterwarnings('ignore', category = warn)

from dataclasses import dataclass # Класс данных

# ######################################################################################################################
# Сообщения
# ######################################################################################################################
@dataclass
class  RunMessages:
    """Класс для сообщений"""

    # ------------------------------------------------------------------------------------------------------------------
    # Конструктор
    # ------------------------------------------------------------------------------------------------------------------

    def __post_init__(self):
        self._in_development = 'The library under development'

# ######################################################################################################################
# Сборка
# ######################################################################################################################
@dataclass
class Run(RunMessages):
    """Класс для сборки"""

    # ------------------------------------------------------------------------------------------------------------------
    # Конструктор
    # ------------------------------------------------------------------------------------------------------------------

    def __post_init__(self):
        super().__post_init__() # Выполнение конструктора из суперкласса

        print(self._in_development)