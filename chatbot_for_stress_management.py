import random

# Define stress level thresholds
HIGH_STRESS_THRESHOLD = 2
NORMAL_STRESS_THRESHOLD = 1
LOW_STRESS_THRESHOLD = 0

# Define stress level responses
STRESS_LEVEL_RESPONSES = {
    'high': [
        'You may want to try practicing mindfulness or meditation to help reduce your stress levels.',
        'When stress levels are high, it can be helpful to take a break from technology and spend some time in nature.',
        'Take a break and do some deep breathing exercises',
        'Practice mindfulness or meditation',
        'Take a walk or engage in physical activity such as yoga or running',
        'It seems like you are experiencing high levels of stress. Try doing some deep breathing exercises or going for a walk to clear your mind.',
        'Listen to calming music or nature sounds',
        'Write in a journal or talk to a therapist or friend',
        'Prioritize self-care activities such as taking a bath, getting a massage or doing something you enjoy',
    ],
    'normal': [
        'Your stress levels seem to be normal. Keep up the good work!',
        'Great job keeping your stress levels under control!',
        'It sounds like you are handling stress well. Keep doing what you are doing!',
        'Practice self-care activities such as taking a break, getting enough sleep and exercise, and eating a balanced diet',
        'Connect with friends and family members regularly',
        'Set aside time for hobbies or activities you enjoy',
        'Practice stress-reducing techniques such as deep breathing or mindfulness',
        'Take time for self-reflection or journaling to help manage stress levels over time.',
    ],
    'low': [
        'Your stress levels are low! Keep up the good work!',
        'Congratulations on keeping your stress levels under control!',
        'It looks like you are doing a great job at managing your stress levels!',
        'Use this time to catch up on tasks or projects you have been putting off'
        'Learn something new, such as a new skill or hobby',
        'Connect with friends or family members',
        'Volunteer or give back to your community',
        'Take a walk outside or spend time in nature',
        'Read a book or watch a movie',
    ],
    'default': [
        'Can you please rephrase it ?'
        'Thank you, Take rest'

    ]
}

# Define function to determine stress level
def get_stress_level(stress_value):
    if stress_value == HIGH_STRESS_THRESHOLD:
        return 'high'
    elif stress_value == LOW_STRESS_THRESHOLD:
        return 'low'
    elif stress_value == NORMAL_STRESS_THRESHOLD:
        return 'normal'
    else:
        return 'default'

# Define function to handle chatbot requests
def handle_request(request, stress_value):
    if 'stress' in request.lower():
        stress_level = get_stress_level(stress_value)
        return random.choice(STRESS_LEVEL_RESPONSES[stress_level])
    elif 'ok' or 'thank you' in request.lower():
      return "Take rest, Bye!"
    else:
        return "I'm sorry, I don't understand. Can you please rephrase your question?"

# Test the chatbot
stress_value = 2

while True:
    request = input('You: ')
    response = handle_request(request, stress_value)
    print('Chatbot:', response)
    if response == "Take rest, Bye!":
      break