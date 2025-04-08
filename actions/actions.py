from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from typing import List, Dict, Text, Any
import random


class ActionPreguntarNombre(Action):
    def name(self) -> Text:
        return "action_preguntar_nombre"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict]:
        dispatcher.utter_message(text="¡Hola! ¿Cómo te llamas? 🙂")
        return []


class ContarCuriosidad(Action):
    def name(self) -> Text:
        return "action_contar_curiosidad"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        respuestas = [
            "¿Sabías que la miel nunca se echa a perder? Se han encontrado vasijas de miel en tumbas egipcias que aún eran comestibles.",
            "El corazón de una ballena azul es tan grande que un humano podría nadar a través de sus arterias.",
            "Los pulpos tienen tres corazones y la sangre azul.",
            "Las abejas pueden reconocer rostros humanos.",
            "Australia es más ancha que la Luna. La Luna tiene 3400 km de diámetro, mientras que el diámetro de Australia de este a oeste es de casi 4000 km.",
            "En Suiza es ilegal tener una sola cobaya. Se considera maltrato animal porque son seres sociales y se sienten solos."
        ]
        
        respuesta = random.choice(respuestas)
        dispatcher.utter_message(text=respuesta)
        return []