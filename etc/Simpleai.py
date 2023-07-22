import pyautogui

# Predefined responses
responses = {
    'halo': 'Halo! Apa yang bisa saya bantu?',
    'siapa namamu?': 'Saya adalah AI sederhana.',
    'apa kabar?': 'Saya hanya sebuah program komputer, jadi tidak memiliki perasaan. Tapi terima kasih sudah bertanya!',
    'keluar': 'Terima kasih! Sampai jumpa lagi.'
}


def process_user_input(user_input):
    user_input = user_input.lower()

    # Check if user input matches any predefined responses
    for key, value in responses.items():
        if key in user_input:
            return value

    # If no predefined response matches, return a default response
    return 'Maaf, saya tidak mengerti pertanyaan Anda.'


def run_chatbot():
    while True:
        # Simulate user input using PyAutoGUI
        user_input = pyautogui.prompt(
            'Masukkan pertanyaan atau ketik "Keluar" untuk keluar.')

        # Check if user wants to exit
        if user_input.lower() == 'keluar':
            pyautogui.alert(responses['keluar'])
            break

        # Process user input and display the response
        response = process_user_input(user_input)
        pyautogui.alert(response)


# Start the chatbot
run_chatbot()
