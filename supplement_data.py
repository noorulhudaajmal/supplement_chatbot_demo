supplements = {
    "muscle_gain": [
        {
            "name": "Whey Protein Isolate",
            "description": "High-quality complete protein for muscle building and recovery",
            "benefits": "Fast absorption, complete amino acid profile, supports muscle protein synthesis",
            "dosage": "25-30g post-workout or between meals",
            "target_demographic": "All ages and genders, especially active individuals"
        },
        {
            "name": "Creatine Monohydrate",
            "description": "Well-researched compound for strength and power enhancement",
            "benefits": "Increases strength, power output, muscle mass, and exercise performance",
            "dosage": "3-5g daily, timing doesn't matter",
            "target_demographic": "Males and females 18+, particularly effective for high-intensity training"
        },
        {
            "name": "Beta-Alanine",
            "description": "Amino acid that helps buffer lactic acid in muscles",
            "benefits": "Reduces muscle fatigue, improves endurance in high-intensity exercise",
            "dosage": "3-5g daily, split into smaller doses to avoid tingling",
            "target_demographic": "Athletes and fitness enthusiasts of all ages"
        },
        {
            "name": "HMB (β-Hydroxy β-Methylbutyrate)",
            "description": "Metabolite of leucine that helps preserve muscle mass",
            "benefits": "Reduces muscle breakdown, aids recovery, supports lean muscle growth",
            "dosage": "3g daily, divided into 1g doses with meals",
            "target_demographic": "Particularly beneficial for older adults (45+) and beginners"
        },
        {
            "name": "Leucine",
            "description": "Essential amino acid that triggers muscle protein synthesis",
            "benefits": "Stimulates muscle building, improves recovery, preserves muscle during calorie restriction",
            "dosage": "2.5-5g per serving, especially post-workout",
            "target_demographic": "All demographics, especially effective for older adults (50+)"
        }
    ],
    "weight_loss": [
        {
            "name": "Green Tea Extract (EGCG)",
            "description": "Natural thermogenic compound from green tea leaves",
            "benefits": "Boosts metabolism, increases fat oxidation, provides antioxidants",
            "dosage": "400-500mg daily (standardized to 50% EGCG)",
            "target_demographic": "Adults of all ages, may be more effective in younger individuals"
        },
        {
            "name": "L-Carnitine",
            "description": "Amino acid derivative that helps transport fatty acids for energy",
            "benefits": "Enhances fat burning, improves exercise performance, supports heart health",
            "dosage": "2-3g daily, preferably before exercise",
            "target_demographic": "All ages, particularly beneficial for older adults (40+)"
        },
        {
            "name": "Glucomannan",
            "description": "Natural fiber from konjac root that promotes satiety",
            "benefits": "Increases fullness, slows digestion, helps control appetite",
            "dosage": "1-3g before meals with plenty of water",
            "target_demographic": "Adults looking to control portion sizes, safe for all ages"
        },
        {
            "name": "Caffeine Anhydrous",
            "description": "Pure caffeine for energy and metabolic boost",
            "benefits": "Increases energy, suppresses appetite, boosts thermogenesis",
            "dosage": "100-400mg daily, avoid late in the day",
            "target_demographic": "Adults under 65, use cautiously with heart conditions"
        },
        {
            "name": "CLA (Conjugated Linoleic Acid)",
            "description": "Fatty acid that may help reduce body fat while preserving muscle",
            "benefits": "May reduce body fat, preserve lean muscle, improve body composition",
            "dosage": "3-6g daily with meals",
            "target_demographic": "Adults of all ages, particularly those doing resistance training"
        }
    ],
    "immunity": [
        {
            "name": "Vitamin C (Ascorbic Acid)",
            "description": "Essential vitamin with powerful immune-supporting properties",
            "benefits": "Strengthens immune system, antioxidant protection, supports collagen synthesis",
            "dosage": "500-1000mg daily, higher doses during illness",
            "target_demographic": "All ages, especially beneficial for older adults (50+) and stressed individuals"
        },
        {
            "name": "Zinc Picolinate",
            "description": "Essential mineral crucial for immune function and wound healing",
            "benefits": "Supports immune response, aids wound healing, maintains healthy skin",
            "dosage": "8-11mg daily for adults (higher for males)",
            "target_demographic": "All ages, particularly important for older adults and vegetarians"
        },
        {
            "name": "Elderberry Extract",
            "description": "Concentrated extract from elderberry fruit with immune benefits",
            "benefits": "May reduce duration of cold/flu, rich in antioxidants, supports upper respiratory health",
            "dosage": "300-600mg daily during cold season",
            "target_demographic": "All ages including children, particularly beneficial during fall/winter"
        },
        {
            "name": "Vitamin D3",
            "description": "Fat-soluble vitamin essential for immune function and bone health",
            "benefits": "Modulates immune response, supports bone health, may improve mood",
            "dosage": "1000-4000 IU daily, depending on blood levels",
            "target_demographic": "Especially important for older adults, those with limited sun exposure"
        },
        {
            "name": "Probiotics (Multi-strain)",
            "description": "Beneficial bacteria that support gut and immune health",
            "benefits": "Supports digestive health, enhances immune function, may improve mood",
            "dosage": "1-10 billion CFU daily, preferably with food",
            "target_demographic": "All ages, particularly beneficial after antibiotic use or for digestive issues"
        }
    ],
    "energy": [
        {
            "name": "Rhodiola Rosea",
            "description": "Adaptogenic herb that helps combat fatigue and stress",
            "benefits": "Reduces fatigue, improves mental performance, helps manage stress",
            "dosage": "200-400mg daily, preferably on empty stomach",
            "target_demographic": "Adults dealing with stress or fatigue, particularly effective for 25-55 age group"
        },
        {
            "name": "Coenzyme Q10 (CoQ10)",
            "description": "Compound essential for cellular energy production",
            "benefits": "Supports cellular energy, heart health, may reduce fatigue",
            "dosage": "100-200mg daily with fat-containing meal",
            "target_demographic": "Particularly beneficial for adults 40+, those on statins"
        },
        {
            "name": "B-Complex Vitamins",
            "description": "Group of vitamins essential for energy metabolism",
            "benefits": "Supports energy production, nervous system function, reduces fatigue",
            "dosage": "Follow label instructions, typically 1 capsule daily",
            "target_demographic": "All ages, especially beneficial for vegetarians and older adults"
        },
        {
            "name": "Iron Bisglycinate",
            "description": "Highly absorbable form of iron for those with deficiency",
            "benefits": "Prevents/treats iron deficiency, reduces fatigue, supports oxygen transport",
            "dosage": "18-25mg daily for adults (higher for women of childbearing age)",
            "target_demographic": "Women 18-50, vegetarians, those with diagnosed iron deficiency"
        },
        {
            "name": "Ashwagandha",
            "description": "Adaptogenic herb that helps manage stress and boost energy",
            "benefits": "Reduces cortisol levels, improves stress response, may boost testosterone in men",
            "dosage": "300-600mg daily, preferably with meals",
            "target_demographic": "Adults dealing with chronic stress, particularly effective for 25-65 age group"
        }
    ]
}

