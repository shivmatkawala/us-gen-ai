from agent import run_agent


def main():
    print("=" * 60)
    print("🤖 Welcome to Multi Tool AI Agent")
    print("=" * 60)
    print("I can help you with:")
    print("🌤 Weather")
    print("📰 Latest Technology News")
    print("🎨 AI Image Generation")
    print("\nType 'exit' to quit.\n")

    while True:
        user_query = input("👤 You : ")

        if user_query.lower() in ["exit", "quit"]:
            print("\n👋 Goodbye!")
            break

        try:
            response = run_agent(user_query)
            print("\n🤖 Agent :")
            print(response)
            print()
        except Exception as e:
            print("\n❌ Error:", e)
            print()


if __name__ == "__main__":
    main()