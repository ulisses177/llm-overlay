.. module:: chat_interface
   :platform: Unix, Windows
   :synopsis: A simple chat interface utilizing Ollama's language models with PyQt5 GUI library.

.. moduleauthor:: Your Name <your@email.address>

This module defines two classes: OverlayWindow and SystemTrayIcon. The OverlayWindow class creates a semi-transparent, always on top window that appears when the mouse pointer is in the top right corner of the screen. It contains a chat interface that sends user messages to Ollama's language models and displays responses.

Classes
-------

OverlayWindow(QWidget)
    A PyQt5 widget that acts as a semi-transparent, always on top window. This widget has a chat interface with an input field and chat history text area.

SystemTrayIcon(QSystemTrayIcon)
    Represents an icon in the system tray. In this module, it's used to create a system tray icon that provides an "Exit" action to quit the application.
