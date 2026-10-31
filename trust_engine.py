# Trust Score Calculation Function
def calculate_trust(capability, feature, activity):

    trust_score = (
        (0.4 * capability) +
        (0.3 * feature) +
        (0.3 * activity)
    )

    return round(trust_score, 2)


# Device Classification Function
def classify_device(trust_score):

    if trust_score >= 75:
        return "Trusted"

    elif trust_score >= 50:
        return "Suspicious"

    else:
        return "Malicious"


# Test the functions
if __name__ == "__main__":

    capability = 90
    feature = 85
    activity = 80

    trust = calculate_trust(capability, feature, activity)

    status = classify_device(trust)

    print("Trust Score :", trust)
    print("Status :", status)