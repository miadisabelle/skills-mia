import argparse
import os

def main():
    parser = argparse.ArgumentParser(description='Generate placeholder RISE specs for a project.')
    parser.add_argument('--features', required=True, help='A comma-separated list of key features.')
    args = parser.parse_args()

    if not os.path.exists('rispecs'):
        os.makedirs('rispecs')

    features = args.features.split(',')

    for feature in features:
        feature_slug = feature.lower().replace(' ', '-')
        spec_content = f"""# RISE Specification: {feature}

## 1. Core Creative Intent

- **Desired Outcome:** [Describe what this feature enables users to create or achieve.]

## 2. Structural Tension Analysis

- **Current Reality:** [Describe the user's state before this feature exists.]
- **Desired Outcome:** [Restate the desired outcome for this feature.]

## 3. Creative Advancement Scenarios

**Scenario 1:** [Scenario Name]
- **Desired Outcome:** 
- **Current Reality:** 
- **Natural Progression:** 
- **Resolution:** 

## 4. Supporting Structures

[Detail the UI elements, data models, and API endpoints that support this feature.]

"""
        with open(os.path.join('rispecs', f'{feature_slug}.spec.md'), 'w') as f:
            f.write(spec_content)
        print(f"Created rispecs/{feature_slug}.spec.md")

if __name__ == '__main__':
    main()
