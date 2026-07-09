# Prompt: An Input given to LLM in order to get the satisfying
# output.

# The Model is Smart. 
# But your prompt decides how smart the answer becomes.

# Bad Prompt:
    # Explain Python

# Better Prompt:
    # Explain python for beginner in  simple language with an example.

# Even Better Prompt:
    # You are an experienced Python Trainer.
    # Explain python to first year Engineering Staudents.
    # Use Simple English
    # Give 5 Examples
    # Keep Answer under 300 words


# Prompt Anatomy:
    # Role:
    # You are a Java Instructor.

    # Task:
    # Teach Exception Handeling.

    # Context:
    # Students know only basic Java.

    # Constraints:
    # Explain in simple Language.

    # Output Format:
    # Bullet points + Examples


# Prompt Engineering Techniques:
    # Zero-Shot Prompting
        # Trnaslate this into French.
        # Hello, How are you?


    # One-Shot Prompting
        # English:
        # Good Morning

        # French:
        # Bonjour

        # Now translate
        # Good Night

    # Few-Shot Prompting
        # Positive -> Happy
        # Negative -> Sad
        # Excited -> Joy
        
        # Now Classify:
        # Angry

    # Chain of Thoughts
        # Insted of "Solve this", "Solve Step by Step"

    # Persona Prompting
        # Act as 
                # Doctor,
                # Engineer
                # Magician
                # Joker

