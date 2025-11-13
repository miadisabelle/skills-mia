import argparse

def main():
    parser = argparse.ArgumentParser(description='Generate an initial prompt for an AI Studio project.')
    parser.add_argument('--name', required=True, help='The name of the application.')
    parser.add_argument('--outcome', required=True, help='The desired outcome of the application.')
    parser.add_argument('--stack', required=True, help='The technology stack.')
    parser.add_argument('--features', required=True, help='A comma-separated list of key features.')
    parser.add_argument('--design', required=True, help='Design principles for the application.')
    parser.add_argument('--ai-features', help='A comma-separated list of AI features.')

    args = parser.parse_args()

    prompt = f"""# AI Studio Initial Prompt

**Project Name:** {args.name}

**Core Intent:**
This application enables users to {args.outcome}.

**Technology Stack:**
- {args.stack.replace(',', '\n- ')}

**Key Features:**
- {args.features.replace(',', '\n- ')}

**Design Principles:**
- {args.design}

"""

    if args.ai_features:
        prompt += f"**AI Features:**\n- {args.ai_features.replace(',', '\n- ')}"

    print(prompt)

if __name__ == '__main__':
    main()

