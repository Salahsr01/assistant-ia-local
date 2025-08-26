"""
Application de base pour l’assistant IA local.

Cette version est minimale et sert de point de départ.  Elle se contente d’afficher
un message de bienvenue et vérifie la présence de la bibliothèque `ollama`.

À terme, cette application inclura :
* une interface graphique permettant d’épingler des éléments ;
* un chat avec un modèle de langage local via Ollama ;
* des connecteurs pour des services externes (Notion, Gmail, GitHub) ;
* un moteur de planification pour organiser vos tâches.
"""

import sys

try:
    import ollama  # type: ignore
except ImportError:
    print(
        "Ollama n’est pas installé. Installez-le en suivant les instructions du README. "
        "Le programme se poursuit sans fonctionnalité IA."
    )
    ollama = None  # type: ignore


def main() -> None:
    """Point d’entrée principal de l’application."""
    print("=== Assistant IA Local ===")
    print(
        "Bienvenue dans l’assistant IA local en cours de développement. "
        "Cette application est encore basique, mais elle sera enrichie grâce aux contributions de la communauté."
    )

    if ollama is not None:
        print("Ollama est disponible. Vous pourrez bientôt interagir avec un modèle de langage local.")
    else:
        print("Ollama n’est pas disponible. Certaines fonctionnalités d’IA seront désactivées.")


if __name__ == "__main__":
    sys.exit(main())
