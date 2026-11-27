import streamlit as st

from src.pipelines.voice_pipeline import process_bulk_audio

from src.database.config import supabase

import pandas as pd


from src.components.dialog_attendance_results import show_attendance_result
from datetime import datetime