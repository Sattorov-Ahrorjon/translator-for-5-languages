from aiogram.dispatcher.filters.state import StatesGroup, State

class Rasm_Data(StatesGroup):
    rasm_id = State()
    rasm_text = State()
    rasm_channel_name = State()
    rasm_channel_link = State()


class Video_Data(StatesGroup):
    video_id = State()
    video_text = State()
    video_channel_name = State()
    video_channel_link = State()