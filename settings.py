# NAMES
USERNAME = None
TOPIC = "Ejecución de instrucciones"

# STYLES
BG_COLOR_LIGHT = "#ebebeb"
BG_COLOR_DARK = "#242424"
HOVER_COLOR_LIGHT = "#b4b4b4"
HOVER_COLOR_DARK = "#3c3c3c"
ASSIST_MESSAGE_COLOR_LIGHT = "#dcdcdc"
ASSIST_MESSAGE_COLOR_DARK = "#2b2b2b"
ERROR_COLOR_LIGHT = "#dc2626"
ERROR_COLOR_DARK = "#dc2626"
SUCCESS_COLOR_LIGHT = "#11a37f"
SUCCESS_COLOR_DARK = "#11a37f"
SELECT_COLOR_LIGHT = "#65B510"
SELECT_COLOR_DARK = "#65B510"

# DEFAULT KEYS
REQUEST_KEY = "Solicitud"
PRESENTATION_KEY = "Presentación"
OPTIONS_KEY = "Opciones"
CONTENT_KEY = "Contenido"
IMAGES_KEY = "Imágenes"
GAMES_KEY = "Opciones de juego"
QUESTION_KEY = "Enunciado"
WORDS_KEY = "Palabras"
HIDDEN_WORD_KEY = "Palabra"

#DEFAULT VALUES
DEFAULT_DATA = {
    WORDS_KEY: [
        {
            QUESTION_KEY: ["No question"],
            HIDDEN_WORD_KEY: ["TEST"]
        },
        {
            QUESTION_KEY: ["No question"],
            HIDDEN_WORD_KEY: ["TESTERS"]
        },
        {
            QUESTION_KEY: ["No question"],
            HIDDEN_WORD_KEY: ["TESTING"]
        }
    ]
}

# QUESTION STRUCTURE KEYS
STATEMENT_KEY = "Pregunta"

# PATHS
IMAGES_PATH = "imgs"
SOUNDS_PATH = "sounds"

#DEFAULT ASPECTS
GAME_NAME = "Sopa de letras"

# MULTIMEDIA
ICON_IMAGE = IMAGES_PATH + "/" + "assist_icon.png"
MICROPHONE_DISABLE_IMAGE = IMAGES_PATH + "/" + "microphone_disable_icon.png"
MICROPHONE_OFF_IMAGE = IMAGES_PATH + "/" + "microphone_off_icon.png"
MICROPHONE_ON_IMAGE = IMAGES_PATH + "/" + "microphone_on_icon.png"
KEYBOARD_IMAGE = IMAGES_PATH + "/" + "keyboard_icon.png"
ARROW_IMAGE = IMAGES_PATH + "/" + "arrow_head_icon.png"
HEARING_GIF = IMAGES_PATH + "/" + "hear_animation.gif"

# SOUNDS
MIC_ON_SOUND = ""
MIC_OFF_SOUND = ""