def get_supplements_for_goal(health_goal):
    """
    Map health goals to supplement categories
    """
    goal_mapping = {
        "Muscle Gain & Strength": "muscle_gain",
        "Weight Loss & Fat Burning": "weight_loss",
        "Immune System Support": "immunity",
        "Energy & Endurance": "energy"
    }

    category = goal_mapping.get(health_goal, "")
    return supplements.get(category, [])

def get_age_specific_recommendations(age_group, supplements_list):
    """
    Filter or prioritize supplements based on age group
    """
    age_priorities = {
        "18-25": ["protein", "creatine", "caffeine"],
        "26-35": ["protein", "multivitamin", "omega-3"],
        "36-45": ["protein", "vitamin_d", "magnesium"],
        "46-55": ["vitamin_d", "calcium", "coq10"],
        "56-65": ["vitamin_d", "calcium", "b12"],
        "65+": ["vitamin_d", "b12", "calcium"]
    }

    return age_priorities.get(age_group, [])

def get_gender_specific_recommendations(gender, supplements_list):
    """
    Provide gender-specific supplement recommendations
    """
    if gender.lower() == "female":
        return {
            "iron": "Women often need more iron due to menstrual losses",
            "calcium": "Important for bone health, especially post-menopause",
            "folate": "Essential for women of childbearing age"
        }
    elif gender.lower() == "male":
        return {
            "zinc": "Men typically need higher zinc intake",
            "lycopene": "Beneficial for prostate health",
            "magnesium": "Important for testosterone production"
        }

    return {}