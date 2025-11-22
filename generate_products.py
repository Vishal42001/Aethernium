import json
import random

categories = ["Personal", "Leisure", "Industrial", "Safety", "Exploration", "Medical", "Military"]
adjectives = ["Quantum", "Flux", "Zero-G", "Ion", "Plasma", "Graviton", "Stellar", "Void", "Nebula", "Chrono", "Hyper", "Nano"]
nouns = ["Thruster", "Lifter", "Shield", "Anchor", "Drive", "Suit", "Module", "Emitter", "Field", "Stabilizer", "Drone", "Synthesizer"]

# Image keywords for Unsplash
image_keywords = {
    "Personal": "futuristic,gadget,wearable",
    "Leisure": "futuristic,furniture,luxury",
    "Industrial": "industrial,machine,robot",
    "Safety": "device,shield,protection",
    "Exploration": "space,rover,exploration",
    "Medical": "medical,scanner,futuristic",
    "Military": "tactical,armor,weapon"
}

def generate_product(i):
    category = random.choice(categories)
    name = f"{random.choice(adjectives)} {random.choice(nouns)} {random.randint(100, 9000)}"
    
    descriptions = {
        "Personal": "Compact personal mobility unit for urban environments. Designed for seamless integration with daily life.",
        "Leisure": "Ultimate comfort with localized gravity manipulation. Experience the pinnacle of relaxation.",
        "Industrial": "Heavy-duty equipment for construction and logistics. Built to withstand the harshest conditions.",
        "Safety": "Essential protection against spacetime anomalies. Your safety is our priority in a quantum world.",
        "Exploration": "Rugged gear for charting the unknown. Survive and thrive in any environment.",
        "Medical": "Advanced bio-stasis and healing fields. The future of personal healthcare.",
        "Military": "Civilian-grade tactical defense and mobility systems. Superior protection for high-risk zones."
    }
    
    features_pool = [
        "Micro-fusion battery", "Haptic feedback interface", "Auto-navigation", "Voice control",
        "Radiation shielding", "Kinetic dampeners", "Neural link", "Solar recharge",
        "Emergency beacon", "Atmospheric recycling", "Gravity tether", "Inertial dampening",
        "Quantum encryption", "Biometric lock", "Self-repair nanobots", "Holographic HUD"
    ]
    
    # Generate 5 images
    gallery = []
    keyword = image_keywords.get(category, "technology")
    for j in range(5):
        # Using source.unsplash.com with random sig to ensure different images
        gallery.append(f"https://source.unsplash.com/random/800x600/?{keyword}&sig={i*10+j}")

    return {
        "id": f"AD-{category[:3].upper()}-{random.randint(1000, 9999)}",
        "name": name,
        "description": descriptions.get(category, "Advanced antigravity technology."),
        "category": category,
        "price": random.randint(1000, 50000),
        "features": random.sample(features_pool, 4),
        "usp": f"The only {category.lower()} unit with {random.choice(features_pool)} technology.",
        "specs": {
            "Weight": f"{random.randint(5, 500)} kg",
            "Range": f"{random.randint(50, 5000)} km",
            "Dimensions": f"{random.randint(10, 200)}x{random.randint(10, 200)}x{random.randint(10, 200)} cm",
            "Power Source": random.choice(["Ion Battery", "Fusion Cell", "Zero-Point Module", "Solar Array"])
        },
        "gallery": gallery,
        "image": gallery[0] # Main image
    }

new_products = [generate_product(i) for i in range(35)]

# Save to file
with open('src/data/products.json', 'w') as f:
    json.dump(new_products, f, indent=2)

print(f"Generated {len(new_products)} rich products.")
