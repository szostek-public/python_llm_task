#!/usr/bin/env python3
import json
from typing import List

INPUT_FILE="regulations.txt"
OUTPUT_FILE="extracted_requirements.jsonl"

def input_processing(the_filename: str = INPUT_FILE) -> List[str]:
    """
    Reads text file relative to same directory as this file.

    Parameters:
    the_filename (str): filename of input file to read.

    Returns:
    str: File content.
    """
    try:
        readable_file = open(the_filename, "r")
        txt = readable_file.read()
    except FileNotFoundError:
        print(f"Can't find file: {the_filename}")
    except PermissionError:
        print(f"Permission error reading from file: {the_filename}")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        print(f"Some error when reading from file: {e}")

    readable_file.close()
    return txt

def text_segmentation(txt: str) -> List[str]:
    """
    Splits text into sections.
    `Lazy` python method to split on '\n' delimiter.

    Parameters:
    txt (str): text string to segment into sections.

    Returns:
    List[str]: A list of the sections as text strings.
    """
    return txt.split("\n\n")

def text_manipulation_dummy_func(txt: str) -> str:
    """
    This function returns the first 5 tokens on the input string.

    Parameters:
    txt (str): input text string to manipulate.

    Returns:
    str: A string of the first 5 tokens from the input text string.
    """
    return ' '.join(txt.split()[:5])

def simulate_llm_summary(txt_section: str) -> str:
    """
    This function simulates an llm summary function by calling
    'text_manipulation_dummy_func' to manipulate text.

    Parameters:
    txt_section (str): a section

    Returns:
    str: 'dummy' summary of a section
    """
    return text_manipulation_dummy_func(txt_section)

if __name__ in "__main__":

	# Input processing
	document_text = input_processing()
	print("Extracted text has {} characters.".format(len(document_text)))
	# Text segmentation
	sections = text_segmentation(document_text)
	print("Segmented text into {} sections.".format(len(sections)))

	# Simulated LLM integration and write to jsonl (one record json per line)
	for i, s in enumerate(sections):
		summarized_requirements = simulate_llm_summary(s)
		record = {
			"number": i,
			"txt": s,
			"summarized_requirements": summarized_requirements,
			"meta": None
		}
		try:
			with open(OUTPUT_FILE, "a") as output_file_handle:
				json.dump(record, output_file_handle)
				output_file_handle.write('\n')
		except FileNotFoundError:
			print(f"Can't find file: {the_filename}")
		except PermissionError:
			print(f"Permission error reading from file: {the_filename}")
		except IOError as e:
			print(f"An I/O error occurred: {e}")
		except Exception as e:
			print(f"Some error when reading from file: {e}")


	print(f"Sections summaried and writen to {OUTPUT_FILE}.")
