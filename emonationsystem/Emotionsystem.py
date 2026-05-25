import json
from collections import defaultdict
from datetime import datetime

# EMOTION DETECTION - SIMPLIFIED VERSION (NO EMOJIS)


# Emotion keywords database
emotions_data = {
    'happy': ['happy', 'joyful', 'delighted', 'love', 'awesome', 'wonderful', 'amazing', 'excellent'],
    'sad': ['sad', 'depressed', 'lonely', 'unhappy', 'miserable', 'grief', 'hurt', 'down'],
    'angry': ['angry', 'furious', 'mad', 'irritated', 'rage', 'hostile', 'livid'],
    'surprised': ['surprised', 'shocked', 'amazed', 'astonished', 'wow', 'unexpected'],
    'fearful': ['afraid', 'scared', 'nervous', 'anxious', 'worried', 'frightened', 'panic'],
    'disgusted': ['disgusted', 'gross', 'nasty', 'vile', 'yuck', 'repulsive']
}

# FUNCTION 1: Detect emotion from text


def detect_emotion(text):
    """
    Simple emotion detection
    Input: text string
    Output: emotion, confidence, scores
    """
    text = text.lower()
    words = text.split()
    
    scores = defaultdict(int)
    
    # Count emotion keywords
    for emotion, keywords in emotions_data.items():
        for word in words:
            if word in keywords:
                scores[emotion] += 1
    
    # If no emotion found, return neutral
    if not scores:
        return 'neutral', 0.0, {}
    
    # Get primary emotion
    emotion = max(scores, key=scores.get)
    confidence = scores[emotion] / len(words) if words else 0
    confidence = min(confidence, 1.0)
    
    return emotion, confidence, dict(scores)

# FUNCTION 2: Store conversation


conversations = []

def save_message(message, emotion, confidence):
    """Save message to conversation history"""
    record = {
        'id': len(conversations) + 1,
        'timestamp': datetime.now().isoformat(),
        'message': message,
        'emotion': emotion,
        'confidence': round(confidence, 2)
    }
    conversations.append(record)
    return record


# FUNCTION 3: Get statistics


def get_statistics():
    """Calculate emotion statistics"""
    if not conversations:
        return {}
    
    stats = defaultdict(int)
    for conv in conversations:
        stats[conv['emotion']] += 1
    
    total = len(conversations)
    result = {}
    for emotion, count in stats.items():
        result[emotion] = {
            'count': count,
            'percentage': round((count / total) * 100, 2)
        }
    
    return result



# FUNCTION 4: Export to JSON

def export_to_json(filename='conversations.json'):
    """Export conversations to JSON file"""
    with open(filename, 'w') as f:
        json.dump(conversations, f, indent=2)
    return filename


# FUNCTION 5: Show all conversations


def show_conversations():
    """Display all stored conversations"""
    if not conversations:
        print("No conversations yet!")
        return
    
    print("\n" + "="*70)
    print("ALL CONVERSATIONS")
    print("="*70)
    
    for conv in conversations:
        message_preview = conv['message'][:40] if len(conv['message']) > 40 else conv['message']
        print(f"{conv['id']}. {message_preview} | {conv['emotion']} ({conv['confidence']:.0%})")

# TESTING - TRY IT!


if __name__ == "__main__":
    
    print("="*70)
    print("EMOTION RECOGNITION SYSTEM - SIMPLE VERSION (NO EMOJIS)")
    print("="*70)
    
    # Test 1: Single detection
    print("\n[TEST 1] Single Message Analysis:")
    msg1 = "I am so happy today!"
    emotion1, conf1, scores1 = detect_emotion(msg1)
    print(f"Message: {msg1}")
    print(f"Emotion: {emotion1}")
    print(f"Confidence: {conf1:.2%}")
    save_message(msg1, emotion1, conf1)
    
    # Test 2: Another message
    print("\n[TEST 2] Another Message:")
    msg2 = "I feel very sad and lonely"
    emotion2, conf2, scores2 = detect_emotion(msg2)
    print(f"Message: {msg2}")
    print(f"Emotion: {emotion2}")
    print(f"Confidence: {conf2:.2%}")
    save_message(msg2, emotion2, conf2)
    
    # Test 3: More messages
    print("\n[TEST 3] Batch Processing:")
    test_messages = [
        "I'm really angry right now!",
        "This is surprising and amazing!",
        "I'm scared and nervous",
        "This is gross and disgusting"
    ]
    
    for msg in test_messages:
        emotion, conf, scores = detect_emotion(msg)
        print(f"'{msg}' -> {emotion} ({conf:.0%})")
        save_message(msg, emotion, conf)
    
    # Test 4: Statistics
    print("\n[TEST 4] Statistics:")
    stats = get_statistics()
    print("Emotion Distribution:")
    for emotion, data in stats.items():
        print(f"  {emotion}: {data['count']} ({data['percentage']}%)")
    
    # Test 5: View all
    print("\n[TEST 5] View All Conversations:")
    show_conversations()
    
    # Test 6: Export
    print("\n[TEST 6] Export to JSON:")
    filename = export_to_json()
    print(f"Exported to: {filename}")
    
    print("\n" + "="*70)
    print("Testing completed!")
    print("="*70)