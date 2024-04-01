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
        You are a coding assistant helping write python code.
        """
        
        # Initialize messages array
        messages_array = [
            {"role": "system", "content": system_message},
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