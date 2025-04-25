# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
import pandas as pd
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCekGizi(Action):
    def name(self) -> Text:
        return "action_cek_gizi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message = tracker.latest_message.get('text').lower()

        # Load data
        df = pd.read_excel("data_gizi.xlsx")

        # Cari makanan yang disebut
        makanan_ditemukan = None
        for makanan in df['Makanan']:
            if makanan.lower() in user_message:
                makanan_ditemukan = makanan
                break

        if makanan_ditemukan:
            row = df[df['Makanan'] == makanan_ditemukan].iloc[0]
            info = f"Kalori: {row['Kalori (kkal)']} kkal\n" \
                   f"Protein: {row['Protein (g)']} g\n" \
                   f"Lemak: {row['Lemak (g)']} g\n" \
                   f"Karbohidrat: {row['Karbohidrat (g)']} g"

            dispatcher.utter_message(text=f"Berikut adalah informasi gizi untuk {makanan_ditemukan}:\n{info}")

        else:
            dispatcher.utter_message(text="Maaf, aku belum punya data makanan itu. Coba makanan lain ya!")

        return []

