# -*- coding: utf-8 -*-
"""keyboards

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19hcTkX0amiB3nNv6UMM906rZ2S_aE541
"""

# keyboards.py
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


def generate_options_keyboard(answer_options):
    builder = InlineKeyboardBuilder()
    for i, option in enumerate(answer_options):
        builder.add(types.InlineKeyboardButton(
            text=option,
            callback_data=f"option_{i}"
        ))
    builder.adjust(1)
    return builder.as_markup()