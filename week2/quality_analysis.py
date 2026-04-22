import matplotlib.pyplot as plt
import numpy as np
from decimal import Decimal, ROUND_HALF_UP

# ============================================
# ISO 25010 Quality Analysis Script
# Lab Session 2 - Software Quality Engineering
# ============================================

# YOUR RATINGS FROM THE TABLE:
# Order: [Functional Suitability, Performance Efficiency, Compatibility, 
#         Usability, Reliability, Security, Maintainability, Portability]

APP1_RATINGS = [4, 5, 5, 4, 4, 5, 4, 4.5]      # WhatsApp
APP2_RATINGS = [5, 5, 4.5, 4.5, 4, 3, 4, 5]    # Telegram

# Weights for each characteristic (as decimals)
WEIGHTS = [0.15, 0.12, 0.10, 0.15, 0.15, 0.15, 0.08, 0.10]

# Characteristic names
CHARACTERISTICS = [
    "Functional\nSuitability",
    "Performance\nEfficiency",
    "Compatibility",
    "Usability",
    "Reliability",
    "Security",
    "Maintainability",
    "Portability"
]

# App names
APP1_NAME = "WhatsApp"
APP2_NAME = "Telegram"


def calculate_weighted_score(ratings, weights):
    """Calculate weighted total score (max 5.0) - matches Excel rounding"""
    weighted_sum = sum(r * w for r, w in zip(ratings, weights))
    rounded = float(Decimal(str(weighted_sum)).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP))
    return rounded


def create_radar_chart(app1_ratings, app2_ratings, characteristics, app1_name, app2_name):
    """Generate and save radar chart PNG"""
    
    N = len(characteristics)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': 'polar'})
    
    plt.xticks(angles[:-1], characteristics, size=10)
    ax.set_rlabel_position(0)
    plt.yticks([1, 2, 3, 4, 5], ["1", "2", "3", "4", "5"], size=8)
    plt.ylim(0, 5.5)
    
    app1_values = app1_ratings + app1_ratings[:1]
    ax.plot(angles, app1_values, 'o-', linewidth=2, color='#2E86AB', label=app1_name)
    ax.fill(angles, app1_values, alpha=0.25, color='#2E86AB')
    
    app2_values = app2_ratings + app2_ratings[:1]
    ax.plot(angles, app2_values, 'o-', linewidth=2, color='#A23B72', label=app2_name)
    ax.fill(angles, app2_values, alpha=0.25, color='#A23B72')
    
    plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.0), fontsize=12)
    
    score1 = calculate_weighted_score(app1_ratings, WEIGHTS)
    score2 = calculate_weighted_score(app2_ratings, WEIGHTS)
    plt.title(f"ISO 25010 Quality Profile\n{app1_name} ({score1}) vs {app2_name} ({score2})", 
              size=14, pad=20)
    
    filename = f"quality_radar_{app1_name}_{app2_name}.png"
    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    print(f"✅ Radar chart saved as: {filename}")
    plt.show()


def main():
    print("=" * 50)
    print("ISO 25010 Quality Analysis")
    print("=" * 50)
    
    app1_score = calculate_weighted_score(APP1_RATINGS, WEIGHTS)
    app2_score = calculate_weighted_score(APP2_RATINGS, WEIGHTS)
    
    print(f"\n📱 {APP1_NAME} Weighted Total Score: {app1_score}/5.0")
    print(f"📱 {APP2_NAME} Weighted Total Score: {app2_score}/5.0")
    
    margin = round(abs(app1_score - app2_score), 2)
    winner = APP1_NAME if app1_score > app2_score else APP2_NAME
    
    print(f"\n📊 Margin: {margin}")
    print(f"🏆 Better App: {winner}")
    
    print("\n" + "=" * 50)
    print("Rating Breakdown")
    print("=" * 50)
    print(f"{'Characteristic':<22} {'Weight':<8} {APP1_NAME:<12} {APP2_NAME:<12}")
    print("-" * 55)
    
    for i, char in enumerate(CHARACTERISTICS):
        char_clean = char.replace("\n", " ")
        print(f"{char_clean:<22} {WEIGHTS[i]*100:>5.0f}%    {APP1_RATINGS[i]:<12} {APP2_RATINGS[i]:<12}")
    
    print("\n" + "=" * 50)
    print("Generating Radar Chart...")
    print("=" * 50)
    create_radar_chart(APP1_RATINGS, APP2_RATINGS, CHARACTERISTICS, APP1_NAME, APP2_NAME)
    
    print("\n✅ Analysis complete!")


if __name__ == "__main__":
    main()