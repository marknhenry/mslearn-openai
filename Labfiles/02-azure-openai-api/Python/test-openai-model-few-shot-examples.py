import os
from dotenv import load_dotenv

from openai import AzureOpenAI


def main(): 
        
    try: 
    
        # Get configuration settings 
        load_dotenv()
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")
        
        # Initialize the Azure OpenAI client...
        client = AzureOpenAI(
            azure_endpoint = azure_oai_endpoint, 
            api_key=azure_oai_key,  
            api_version="2024-02-15-preview"
        )

        
        system_message = """
        You are an AI assistant that helps people find information.
        """
        
        # Initialize messages array
        messages_array = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": """What kind of article is this?
            ---
            New York Baseballers Wins Big Against Chicago
            New York Baseballers mounted a big 5-0 shutout against the Chicago Cyclones last night, solidifying their win with a 3 run homerun late in the bottom of the 7th inning.
            Pitcher Mario Rogers threw 96 pitches with only two hits for New York, marking his best performance this year.
            The Chicago Cyclones' two hits came in the 2nd and the 5th innings but were unable to get the runner home to score."""},
            {"role": "assistant", "content": "Sports"},
            {"role": "user", "content": """ Categorize this article:
            ---
            Joyous moments at the Oscars
            The Oscars this past week where quite something!
            Though a certain scandal might have stolen the show, this year's Academy Awards were full of moments that filled us with joy and even moved us to tears.
            These actors and actresses delivered some truly emotional performances, along with some great laughs, to get us through the winter.
            From Robin Kline's history-making win to a full performance by none other than Casey Jensen herself, don't miss tomorrows rerun of all the festivities."""},
            {"role": "assistant", "content": " Entertainment"},
            {"role": "user", "content": """  What kind of article is this?
            ---
            Severe drought likely in California
            Millions of California residents are bracing for less water and dry lawns as drought threatens to leave a large swath of the region with a growing water shortage.
            In a remarkable indication of drought severity, officials in Southern California have declared a first-of-its-kind action limiting outdoor water use to one day a week for nearly 8 million residents.
            Much remains to be determined about how daily life will change as people adjust to a drier normal. But officials are warning the situation is dire and could lead to even more severe limits later in the year."""},
                          ]

        while True:
            # Get input text
            input_text = input("Enter the prompt (or type 'quit' to exit): ")
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue

            print("\nSending request for summary to Azure OpenAI endpoint...\n\n")
            
            # Add code to send request...
            # Send request to Azure OpenAI model
            
            messages_array.append({"role": "user", "content": input_text})
            
            response = client.chat.completions.create(
                model=azure_oai_deployment,
                temperature=0.7,
                max_tokens=1200,
                messages=messages_array
            )
            generated_text = response.choices[0].message.content
            # Add generated text to messages array
            messages_array.append({"role": "system", "content": generated_text})


            # Print the response
            print("Response: " + generated_text + "\n")
            
            
            

    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()