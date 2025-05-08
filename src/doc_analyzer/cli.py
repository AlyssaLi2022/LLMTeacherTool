# src/doc_analyzer/cli.py
import argparse
# Use absolute import based on the package structure found from 'src'
from doc_analyzer.analyzer import generate_material, provide_feedback, grade_document
# ... rest of the file
def main():
    """Main function to parse arguments and call the appropriate analyzer function."""
    parser = argparse.ArgumentParser(description="Teacher Document Analyzer CLI Tool")

    # Create subparsers for different commands (generate, feedback, grade)
    subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)

    # --- Subparser for the 'generate' command ---
    parser_generate = subparsers.add_parser("generate", help="Generate teaching material")
    parser_generate.add_argument("topic", type=str, help="The topic for the material")
    parser_generate.add_argument(
        "-l", "--length", type=str, default="brief", choices=["brief", "medium", "detailed"],
        help="Desired length of the material (brief, medium, detailed)"
    )

    # --- Subparser for the 'feedback' command (placeholder) ---
    parser_feedback = subparsers.add_parser("feedback", help="Provide feedback on a document")
    parser_feedback.add_argument("filepath", type=str, help="Path to the document file (.txt)")
    # TODO: Implement file reading later

    # --- Subparser for the 'grade' command (placeholder) ---
    parser_grade = subparsers.add_parser("grade", help="Grade a document based on criteria")
    parser_grade.add_argument("filepath", type=str, help="Path to the document file (.txt)")
    parser_grade.add_argument("criteria", type=str, help="Grading criteria or rubric")
    # TODO: Implement file reading later

    # Parse the arguments provided by the user
    args = parser.parse_args()

    # --- Execute the corresponding command ---
    if args.command == "generate":
        print(f"\nGenerating material for topic: '{args.topic}' (Length: {args.length})...\n")
        # Call the generate_material function from analyzer.py
        result = generate_material(topic=args.topic, length=args.length)
        print("\n--- Generated Material ---")
        print(result)
        print("------------------------\n")

   # In src/doc_analyzer/cli.py, inside the main() function

    elif args.command == "feedback":
        print(f"\nProviding feedback for file: {args.filepath} (using sample text for now)...\n")
        # --- File Reading Placeholder ---
        # TODO: Implement actual file reading based on args.filepath
        sample_document_text = "The water cycle are a complex system. Water evaporate from the see, forms clowds, and then fall as rain. It helps plants growwing." # Sample text with errors
        print(f"--- Sample Document Text ---\n{sample_document_text}\n--------------------------\n")

        # Call the provide_feedback function from analyzer.py
        result = provide_feedback(document_text=sample_document_text)
        print("\n--- Feedback ---")
        print(result)
        print("----------------\n")

   # In src/doc_analyzer/cli.py, inside the main() function

    elif args.command == "grade":
        print(f"\nGrading file: {args.filepath} based on criteria: '{args.criteria}' (using sample text for now)...\n")
        # --- File Reading Placeholder ---
        # TODO: Implement actual file reading based on args.filepath
        sample_document_text = "The water cycle are a complex system. Water evaporate from the see, forms clowds, and then fall as rain. It helps plants growwing." # Same sample text
        print(f"--- Sample Document Text ---\n{sample_document_text}\n--------------------------\n")
        # Use the criteria passed from the command line argument
        criteria_to_use = args.criteria
        print(f"--- Grading Criteria ---\n{criteria_to_use}\n----------------------\n")

        # Call the grade_document function from analyzer.py
        result = grade_document(document_text=sample_document_text, criteria=criteria_to_use)
        print("\n--- Grading Result ---")
        print(result)
        print("----------------------\n")

# --- Entry point for the script ---
# This allows running the CLI using "python -m src.doc_analyzer.cli"
if __name__ == "__main__":
    main()